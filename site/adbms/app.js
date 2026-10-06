'use strict';
/* ADBMS exam book — progress, countdown, quiz engine (Papermorph scoring rules:
   first attempt is the diagnostic; retries never overwrite it). */
const LSKEY = 'adbms-exam-book-v1';
const store = {
  data: { done: [], mcq: {}, sort: {}, ms: {}, examAt: null },
  load() {
    try {
      const raw = JSON.parse(localStorage.getItem(LSKEY) || '{}');
      if (raw && typeof raw === 'object') this.data = Object.assign(this.data, raw);
    } catch { /* corrupted progress starts empty */ }
    if (!Array.isArray(this.data.done)) this.data.done = [];
    for (const k of ['mcq', 'sort', 'ms']) if (typeof this.data[k] !== 'object' || !this.data[k]) this.data[k] = {};
  },
  save() { try { localStorage.setItem(LSKEY, JSON.stringify(this.data)); } catch {} },
};
store.load();
const firstMark = (bucket, id, right, hinted) => {
  if (!Object.hasOwn(store.data[bucket], id)) {
    store.data[bucket][id] = { right: right ? 1 : 0, total: 1, hinted: hinted ? 1 : 0 };
    store.save();
  }
  return store.data[bucket][id];
};

/* ---------- cover / contents ---------- */
function initCover() {
  const open = location.hash.length > 1 && location.hash !== '#book';
  document.body.classList.toggle('open', open);
  const here = open ? document.getElementById(location.hash.slice(1)) : null;
  if (here && here.scrollIntoView) here.scrollIntoView({ block: 'center' });
  else if (!open) scrollTo(0, 0);
}
addEventListener('hashchange', initCover);

/* ---------- countdown ---------- */
function nextExamDefault() {
  const d = new Date(); d.setDate(d.getDate() + 1); d.setHours(9, 0, 0, 0);
  return d.getTime();
}
function initCountdown() {
  const el = document.getElementById('countdown');
  const input = document.getElementById('examAt');
  if (!el) return;
  let t = +store.data.examAt || 0;
  if (!t || t < Date.now()) { t = nextExamDefault(); store.data.examAt = t; store.save(); }
  if (input) {
    const d = new Date(t);
    input.value = new Date(d.getTime() - d.getTimezoneOffset() * 60000).toISOString().slice(0, 16);
    input.addEventListener('change', () => {
      const v = new Date(input.value).getTime();
      if (v) { store.data.examAt = v; store.save(); }
    });
  }
  const tick = () => {
    const ms = (+store.data.examAt || t) - Date.now();
    if (ms <= 0) { el.innerHTML = 'Exam time — <b>go get the marks.</b>'; return; }
    const h = Math.floor(ms / 3600000), m = Math.floor(ms % 3600000 / 60000), s = Math.floor(ms % 60000 / 1000);
    el.innerHTML = `Exam in <b>${h}h ${m}m ${s}s</b>`;
  };
  tick(); setInterval(tick, 1000);
}

/* ---------- progress on contents ---------- */
function initContents(total) {
  const done = store.data.done.filter(n => Number.isInteger(n) && n > 0 && n <= total);
  const p = document.getElementById('prog');
  if (p) p.innerHTML = done.length ? `<b>${done.length}</b> of ${total} finished` : `${total} chapters`;
  document.querySelectorAll('.ch[data-ch]').forEach(a => {
    if (store.data.done.includes(+a.dataset.ch)) a.classList.add('done');
  });
  const last = [...store.data.done].sort((a, b) => a - b).pop();
  const r = document.getElementById('resume');
  if (r && last && last < total) {
    const nxt = document.querySelector(`.ch[data-ch="${last + 1}"]`);
    if (nxt) { r.hidden = false; r.href = nxt.getAttribute('href'); r.textContent = `Continue · Chapter ${last + 1}`; }
  }
  const meta = document.getElementById('meta');
  if (meta) meta.textContent = `${total} chapters · 5 units · exam-optimized`;
}
function markDone(n) {
  if (!store.data.done.includes(n)) { store.data.done.push(n); store.save(); }
  const b = document.getElementById('donebtn');
  if (b) { b.textContent = '✓ Finished — saved'; b.disabled = true; }
}

