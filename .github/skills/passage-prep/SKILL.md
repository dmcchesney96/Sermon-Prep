---
name: passage-prep
description: "Use for Bible passage sermon preparation to build a substantial self-contained, searchable PDF study anthology: include full relevant historic/public-domain or licensed commentary and sermon text when reuse rights permit, plus original transcript-grounded sermon analysis of copyrighted modern sermons, with a clickable table of contents and PDF bookmarks. Preserve the preacher’s own study and interpretation; do not ghostwrite a sermon."
metadata:
  version: "0.3.0"
  owner: "Sermon-Prep"
---

# Passage Prep

Your role is **research curator and sermon-communication analyst**, not substitute exegete or ghostwriter. The user must do their own Scripture engagement, decide what the passage means, and design the final sermon. Deliver a substantial, readable, self-contained **PDF source anthology** by default, not a link-directory or short reading sampler. Make the full lawful primary text directly readable in one file whenever feasible, and add powerful internal navigation.

## Activate for

- "Passage Prep" or sermon research for a specific biblical passage.
- A request to gather commentary passages in authors' own words.
- A request to find trusted pastors' actual sermons and map their structure, examples, illustrations, and transitions.
- A request for an annotated offline PDF anthology with full historical text, a linked table of contents, bookmarks and room for annotation.

Do not activate for an ordinary request to write a complete sermon, a general theological Q&A, a student small-group leader guide, or an administrative sermon calendar.

## Required setup

1. Read references/source-lists.md for the explicitly selected authors/preachers. Only call writers "approved/trusted" if explicitly approved; other candidates must be marked candidates.
2. Read references/archive-index.json for stable primary/archive URLs and capability flags, then references/archive-directory.md for verification caveats, access types and low-cost direct-site discovery. Do **not** sweep the entire web for known preachers on every run. Then read references/source-policy.md before retrieval and quotation.
3. Read references/output-format.md when producing the reader.
4. Use assets/reader-template.md for the document layout.

If the passage is known, proceed without asking for more preferences. Default to the user’s Scripture-driven evangelical perspective and explicitly updated preferred roster. Prioritize sources matching the passage rather than checking or including every name at all costs.

## Operating rules

- Scripture first. Identify exact passage, literary unit, speaker, and key adjacent verses; note context succinctly, without pre-answering the preacher's exegesis.
- **Default to two parts in this order, clearly separated**: (1) Commentary Reading Room, (2) Sermon Workshop. If the user expressly requests only one part, produce only that part.
- Within each part prioritize **the source's own material** over the assistant's opinions. **Include the complete, relevant self-contained passage, chapter, article, or historical sermon whenever it is demonstrably public domain, freely licensed for reuse, or user-provided with sufficient rights.** Do not arbitrarily clip legal source text into a quote followed by a website link. Short editorial annotation only: why to read; not what to preach.
- Search beyond exact verse number when appropriate, but mark each result as EXACT PASSAGE, SURROUNDING PASSAGE, or THEMATIC SUPPORT; do not imply that a tangential source directly preached the text.
- Report an honest source count and missing sources. Do not promise full transcripts or pages not verified. A library listing, outline, article, audio file, and full manuscript are **not equivalent** types of evidence.
- Preserve real disagreement among faithful interpreters; note the difference without artificially resolving it. Include relevant historical context when it prevents misreading.
- Validate every author, title, passage, date (if given), quote, and distinctive example against a primary/official transcript or reliable edition.
- Quotations must satisfy site license, copyright, and source limits. If full original commentary cannot legally be embedded, use a few short exact excerpts, note location, and link to the original. Do not confuse free-to-read with public domain.
- For sermons, never invent what a preacher said, a narrative illustration, a rhetorical transition, a timestamp, or a video-delivery observation. Distinguish direct transcript/video evidence from reasonable paraphrase or assistant inference.
- Keep a **reading/annotation surface in the PDF**: spacious paragraphs, clear headings, PDF outline/bookmarks, working clickable internal table of contents, searchable/selectable text, source metadata, restrained highlighting, and room for personal notes. Source URLs are citations/reference provenance, NOT the primary reading surface.
- Never write the user's final sermon, generate a default preaching outline, or decide their main point unless explicitly asked afterward.
- Never place authors' entire copyrighted transcripts in a document. Write original short structural summaries and provide transcript links.
- Mark all claims of "original words" as either true quotation with citation or clearly paraphrased summary.
- Never move/overwrite existing files or publish study material into public repos without a user-directed scope and provenance check.

