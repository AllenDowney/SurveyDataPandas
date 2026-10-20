# SurveyDataPandas Project Board

Numbered tasks for tracking work. Each task has a permanent number; add new tasks at the end. Update status as work progresses.

**Status values:** `Pending`, `In progress`, `DONE`

---

## Task 1: Refresh

**Status:** DONE (2026-10-20), except Allen's Search Console submission and the SurveyDataPyMC back-link

**Context:** SurveyDataPandas is a "current" workshop (GreenTeaPress Task 24). The guide is the "Refresh checklist" in `~/GreenTeaPress/plans/workshops.md`; BayesMadeSimple and CompStats are the worked examples. Given at PyCon US 2025 (May 15, 2025); not recorded. 0 stars; last content change 2025-05-06. Companion workshop: SurveyDataPyMC (same GSS data and audience, ODSC East 2025); the two should link to each other.

**0. Set up**
- [x] `git fetch`, pulled one commit (README: venues, recordings); no uncommitted edits; untracked files listed (Inventory, below) (2026-10-20)
- [x] `PROJECT_BOARD.md` and `CLAUDE.md` (2026-10-20)
- [x] Tags: `pycon-2025` at `83be401` (2025-05-06, the last commit before the tutorial; no recording, but Allen wants the event version tagged), `pre-refresh-2026` at `568411d` (the notebooks are the same as `pycon-2025`; only the README changed)
- [x] Tags pushed (2026-10-20)
- [x] Leftovers (Decisions): `jb/` sources committed; data copies, `.gitkeep`, `soln/01_simpson.py` deleted (the `.py` backed up to the session scratchpad)
- [x] Inventory (below)
- [x] Environment: `mamba env create -f environment.yml` (name `SurveyDataPandas`, recreated 2026-10-20; Python 3.12.15, NumPy 2.5, pandas 3.0, Matplotlib 3.11, seaborn 0.13, statsmodels 0.15, PyTables 3.11, SciPy 1.18)

**1. Runs in a current environment**
- [x] `environment.yml` (Python 3.12, conda-forge, Jupyter, the libraries, pytest, nbmake, the site build tools), `requirements.txt` (unpinned: numpy, pandas, matplotlib, seaborn, statsmodels, tables; scipy and jupyter dropped), `requirements-dev.txt` (adds jupyter, pytest, nbmake; black and flake8 dropped) (2026-10-20)
- [x] First code cell: nothing to install. Colab has every library (backend-info, 2026-10-03: pandas 2.2.3, NumPy 2.1.3, Matplotlib 3.10, seaborn 0.13.2, statsmodels 0.15.0, tables 3.10.2). The notebooks already download the data if missing
- [x] Breakage and warnings: none. The three notebooks run in scratch copies with Deprecation/Future/PendingDeprecation/User/Runtime warnings as errors. Outputs match the 2025 ones, except `gss.columns` shows `dtype='str'` (pandas 3) and a weighted resample (random). One `ConvergenceWarning` (it was there in 2025 too; Content issues)
- [x] NumPy 2 scalar reprs (`np.float64(0.36)`): `np.set_printoptions(legacy='1.25')` in the import cell of `01_simpson` and `test_notebook` (Allen, 2026-10-20); solution version re-executed
- [x] Data URL: kept (Decisions)
- [x] Running instructions in `jb/index.md`: pip or mamba instead of the Makefile; the Colab links above them were already there. `Makefile` kept, updated (Decisions): `create_environment` uses `environment.yml`, `requirements` installs `requirements-dev.txt`, `tests` runs all three notebooks (3 passed, 15 s)

**2. Tests and CI**
- [x] `make tests` = `pytest --nbmake` on all three notebooks (the student version runs too: its blanks are missing cells, not failing code). 3 passed, about 15 s, in the mamba env and in a fresh pip venv from `requirements-dev.txt` (2026-10-20)
- [x] `.github/workflows/tests.yml` (push to main, PR, monthly, manual; Python 3.12; pip; 20-minute timeout; checkout@v5, setup-python@v6). First run passed: https://github.com/AllenDowney/SurveyDataPandas/actions/runs/39478513062
- [x] Status badge in the README

**3. Colab**
- [x] Colab cell after the title (2026-10-20): the solution version opens itself and links to the version with blanks (house wording, as in BayesMadeSimple); `remove_soln.py` now rewrites that cell so the student version opens itself; `test_notebook` got one. README links come with the step 5 rewrite; the site pages should open the version with blanks (step 6, `prep_notebooks.py`)
- [x] Allen ran `soln/01_simpson.ipynb` on Colab end to end (2026-10-20)