/* ---------- MCQ choice engine ---------- */
function el(tag, cls, text) {
  const e = document.createElement(tag);
  if (cls) e.className = cls;
  if (text != null) e.textContent = text;
  return e;
}
function renderChoice(host, q) {
  const card = el('div', 'qcard');
  card.id = 'q-' + q.id;
  const tags = el('div', 'qtags');
  const tchip = el('span', 'qtag', q.id + ' · ' + q.topic);
  const pchip = el('span', 'qtag ' + q.pri.toLowerCase(), q.pri);
  tags.append(tchip, pchip);
  const prev = store.data.mcq[q.id];
  if (prev) tags.append(el('span', 'qtag', prev.right ? '✓ first try' : '✗ first try'));
  card.append(tags, el('div', 'qprompt', q.text));
  const box = el('div', 'qopts');
  const fb = el('div', 'qfb');
  const hint = el('div', 'qhint', 'Keys: ' + q.hint);
  let sel = -1, resolved = false, hinted = false;
  const btns = q.opts.map((o, i) => {
    const b = el('button', 'qopt', String.fromCharCode(65 + i) + '. ' + o);
    b.onclick = () => {
      if (resolved) return;
      sel = i;
      btns.forEach(x => x.classList.remove('sel'));
      b.classList.add('sel');
      bCheck.disabled = false;
    };
    box.append(b);
    return b;
  });
  const acts = el('div', 'qacts');
  const bCheck = el('button', 'btn small go', 'Check  ⏎');
  const bHint = el('button', 'btn small quiet', 'Hint');
  const bShow = el('button', 'btn small quiet', 'Show answer (S)');
  const bNext = el('button', 'btn small go', 'Next →');
  bCheck.disabled = true; bNext.style.display = 'none';
  const say = (ok, html) => {
    fb.className = 'qfb ' + (ok === true ? 'ok' : ok === false ? 'no' : 'info');
    fb.innerHTML = html;
  };
  const resolve = () => {
    resolved = true;
    btns.forEach(b => b.disabled = true);
    bCheck.style.display = 'none'; bHint.style.display = 'none'; bShow.style.display = 'none';
    const nx = card.parentElement && card.parentElement.dataset && card.parentElement.dataset.next;
    if (nx) { bNext.style.display = ''; } else { bNext.style.display = 'none'; }
  };
  bCheck.onclick = () => {
    if (sel < 0 || resolved) return;
    const ok = sel === q.ans;
    firstMark('mcq', q.id, ok, hinted);
    btns[q.ans].classList.add('right');
    if (!ok) btns[sel].classList.add('wrong');
    say(ok, (ok ? 'Correct. ' : 'Not quite. ') + (q.why || ''));
    if (!ok && q.whyNot) say(false, 'Not quite. ' + q.whyNot + '<br>' + (q.why || ''));
    resolve(); updateScores();
  };
  bHint.onclick = () => { hinted = true; hint.classList.add('show'); bHint.disabled = true; };
  bShow.onclick = () => {
    firstMark('mcq', q.id, false, true);
    btns[q.ans].classList.add('right');
    say(null, 'Answer: <b>' + String.fromCharCode(65 + q.ans) + '</b>. ' + (q.why || ''));
    resolve(); updateScores();
  };
  bNext.onclick = () => {
    const cards = [...card.parentElement.querySelectorAll('.qcard')];
    const i = cards.indexOf(card);
    if (cards[i + 1]) cards[i + 1].scrollIntoView({ behavior: 'smooth', block: 'center' });
  };
  card.addEventListener('keydown', e => {
    if (e.key === 'Enter' && !resolved && sel >= 0) bCheck.onclick();
    else if ((e.key === 's' || e.key === 'S') && !resolved) bShow.onclick();
  });
  card.tabIndex = 0;
  acts.append(bCheck, bHint, bShow, bNext);
  card.append(box, hint, acts, fb);
  host.append(card);
}
function mcqScore() {
  const v = Object.values(store.data.mcq);
  return { right: v.filter(x => x.right).length, total: v.length };
}
function updateScores() {
  document.querySelectorAll('[data-score]').forEach(s => {
    const { right, total } = mcqScore();
    s.innerHTML = total ? `First-try score: <b>${right}</b> / ${total}` : 'No attempts yet — first tries count.';
  });
}
/* arena: filters + render */
function initArena() {
  const host = document.getElementById('arena');
  if (!host || !window.MCQS) return;
  const render = (list) => {
    host.innerHTML = '';
    host.dataset.next = '1';
    list.forEach(q => renderChoice(host, q));
    updateScores();
    const c = document.getElementById('arenacount');
    if (c) c.textContent = `showing ${list.length} of ${window.MCQS.length}`;
  };
  let unit = 'all', weak = false;
  const apply = () => {
    let list = window.MCQS.filter(q =>
      (unit === 'all' || q.unit === unit || (unit === 'mixed' && q.unit === 'mixed')) &&
      (!weak || (store.data.mcq[q.id] && !store.data.mcq[q.id].right)));
    render(list);
  };
  document.querySelectorAll('[data-unit]').forEach(b => {
    b.onclick = () => {
      document.querySelectorAll('[data-unit]').forEach(x => x.classList.remove('on'));
      b.classList.add('on'); unit = b.dataset.unit; apply();
    };
  });
  const w = document.getElementById('weakonly');
  if (w) w.onclick = () => { weak = !weak; w.classList.toggle('on', weak); apply(); };
  const reset = document.getElementById('resetmcq');
  if (reset) reset.onclick = () => {
    if (confirm('Clear all MCQ first-attempt scores?')) {
      store.data.mcq = {}; store.save(); apply();
    }
  };
  apply();
}

