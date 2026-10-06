'use strict';
/* Narrated-beats player (skill-shaped, offline): stage SVG + speechSynthesis narration.
   Beats carry [[marks]] like the skill's narration JSON; marks fire timed actions.
   Honors prefers-reduced-motion. */
function parseMarks(say) {
  const marks = {};
  let wi = 0;
  const clean = say.replace(/\[\[(\w+)\]\]|(\S+)/g, (m, mark, word) => {
    if (mark) { marks[mark] = wi; return ''; }
    wi++;
    return word;
  });
  const words = [];
  clean.replace(/\S+/g, (w, off) => { words.push({ w, off }); return w; });
  return { clean: clean.replace(/\s+/g, ' ').trim(), marks, words };
}

function pickVoice() {
  const vs = speechSynthesis.getVoices().filter(v => v.lang && v.lang.toLowerCase().startsWith('en'));
  if (Narrate.voiceURI) { const v = vs.find(v => v.voiceURI === Narrate.voiceURI); if (v) return v; }
  const pref = ['Google US English', 'Microsoft David', 'Microsoft Zira', 'Microsoft Mark', 'Samantha', 'Google UK English Female', 'Microsoft Aria'];
  for (const p of pref) { const v = vs.find(v => v.name.includes(p)); if (v) return v; }
  return vs.find(v => v.localService) || vs[0] || null;
}

