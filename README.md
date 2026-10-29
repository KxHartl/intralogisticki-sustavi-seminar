# Autonomous forklifts and industrial vehicles

**Autonomni viličari i industrijska vozila**

> Seminar paper, Automated Intralogistics Systems (Automatizirani intralogistički sustavi), MSc in Mechatronics and Robotics, 4th semester, FSB, University of Zagreb, 2026

![LaTeX](https://img.shields.io/badge/paper-LaTeX-008080)
![biblatex](https://img.shields.io/badge/citations-biblatex%20%C2%B7%20IEEE-4b5563)
![Python](https://img.shields.io/badge/charts-Python%20%C2%B7%20matplotlib-3776AB)

A seminar paper in Croatian on autonomous forklifts in warehouse and production logistics. It
compares classic and autonomous forklifts across the levels of autonomy, describes the safety
systems and the ISO 3691-4 standard, explains the navigation technologies (sensors, SLAM, LiDAR,
computer vision for pallet handling and sensor fusion), and looks at industrial examples from
Toyota Material Handling, Jungheinrich and Gideon along with the VDA 5050 interoperability
standard. It closes with the advantages, an economic comparison (TCO, NPV, ROI and payback
period) and the technical and operational limits.

This repository holds the complete seminar: the paper, its LaTeX source, the presentation and
the working notes.

## The paper

- [Seminar paper (PDF)](dist/Kresimir_Hartl_seminar_autonomni_vilicari.pdf)
- [Presentation (PDF)](dist/AIS_prezentacija.pdf)

## What's inside

| Path | Contents |
|---|---|
| `docs/main.tex` | the main LaTeX document with the title page and table of contents |
| `docs/01_uvod.tex` … `docs/07_zakljucak.tex` | one file per chapter, from the introduction to the conclusion |
| `docs/seminar.tex`, `docs/split_tex.py` | the paper as a single file before it was split into chapters, and the script that split it |
| `docs/slike/` | figures used in the paper |
| `docs/generate_charts.py` | the Python script that draws the cost comparison chart |
| `sources.bib` | the bibliography (biblatex, IEEE style) |
| `dist/` | the submitted paper, the presentation (PowerPoint and PDF), the speaker notes, a glossary, notes on figures and two other builds of the paper |
| `outline.md`, `chapters_plan.md` | the outline and the chapter plan written before the paper |
| `TASK.md`, `critic_review.md`, `to_fix.md`, `sources_notes.md`, `prezentacija.md` | the task, a review of the draft, the list of fixes, notes on the sources and the presentation script |
| `data/rag/sources/` | course material and the list of web sources used while writing |

## Build

The paper uses biblatex with the biber backend.

```bash
cd docs
latexmk -pdf main.tex
```

The chart is regenerated with `python generate_charts.py`, run from `docs/` (it needs `matplotlib`
and `numpy`).

The repository was set up with the owner's [LiteRealm](https://github.com/KxHartl/LiteRealm)
template, which is where `.ai/`, `CLAUDE.md` and `GEMINI.md` come from.
