# Bench Buddy

## The spark
Half of everything carried into a Repair Café leaves fixed. A quarter leaves declared dead, and most of that quarter was killable only because a volunteer with a screwdriver in one hand and a phone in the other ran out of time hunting for a part number. The device was fine. The search was broken.

Picture Saturday at the library in Utrecht. A woman brings a ten-year-old Miele vacuum. The fixer opens it in four minutes, finds a burnt thermal fuse, and instead of thirty minutes of forum tabs types "Miele S5 thermal fuse" into one box and gets the part, two sellers, and a teardown link in three seconds. She goes home with a working vacuum and no new one gets made.

I'd tell a friend: it's a search box for the moment the device is already open on the bench. The Builder lens put it best: "The dataset already exists and it's public; the only thing missing is the index."

## The problem
Volunteer fixers at community repair events open a device, then search supplier sites and forums by phone for a part or a schematic inside a 20 to 30 minute slot. About a quarter of items are declared end of life and 18% are logged as repairable but not repaired on the day, mostly for lack of a part, time or skill. Parts and manuals are scattered with no shared index by device model. Evidence: Open Repair Alliance report 2024 and supporting data, over 100,000 repair records.

## The idea
A single command-line lookup that takes a brand and model, cross-references the Open Repair Alliance dataset for known faults on that model, and returns the three most likely failed parts with links to where earlier fixers found them. Fixers add "found it here" links in one line after a repair, which is how the index grows.
What it is NOT: not a marketplace, not a manufacturer portal, not a chat assistant that guesses.

## Values fit
- Circularity: strong — every repair keeps a device in the loop and every lookup feeds the next one.
- Sustainability: strong — a repaired vacuum is a vacuum not manufactured.
- AI for good: medium — the intelligence is in matching fault descriptions to parts; retrieval does most of the work.

## Council verdicts
- Jobs: one box, one result list, no accounts; cut the "add a link" feature until someone asks.
- Einstein: if every part were free and instant, the bottleneck would be diagnosis, so lead with fault-to-part matching, not sellers.
- Gandhi: serves volunteers and owners; the only cost is fixers' time entering links, which must stay optional.
- Ostrom: the index must live in the Open Repair Alliance's open data, not in this tool, or it gets captured; the Jobs lens is wrong to cut the contribution path.
- Builder: the dataset is public CSV; a weekend is enough for ingest plus one command.
Open question I chose not to answer: who moderates a bad link once fixers start adding them?

## Weekend scope
Ships: a CLI that ingests the ORA CSV once and answers "brand model" with the top faults and known part sources.
Stack: Python, SQLite, one script, no web.
Data source: Open Repair Alliance open data export (CSV, CC BY-SA).
The one screen or command: `bench "Miele S5"`.

## First prompt for Claude Code
```
Create a Python CLI called `bench` in a new folder `bench-buddy/`. Download the latest Open Repair Alliance
open data CSV, ingest it into SQLite, and implement `bench "<brand> <model>"` which prints the top 3 fault
categories for that model, their repair rates, and any URLs found in the free-text problem field. Done means:
`bench "Miele S5"` returns results in under a second on a laptop, and `bench --add "<brand> <model>" <url>`
appends a source link that shows up in the next query.
```

## Kill criteria
- If the ORA free-text field contains fewer than 500 usable URLs after ingest, stop; check on day 1 before building the query side.
- If two Repair Café fixers try it and neither uses it a second time within a month, stop; check on 2026-11-01.
