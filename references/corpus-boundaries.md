# Corpus Boundaries

- External snapshot: 768 records from official `developer.ninjatrader.com`, `docs.ninjatrader.com`, and `ninjatrader.com` sources.
- Source index: `references/source-index.jsonl` contains the portable public index for that snapshot: record ID, canonical URL, title, focused track, reference version, and classification.
- Reference build: NinjaTrader 8.1.8.2.
- Version status: most records are ambiguous because reliable publication/update dates were unavailable.
- Retrieval: bounded local HTTPS workflow; Exa was used only for discovery/cross-checking, never as source content.
- Safety: downloaded code was not executed; examples were not compiled.
- Runtime: no authorized NinjaTrader installation, provider session, compiler, or runtime harness was available.
- Graph: deterministic structural extraction only; 768 nodes, 6,222 explicit reference edges, zero dangling endpoints, self-loops, or missing endpoints.
- Known gaps: provider-specific availability, licensing details, generated-code behavior, testing, deployment, and runtime verification.

The focused corpus is suitable for practical indicator coding but does not establish exhaustive official coverage. The source index identifies the public source records; it does not bundle the external snapshot or claim that its source pages remain unchanged.
