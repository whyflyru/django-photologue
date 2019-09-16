.PHONY: clean clean-test clean-pyc clean-build release
.DEFAULT_GOAL := clean

clean: clean-build clean-pyc clean-test clean-cache ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -rf reports/
	rm -fr .pytest_cache

clean-cache: ## remove pip cache
	rm -rf .cache

clean-venv: ## remove local venv
	rm -rf `pipenv --venv`

release:
	python setup.py sdist
	twine upload dist/*
