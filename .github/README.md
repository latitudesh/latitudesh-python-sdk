# GitHub Actions Workflows

This directory contains CI/CD workflows for the Latitude.sh Python SDK.

## Workflows

### Integration Tests (`workflows/integration-tests.yml`)

Runs the complete integration test suite across multiple Python versions.

**Triggers:**
- Push to `main`, `master`, or `develop` branches
- Pull requests targeting these branches
- Manual workflow dispatch

**Matrix Strategy:**
- Python versions: 3.10, 3.11, 3.12
- OS: Ubuntu Latest

**Steps:**
1. Checkout code
2. Set up Python environment
3. Install Poetry and cache dependencies
4. Install project dependencies
5. Run integration tests with pytest
6. Generate coverage report (Python 3.12 only)
7. Upload coverage to Codecov (Python 3.12 only)

**Status Badge:**
```markdown
![Integration Tests](https://github.com/latitudesh/latitudesh-python-sdk/workflows/Integration%20Tests/badge.svg)
```

### Lint & Type Check (`workflows/lint.yml`)

Runs code quality checks and static type analysis.

**Triggers:**
- Push to `main`, `master`, or `develop` branches
- Pull requests targeting these branches
- Manual workflow dispatch

**Tools:**
- **Pylint**: Code quality and style checking
- **Mypy**: Static type checking
- **Pyright**: Microsoft's static type checker

**Status Badge:**
```markdown
![Lint & Type Check](https://github.com/latitudesh/latitudesh-python-sdk/workflows/Lint%20%26%20Type%20Check/badge.svg)
```

## Local Development

To run the same checks locally before pushing:

```bash
# Run integration tests
poetry run pytest tests/integration -v

# Run with coverage
poetry run pytest tests/integration --cov=latitudesh_python_sdk --cov-report=term

# Run linters
poetry run pylint src/latitudesh_python_sdk
poetry run mypy src/latitudesh_python_sdk
poetry run pyright src/latitudesh_python_sdk
```

## Dependencies

All workflow dependencies are managed via Poetry and defined in `pyproject.toml`:

```toml
[tool.poetry.group.dev.dependencies]
pytest = "^8.3.4"
pytest-asyncio = "^0.25.2"
pytest-mock = "^3.14.0"
pytest-cov = "^6.0.0"
mypy = "==1.15.0"
pylint = "==3.2.3"
pyright = "==1.1.398"
```

## Cache Strategy

Workflows use GitHub Actions cache to speed up runs:
- Cache key: `venv-{os}-{python-version}-{poetry.lock-hash}`
- Cached path: `.venv` (Poetry virtual environment)
- Cache hit: Skip dependency installation
- Cache miss: Install dependencies and update cache

## Coverage Reporting

Test coverage is automatically:
1. Generated during the Python 3.12 test run
2. Uploaded to Codecov with the `integration` flag
3. Available in the workflow artifacts

To view coverage locally:

```bash
poetry run pytest tests/integration --cov=latitudesh_python_sdk --cov-report=html
open htmlcov/index.html
```