const Narrate = {
  beats: [], i: 0, playing: false, timers: [], utter: null, mode: 'est',
  reduced: matchMedia('(prefers-reduced-motion: reduce)').matches,
  WPM: 400, // ms per word at rate 1.0
  rate: 1.0, voiceURI: null, auto: false, askTimer: null, chapter: 19,

  loadPrefs() {
    try {
      const s = (typeof store !== 'undefined' && store.data) || JSON.parse(localStorage.getItem('adbms-exam-book-v1') || '{}');
      if (s.nrate) this.rate = Math.min(1.5, Math.max(0.7, +s.nrate));
      if (s.nvoice) this.voiceURI = s.nvoice;
      if (s.nauto) this.auto = !!s.nauto;
    } catch {}
  },
  savePrefs() {
    try {
      if (typeof store !== 'undefined') {
        store.data.nrate = this.rate; store.data.nvoice = this.voiceURI; store.save();
      }
    } catch {}
  },

  init(beats, stageId) {
    this.loadPrefs();
    this.beats = beats;
    this.stage = document.getElementById(stageId || 'stage');
    this.cap = document.getElementById('caption');
    this.dots = document.getElementById('beatdots');
    this.buildDots();
    this.bindKeys();
    if ('speechSynthesis' in window) {
      const load = () => pickVoice();
      speechSynthesis.onvoiceschanged = load; load();
    }
    this.showBeat(0, false);
  },
  buildDots() {
    if (!this.dots) return;
    this.dots.innerHTML = '';
    this.beats.forEach((b, i) => {
      const d = document.createElement('button');
      d.className = 'bdot'; d.textContent = b.short || (i + 1);
      d.title = b.title; d.onclick = () => this.showBeat(i, false);
      this.dots.append(d);
    });
  },
  markDots() {
    if (!this.dots) return;
    [...this.dots.children].forEach((d, i) => d.classList.toggle('on', i === this.i));
  },
  clearTimers() { this.timers.forEach(clearTimeout); this.timers = []; },
  stop() {
    this.playing = false;
    this.clearTimers();
    if (this.askTimer) { clearInterval(this.askTimer); this.askTimer = null; }
    try { speechSynthesis.cancel(); } catch {}
    const p = document.getElementById('btnplay');
    if (p) p.textContent = '▶ Play';
  },
  showBeat(i, autoplay) {
    this.stop();
    this.i = Math.max(0, Math.min(this.beats.length - 1, i));
    const b = this.beats[this.i];
    this.markDots();
    document.getElementById('beattitle').textContent = `Beat ${this.i + 1}/${this.beats.length} · ${b.title}`;
    this.stage.innerHTML = b.svg;
    this.parsed = parseMarks(b.say);
    // reset steps
    this.fired = {};
    this.stage.querySelectorAll('[data-step]').forEach(elm => elm.classList.add('pre'));
    if (this.cap) this.cap.innerHTML = '<span class="dim">Press Play — or read the captions below.</span>';
    const ask = document.getElementById('ask');
    if (ask) ask.innerHTML = '';
    this.updateNav();
    if (autoplay) this.play();
    else if (b.static) this.revealAll();
  },
  revealAll() {
    this.stage.querySelectorAll('[data-step]').forEach(elm => elm.classList.remove('pre'));
  },
  fireStep(name) {
    if (this.fired[name]) return;
    this.fired[name] = true;
    this.stage.querySelectorAll(`[data-step="${name}"]`).forEach(elm => {
      elm.classList.remove('pre');
      if (elm.tagName === 'path' || elm.tagName === 'line') elm.classList.add('draw');
    });
  },
  schedule() {
    const { marks } = this.parsed;
    const base = this.reduced ? 0 : 1 / this.rate; // faster speech → earlier marks
    Object.entries(marks).forEach(([name, wi]) => {
      this.timers.push(setTimeout(() => this.fireStep(name), wi * this.WPM * base + 300));
    });
    // steps with numeric delays
    (this.beats[this.i].timed || []).forEach(([ms, name]) => {
      this.timers.push(setTimeout(() => this.fireStep(name), ms));
    });
  },
  speak() {
    const { clean, words } = this.parsed;
    if (!('speechSynthesis' in window)) return false;
    const u = new SpeechSynthesisUtterance(clean);
    const v = pickVoice();
    if (v) u.voice = v;
    u.rate = this.rate;
    let firstBoundary = 0;
    u.onboundary = e => {
      if (e.name !== 'word' || typeof e.charIndex !== 'number') return;
      if (!firstBoundary) firstBoundary = performance.now();
      let wi = 0;
      for (let k = 0; k < words.length; k++) if (words[k].off <= e.charIndex) wi = k;
      Object.entries(this.parsed.marks).forEach(([name, mwi]) => { if (mwi <= wi) this.fireStep(name); });
      this.captionAt(e.charIndex);
    };
    u.onend = () => this.onBeatSpoken();
    u.onerror = () => this.onBeatSpoken();
    this.utter = u;
    speechSynthesis.speak(u);
    // watchdog: if speech never starts (blocked autoplay, missing voices),
    // fall back to timed captions instead of hanging the beat
    const est = (this.parsed ? this.parsed.words.length : 40) * this.WPM / this.rate + 2500;
    this.timers.push(setTimeout(() => {
      if (!this.playing) return;
      try {
        if (!speechSynthesis.speaking) {
          speechSynthesis.cancel();
          if (this.cap) this.cap.textContent = this.parsed.clean;
          this.onBeatSpoken();
        }
      } catch {}
    }, est));
    return true;
  },
  captionAt(charIdx) {
    if (!this.cap) return;
    const sents = this.parsed.clean.match(/[^.?!]+[.?!]/g) || [this.parsed.clean];
    let acc = 0, cur = sents[0], idx = 0;
    sents.forEach((s, k) => { if (charIdx >= acc) { cur = s; idx = k; } acc += s.length + 1; });
    this.cap.innerHTML = sents.map((s, k) =>
      `<span class="${k === idx ? 'saying' : k < idx ? 'said' : ''}">${s.trim()}</span>`).join(' ');
  },
  play() {
    const b = this.beats[this.i];
    if (this.playing) { this.stop(); this.showBeat(this.i, false); return; }
    this.playing = true;
    const p = document.getElementById('btnplay');
    if (p) p.textContent = '⏸ Restart';
    this.schedule();
    const ok = this.speak();
    if (!ok) {
      // no speech API: timed captions only
      const sents = this.parsed.clean.match(/[^.?!]+[.?!]/g) || [this.parsed.clean];
      let acc = 600;
      sents.forEach(s => {
        this.timers.push(setTimeout(() => { if (this.cap) this.cap.textContent = s.trim(); }, acc));
        acc += s.split(/\s+/).length * this.WPM;
      });
      this.timers.push(setTimeout(() => this.onBeatSpoken(), acc + 400));
    } else if (this.cap) {
      this.cap.textContent = this.parsed.clean.split(/(?<=[.?!])\s/)[0];
    }
  },
  onBeatSpoken() {
    if (!this.playing) return;
    this.playing = false;
    const p = document.getElementById('btnplay');
    if (p) p.textContent = '▶ Replay';
    const b = this.beats[this.i];
    this.revealAll();
    if (b.ask) {
      this.renderAsk(b.ask);
      if (this.auto) this.watchAsk();
    } else if (this.auto) {
      this.timers.push(setTimeout(() => this.next(true), 1600));
    }
    this.updateNav(true);
  },
  watchAsk() {
    if (this.askTimer) clearInterval(this.askTimer);
    this.askTimer = setInterval(() => {
      const host = document.getElementById('ask');
      if (!host) return;
      const cards = [...host.querySelectorAll('.qcard')];
      if (!cards.length) return;
      const done = cards.every(c => [...c.querySelectorAll('.qopt')].every(o => o.disabled));
      if (done) {
        clearInterval(this.askTimer); this.askTimer = null;
        this.timers.push(setTimeout(() => this.next(true), 2200));
      }
    }, 600);
  },
  toggleAuto() {
    this.auto = !this.auto;
    try { if (typeof store !== 'undefined') { store.data.nauto = this.auto; store.save(); } } catch {}
    const b = document.getElementById('btnauto');
    if (b) { b.textContent = this.auto ? '⏩ Auto-play: ON' : '▶ Auto-play all'; b.classList.toggle('on', this.auto); }
    if (!this.auto && this.askTimer) { clearInterval(this.askTimer); this.askTimer = null; }
  },
  renderAsk(ask) {
    const host = document.getElementById('ask');
    if (!host || !window.renderChoice || !window.MCQ_BY_ID) return;
    host.innerHTML = '<h3>Quick check — answer from memory</h3>';
    ask.forEach(id => window.renderChoice(host, window.MCQ_BY_ID[id]));
  },
  setRate(r) {
    this.rate = Math.min(1.5, Math.max(0.7, +r));
    this.savePrefs();
    const lab = document.getElementById('ratelab');
    if (lab) lab.textContent = this.rate.toFixed(2).replace(/0$/, '') + '×';
  },
  setVoice(uri) { this.voiceURI = uri || null; this.savePrefs(); },
  listVoices() {
    try {
      return speechSynthesis.getVoices().filter(v => v.lang && v.lang.toLowerCase().startsWith('en'));
    } catch { return []; }
  },
  syncAutoBtn() {
    const b = document.getElementById('btnauto');
    if (b) { b.textContent = this.auto ? '⏩ Auto-play: ON' : '▶ Auto-play all'; b.classList.toggle('on', this.auto); }
  },
  updateNav(spoken) {
    const prev = document.getElementById('btnprev'), next = document.getElementById('btnnext');
    if (prev) prev.disabled = this.i === 0;
    if (next) next.textContent = this.i === this.beats.length - 1 ? 'Finish ✓' : 'Next beat →';
  },
  next() {
    if (this.i === this.beats.length - 1) {
      try { if (typeof markDone === 'function') markDone(this.chapter); } catch {}
      location.href = 'index.html#contents';
    } else this.showBeat(this.i + 1, true);
  },
  prev() { this.showBeat(this.i - 1, false); },
  bindKeys() {
    addEventListener('keydown', e => {
      if (e.target.matches('input,select,textarea')) return;
      if (e.code === 'Space') { e.preventDefault(); this.play(); }
      if (e.key === 'ArrowRight') this.next();
      if (e.key === 'ArrowLeft') this.prev();
    });
    addEventListener('pagehide', () => this.stop());
  },
};
