# Student Records (SEN 401 - SCM Lab)

A small, modular Python project used to practise Software Configuration
Management (SCM): version control, branching, baselines and maintenance.

## Project structure

```
.
├── app.py              # Entry point - runs the demo application
├── students.py         # Data module - list of students + add/average functions
├── utils/
│   ├── __init__.py     # Marks utils as a Python package
│   └── helpers.py      # Utility functions: highest_score(), lowest_score()
├── requirements.txt    # Dependencies: pydantic (v1.1+)
└── README.md           # This file
```

## Requirements

Python **3.12+** (uses the PEP 695 `type` statement).

## How to run

```bash
pip install -r requirements.txt
python app.py
```

## Branching model

| Branch      | Purpose                                           |
|-------------|---------------------------------------------------|
| `main`      | Stable, released code. Protected - PR review only |
| `dev`       | Integration branch for ongoing work               |
| `feature/*` | New features (e.g. `feature/median-score`)        |
| `maint/*`   | Maintenance work (e.g. `maint/empty-list-fix`)    |

## Baselines

| Tag | Description |
|-----|-------------|
| `lab1-v1.0` | Initial baseline of the project |
| `lab2-v1.1` | Corrective, adaptive, perfective and preventive maintenance |

## Changes in v1.1 (`lab2-v1.1`)

| Type | Change |
|------|--------|
| Corrective | `average_score()` no longer crashes on an empty list; invalid scores are rejected; `students.py` no longer prints when imported; helpers handle empty lists |
| Adaptive | Python 3.12 type syntax; Pydantic v2 `Student` model validates every new student |
| Perfective | Median score, letter grades, ranked and formatted report |
| Preventive | Refactored into small documented functions, constants for grade boundaries, shared `_scores()` helper |
