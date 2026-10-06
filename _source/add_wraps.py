import pathlib

wraps = {
 1: "1) DBMS = define, store, retrieve, update, protect, recover. 2) External=user views, Conceptual=blueprint, Internal=storage. 3) Physical independence = storage changes; logical = schema changes; schema=blueprint, instance=data now.",
 2: "1) Thing=entity, detail=attribute, association=relationship. 2) 1:N → FK on N side; M:N → junction table. 3) Cardinality=how many; participation=mandatory-or-optional — never swap them.",
 3: "1) σ=rows, π=columns. 2) DDL Defines, DML Manipulates, DCL Controls, TCL Tames. 3) WHERE filters rows → GROUP BY → HAVING filters groups; PK can never be NULL.",
 4: "1) Closure X⁺ → key = smallest set reaching everything. 2) Ladder: atomic (1NF) → whole-key (2NF) → no transitive (3NF=OR) → determinant-superkey (BCNF=ONLY). 3) Lossless = intersection is a super key of one part; preservation = FDs checkable without joins.",
 5: "1) B+ tree = sorted + linked leaves → ranges fast (B for Between). 2) Hash = bucket from key → equality fast (H for Has-exactly). 3) Indexes = faster reads, slower writes, extra storage.",
 6: "1) Insert anomaly = can't add a fact without unrelated data. 2) Update anomaly = one fact in many places → inconsistency. 3) Delete anomaly = deleting a row destroys unrelated facts; normalization cures all three.",
 7: "1) Transaction = one logical unit; states Active → Partially Committed → Committed. 2) A=all-or-nothing, C=correct state, I=isolated, D=durable after commit. 3) Isolation ladder weakest→strongest: Read Uncommitted → Read Committed → Repeatable Read → Serializable.",
 8: "1) Anomalies: Lost=overwrite, Dirty=uncommitted, Non-repeatable=same row new value, Phantom=new row. 2) Precedence graph: cycle = NOT serializable. 3) 2PL: grow=grab, shrink=surrender, never regrow; deadlock = circular wait, caught by wait-for graph.",
 9: "1) Deferred = Delay → REDO only. 2) Immediate = I need both → UNDO+REDO. 3) WAL = log before data, always; checkpoint bounds where recovery starts; shadow paging = switch root pointer, no UNDO.",
 10: "1) Horizontal=rows (σ), vertical=columns (π, key kept); rebuild: UNION / JOIN-on-key. 2) 2PC: Prepare→vote→Commit/Abort; any NO = global abort; blocking = its drawback. 3) CAP = at most two of C/A/P *during a partition* — never 'any two at all times'; BASE = Basically Available, Soft state, Eventual consistency.",
 11: "1) MongoDB: table→collection, row→document; pipeline $match first. 2) Cassandra: partition key=where, clustering=order. 3) Redis=key-value+TTL, Neo4j=graph traversal, vectors: cosine=angle, HNSW=graph, IVF=clusters.",
 12: "1) Define 5–7 lines → 2) diagram + components under headings → 3) example, pros/cons, 3–4 line conclusion on correctness/speed/reliability.",
}

p = pathlib.Path('exam/notes/learning-path-from-zero.md')
t = p.read_text(encoding='utf-8')
lines = t.splitlines()
out = []
lesson = 0
for line in lines:
    if line.startswith('### Lesson '):
        lesson = int(line.split('Lesson ')[1].split(' ')[0])
    out.append(line)
    if line.startswith('**Checkpoint →**') and lesson in wraps:
        out.append(f"**Wrap (3 steps):** {wraps[lesson]}")
p.write_text('\n'.join(out) + '\n', encoding='utf-8')
print('inserted wraps for lessons:', sorted(wraps))
