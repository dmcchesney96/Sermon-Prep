# Passage Prep evaluations

Purpose: ensure this skill curates sources and exposes genuine sermon craft, without outsourcing interpretation or fabricating sermon content.

## How to run

1. Use the prompt for each case in evals.json with a skill-aware agent.
2. Collect the actual two-part reader or documented unavailable-source response.
3. Verify the listed assertions against the actual output and the primary manuscripts.
4. Mark each assertion PASS/FAIL with a quote, document location, or screenshot.
5. When an assertion fails, propose a change in SKILL.md, sources, or output-format. Keep the input and output as a regression example.
6. For the Matthew 5:4 pilot, explicitly compare John Piper's February 2, 1986 sermon (direct exposition of 5:3–4) with David Platt's “The Good Life Redefined” (the 5:4 teaching occurs in a recap of a sermon mainly on 5:7–12). The map must NOT turn Platt's recap into a dedicated 5:4 sermon.

## Check categories

- **Trigger:** activates on research and reading packet requests; NOT on pure sermon writing or unrelated ministry admin.
- **Commentary:** citations verified; original wording only when reuse permissible; diverse arguments not crushed into a single assistant view.
- **Sermon:** true chronology, memorable specific examples, no invented illustrations, exact text coverage labeled.
- **Agency:** enough original material to read and annotate; no assistant-produced final sermon thesis/points in place of user.
- **Rendering:** two clearly separated parts, working links, actual highlighted phrases, generous annotation space.

## Tested versus planned

Files here are **evaluation scenarios**, not claims that the agent has executed them all. Record actual run date, sources, results, and concrete failures only after running a complete output test.

### Initial static validation to perform after installation

- SKILL.md frontmatter opens and closes properly.
- name field equals passage-prep and the parent folder name.
- description field is nonempty and the intent is discoverable.
- all four reference/template paths cited in the skill exist.
- evals.json parses and contains >=5 cases with observable assertions.
- copyright safeguards and exact-passage labeling are present.
