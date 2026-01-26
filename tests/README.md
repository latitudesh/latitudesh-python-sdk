# Integration Tests

This directory contains the integration tests for the Latitude.sh Python SDK, created following the same patterns as the TypeScript SDK tests.

## Structure

```
tests/
├── __init__.py
├── README.md
└── integration/
    ├── __init__.py
    ├── helpers/
    │   ├── __init__.py
    │   ├── mock_http_client.py  # Mock HTTP client to intercept requests
    │   ├── test_client.py        # Test client setup
    │   └── mock_data.py          # Mock data for tests
    ├── test_servers.py           # Integration tests for Servers
    ├── test_projects.py          # Integration tests for Projects
    ├── test_apikeys.py           # Integration tests for API Keys
    ├── test_plans.py             # Integration tests for Plans
    ├── test_teams.py             # Integration tests for Teams
    └── test_userdata.py          # Integration tests for User Data
```

## CI/CD Integration

This test suite is automatically executed via GitHub Actions on:
- Every push to `main`, `master`, or `develop` branches
- Every pull request to these branches
- Manual workflow dispatch

**Workflows:**
- **Integration Tests** (`.github/workflows/integration-tests.yml`): Runs tests on Python 3.9, 3.10, 3.11, and 3.12
- **Lint & Type Check** (`.github/workflows/lint.yml`): Runs pylint, mypy, and pyright

## Installing Dependencies

Install the required development dependencies:

```bash
# Using poetry
poetry install --with dev

# Or using pip
pip install pytest pytest-asyncio pytest-mock pytest-cov
```

## Running Tests

### Run all integration tests

```bash
# Using poetry
poetry run pytest tests/integration

# Using pytest directly
pytest tests/integration
```

### Run specific tests

```bash
# Run only server tests
pytest tests/integration/test_servers.py

# Run only project tests
pytest tests/integration/test_projects.py

# Run a specific test
pytest tests/integration/test_servers.py::TestServersIntegration::test_list_all_servers
```

### Run with verbosity

```bash
# Verbose mode
pytest tests/integration -v

# Very verbose mode (shows test output)
pytest tests/integration -vv
```

### Run with coverage

```bash
# Generate coverage report
pytest tests/integration --cov=latitudesh_python_sdk --cov-report=html

# View report in terminal
pytest tests/integration --cov=latitudesh_python_sdk --cov-report=term
```

## Test Structure

### Mock HTTP Client

The `MockHTTPClient` intercepts HTTP requests and returns mocked responses, allowing you to test the SDK without making real API calls.

```python
from tests.integration.helpers import setup_test, MockResponse

# Setup
sdk, mock_client, reset = setup_test()

# Mock a response
mock_client.mock_response(
    "GET",
    "/servers",
    MockResponse(status=200, body={"data": []})
)

# Make request
result = sdk.servers.list()

# Verify the request was made
assert mock_client.verify_request("GET", "/servers")
```

### Test Structure

Each test follows the **Arrange-Act-Assert** pattern:

```python
def test_list_servers(self):
    """Should list all servers"""
    # Arrange: Setup mocks and data
    self.mock_client.mock_response(
        "GET",
        "/servers",
        MockResponse(status=200, body=mock_server_list)
    )

    # Act: Execute action
    result = self.sdk.servers.list()

    # Assert: Verify results
    assert result is not None
    assert len(result.result.data) == 2
    assert self.mock_client.verify_request("GET", "/servers")
```

## Implemented Tests

### Servers (`test_servers.py`)
- List, create, get, update and delete servers
- Filters and pagination
- Error handling (404, 422, 500, etc.)
- Rate limiting and authentication

### Projects (`test_projects.py`)
- Complete CRUD operations
- Filters by name and environment
- Project statistics
- Validations and errors

### API Keys (`test_apikeys.py`)
- List and create API keys
- Update and delete
- Error handling

### Plans (`test_plans.py`)
- List plans
- Specification details
- Regions and availability
- Filters

### Teams (`test_teams.py`)
- Team information
- Team users and projects
- MFA and feature flags
- Team updates

### User Data (`test_userdata.py`)
- User data script management
- Project association
- Script CRUD operations

## Mock Data

Mock data is defined in `helpers/mock_data.py` and includes:

- `mock_server` - Individual server
- `mock_server_list` - List of servers
- `mock_project` - Individual project
- `mock_project_list` - List of projects
- `mock_api_key` - Individual API key
- `mock_plan` - Individual plan
- `mock_team` - Individual team
- `mock_user_data` - User data script

Helper functions:
- `create_mock_servers(count)` - Create multiple mock servers
- `create_paginated_response(data, page, per_page)` - Create paginated response

## Fixtures

All tests use the `setup` fixture which:
1. Creates an SDK instance with mock HTTP client
2. Resets state before each test
3. Provides access to SDK, mock client and reset function

```python
@pytest.fixture(autouse=True)
def setup(self):
    """Setup test client before each test"""
    self.sdk, self.mock_client, self.reset = setup_test()
    self.reset()
    yield
```

## Best Practices

1. **Use mocks for all HTTP requests** - Never make real requests in integration tests
2. **Follow the Arrange-Act-Assert pattern** - Organize your tests clearly
3. **Test success and error cases** - Include tests for expected errors (404, 422, etc.)
4. **Use consistent mock data** - Reuse data defined in `mock_data.py`
5. **Document tests** - Use descriptive docstrings for each test

## Comparison with TypeScript SDK

This test structure was created to mirror the TypeScript SDK tests, maintaining:
- Same directory structure
- Same test cases
- Same mocking approach
- Equivalent coverage

Main differences:
- Uses pytest instead of Bun test
- Uses httpx.MockTransport instead of fetch mock
- Python syntax instead of TypeScript
