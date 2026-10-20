# SurveyDataPandas Project Board

Numbered tasks for tracking work. Each task has a permanent number; add new tasks at the end. Update status as work progresses.

**Status values:** `Pending`, `In progress`, `DONE`

---

## Task 1: Refresh

**Status:** In progress (2026-10-20)

**Context:** SurveyDataPandas is a "current" workshop (GreenTeaPress Task 24). The guide is the "Refresh checklist" in `~/GreenTeaPress/plans/workshops.md`; BayesMadeSimple and CompStats are the worked examples. Given at PyCon US 2025 (May 15, 2025); not recorded. 0 stars; last content change 2025-05-06. Companion workshop: SurveyDataPyMC (same GSS data and audience, ODSC East 2025); the two should link to each other.

**0. Set up**
- [x] `git fetch`, pulled one commit (README: venues, recordings); no uncommitted edits; untracked files listed (Inventory, below) (2026-10-20)
- [x] `PROJECT_BOARD.md` and `CLAUDE.md` (2026-10-20)
- [x] Tags: `pycon-2025` at `83be401` (2025-05-06, the last commit before the tutorial; no recording, but Allen wants the event version tagged), `pre-refresh-2026` at `568411d` (the notebooks are the same as `pycon-2025`; only the README changed)
- [x] Tags pushed (2026-10-20)
- [x] Leftovers (Decisions): `jb/` sources committed; data copies, `.gitkeep`, `soln/01_simpson.py` deleted (the `.py` backed up to the session scratchpad)
- [x] Inventory (below)
- [ ] Environment: a `SurveyDataPandas` env exists (2025, from the Makefile: Python 3.11 + pip); replace with `environment.yml` in step 1

**1. Runs in a current environment**
- [ ] `environment.yml`, `requirements.txt`, `requirements-dev.txt`
- [ ] First code cell: installs what Colab lacks; the data download is already there
- [ ] Breakage and deprecation warnings (scratch runs with warnings as errors)
- [ ] Data URL (works; Decisions)
- [ ] Running instructions: Colab first, then pip or mamba (now the Makefile, in `jb/index.md`)

**2. Tests and CI**
- [ ] `pytest --nbmake` on the notebooks
- [ ] `.github/workflows/tests.yml`
- [ ] Status badge in the README

**3. Colab**
- [ ] Colab cell after the title of each notebook (the solution notebook has one; the student notebook and `test_notebook` don't)
- [ ] Allen runs one notebook on Colab end to end

**4. Text**
- [ ] Typos and broken links
- [ ] Notebook layout (title, Colab cell, copyright and license at the end) and license (code MIT, text CC)

**5. README in the standard shape**
- [ ] README rewritten; `LICENSE` file

**6. Site and visibility**
- [ ] Rebuild the existing site (Jupyter Book in `jb/`, `gh-pages`), with `prep_notebooks.py` from the template
- [ ] Remove the SurveyDataPyMC pages from the published site (Inventory)
- [ ] SEO checklist
- [ ] Publish; `Sitemap:` line in `~/AllenDowney.github.io/robots.txt`; Search Console; GreenTeaPress Task 22
- [ ] Cross-links with SurveyDataPyMC (README and site, both ways); hub entry; repo description and topics

**7. Close**
- [ ] Tag `2026-refresh`; note in GreenTeaPress Task 24

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

### Content issues

(For Allen to decide.)

1. The title cell has a three-line subtitle ("Tutorial for PyCon 2025", "Allen B. Downey"); the layout rule allows one line. Copyright says 2025 and MIT only (new rule: code MIT, text CC).
2. The slides (Google Slides) are linked only from the site; check they match the notebook.