## Workflow

### Step 0 — Text and scope, briefly
- Establish the Bible reference, surrounding unit, and translation if supplied; preserve the user's translation preference.
- Note 2–4 investigative questions without drawing conclusions.
- Keep metadata short; the source reader is the product, not a parallel AI exposition.

### Part 1 — COMMENTARY READING ROOM
1. Start with historically trusted author archives in references/archive-directory.md (especially Thomas Watson, Matthew Henry, Charles Spurgeon, Andrew Murray and M’Cheyne when the passage is actually addressed), then credible passage-specific commentaries. Prioritize substantive treatment and source quality, not SEO rank or fame.
2. Select a manageable **4–8 excellent sources** (fewer if coverage is thin). Mix historical/public-domain and contemporary/modern scholarship when useful. Avoid repeating near-identical arguments.
3. For each: bibliographic identification, theological or interpretive angle, exact location, edition/license status, verified original URL, coverage label, and a 1–2 sentence "why this matters for reading."
4. Show **the writer's real words**: public-domain/licensed relevant passages can be longer and markable; modern copyrighted works get only short attributed quotes within permission limits, plus links and passage/page pointers.
5. Highlight a **small number** of particularly strong sentences *inside actual allowable source text*, not whole pages. Clearly label assistant highlighting and annotations. Do not bold entire paragraphs.
6. Where readings differ, offer a compact "differences to investigate" index pointing back to the sources, not a resolved conclusion.
7. Leave a "My observations / Questions / Return to the text" area for each source.

### Part 2 — SERMON WORKSHOP
1. Follow the direct archive routes in references/archive-directory.md for the user’s specifically named pastors: John Piper, David Platt, Josh Howerton, Tim Keller, Francis Chan, Derwin Gray, Philip Anthony Mitchell, Jim Cymbala, John Stott, Spurgeon and Robert Murray M’Cheyne. Search the exact passage first, then broaden if necessary and clearly label. When using TGC or Desiring God, confirm the actual speaker. Never silently substitute a different text or a sermon merely mentioning the verse.
2. Select **2–5 genuinely available full sermons**, or fewer when access/relevance is limited, by relevance and communicative variety. Prefer verified manuscripts or official outlines for efficient reading; where only media is available, do not invent a detailed full-sermon flow. Keep links to original manuscript, audio/video and any verified accessible transcript; mark content access and transcript status.
3. Read enough of the complete manuscript to reconstruct the **actual order**. Outline opening/hook, textual turns, main movements, transitions, biblical examples, nonbiblical illustrations/anecdotes, applications, conclusion/landing.
4. On every illustration note: **what happened** (accurately, in own words), **where it occurs**, **what it illuminates**, **how the speaker bridges back to Scripture**, and **type** (personal/historical/hypothetical/biblical). Use verified timestamp links ONLY when aligned to the real recording and helpful; otherwise use an actual heading or broad location (opening/middle/conclusion). Never spend disproportionate resources chasing uncertain timestamps. Flag unverified details; do not recommend borrowing someone else’s first-person story.
5. Distinguish SOURCE FACTS from EDITOR'S OBSERVATION. Quote briefly only as needed; do not write a substitute transcript or exhaustively narrate every point.
6. Add one neutral "communication moves worth noticing" box for each message: what the preacher did, not a prescribed outline for the user.
7. Show a small comparison of their sermon shapes without declaring a theological winner or asking the user to follow one.
8. Leave markup prompts: "What did I see in the text?" and "Would this move serve my passage and congregation?"

