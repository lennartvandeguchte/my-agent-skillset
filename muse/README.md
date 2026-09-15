# MUSE

Personal, on-demand session tool. Input: "I'm blank." Output: a written spec for one thing worth
building, aligned with my values. One user, no retention, no auth, no polish.

v1 is a Claude Code project: there is no code to run beyond the prompts in this folder and one test.

## Run

```
cd muse
claude
```

Then type one of:

- `/session` — the interactive session. Six steps, target 20 minutes, ends with a spec in `sessions/`.
- `/harvest` — background agent. Finds real, specific problems in your domains and writes them to
  `problems/`; checks `ideas/` for status changes; updates `memory.md`.

Run `/harvest` before a session so it never starts from zero. Non-interactive, for cron:

```
cd /path/to/muse && claude -p "/harvest"
```

## Files

| Path                          | What                                                                |
|-------------------------------|---------------------------------------------------------------------|
| `values.md`                   | Values (filter), domains (steering), anti-patterns (hard rejects). Edit by hand. |
| `memory.md`                   | The agent's dated notes on you. Append-only.                        |
| `problems/`                   | One markdown file per harvested problem, with frontmatter and score. |
| `ideas/`                      | One file per idea ever produced, with a status you maintain by hand. |
| `sessions/`                   | One spec per session, `YYYY-MM-DD-slug.md`.                         |
| `CLAUDE.md`                   | Session rules, council lenses, spec format. The agent's constitution. |
| `.claude/commands/session.md` | The `/session` procedure.                                           |
| `.claude/commands/harvest.md` | The `/harvest` procedure.                                           |
| `tests/check_spec.py`         | Verifies a spec has every section, in order, with the required lines. |

Four seed problems ship in `problems/`, one per default domain, so the first `/session` works
before the first `/harvest`.

## Test

```
python3 tests/check_spec.py                       # all specs in sessions/ plus the fixture
python3 tests/check_spec.py sessions/<file>.md    # one spec
```

The session runs this itself after writing a spec and fixes the spec until it passes.

## Maintaining ideas

After a session, `ideas/<slug>.md` has `status: specced`. Change it yourself as things happen:
`building`, `shipped`, `abandoned`, `killed` (note which kill criterion fired). The harvester sets
`superseded` when it finds someone else shipped the same thing, and never touches your statuses.

## Tuning

- Council not disagreeing enough: edit the "Disagreement rule" and "fault lines" in `CLAUDE.md`.
- Spark not making you want to open Claude Code: rewrite "The spark" rules in `CLAUDE.md`, not the
  individual spark.
- Harvester finding vague problems: tighten the acceptance rule in `CLAUDE.md`, or narrow the
  domains in `values.md`.
- Add a lens: add it to "The council" in `CLAUDE.md`, to `REQUIRED_LINES["Council verdicts"]` in
  `tests/check_spec.py`, and to the "Council verdicts" section of the spec format.

## v2 (only if needed)

Port to the Agent SDK (`@anthropic-ai/claude-agent-sdk`, TypeScript, auth via `claude login`) with the
same folder layout and the same two commands as `muse harvest` / `muse session`. Not started.
