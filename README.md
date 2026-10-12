# Sermon Prep

A curated, passage-first research workspace. The first reusable Agent Skill is **Passage Prep**, which helps a preacher collect and mark up sources without outsourcing the preacher's own study, interpretation, or sermon writing.

## What Passage Prep creates

**Part 1 — Commentary Reading Room.** A substantial offline PDF anthology of COMPLETE relevant public-domain or explicitly reusable commentary chapters/units, prioritizing trustworthy authors with compatible, Scripture-centered theological commitments. Preserve authorial wording and context, with selective, visible yellow highlighting directly on important original words, edition/rights notes, source citations and annotation space. Modern copyrighted works get original analytical notes and short lawful quotes, not unauthorized full copied chapters.

**Part 2 — Sermon Workshop.** Include FULL original historical public-domain sermons directly in the PDF when relevant and permissible, and detailed manuscript-grounded maps of modern copyrighted sermons (not copied modern transcripts). Explain the preacher's *real* flow in order, identify verifiable stories and illustrations, their placement and rhetorical purpose, Scripture connections, transitions and landing. Cite original sources; use only short copyright-permitted modern quotes.

Both parts should make it **easier for the preacher to do their own reading and thinking**, without leaving the PDF to consult historic works. **The default deliverable is a downloadable PDF** with searchable/selectable text, clickable internal table of contents, native outline/bookmarks, page numbers and room for annotation. Source web links document provenance; they do not replace full lawfully reusable source text. The required editorial highlight pass selectively marks the most valuable source wording **inside the PDF itself**, not just in a summary. No default AI sermon manuscript, main-point prescription, or prewritten application.

## Structure

- .github/skills/passage-prep/SKILL.md — installation-friendly, triggerable skill
- .github/skills/passage-prep/references/source-policy.md — trust/copyright/verification
- .github/skills/passage-prep/references/source-lists.md — editable approved author and pastor rosters
- .github/skills/passage-prep/references/archive-directory.md — verified archive URLs, access types and timestamp safeguards
- .github/skills/passage-prep/references/archive-index.json — machine-readable index of 15 direct sources and access conditions
- .github/skills/passage-prep/references/output-format.md — two-part reading reader and markup conventions
- .github/skills/passage-prep/assets/reader-template.md — study document layout
- .github/skills/passage-prep/evals/evals.json — five realistic evaluation scenarios
- .github/skills/passage-prep/evals/README.md — testing and release checklist
- .github/skills/passage-prep/examples/matthew-5-4-smoke-test.md — initial verified use-case

## How to use

Ask your skill-compatible agent:

> Run Passage Prep for Matthew 5:4. Make one LARGE self-contained searchable PDF with full relevant public-domain commentary chapters and historical sermons embedded, detailed source-verified maps and examples from modern sermons, and a clickable table of contents plus PDF sidebar bookmarks. Highlight the most helpful exact passages in yellow within the original source text so I can skim them. I want to read everything I legally can inside the file, not click away to websites. Don't write my sermon.

Other examples: "Passage Prep for 1 Samuel 20" or "Passage Prep for Luke 15, just the commentaries."

Skills-compatible clients typically discover skills from the .github/skills location; if your client doesn't, point it to the SKILL.md path.

## Philosophy and safeguards

- Read and wrestle with the passage yourself; let the text govern all research.
- Separate SOURCE (what the actual preacher/commentator said) from EDITOR (why it might repay attention).
- Label exact-passage expositions separately from adjacent or thematic sources.
- Do not fabricate sermons, books, quotes, anecdotes, page numbers, or illustrations.
- Do not reproduce substantial copyrighted sermons/commentary chapters from the web. Use short attributed quotations and original explanatory summaries plus links; preserve full passages only where licensed, public-domain, user-owned, or otherwise authorized.
- Keep an independent record of sources, dates, permission status, and what was actually examined.
- No automatic publishing or overwriting another document without a clear request.

Status: v0.4. Mandatory, visually verified in-text highlighting was added October 12, 2026. Previous PDF-first release: v0.3. Default revised October 12, 2026, after user feedback that link-based Google Docs did not meet the desired reading workflow. Source acquisition, full lawful source inclusion, a substantial downloadable PDF, clickable table of contents, bookmarks and quality checks are now required. Previous status: v0.2. The approved source list was expanded by user request on October 11, 2026. A dedicated [archive directory](.github/skills/passage-prep/references/archive-directory.md) records exact starting URLs, text availability, and targeted search routes for Josh Howerton, Piper, Platt, Keller, Chan, Gray, Philip Anthony Mitchell, Jim Cymbala, Stott, Spurgeon, M’Cheyne, and historical commentary authors. Timestamps are optional and must be verified. Full end-to-end evaluations remain to be run. 
