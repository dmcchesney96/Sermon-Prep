# Passage Prep evaluations

Purpose: ensure this skill curates sources and exposes genuine sermon craft, without outsourcing interpretation or fabricating sermon content.

## How to run

1. Use the prompt for each case in evals.json with a skill-aware agent.
2. Collect the actual two-part reader or documented unavailable-source response.
3. Verify the listed assertions against the actual output and the primary manuscripts.
4. Mark each assertion PASS/FAIL with a quote, document location, or screenshot.
5. When an assertion fails, propose a change in SKILL.md, sources, or output-format. Keep the input and output as a regression example.
6. For the Matthew 5:4 pilot, explicitly compare John Piper's February 2, 1986 sermon (direct exposition of 5:3–4) with David Platt's “The Good Life Redefined” (the 5:4 teaching occurs in a recap of a sermon mainly on 5:7–12). The map must NOT turn Platt's recap into a dedicated 5:4 sermon.

## New archive-routing checks (v0.2)

- For Josh Howerton, check Lakepointe messages/podcast before any broad web search. Treat spoken.md as independent, possibly metered transcription—not official evidence.
- For Derwin Gray, distinguish Transformation Church's official sermon outline from a complete recorded transcript.
- For Philip Anthony Mitchell and Jim Cymbala, an audio/video listing alone is not proof of a full manuscript. Give media links without inventing precise illustrations, timing or vocal delivery.
- For Tim Keller, use Gospel in Life's Scripture filter; do not assume all entries have text transcripts.
- For John Stott, note the extensive Logos sermon archive is licensed, not an openly reproducible transcript collection.
- For Andrew Murray, distinguish real treatment of the passage from a devotional thematic overlap.
- Timestamps should be omitted gracefully unless independently checked in the exact recording. Their absence is never a failure.

## Check categories

- **Trigger:** activates on research and reading packet requests; NOT on pure sermon writing or unrelated ministry admin.
- **Commentary:** citations verified; original wording only when reuse permissible; diverse arguments not crushed into a single assistant view.
- **Sermon:** true chronology, memorable specific examples, no invented illustrations, exact text coverage labeled.
- **Agency:** enough original material to read and annotate; no assistant-produced final sermon thesis/points in place of user.
- **Rendering:** two clearly separated parts, working links, **actual soft-yellow highlighted source wording on original reading pages**, generous annotation space. A highlighted summary is not enough.

## Mandatory highlight quality test — v0.4

1. Select genuine helpful original passages only *after* reading the original historical chapter or sermon. Verify exact selected wording, author's attribution and chapter position.
2. Prioritize thoughtfully: roughly 1–3 highlights for short pieces, 3–8 for a substantial chapter when warranted. Avoid automatic page quotas, marking whole paragraphs or highlighting more than about 10% of the source.
3. Examine PDF beginning, middle, and end for in-place source-text highlights, correct positioning, legibility and searchable/selectable underlying words.
4. Use native PDF highlight annotations when possible; otherwise document a visually tested behind-text yellow fallback.
5. If a brief 'Study trail' is created, confirm it links directly to highlighted source passages.
6. Fail if only a separate quote list, editorial note, or TOC is highlighted while the authorial body text remains unmarked.

## Tested versus planned

Files here are **evaluation scenarios**, not claims that the agent has executed them all. Record actual run date, sources, results, and concrete failures only after running a complete output test.

### Initial static validation to perform after installation

- SKILL.md frontmatter opens and closes properly.
- name field equals passage-prep and the parent folder name.
- description field is nonempty and the intent is discoverable.
- all four reference/template paths cited in the skill exist.
- evals.json parses and contains >=5 cases with observable assertions.
- copyright safeguards and exact-passage labeling are present.
