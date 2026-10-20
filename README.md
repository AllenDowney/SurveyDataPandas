# Survey Data with Pandas

[![tests](https://github.com/AllenDowney/SurveyDataPandas/actions/workflows/tests.yml/badge.svg)](https://github.com/AllenDowney/SurveyDataPandas/actions/workflows/tests.yml)

[Allen Downey](https://allendowney.com)

Survey data analysis is a cornerstone of data science, whether you're analyzing customer feedback, tracking election polls, or studying social trends. This tutorial introduces powerful tools from pandas and StatsModels for extracting meaningful insights from survey data. Using real-world examples from the [General Social Survey](https://gss.norc.org/) (GSS), we'll explore how political beliefs have evolved in the United States over the past 50 years. Through hands-on exercises, you'll master essential data science workflows: from data loading and validation to exploration, visualization, modeling, and effective communication of results.

This is one of [my workshops and tutorials](https://allendowney.github.io/#workshops). Its companion, [Bayesian Regression for Survey Data with PyMC](https://allendowney.github.io/SurveyDataPyMC/), uses the same GSS data.

**Level:** beginner. You should be familiar with basic Python programming, fundamental data analysis concepts, and basic statistics. You don't need any experience with pandas or survey data.

**Length:** about 3 hours.

## Outline

1. **Data:** loading and validating an extract of the GSS.
2. **Distributions:** value counts, KDE plots, and cross tabulation.
3. **Time series:** how responses have changed over time, smoothed with LOWESS.
4. **Pivot tables and groupby:** changes over time in groups defined by political views.
5. **Logistic regression:** modeling those changes with StatsModels.
6. **Cohorts:** grouping respondents by decade of birth, and Simpson's paradox when the composition of the population changes.
7. **Sampling weights:** correcting for stratified sampling by weighted resampling.

You choose the target variable: whether people say they are happy, or that other people are helpful, fair, or can be trusted.

The notebook comes in two versions: one with blanks for the exercises, and one with solutions. The setup check makes sure your environment can run the tutorial.

| Notebook | Exercises | Solutions |
|---|---|---|
| Setup check | [Run on Colab](https://colab.research.google.com/github/AllenDowney/SurveyDataPandas/blob/main/notebooks/test_notebook.ipynb) | |
| 1. Survey data and Simpson's paradox | [Run on Colab](https://colab.research.google.com/github/AllenDowney/SurveyDataPandas/blob/main/notebooks/01_simpson.ipynb) | [Run on Colab](https://colab.research.google.com/github/AllenDowney/SurveyDataPandas/blob/main/soln/01_simpson.ipynb) |

[Slides for this tutorial are here](https://docs.google.com/presentation/d/e/2PACX-1vTNdX7EizUOSVLxl7yWcR627FWnnPXcydIw6_eB6mXNlBlP4AjxG0YZNvFzLzL8Muuj-tJGZI3ID551/pub).

### Data

The notebooks download `gss_extract_pacs_workshop.hdf`, an extract of the GSS made in the [GssExtract](https://github.com/AllenDowney/GssExtract) repository by [this notebook](https://github.com/AllenDowney/GssExtract/blob/main/notebooks/pacs_workshop_extract.ipynb).

## Recordings

I presented this tutorial at PyCon US 2025 (May 15, 2025). It was not recorded. The version of the code I presented is tagged [`pycon-2025`](https://github.com/AllenDowney/SurveyDataPandas/tree/pycon-2025).

## Running the notebooks

The easiest way to run the notebooks is on Colab: click one of the links above. You need a Google account, but you don't have to install anything. The notebooks download the data they need.

To run them on your own computer, you need Python 3 with Jupyter, NumPy, pandas, Matplotlib, Seaborn, StatsModels, and PyTables. You can [download the code in this zip file](https://github.com/AllenDowney/SurveyDataPandas/archive/main.zip), or clone the repository:

```
git clone https://github.com/AllenDowney/SurveyDataPandas
cd SurveyDataPandas
```

Then install the packages with pip:

```
pip install -r requirements.txt jupyter
```

Or, if you use conda or mamba, create an environment:

```
mamba env create -f environment.yml
mamba activate SurveyDataPandas
```

Then run `jupyter lab` and open `notebooks/test_notebook.ipynb`. If it runs with no errors, you're ready.

## Next steps

* [Bayesian Regression for Survey Data with PyMC](https://allendowney.github.io/SurveyDataPyMC/), the companion tutorial: logistic, categorical, and ordered logistic regression with the same GSS data.
* [Political Alignment Case Study](https://allendowney.github.io/PoliticalAlignmentCaseStudy/): a longer project with GSS data on political views.
* [*Think Stats*](https://allendowney.github.io/ThinkStats/), which is free online.
* *Probably Overthinking It*, which uses GSS data in several chapters; [its companion notebooks are here](https://allendowney.github.io/ProbablyOverthinkingIt/).
* [My other workshops](https://allendowney.github.io/#workshops).

## License

The code is available under the [MIT License](LICENSE). The text is available under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).
