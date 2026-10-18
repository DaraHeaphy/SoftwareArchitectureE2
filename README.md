# EVA analysis - Software Raconteur handoff

This is the outgoing version of my EVA application, ready for the next student's development round. It preserves the existing single-file implementation and Git history.

## Setup

Requires Python 3 and Matplotlib. Verified with Python 3.11.9. From the repository directory:

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe evacodev2.py
```

On macOS/Linux use `.venv/bin/python` in place of `.venv\Scripts\python.exe`. If Matplotlib is already installed, run `python evacodev2.py` directly.

## Run

1. Enter `eva-data.json` when asked for a data filename, or supply another compatible file path.
2. Enter `USA` or `Russia` for the country total. Country matching ignores case and surrounding whitespace.
3. The program prints the selected country's all-time EVA hours and counts/percentages for duration categories across all countries.
4. It saves `cumulative_duration.png` in the current directory and opens the cumulative plot. Close that window to finish.

The plot is cumulative across all dated EVAs, not a separate annual total or a filter for the selected country.

## Current features

- Reads a user-selected JSON dataset.
- Reports total EVA duration in hours for one selected country.
- Classifies duration-bearing EVAs across all countries: Short <4 hours; Standard >=4 and <7 hours; Long >=7 hours.
- Reports category counts and percentages.
- Saves and displays a chronologically sorted cumulative-duration plot.

Duration values are interpreted as hours:minutes. Records with no duration are skipped. Duration-bearing records without dates still contribute to country totals and categories, but cannot appear in the chronological plot. Zero-duration records count in the categories.

## Files and handoff

- `evacodev2.py`: current application; execution begins at the top of this script.
- `eva-data.json`: supplied dataset, unchanged.
- `original-file-answers.txt`: historical Week 2 planning and review answers.
- `HANDOFF.md`: completed changes, verification results and known limitations.
- `requirements.txt`: the application dependency.

Pass on this Git repository with its history, preferably by sharing the repository URL so the next student can clone it. A GitHub source ZIP does not contain the Git history. Follow the assigned A/B/C/D/E handoff sequence. The next student should first run and examine this inherited version, then carry out their assigned development round.

This outgoing version retains the work completed before the Week 6 inherited-code round. It does not include the Week 6 modular restructuring or two-country/year-range comparison.
