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
├── requirements.txt    # Dependencies (none for v1.0)
└── README.md           # This file
```

## How to run

```bash
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
