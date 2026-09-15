---
description: Run a MUSE session. Start when blank, end with a spec in sessions/.
---

Run a MUSE session. Follow `CLAUDE.md` for all rules, the council lenses and the spec format.
Target: 20 minutes. Six steps. One question per turn. End your turn every time you ask something.

Today's date is the date in the environment. Use it for filenames and frontmatter.

## Before step 1 (silent)

Do all of this without printing anything:

1. Read `values.md` and `memory.md`.
2. Read every `problems/*.md` except `_template.md`. Parse frontmatter. Keep the ones with `status: open`.
   If there are none, say so in one line and stop: "No open problems. Run /harvest first."
3. Read every `ideas/*.md` except `_template.md`. Note any whose `status` or status log changed since the
   most recent line in the "Blank types" section of `memory.md` (that line's date is the last session).
4. Rank open problems: `score` descending, then `freshness` descending. Steer with `memory.md`: nudge
   up problems that resemble "What I flinch at", nudge down ones that resemble "What bores me".
   Do not filter anything out on memory alone.
5. Pick the top 3 as the flinch set. Keep the rest, in order, as the reject queue.

## Step 1 — Check-in

Ask exactly one question:

> What kind of blank: bored, stuck, or overwhelmed?

End your turn. When the answer comes, set the mode from the "Tone by blank type" table in `CLAUDE.md`.
If the answer is none of the three, map it to the closest one, say which in three words, and continue.

## Step 2 — Since last time

One short block, then straight into step 3 without asking anything. Maximum 3 items in any list.

- If there are idea changes since the last session: up to 3 lines, one per idea, "<name>: <old status> → <new status>".
  If there are none: one line, "No idea changes since last time." If there has never been a session: skip this line.
- Then: "Three freshest problems worth your attention:" followed by the flinch set, one line each,
  `<title> (<domain>, <score>/5)`. No descriptions yet.

Then immediately begin step 3 in the same turn.

## Step 3 — Flinch test

Present the flinch-set problems **one at a time**. For each:

1. Print the title, then the "Who" and "What they do today instead" sections compressed into 3 sentences. No evidence links yet.
2. Ask exactly: "One line: what annoys you about this?"
3. End your turn.

After all three answers, apply "Energy detection" from `CLAUDE.md`. Pick one. Confirm in one sentence:
"Most energy in <title>. Go with that?" End your turn.

- Yes: mark that problem's frontmatter `status: picked` and go to step 4.
- No, or the user names a different one: take their pick without argument, mark it `picked`, go to step 4.

## Step 4 — Council

Run the five lenses on the picked problem per "The council" in `CLAUDE.md`: mode-dependent speaking order,
2–3 sentences each (2 in overwhelmed mode), one hard question each, and at least one explicit disagreement
where a lens names another lens and contradicts it. Check the disagreement rule before printing.

Close with: "Answer any of the hard questions you want to. Silence is fine." End your turn.

Whatever the user answers (including nothing), note which questions went unanswered. Do not comment on
the user's silence. Do not re-ask.

## Step 5 — Idea lock

Propose one idea, one paragraph. It must be a concrete thing that can be built: a tool, a command, a
dataset with an interface, a device. It must use the user's answers where they exist. In overwhelmed mode
it must remove a step from what the "Who" does today rather than add one.

Then ask exactly: "Accept, twist, or reject?" End your turn.

- **Accept**: go to step 6.
- **Twist**: apply the change, restate the idea in one paragraph, ask "Accept, twist, or reject?" again.
  Twists are unlimited and do not count as loops.
- **Reject**: increment the reject counter. If it is now 3, stop per the "Idea lock" section of `CLAUDE.md`
  (say the session is out of problems, write no spec, append to `memory.md`, end). Otherwise set the
  picked problem back to `status: open`, take the next problem from the reject queue, and run step 3 for
  that single problem (present it, ask the one-line question, confirm). Then re-run step 4 and step 5.

## Step 6 — Spec

1. Write `sessions/<YYYY-MM-DD>-<slug>.md` in exactly the "Spec output format" from `CLAUDE.md`.
   Write "The spark" last, following "The spark" rules, then place it first in the file.
   The council verdicts must be the real lenses from step 4, condensed. The open question must be one the
   user actually did not answer.
2. Run `python3 tests/check_spec.py sessions/<file>` and fix the spec until it passes. Do not print the
   spec to the terminal; the file is the deliverable.
3. Create `ideas/<slug>.md` from `ideas/_template.md`, status `specced`, linking the problem and the session.
4. Set the picked problem's frontmatter to `status: specced`.
5. Append to `memory.md`, one dated line each, without rewriting anything above:
   - "What I pick": the shape of what was chosen (domain, who it serves, interface type).
   - "What I flinch at": the flinch answer with the most energy, quoted or closely paraphrased.
   - "What bores me": any flinch answer with clearly no energy, if there was one.
   - "Blank types": `<date>: <blank type> — spec written: <slug>`.
6. Print two lines only: the path of the spec and the first paragraph of "The spark". Stop.
