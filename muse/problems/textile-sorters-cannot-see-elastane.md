---
title: Textile sorters can't detect low-percentage elastane, so "100% cotton" bales contaminate recycling
domain: textile waste
score: 5
freshness: 2025-09-01
status: picked
source: seed
---

## Who
Operators of automated post-consumer textile sorting lines (Fibersort-style NIR lines in the Netherlands
and Belgium, and the sorters feeding chemical recyclers) and the recyclers who buy their bales.

## What they do today instead
They trust the care label or the NIR reading, both of which miss elastane below a few percent because it
sits in the yarn core and barely shows in the NIR spectrum. Bales sold as "100% cotton" go into mechanical
or chemical recycling, where a small elastane fraction fouls the output and lowers its value. When the
buyer complains, the sorter has no way to tell which garments were the cause. Some operators send samples
for lab analysis, which is slow and too expensive per garment, so most just accept the contamination or
downgrade whole bales to lower-value uses like insulation or incineration.

## Why it's unsolved
NIR penetrates only about 150 µm, so core-spun elastane and multilayer textiles are invisible to it.
Low-content blends produce spectra that overlap with the main fibre. Care labels are unreliable and
often omit elastane under a threshold. Hyperspectral and AI classification improve detection but are
not yet deployed on production lines, and no one has closed the loop from "recycler found contamination"
back to "which sorter, which input stream".

## Evidence
- [Using NIR for Textile Sorting (AZoM)](https://www.azom.com/article.aspx?ArticleID=21755) — explains why elastane in the fibre core cannot be detected at low amounts by NIRS, and the '100% cotton' contamination problem.
- [Challenges and spectra interpretability in textile sorting: NIR hyperspectral images and chemometrics](https://www.sciencedirect.com/science/article/pii/S1386142525009722) — penetration depth limit and low-content blend overlap.
- [Quantifying Cotton Content in Post-Consumer Polyester/Cotton Blend Textiles via NIR Spectroscopy](https://doi.org/10.3390/recycling10040152) — attainable accuracy in practice and remaining gaps.
- [AI Model for Textile Materials Identification Using Hyperspectral Data](https://pmc.ncbi.nlm.nih.gov/articles/PMC13301267/) — research-stage AI classification, not yet on lines.

## Harvest notes
- 2026-09-15: created as a seed problem. Re-verify freshness on first /harvest.
