# SurveyDataPandas

Allen Downey's tutorial "Survey Data with Pandas": analyzing General Social Survey (GSS) data with pandas and StatsModels (cross tabulation, time series, LOWESS, pivot tables, logistic regression, age-period-cohort analysis, Simpson's paradox). Given at PyCon US 2025 (May 15, 2025); not recorded. The GitHub Pages site (`allendowney.github.io/SurveyDataPandas/`) is the Jupyter Book in `jb/`, published to the `gh-pages` branch.

Companion workshop: SurveyDataPyMC (`~/SurveyDataPyMC`; Bayesian regression with PyMC on the same GSS data, same audience). The two link to each other.

**Guide for the 2026 refresh:** the "Refresh checklist" in `~/GreenTeaPress/plans/workshops.md` (BayesMadeSimple and CompStats are the worked examples). Progress goes on `PROJECT_BOARD.md` here (Task 1) and in GreenTeaPress Task 24.

## Which notebooks are the workshop

- `soln/01_simpson.ipynb`: the solution version, the one to edit.
- `notebooks/01_simpson.ipynb`: the version with blanks, generated from the solution version by `soln/build.sh` (`remove_soln.py` drops cells that start with `# Solution` and clears outputs). Don't edit it by hand.
- `notebooks/test_notebook.ipynb`: a setup check for participants.

The notebook downloads its data, `gss_extract_pacs_workshop.hdf`, from the GssExtract repo. No helper modules.

## Tags

- `pycon-2025`: the version given at PyCon US 2025 (not recorded).
- `pre-refresh-2026`: the state before the 2026 refresh.
- `2026-refresh`: the refreshed version.

## Testing

Environment: `mamba env create -f environment.yml` (name `SurveyDataPandas`). Then `make tests`, which runs:

```
pytest --nbmake soln/01_simpson.ipynb notebooks/01_simpson.ipynb notebooks/test_notebook.ipynb
```

The target environment is Google Colab's current Python and libraries.

## Conventions

- Don't change the substance of the text; list content questions under "Content issues" on the board for Allen to decide.
- Keep the student and solution versions in sync by regenerating the student version: `cp soln/01_simpson.ipynb notebooks/ && python soln/remove_soln.py notebooks/01_simpson.ipynb` (`soln/build.sh` does the same, then commits and pushes).
