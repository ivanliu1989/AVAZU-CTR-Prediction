# Makefile for AVAZU CTR Prediction
# ==================================

.PHONY: help install test lint format clean run-ftrl run-blend docs

# Default target
help:
	@echo "AVAZU CTR Prediction - Makefile Commands"
	@echo "========================================"
	@echo ""
	@echo "Setup:"
	@echo "  make install          Install dependencies"
	@echo "  make install-dev      Install dev dependencies"
	@echo ""
	@echo "Code Quality:"
	@echo "  make lint             Run linting (flake8)"
	@echo "  make format           Format code (black)"
	@echo "  make type-check       Run type checking (mypy)"
	@echo "  make check-all        Run all checks"
	@echo ""
	@echo "Testing:"
	@echo "  make test             Run tests"
	@echo "  make test-verbose     Run tests with verbose output"
	@echo "  make test-coverage    Run tests with coverage report"
	@echo ""
	@echo "Execution:"
	@echo "  make run-ftrl         Run FTRL training example"
	@echo "  make run-blend        Run blending example"
	@echo ""
	@echo "Cleanup:"
	@echo "  make clean            Remove generated files"
	@echo "  make clean-all        Remove all generated files including logs"
	@echo ""
	@echo "Documentation:"
	@echo "  make docs             Open documentation"

# Installation
install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements.txt
	pip install pytest pytest-cov black flake8 mypy pylint

# Code Quality
lint:
	@echo "Running flake8..."
	flake8 models/ utils/ config.py examples/ tests/

format:
	@echo "Formatting code with black..."
	black models/ utils/ config.py examples/ tests/

type-check:
	@echo "Running mypy type checking..."
	mypy models/ utils/ config.py

check-all: lint type-check
	@echo "All checks passed!"

# Testing
test:
	pytest tests/ -v

test-verbose:
	pytest tests/ -vv

test-coverage:
	pytest tests/ --cov=models --cov=utils --cov-report=html --cov-report=term
	@echo "Coverage report generated in htmlcov/index.html"

# Execution
run-ftrl:
	python examples/train_ftrl_example.py

run-blend:
	python examples/blend_predictions_example.py

# Cleanup
clean:
	@echo "Cleaning generated files..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	rm -rf build/ dist/ htmlcov/ .coverage
	@echo "Cleanup complete!"

clean-all: clean
	@echo "Removing logs and outputs..."
	rm -rf logs/*.log
	@echo "Deep cleanup complete!"

# Documentation
docs:
	@echo "Opening documentation..."
	@echo "Main docs:"
	@echo "  - SETUP.md"
	@echo "  - ARCHITECTURE.md"
	@echo "  - README.md"

# Development workflow
dev-setup: install-dev
	@echo "Setting up development environment..."
	mkdir -p logs/ data/ pred/ models_output/
	@echo "Development environment ready!"

# Run all quality checks before commit
pre-commit: format lint type-check test
	@echo "Pre-commit checks passed!"

# Python version check
python-version:
	@python --version
	@echo "Required: Python 3.7+"
