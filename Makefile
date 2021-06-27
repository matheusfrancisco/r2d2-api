.DEFAULT_GOAL := help


.PHONY: clean-pyc
clean-pyc: ## Remove Python file artifacts
	@echo "+ $@"
	@find . -type f -name "*.py[co]" -delete
	@rm -fr .pytest_cache
	@find . -name '*~' -delete


.PHONY: setup
setup:  ## Set up project for development
	@pipenv install --dev

.PHONY: test
test:  ## Run test suite
	@pipenv run pytest tests/
