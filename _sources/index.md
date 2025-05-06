# Survey Data with Pandas

**Abstract**

Survey data analysis is a cornerstone of data science, whether you're analyzing customer feedback, tracking election polls, or studying social trends. This tutorial introduces powerful tools from Pandas and StatsModels for extracting meaningful insights from survey data. Using real-world examples from the General Social Survey (GSS), we'll explore how political beliefs have evolved in the United States over the past 50 years. Through hands-on exercises, you'll master essential data science workflows: from data loading and validation to exploration, visualization, modeling, and effective communication of results.

**What You'll Learn**

In this tutorial, you'll develop practical skills in:
- Loading and cleaning survey data using Pandas
- Exploring relationships between variables
- Creating informative visualizations
- Identifying and analyzing Simpson's Paradox
- Drawing valid conclusions from complex data

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

If you prefer to run the notebooks on your local machine, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AllenDowney/SurveyDataPandas.git
   cd SurveyDataPandas
   ```

2. **Set up the environment**:
   ```bash
   # Create a conda environment
   make create_environment
   
   # Activate the environment
   conda activate SurveyDataPandas
   
   # Install required packages
   make requirements
   ```

3. **Start Jupyter**:
   ```bash
   jupyter notebook
   ```

4. **Open the notebook**:
   - Navigate to the `notebooks` directory
   - Open `test_notebook.ipynb`

If the code in `test_notebook.ipynb` runs with no errors, your setup is ready to go!





