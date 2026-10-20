---
myst:
  html_meta:
    description: "A beginner's tutorial on survey data in Python: explore 50 years of General Social Survey data with pandas and StatsModels, from loading to modeling."
og:description: "A beginner's tutorial on survey data in Python: explore 50 years of General Social Survey data with pandas and StatsModels, from loading to modeling."
---

# Survey Data with Pandas: A Tutorial in Python

[Allen Downey](https://allendowney.com)

Survey data analysis is a cornerstone of data science, whether you're analyzing customer feedback, tracking election polls, or studying social trends. This tutorial introduces powerful tools from pandas and StatsModels for extracting meaningful insights from survey data. Using real-world examples from the [General Social Survey](https://gss.norc.org/) (GSS), we'll explore how political beliefs have evolved in the United States over the past 50 years. Through hands-on exercises, you'll master essential data science workflows: from data loading and validation to exploration, visualization, modeling, and effective communication of results.

I presented this tutorial at PyCon US 2025. Its companion, [Bayesian Regression for Survey Data with PyMC](https://allendowney.github.io/SurveyDataPyMC/), uses the same GSS data.

**Level:** beginner. You should be familiar with basic Python programming, fundamental data analysis concepts, and basic statistics. You don't need any experience with pandas or survey data.

**Length:** about 3 hours.

## The notebook

The page on this site shows the notebook with solutions; click on a hidden cell to see it. To do the exercises, run the version with blanks on Colab:

* [Survey data and Simpson's paradox](01_simpson): distributions, cross tabulation, time series and LOWESS, pivot tables, logistic regression, birth cohorts, Simpson's paradox, and sampling weights. [Exercises on Colab](https://colab.research.google.com/github/AllenDowney/SurveyDataPandas/blob/main/notebooks/01_simpson.ipynb)

To check your setup before the tutorial, run the [setup notebook on Colab](https://colab.research.google.com/github/AllenDowney/SurveyDataPandas/blob/main/notebooks/test_notebook.ipynb).

[Slides for this tutorial are here](https://docs.google.com/presentation/d/e/2PACX-1vTNdX7EizUOSVLxl7yWcR627FWnnPXcydIw6_eB6mXNlBlP4AjxG0YZNvFzLzL8Muuj-tJGZI3ID551/pub).

## Running the notebooks

The easiest way to run the notebooks is on Colab: click one of the links above. You need a Google account, but you don't have to install anything. The notebooks download the data they need.

To run them on your own computer, clone the [repository](https://github.com/AllenDowney/SurveyDataPandas):

```bash
git clone https://github.com/AllenDowney/SurveyDataPandas.git
cd SurveyDataPandas
```

Then install the packages with pip:

```bash
pip install -r requirements.txt jupyter
```

Or create a conda environment with [mamba](https://mamba.readthedocs.io/) (or conda):

```bash
mamba env create -f environment.yml
conda activate SurveyDataPandas
```

Then run `jupyter lab` and open `notebooks/test_notebook.ipynb`. If it runs with no errors, your setup is ready to go!

## Next steps

* [Bayesian Regression for Survey Data with PyMC](https://allendowney.github.io/SurveyDataPyMC/), the companion tutorial: logistic, categorical, and ordered logistic regression with the same GSS data.
* [Political Alignment Case Study](https://allendowney.github.io/PoliticalAlignmentCaseStudy/): a longer project with GSS data on political views.
* [*Think Stats*](https://allendowney.github.io/ThinkStats/), which is free online.
* *Probably Overthinking It*, which uses GSS data in several chapters; [its companion notebooks are here](https://allendowney.github.io/ProbablyOverthinkingIt/).
* [My other workshops](https://allendowney.github.io/#workshops).

The code is available under the [MIT License](https://github.com/AllenDowney/SurveyDataPandas/blob/main/LICENSE). The text is available under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).
