# Sermon Prep

A curated, passage-first research workspace. The first reusable Agent Skill is **Passage Prep**, which helps a preacher collect and mark up sources without outsourcing the preacher's own study, interpretation, or sermon writing.

## What Passage Prep creates

**Part 1 — Commentary Reading Room.** A readable collection of genuinely useful commentary excerpts, prioritizing trustworthy authors with compatible, Scripture-centered theological commitments. Preserve original words when licensing permits; highlight only the few passages worth attention. Provide source citations, original-page links, concise context, and ample annotation space.

**Part 2 — Sermon Workshop.** A distinct collection of individual sermon maps from a configurable list of trusted preachers. Find actual messages on the passage, explain the preacher's *real* flow in order, identify verifiable stories and illustrations, their placement and rhetorical purpose, Scripture connections, transitions, and landing. Include direct transcript/audio links, and short original-voice quotes only within copyright limits.

Both parts should make it **easier for the preacher to do their own reading and thinking**. No default AI sermon manuscript, main-point prescription, or prewritten application.

## Structure

- .github/skills/passage-prep/SKILL.md — installation-friendly, triggerable skill
- .github/skills/passage-prep/references/source-policy.md — trust/copyright/verification
- .github/skills/passage-prep/references/source-lists.md — editable author and pastor rosters
- .github/skills/passage-prep/references/output-format.md — two-part reading reader and markup conventions
- .github/skills/passage-prep/assets/reader-template.md — study document layout
- .github/skills/passage-prep/evals/evals.json — five realistic evaluation scenarios
- .github/skills/passage-prep/evals/README.md — testing and release checklist
- .github/skills/passage-prep/examples/matthew-5-4-smoke-test.md — initial verified use-case

## How to use

Ask your skill-compatible agent:

> Run Passage Prep for Matthew 5:4. Find relevant commentaries and original excerpts first. Then check my approved pastor list for sermons on this passage and show their flow, specific illustrations, and transcript links. Make a clean Google Doc I can highlight on my iPad. Don't write my sermon.

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

Status: v0.1 initial design, to be refined with more user-approved writers and real evaluation runs. 