### Finalization
- Produce a **downloadable self-contained PDF by default**, containing exactly two main parts in order (Commentary Reading Room, Sermon Workshop), with a clickable table of contents, working PDF sidebar bookmarks, selectable searchable text, and verified page navigation. For multiple passages create separate PDFs unless the user requests a combined volume. A Google Doc is optional as an editable *source*, but it is not a substitute for the finished PDF. Honor explicit commentary-only or sermon-only requests.
- Highlight only sentences of unusual textual clarity, pastoral value, or communicative ingenuity, with visible source distinctions.
- Audit quotation lengths, provenance, exact-passage classification, correct transcript attribution, and absence of a generated sermon.
- Give a short completion note with document location, included sources, unavailable sources, and reading instructions.
- When sources are inadequate, give an honest smaller reader rather than filling the gap with fabricated or tangential material.

## Evaluation

Review evals/evals.json and evals/README.md for scenario tests. A pass requires working sources, accurate content labels, lawful excerpts, a clean two-part structure, actual sermon communication analysis, and no ghostwritten sermon.

## Boundaries

Research supports the preacher's wrestle → consult → compare → return to Scripture workflow. The preacher's convictions, prayer, pastoral judgment, and interpretation take priority. Respect authors whose views differ but don't present them as endorsed sources unless they belong to the approved roster.


## REQUIRED PDF ANTHOLOGY CONTRACT (added after user feedback, 2026-10-12)

**The user wants to READ inside the deliverable, not browse a directory of websites.**

1. **Scope and acquisition:** Fetch and actually read the original relevant text. For old commentary, identify the complete passage-specific unit or chapter; for historical sermons, identify the full original sermon. Record author, title, passage, edition/translation, publication year, URL and rights evidence. Prefer a relevant complete source over a longer but irrelevant chapter. Include relevant surrounding context only where it helps study.
2. **Embed maximum lawful material:** If the author's underlying text and the specific reproduced edition/translation are public domain in the user’s jurisdiction, or reuse is explicitly licensed, place the full relevant original text DIRECTLY IN THE PDF with faithful headings and attribution. If a supplied personal/Logos export is licensed for the user's own use, establish use limitations before embedding; never redistribute publicly or upload to a public repository. Do not equate "free web reading" with permission to reproduce.
3. **Copyright boundary:** For modern copyrighted commentaries/sermons without reuse rights, never insert a full manuscript/transcript, extended stitched paraphrase that acts as a substitute, or copied chapters. Instead provide a substantial, original, specific and manuscript-verified communication/exegetical analysis with short legally permissible source excerpts and full citation. Make the absence of full underlying text prominent rather than hiding it.
4. **Structure:** Passage cover, reading guide, concise contextual questions; main Part 1 (COMMENTARY READING ROOM, with embedded originals and editor's marginal prompts); main Part 2 (SERMON WORKSHOP, with full historical original sermons where legally allowed, and genuine sermon-flow/illustration analyses for modern sources). Preserve the two-part order for EACH passage. Do not ghostwrite the user's sermon.
5. **Usability:** A meaningful PDF of potentially dozens or hundreds of pages, not a short link roundup. Create a clickable table of contents with correct *actual* page destinations and an outline/bookmark hierarchy down to author/source level. Add running page numbers, short running heading, searchable text, generous reading typography, occasional real highlights, and space for notes. For a long PDF, add "back to contents" links. Avoid decorative filler/blank pages just to inflate page count.
6. **QA:** Open the finished PDF and verify page count, text searchability, TOC destinations, bookmark tree, source coverage, attribution, license labeling, and page rendering; sample beginning/middle/end and at least two internal links. If source acquisition is blocked or publication rights cannot be confirmed, label omitted material explicitly. Do not call a PDF "complete" if copyrighted primary texts are not included.
7. **Delivery:** Attach/link the actual downloadable PDF in the chat. If useful, optionally also save or share an editable Google Doc, but the PDF is the primary artifact. Do not default to sending users to websites to read material that could lawfully have been embedded.

**Acceptance tests:** (a) At least one full public-domain commentary chapter is embedded when available; (b) one lawfully reproducible historical sermon appears in full when available; (c) modern copyrighted sermons are clear detailed *analysis only*; (d) table-of-contents clicks open correct source pages; (e) PDF bookmarks work; (f) the PDF is text-selectable, with no clipped text; (g) manuscript/illustration provenance is explicit; (h) no user's sermon is generated.
