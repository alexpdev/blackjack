.PHONY: clean docs help push release dist install lint
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

PROJECTNAME = blackjack

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	rm -fr *.egg-info
	rm -fr *.egg
	rm -f **.pyc
	rm -f **.pyo
	rm -f **~
	rm -fr **/__pycache__
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache
	rm -f corbertura.xml
	rm -f coverage.xml
	rm -fr .codacy-coverage

lint: ## check style with flake8
	black ${projectname}
	black tests
	isort ${projectname}
	isort tests
	pylint ${projectname} tests
	pycodestyle ${projectname} tests
	pydocstyle ${projectname} tests
	pyroma .
	bandit ${projectname}/*
	pep257 ${projectname}
	prospector ${projectname}
	prospector tests

test: ## run tests quickly with the default Python
	pytest tests
	pytest tests --cov
	pytest tests --pylint

coverage: ## check code coverage quickly with the default Python
	coverage run -m pytest tests --cov
	coverage xml -o coverage.xml

push: lint clean test coverage
	git add .
	git commit -m "Updates to testing suit, style linting, bug fixes."
	git push
	bash codacy.sh report -r coverage.xml

play: ## Play game


build: clean ## Create executable
	python setup.py sdist bdist_wheel bdist_egg
	pip install dist/*.whl --force-reinstall
	rm -rfv ../runner
	mkdir ../runner
	cp -rv ./blackjack/assets ../runner
	touch ../runner/exe
	@echo "#! /usr/sbin/python3" >> ../runner/exe
	@echo "import blackjack" >> ../runner/exe
	@echo "blackjack.Driver.main()" >> ../runner/exe
	pyinstaller ../runner/exe --distpath ../runner/dist --workpath ../runner/build -F -n blackjack -w -i ../runner/assets/blackjackicon.ico --collect-all blackjack --specpath ../runner
	mv -fv ../runner/dist/blackjack.exe .
	rm blackjack.spec
