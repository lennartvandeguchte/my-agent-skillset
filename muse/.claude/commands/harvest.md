---
description: Background harvest. Find real, specific, unsolved problems in the user's domains; update ideas and memory.
---

Run a MUSE harvest. Follow `CLAUDE.md` for the problem file format, the acceptance rule and the folder
layout. This is background work: no questions to the user, no conversation. Work, write files, print a
short report at the end.

Today's date is the date in the environment.

## 1. Read

Read `values.md` (values, domains, anti-patterns) and `memory.md`. Read the titles and frontmatter of every
existing `problems/*.md` and `ideas/*.md` (skip `_template.md`), so you do not create duplicates.

## 2. Search for frictions

For **each** domain in `values.md`, run at least 3 web searches. Look for **specific, unsolved, real**
frictions: things a named group of people put up with today. Good sources: trade press, industry
reports, forum threads, government or municipal reports, academic papers with practical findings,
repair and recycling operator blogs, regulatory guidance and its complaints.

Search strategies that work:
- "<domain> workaround", "<domain> manual process", "<domain> still done by hand"
- "<domain> operators complain", "<domain> bottleneck", "<domain> why is it hard"
- "<domain> report <this year>", "<domain> pilot failed"
- Search in Dutch as well as English for local frictions (the user is in the Netherlands).

Use `memory.md` to steer: search more in the neighbourhood of "What I flinch at", less near "What bores me".
Values are the filter, domains are the steering. Never search outside the domains.

## 3. Accept or reject

Apply the acceptance rule from `CLAUDE.md` to every candidate. A problem must name **who** has it and
**what they do today instead**. Reject anything that:
- describes a topic, trend or statistic without a person and a workaround ("textile waste is bad");
- is already solved by a shipped product the target group actually uses (check with one search);
- matches an anti-pattern in `values.md`;
- duplicates an existing file in `problems/` (same who + same friction). If the existing file is older,
  update its Evidence and freshness instead of creating a new file, and add a Harvest note.

Aim for **2 to 4 accepted problems per domain per harvest**, not more. Quality over count. Every accepted
problem needs at least 2 evidence links you actually opened, with the freshest date you found.

## 4. Write problem files

For each accepted problem, write `problems/<slug>.md` in exactly the "Problem file format" from `CLAUDE.md`.
Score 1–5 for fit with the three values together, honestly: a problem that only serves sustainability
and has no circular loop and no role for intelligence is a 2, not a 4. Set `status: open`, `source: harvest`,
and one Harvest note: `<date>: created`.

Mark any existing problem `status: stale` if its newest evidence is more than 18 months old and a search
finds nothing newer. Do not delete files.

## 5. Check ideas

For every `ideas/*.md` with status `specced`, `building` or `shipped`:
- Run one or two searches: has someone shipped this, or something close, since `last_checked`?
- Has the underlying problem shifted (regulation passed, the workaround disappeared, the group changed)?
- Append one dated line to its "Status log" with what you found, or "no change". Update `last_checked`.
- If someone shipped the same thing for the same group, set `status: superseded` and link the evidence.
  Do not change any other status; those belong to the user.

## 6. Update memory

Append one dated line to the "Harvest notes" section of `memory.md`: domains searched, problems accepted /
rejected, anything surprising. If you noticed a pattern across `ideas/` (for example, specced ideas that are
never marked building all share a shape), append one line to "What I abandon". Never rewrite existing lines.

## 7. Report

Print at most 6 lines: problems created, problems updated, problems marked stale, ideas changed, and
the single most promising new problem with its score. Then stop.
