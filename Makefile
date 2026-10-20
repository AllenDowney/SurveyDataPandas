PROJECT_NAME = SurveyDataPandas

create_environment:
	mamba env create -f environment.yml
	@echo ">>> environment created. Activate with:\nconda activate $(PROJECT_NAME)"

delete_environment:
	mamba env remove --name $(PROJECT_NAME)

requirements:
	python -m pip install -r requirements-dev.txt

clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

tests:
	pytest --nbmake soln/01_simpson.ipynb notebooks/01_simpson.ipynb notebooks/test_notebook.ipynb