**4. Text**
- [x] Typos: none found (codespell's hits are all in embedded images; markdown, comments and docstrings read) (2026-10-20)
- [x] Links: GssExtract extract notebook `02_make_extract-2022_4.ipynb` (404) → `pacs_workshop_extract.ipynb` (renamed in GssExtract's 2026-02 "Consolidated notebooks"; it writes `gss_extract_pacs_workshop.hdf`, last changed 2025-04-23); Matplotlib `api/axes_api.html` → `stable/api/axes_api.html`. The GSS Data Explorer links are dead (Content issues)
- [x] Layout and license (Decisions): title cell is the H1 plus "Examples and exercises for a tutorial on survey data analysis."; `test_notebook` split (H1 + "A setup check for the tutorial.", Colab cell, then the setup paragraphs); last cell "Copyright 2025–2026 Allen Downey", code MIT, text CC BY-NC-SA 4.0 (CompStats wording); trailing empty code cell removed. Headings were already ATX, one H1, sections `##`

**5. README in the standard shape**
- [x] README rewritten (2026-10-20): badge, author, abstract (from `jb/index.md`, pandas lowercase), companion link, level (beginner) and length (3 hours, Allen), outline, notebook table with Colab links (setup check, exercises, solutions), slides, data, recordings (none; tag `pycon-2025`), running instructions, next steps (SurveyDataPyMC, PoliticalAlignmentCaseStudy, *Think Stats*, the *Probably Overthinking It* notebooks, the hub), license. `LICENSE` file (MIT, 2025)

**6. Site and visibility**
- [x] `jb/` from the BayesMadeSimple template (2026-10-20): `build.sh [publish]` (publishes only with `publish`), `prep_notebooks.py` (copies `../soln/01_simpson.ipynb` in, keeps the `hide-cell` tags on the solutions as before, writes the page description), `_config.yml` (executes the notebook, `main` branch, sitemap, opengraph, page-view counter, *Think Stats* 3e cover as the social image), `index.md` mirrors the README. The notebook's own Colab cell links to the version with blanks
- [x] SEO checklist in a test build (scratch copy): sitemap lists only `index.html` and `01_simpson.html`; each page has one description, one `og:description`, `rel="canonical"`; landing H1 ("Survey Data with Pandas: A Tutorial in Python") differs from the site title; counter in the footer; no stray SurveyDataPyMC pages
- [x] Allen approved the two descriptions (2026-10-20)
- [x] Published (2026-10-20) from a clean `jb/_build/`: the stray SurveyDataPyMC pages are gone (`04_hierarchical.html` now 404); `Sitemap:` line in `~/AllenDowney.github.io/robots.txt` (pushed); noted in GreenTeaPress Tasks 22 and 24
- [ ] Allen submits the sitemap in Search Console
- [x] Cross-link this workshop to SurveyDataPyMC: README and site (intro and next steps)
- [ ] Cross-link SurveyDataPyMC back to this workshop: left for that repo's refresh (Allen), since it has uncommitted edits (noted in GreenTeaPress Task 24)
- [x] Hub entry and description unchanged (still fit); topics `jupyter-book`, `statsmodels`, `general-social-survey` added (Allen)

**7. Close**
- [x] Tag `2026-refresh` (pushed); noted in GreenTeaPress Task 24 (2026-10-20)

### Inventory (2026-10-20)

**The workshop:** one notebook, in two versions.

| Notebook | Topic | Imports |
|---|---|---|
| `soln/01_simpson.ipynb` (solutions, executed) / `notebooks/01_simpson.ipynb` (blanks, no outputs) | GSS: distributions, crosstabs, time series, LOWESS, pivot tables, groupby, logistic regression, cohorts, Simpson's paradox, sampling weights | pandas, numpy, matplotlib, seaborn, statsmodels; `pd.read_hdf` needs PyTables |
| `notebooks/test_notebook.ipynb` | Setup check: downloads the data, reads it, plots, imports statsmodels | same |

- The student version is generated: `soln/build.sh` copies the solution notebook to `notebooks/`, runs `soln/remove_soln.py` (drops cells that start with `# Solution` and clears outputs), then commits and pushes. The two are in sync now (40 non-solution cells, identical).
- Data: `gss_extract_pacs_workshop.hdf` (1.9 MB), downloaded by the notebook from `https://github.com/AllenDowney/GssExtract/raw/main/data/interim/` (works; 302 → 200, 2026-10-20). Made in the GssExtract repo.
- Helpers: `download` and `decorate` are defined in the notebook; no helper modules.
- Kernel metadata: Python 3.13.2. The `# Solution` cells are hidden (`hide-cell`) on the site by `jb/prep_notebooks.py`.
- Build and setup files: `Makefile` (cookiecutter: conda env with Python 3.11, pip install, `make tests` runs `pytest --nbmake soln/0*.ipynb`), `requirements.txt` (unpinned: jupyter, numpy, matplotlib, pandas, seaborn, scipy, statsmodels, tables), `requirements-dev.txt` (black, flake8, nbmake, pytest). No `environment.yml`, no CI, no `LICENSE`. The notebooks say "code under the MIT license".
- README: three lines, pointing to the site. The abstract, prerequisites, slides link (Google Slides), notebook links and local setup are in `jb/index.md`.

**Site:** `allendowney.github.io/SurveyDataPandas/`, Pages source `gh-pages` (last published 2025-05-07). `jb/` is untracked: `_config.yml`, `_toc.yml` (only `01_simpson.ipynb`), `index.md`, `build.sh` (copies `../soln/0*.ipynb`, runs `prep_notebooks.py`, `jb build`, then always `ghp-import -n -p -f`), `prep_notebooks.py` (only adds `hide-cell`), a copy of the solution notebook, and `_build/`. Execution is off.

- **Problem:** `jb/_build/html` and the published `gh-pages` include five pages from SurveyDataPyMC (`00_intro`, `01_logistic_regression`, `02_categorical_regression`, `03_ordinal_regression`, `04_hierarchical`, dated 2025-05-05, plus their `_sources`). `jb/` was probably copied from SurveyDataPyMC with its `_build`, and `jb build` doesn't clean it. They are live (e.g. `.../SurveyDataPandas/04_hierarchical.html` returns 200), not in the TOC, but in the search index and likely in search results.

**Local state not in git:**

- `jb/` (above): the site sources were never committed.
- `notebooks/.gitkeep` (empty), `notebooks/gss_extract_pacs_workshop.hdf` and `soln/gss_extract_pacs_workshop.hdf` (identical, the downloaded data).
- `soln/01_simpson.py`: an nbconvert export from 2025-05-05, an older draft (abstract in the title cell, Colab link to the repo root, `np.random.seed(17)`).
- Ignored: `.ipynb_checkpoints/` (root: `03_outlook-checkpoint.ipynb`, `simpson-checkpoint.ipynb`; also in `notebooks/` and `soln/`), `__pycache__/` (`utils.cpython-312/313.pyc`; no `utils.py` in the repo now).

### Decisions

Allen, 2026-10-20:

- Tag the PyCon version `pycon-2025` even though it wasn't recorded; push both tags.
- Commit the `jb/` sources; the copied notebook and `jb/_build/` go in `.gitignore`; the old `_build` (with the stray PyMC pages) deleted.
- Delete the downloaded data copies (`*.hdf` ignored), `notebooks/.gitkeep`, and `soln/01_simpson.py`.
- The stray SurveyDataPyMC pages on `gh-pages` come off at the step 6 republish, not before.
- Data: keep downloading from `GssExtract/raw/main/data/interim/` (SurveyDataPyMC uses the same URL).
- Makefile: keep it, updated for `environment.yml`.
- 2000 cohort warning: leave the code, explain it in the text. Added to the "All the Cohorts" exercise cell: the cohort is in only two surveys, not enough to fit a quadratic, so the optimizer might not converge; the predictions for those years are still good. Student version regenerated with `remove_soln.py`.
- Commits stay local for now (no push before step 2, nor after it).
- Colab cells: the solution version opens itself and links to the version with blanks.
- Title subtitle like CompStats; text license CC BY-NC-SA 4.0, copyright 2025–2026; `test_notebook` title cell split.
- GSS Data Explorer links: keep them; Allen checks one in a browser (the host is up, but sends an incomplete certificate chain, so curl fails).
- `happy` label "Happy" → "Pretty happy".
- GSS Data Explorer links work in a browser; kept.
- NumPy legacy print options in the notebooks (and in the checklist, for the other refreshes).
- README: beginner, about 3 hours.
- Pushed the 7 commits (2026-10-20); CI passed.
- Site: rebuild from the BayesMadeSimple template; test build before publishing.
- The SurveyDataPyMC → SurveyDataPandas link waits for SurveyDataPyMC's own refresh.

### Content issues

(For Allen to decide.)

1. Resolved 2026-10-20 (Decisions): the title cell's three-line subtitle; copyright 2025 and MIT only.
2. The slides (Google Slides) are linked only from the site; check they match the notebook.
3. Resolved 2026-10-20 (explained in the text; Decisions). "All the Cohorts": the 2000 cohort (born 2000–2004) is in the GSS only in 2018 and 2022 (126 respondents), so `fit_model`'s quadratic (3 parameters, 2 distinct years) is not identified and statsmodels warns `ConvergenceWarning`. The predictions are still right at the two years, so the plot is fine, but participants see the warning. Options: stop at the 1990 cohort (`last = 1999`), fit a line for cohorts with fewer than 3 years, or leave it and say why in the text.
4. Resolved 2026-10-20 (Allen: the links work in a browser; kept). The four "Target variable" cells link `https://gssdataexplorer.norc.org/variables/<n>/vshow` (434 `happy`, 439 `helpful`, 440 `fair`, 441 `trust`). The site is up, but it is a JavaScript app, so I couldn't check that these pages still show the variables. **Allen:** open one in a browser; if it doesn't, replace the four with the Data Explorer home (Allen, 2026-10-20).
5. Resolved 2026-10-20 (now "Pretty happy"). `happy`: the `responses` labels are "Very happy", "Happy", "Not too happy", but the GSS answer (and the `question` text) is "pretty happy".
