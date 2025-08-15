

> From zero to production‑ready skills, one build at a time.


[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB.svg)](https://www.python.org/)
[![Build](https://img.shields.io/github/actions/workflow/status/your-username/100-days-python-dsa-ai-ml/ci.yml?label=CI)](.github/workflows/ci.yml)
[![Docs](https://img.shields.io/badge/Docs-GitHub%20Pages-0A0A0A.svg)](https://your-username.github.io/100-days-python-dsa-ai-ml/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

This is a complete, hands‑on course you can take entirely on GitHub. You’ll ship 100 small, purposeful projects that compound into real‑world mastery: Python, data structures and algorithms, databases, APIs, data science, machine learning, deep learning, and deployment — along with professional engineering habits like testing, typing, packaging, containers, and CI/CD.

---

## Why this course

- **Outcome‑focused:** 100 portfolio‑ready projects, not theory dumps.
- **Engineer’s workflow:** Tests, typing, linting, docs, automation, deploys.
- **Hiring signal:** Clean repo, reproducible builds, and demos recruiters can run.
- **Community‑ready:** Issues, discussions, and PRs welcomed to learn together.

---

## What you’ll learn and build

- **Core skills:** Python, OOP, concurrency/async, problem solving with DS&A.
- **Data & backend:** SQL/Postgres, MongoDB, Redis, FastAPI, WebSockets, scraping.
- **Data science:** NumPy, Pandas, visualization, stats, experiments, reporting.
- **ML/DL:** scikit‑learn, XGBoost, PyTorch, transfer learning, model serving.
- **Ops:** Docker, GitHub Actions, reproducibility, monitoring, performance.
- **Portfolio:** 100 projects with READMEs, tests, and screenshots/demos.

---

## Prerequisites

- **Basic computer literacy:** Comfortable with terminal, files, and folders.
- **Installed tools:** Git, Python 3.11+, VS Code (or your editor of choice).
- **Operating systems:** Works on Windows, macOS, Linux.

---

## Quick start

1. **Clone the repo**
   ```bash
   git clone https://github.com/manitejagarlapati/100_projects_for-python-beginer-to-end.git
   cd 100-days-python-dsa-ai-ml
   ```

2. **Create and activate a virtual environment**
   ```bash
   # Windows (PowerShell)
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

   # macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install base developer tools**
   ```bash
   pip install -r requirements-dev.txt
   pre-commit install
   ```

4. **Run your first project**
   ```bash
   cd day-001_expense-categorizer
   pip install -r requirements.txt
   python src/main.py data/sample.csv
   ```

5. **Open the docs (optional)**
   ```bash
   mkdocs serve
   # Visit http://127.0.0.1:8000
   ```

---

## How to use this course

- **Daily loop:** Code 60–120 minutes. Build the project, write 3–5 lines of “What I learned,” add a screenshot/GIF, run tests, and push.
- **Quality bar:** Lint clean, tests pass, clear CLI/API instructions, small demo dataset.
- **Share progress:** Open a weekly discussion post. Tag your build on social with #100DaysPythonAI and link your repo.
- **Stretch goals:** After finishing a day, explore the optional “Plus” ideas to deepen your skills.

---

## Roadmap and daily projects

> Each project title states the topic. Every folder contains src, tests, and a README with exact steps.

### Phase 1 — Python foundations (Days 1–20)

- **Day 01:** Expense categorizer CLI — Variables & data types  
- **Day 02:** Temperature converter CLI — Input & output  
- **Day 03:** Fitness/BMI calculator — Operators & expressions  
- **Day 04:** Text sanitizer and word stats — Strings  
- **Day 05:** Priority to‑do list — Lists & tuples  
- **Day 06:** Contact de‑duplicator — Dictionaries & sets  
- **Day 07:** Quiz engine with scoring — Control flow  
- **Day 08:** Unit converter — Functions & pure functions  
- **Day 09:** Greeting package — Scopes & modules  
- **Day 10:** Robust file copier — Exceptions & retries  
- **Day 11:** CSV→JSON transformer — File I/O  
- **Day 12:** Habit tracker with streaks — Date & time  
- **Day 13:** Log parser summarizer — Comprehensions  
- **Day 14:** Streaming line reader — Iterators & generators  
- **Day 15:** Publish tiny utility — Virtual envs & packaging  
- **Day 16:** Structured logger wrapper — Logging  
- **Day 17:** Typed math library — Type hints & mypy  
- **Day 18:** TDD FizzBuzz+ — Testing with pytest  
- **Day 19:** Markdown→HTML CLI — argparse/Typer  
- **Day 20:** Clean code makeover — Refactoring

### Phase 2 — OOP, patterns, and async (Days 21–30)

- **Day 21:** Bank account simulator — OOP basics  
- **Day 22:** Shape area library — Inheritance & polymorphism  
- **Day 23:** Money type — Dunder methods  
- **Day 24:** Strategy‑based tax calculator — Design patterns  
- **Day 25:** Safe resource manager — Context managers  
- **Day 26:** Caching & timing pack — Decorators  
- **Day 27:** Multi‑file downloader — Threads  
- **Day 28:** Image thumbnail worker — Multiprocessing  
- **Day 29:** Async web fetcher — asyncio + rate limiting  
- **Day 30:** Task scheduler — APScheduler

### Phase 3 — Data structures & algorithms (Days 31–45)

- **Day 31:** Two‑pointer toolkit — Arrays & strings  
- **Day 32:** Frequency maps — Hashing  
- **Day 33:** LRU cache — Linked lists  
- **Day 34:** Min stack & BFS queue — Stacks & queues  
- **Day 35:** Traversal visualizer — Trees & BST  
- **Day 36:** Streaming median — Heaps  
- **Day 37:** Dijkstra explorer — Graphs  
- **Day 38:** Island counter — Union‑find  
- **Day 39:** Quick/Merge/Heap sort — Sorting  
- **Day 40:** Binary search variants — Searching  
- **Day 41:** Sudoku solver — Recursion & backtracking  
- **Day 42:** Interval scheduler — Greedy  
- **Day 43:** Coin change & knapsack — Dynamic programming  
- **Day 44:** LCS & edit distance — DP on strings  
- **Day 45:** Benchmark suite — Complexity & profiling

### Phase 4 — Databases, wrangling, and APIs (Days 46–60)

- **Day 46:** Library DB CRUD — SQL basics (SQLite)  
- **Day 47:** Student‑course DB — Schema design & normalization  
- **Day 48:** Joins & windows lab — SQL queries  
- **Day 49:** Txns & indexes — Performance lab  
- **Day 50:** SQLAlchemy models — ORM + migrations  
- **Day 51:** Postgres in Docker — Backups & restore  
- **Day 52:** Mongo microblog — NoSQL schemas  
- **Day 53:** Leaderboard — Redis caching & rate limiting  
- **Day 54:** Notes API — FastAPI CRUD  
- **Day 55:** JWT auth — Access & refresh flow  
- **Day 56:** Pydantic contracts — Validation & DTOs  
- **Day 57:** Live chat — WebSockets  
- **Day 58:** Weather aggregator — External APIs & retries  
- **Day 59:** News collector — Web scraping (robots‑aware)  
- **Day 60:** Sales EDA — Pandas dataframes

### Phase 5 — Data science and visualization (Days 61–70)

- **Day 61:** Vectorization lab — NumPy  
- **Day 62:** Missing/outliers clinic — Data cleaning  
- **Day 63:** Feature pipelines — Feature engineering  
- **Day 64:** Story report — Matplotlib & Seaborn  
- **Day 65:** Interactive dashboard — Plotly  
- **Day 66:** A/B testing toolkit — Hypothesis testing  
- **Day 67:** Power & sample size — Experiment design  
- **Day 68:** DVC dataset repo — Data versioning  
- **Day 69:** From notebooks to scripts — Reproducibility  
- **Day 70:** Auto‑PDF reporter — Reporting

### Phase 6 — Machine learning (Days 71–85)

- **Day 71:** Problem cards & metrics — ML framing  
- **Day 72:** Majority & linear baselines — Baselines  
- **Day 73:** TF‑IDF classifier — scikit‑learn pipelines  
- **Day 74:** Ridge & Lasso — Regularized regression  
- **Day 75:** RandomForest/XGBoost — Trees & ensembles  
- **Day 76:** Cross‑val & leakage guard — Evaluation  
- **Day 77:** Grid/Random search — Hyperparameter tuning  
- **Day 78:** SMOTE & thresholds — Imbalanced data  
- **Day 79:** Text classifier — NLP basics  
- **Day 80:** ARIMA/Prophet — Time series forecasting  
- **Day 81:** K‑Means/DBSCAN — Clustering  
- **Day 82:** PCA/UMAP — Dimensionality reduction  
- **Day 83:** joblib + registry — Model persistence  
- **Day 84:** sklearn Pipeline — End‑to‑end pipelines  
- **Day 85:** FastAPI model endpoint — Serving ML

### Phase 7 — Deep learning, vision/NLP, and MLOps (Days 86–95)

- **Day 86:** Autograd & modules — PyTorch basics  
- **Day 87:** CIFAR‑10 CNN — Image classification  
- **Day 88:** ResNet fine‑tune — Transfer learning  
- **Day 89:** Datasets & augmentations — Data pipelines  
- **Day 90:** Text classifier (pretrained) — RNN/Transformers intro  
- **Day 91:** ONNX export — Inference optimization  
- **Day 92:** Prediction logging & drift — Monitoring  
- **Day 93:** Celery + Redis — Batch & queues  
- **Day 94:** Dockerized API + model — Containerization  
- **Day 95:** GitHub Actions — CI/CD pipeline

### Phase 8 — Capstones, security, and polish (Days 96–100)

- **Day 96:** Secrets & input hardening — Security  
- **Day 97:** Profiling & caching — Performance  
- **Day 98:** MkDocs site — Documentation excellence  
- **Day 99:** Full‑stack ML app — Capstone 1 (API + DB + UI/Streamlit)  
- **Day 100:** Productionized service — Capstone 2 (monitoring + CI)

---



## Project template

```
# Day XX — Project title
**Topic:** One line on core concept  
**Goal:** What you’ll build and why it matters.

## Setup
```bash
pip install -r requirements.txt
```

## Run
```bash
python src/main.py <args>
```

## Tests
```bash
pytest -q
```

## What I learned
- Key insight 1
- Key insight 2

## Screenshot
![output](screenshot.png)
```

---

## Quality standards

- **Correctness:** All required features implemented, edge cases handled, tests pass with coverage goals.
- **Code health:** Black, Ruff, and mypy clean; meaningful names; small functions; docstrings where helpful.
- **UX/dev‑ex:** Simple CLI/API usage; clear error messages; sample inputs; deterministic seeds for ML.
- **Docs:** Each project README explains setup, commands, and learnings in concise bullets.
- **Reusability:** Common utilities live in /common and are imported rather than duplicated.

---

## Progress tracker

- [ ] **Phase 1:** Days 01–20 — Python foundations
- [ ] **Phase 2:** Days 21–30 — OOP, patterns, async
- [ ] **Phase 3:** Days 31–45 — DS&A
- [ ] **Phase 4:** Days 46–60 — DBs, wrangling, APIs
- [ ] **Phase 5:** Days 61–70 — Data science
- [ ] **Phase 6:** Days 71–85 — Machine learning
- [ ] **Phase 7:** Days 86–95 — Deep learning & MLOps
- [ ] **Phase 8:** Days 96–100 — Capstones & polish

---

## Contributing and community

- **Issues:** Use issues for bugs, questions, or topic requests. Use labels (good first issue, help wanted).
- **Pull requests:** Fork, create a feature/day-XXX branch, follow the checklist in the PR template, and ensure CI passes.
- **Discussions:** Share wins, blockers, and demos. Peer review is encouraged.

> See CONTRIBUTING.md and CODE_OF_CONDUCT.md for details.

---

## License and attribution

- **License:** MIT — feel free to learn, remix, and share with attribution.
- **Attribution:** Created by Maniteja. Credit the course when you use parts in your projects or teaching.

---

## FAQ

- **Schedule flexibility:** Yes. If you miss a day, resume without guilt. Consistency beats intensity.
- **Tools choice:** Defaults are provided (pytest, black, ruff, mypy, FastAPI, scikit‑learn, PyTorch), but you can swap equivalents.
- **Hardware needs:** CPU is fine for most builds. For CNN/transfer learning, use a small dataset or a free GPU runtime.

---