/* ---------- scroll reveal (motion polish on content cards) ---------- */
function initReveal() {
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  if (!('IntersectionObserver' in window)) return;
  const io = new IntersectionObserver(es => es.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('seen'); io.unobserve(e.target); }
  }), { threshold: 0.08 });
  document.querySelectorAll('.callout,.qcard,.drill,.ch,.msrow').forEach(elm => {
    elm.classList.add('rv');
    io.observe(elm);
  });
}
/* ---------- written answer bank ---------- */
function writtenScore() {
  const v = Object.values(store.data.written || {});
  return { right: v.filter(x => x.right).length, total: v.length };
}
function updateWrittenScores() {
  document.querySelectorAll('[data-wscore]').forEach(s => {
    const { right, total } = writtenScore();
    s.innerHTML = total ? `Self-marked: <b>${right}</b> / ${total} got-it` : 'No self-marks yet — first marks only.';
  });
  document.querySelectorAll('.qcard.written').forEach(c => {
    const prev = (store.data.written || {})[c.id];
    const chip = c.querySelector('.wprev');
    if (chip) {
      chip.textContent = prev ? (prev.right ? '✓ first try' : '✗ first try') : '';
      chip.style.display = prev ? '' : 'none';
    }
  });
}
function initWritten() {
  const host = document.getElementById('written');
  if (!host) return;
  if (!store.data.written) store.data.written = {};
  let unit = 'all', wrong = false;
  const apply = () => {
    host.querySelectorAll('.qcard.written').forEach(c => {
      const okU = unit === 'all' || c.dataset.unit === unit;
      const prev = store.data.written[c.id];
      const okW = !wrong || (prev && !prev.right);
      c.style.display = okU && okW ? '' : 'none';
    });
  };
  document.querySelectorAll('[data-wunit]').forEach(b => {
    b.onclick = () => {
      document.querySelectorAll('[data-wunit]').forEach(x => x.classList.remove('on'));
      b.classList.add('on'); unit = b.dataset.wunit; apply();
    };
  });
  const w = document.getElementById('wwrong');
  if (w) w.onclick = () => { wrong = !wrong; w.classList.toggle('on', wrong); apply(); };
  host.querySelectorAll('.wmark').forEach(b => {
    b.onclick = () => {
      const card = b.closest('.qcard');
      firstMark('written', card.id, b.dataset.v === '1', false);
      card.querySelectorAll('.wmark').forEach(x => x.disabled = true);
      updateWrittenScores();
    };
  });
  apply();
  updateWrittenScores();
}
/* ---------- flashcards flip deck ---------- */
function initCards() {
  const host = document.getElementById('cards');
  if (!host) return;
  if (!store.data.cards) store.data.cards = {};
  let deck = 'all', wrong = false;
  const apply = () => {
    host.querySelectorAll('.fcard').forEach(c => {
      const okD = deck === 'all' || c.dataset.deck === deck;
      const prev = store.data.cards[c.id];
      const okW = !wrong || (prev && prev.right < 1);
      c.style.display = okD && okW ? '' : 'none';
    });
  };
  const paint = () => {
    let got = 0, part = 0;
    const v = Object.values(store.data.cards);
    v.forEach(x => { if (x.right >= 1) got++; else if (x.right > 0) part++; });
    document.querySelectorAll('[data-cscore]').forEach(s => {
      s.innerHTML = v.length ? `Cards marked: <b>${got}</b> got-it · ${part} partial · ${v.length} total` : 'No cards marked yet — first marks only.';
    });
    host.querySelectorAll('.fcard').forEach(c => {
      const prev = store.data.cards[c.id];
      c.classList.remove('got', 'part', 'miss');
      if (prev) c.classList.add(prev.right >= 1 ? 'got' : prev.right > 0 ? 'part' : 'miss');
    });
  };
  document.querySelectorAll('[data-cdeck]').forEach(b => {
    b.onclick = () => {
      document.querySelectorAll('[data-cdeck]').forEach(x => x.classList.remove('on'));
      b.classList.add('on'); deck = b.dataset.cdeck; apply();
    };
  });
  const w = document.getElementById('cwrong');
  if (w) w.onclick = () => { wrong = !wrong; w.classList.toggle('on', wrong); apply(); };
  host.querySelectorAll('.fcard').forEach(c => {
    c.addEventListener('click', e => { if (!e.target.closest('.cmark')) c.classList.toggle('open'); });
    c.addEventListener('keydown', e => {
      if (e.key === 'Enter' && !e.target.closest('.cmark')) { e.preventDefault(); c.classList.toggle('open'); }
    });
    c.querySelectorAll('.cmark').forEach(b => {
      b.onclick = () => {
        if (store.data.cards[c.id] === undefined) store.data.cards[c.id] = { right: parseFloat(b.dataset.v), total: 1 };
        store.save();
        c.querySelectorAll('.cmark').forEach(x => x.disabled = true);
        paint();
      };
    });
  });
  apply();
  paint();
}
function initDrills() {
  document.querySelectorAll('.drill[data-drill]').forEach(d => {
    const kind = d.dataset.kind, id = d.dataset.drill;
    const btn = d.querySelector('.checkbtn');
    if (!btn) return;
    btn.onclick = () => {
      if (kind === 'sort') {
        let right = 0, n = 0;
        d.querySelectorAll('select[data-ans]').forEach((s, i) => {
          n++;
          const ok = s.value === s.dataset.ans;
          if (ok) right++;
          firstMark('sort', id + ':' + i, ok, false);
          const td = s.closest('td');
          td.classList.remove('ok', 'bad');
          td.classList.add(ok ? 'ok' : 'bad');
        });
        d.querySelector('.drillscore').innerHTML =
          `First-try on this check: <b>${right}</b> / ${n}` + (right / n <= 0.6 ? ' — ≤60%: re-read the named section, then redo.' : ' — solid.');
      } else if (kind === 'ms') {
        let right = 0, n = 0;
        d.querySelectorAll('.msrow[data-ans]').forEach((row, i) => {
          n++;
          const picked = row.querySelector('.msbtns button.sel');
          const ok = picked && picked.dataset.v === row.dataset.ans;
          if (ok) right++;
          firstMark('ms', id + ':' + i, !!ok, false);
          row.classList.remove('ok', 'bad');
          row.classList.add(ok ? 'ok' : 'bad');
          const ex = row.querySelector('.explain');
          if (ex) ex.style.display = '';
        });
        d.querySelector('.drillscore').innerHTML =
          `First-try on this check: <b>${right}</b> / ${n}` + (right / n <= 0.6 ? ' — ≤60%: re-read the named section, then redo.' : ' — solid.');
      }
    };
  });
  document.querySelectorAll('.msbtns button').forEach(b => {
    b.setAttribute('aria-pressed', 'false');
    b.onclick = () => {
      b.parentElement.querySelectorAll('button').forEach(x => {
        x.classList.remove('sel');
        x.setAttribute('aria-pressed', 'false');
      });
      b.classList.add('sel');
      b.setAttribute('aria-pressed', 'true');
    };
  });
}
