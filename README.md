# Lessons from Ars Inquirendi 2026

Notes and data from [Ars Inquirendi 2026](https://www.arsinq.com/), "Querying Pre-Print Cultures with LLMs", St Edmund Hall, Oxford, 20–22 November 2026.

## What is here

- **[index.html](index.html)**: a searchable, interlinked list of every AI model, dataset, archive, tool, training or adaptation method, benchmark and paper named by participants. It has 160 distinct items. You can:
  - browse by type, by session, by speaker, or see only items shared between sessions
  - search with accents ignored, and filter by type, openness and day
  - click a speaker to see everything they named
  - link to any item with `#item-<id>`

  Open the file in a browser; it needs no server.
- **[resources.md](resources.md)**: the same list as Markdown, grouped by type.
- **[data/](data/)**: the data as JSON (with every mention by session and speaker) and as CSV.

## How it was compiled

Three research agents, one for each conference day, read these sources on 20 November 2026:
- the public programme and abstracts on arsinq.com
- the slides, papers and repositories linked from them
- machine transcripts of the Graphosphere I recordings
- notes on Marieke Meelen's keynote

They looked up official links by web search. The results were merged, and duplicates across days were combined.

## Limits

- **Links:** they were found by web search and have not been checked by a person. "Likely" means the identification or link is probable but unconfirmed; "not found" means no public link turned up. Often that is because a talk describes a method without naming a product.
- **Sources:** most sessions are covered from their abstracts only. Tools named only in slides or in the talks themselves may be missing.
- **Licences:** these come from model cards and project pages, not from licence files. Check before reuse.

## Rebuilding

Edit `data/conference-resources-2026.json` or `template.html`, then run `python3 build.py`.

Compiled by Dominik Lukeš with AI assistance (Claude).
