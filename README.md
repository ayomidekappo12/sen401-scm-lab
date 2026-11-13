# SEN 401 – Software Configuration Management & Maintenance (Lab Assessment)

MIVA Open University · SEN 401 group lab project.

| Folder | Lab | Description | Baseline tag |
|--------|-----|-------------|--------------|
| [`lab1-2_student-records/`](lab1-2_student-records) | Lab 1 & Lab 2 | Modular Python student-records app: SCM setup, baseline, then corrective / adaptive / perfective / preventive maintenance | `lab1-v1.0`, `lab2-v1.1` |
| [`lab3_inventory/`](lab3_inventory) | Lab 3 | Inventory manager: maintenance + Configuration Status Accounting (`changelog.txt`) | `lab3-v1.0` |
| [`lab4_campus-records/`](lab4_campus-records) | Lab 4 | Re-engineered app: modular layers, JSON/CSV → SQLite migration, FastAPI REST API, Docker Compose | `lab4-v2.0` |

## Branching model

| Branch | Purpose |
|--------|---------|
| `main` | Stable, released code – protected, changes only through reviewed pull requests |
| `dev` | Integration branch (Lab 3 maintenance work) |
| `feature/*` | New features, e.g. `feature/median-score` |
| `maint/*` | Maintenance work, e.g. `maint/empty-list-fix` |
| `maintenance` | Lab 2 maintenance tasks |
| `reengineering` | Lab 4 re-engineering & migration |

## Group members

| Name | Matric number | Role |
|------|---------------|------|
| _to be filled_ | | Group leader |
