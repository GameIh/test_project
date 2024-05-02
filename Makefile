.PHONY: all lint type-check test

all: lint type-check test

lint:
	@echo "Running flake8..."
	@flake8 .

type-check:
	@echo "Running mypy..."
	@mypy .

test:
	@echo "Running tests..."
	@pytest
