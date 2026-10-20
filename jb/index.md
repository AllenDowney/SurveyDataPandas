# Survey Data with Pandas

This is the landing page for a tutorial at PyCon US 2025.

[The slides are here](https://docs.google.com/presentation/d/e/2PACX-1vTNdX7EizUOSVLxl7yWcR627FWnnPXcydIw6_eB6mXNlBlP4AjxG0YZNvFzLzL8Muuj-tJGZI3ID551/pub)

Links to the notebooks and setup instructions are below.

**Abstract**

Survey data analysis is a cornerstone of data science, whether you're analyzing customer feedback, tracking election polls, or studying social trends. This tutorial introduces powerful tools from Pandas and StatsModels for extracting meaningful insights from survey data. Using real-world examples from the General Social Survey (GSS), we'll explore how political beliefs have evolved in the United States over the past 50 years. Through hands-on exercises, you'll master essential data science workflows: from data loading and validation to exploration, visualization, modeling, and effective communication of results.

**Prerequisites**

This tutorial is designed for Python users who are familiar with:
- Basic Python programming
- Fundamental data analysis concepts
- Basic statistics

No prior experience with Pandas or survey data analysis is required.

## Run the notebook

You have two options to run the notebook:

1. **Practice Version** (Recommended for learning):
   * [Notebook 1: Simpson's Paradox](https://colab.research.google.com/github/AllenDowney/SurveyDataPandas/blob/main/notebooks/01_simpson.ipynb)

2. **Solution Version** (For reference):
   * [Notebook 1: Simpson's Paradox with solutions](https://colab.research.google.com/github/AllenDowney/SurveyDataPandas/blob/main/soln/01_simpson.ipynb)

**Note:** The notebook uses data from the General Social Survey (GSS), which will be automatically downloaded when you run the notebook. The GSS is a nationally representative survey of adults in the United States, conducted since 1972, making it an excellent resource for studying social trends and attitudes.

## Running Locally

If you prefer to run the notebooks on your own computer, clone the repository:

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

Then start Jupyter, navigate to the `notebooks` directory, and open `test_notebook.ipynb`.

```bash
jupyter notebook
```

If the code in `test_notebook.ipynb` runs with no errors, your setup is ready to go!
