"""
Integration tests for Servers API
"""

import pytest
from tests.integration.helpers import (
    setup_test,
    mock_server,
    mock_server_list,
    mock_server_create_request,
    create_mock_servers,
    MockResponse,
)


class TestServersIntegration:
    """Integration tests for Servers resource"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test client before each test"""
        self.sdk, self.mock_client, self.reset = setup_test()
        self.reset()
        yield
        # Cleanup if needed

    def test_list_all_servers(self):
        """Should list all servers"""
        # Arrange: Mock the list endpoint
        self.mock_client.mock_response(
            "GET",
            "/servers",
            MockResponse(status=200, body=mock_server_list)
        )

        # Act: Call list method
        result = self.sdk.servers.list()

        # Assert: Verify response
        assert result is not None
        assert result.result is not None
        assert len(result.result.data) == 2
        assert result.result.data[0].id == "srv_test123"
        assert result.result.data[0].attributes.hostname == "test-server-01"
        assert self.mock_client.verify_request("GET", "/servers")

    def test_list_servers_pagination(self):
        """Should handle pagination"""
        # Arrange: Create mock data with 5 servers
        all_servers = create_mock_servers(5)
        page1 = {
            "data": all_servers,
            "meta": {
                "total": 5,
                "current_page": 1,
                "last_page": 1,
                "per_page": 20,
            },
        }

        self.mock_client.mock_response(
            "GET",
            "/servers",
            MockResponse(status=200, body=page1)
        )

        # Act
        result = self.sdk.servers.list()

        # Assert
        assert result is not None
        assert len(result.result.data) == 5
        assert self.mock_client.count_requests("GET", "/servers") >= 1

    def test_filter_servers_by_project(self):
        """Should filter servers by project"""
        # Arrange
        self.mock_client.mock_response(
            "GET",
            "/servers",
            MockResponse(
                status=200,
                body={
                    "data": [mock_server],
                    "meta": {"total": 1, "current_page": 1, "last_page": 1, "per_page": 25},
                }
            )
        )

        # Act
        result = self.sdk.servers.list(filter_project="proj_test123")

        # Assert
        assert result is not None
        assert len(result.result.data) == 1
        assert result.result.data[0].attributes.project.id == "proj_test123"

    def test_list_empty_servers(self):
        """Should handle empty list"""
        # Arrange
        self.mock_client.mock_response(
            "GET",
            "/servers",
            MockResponse(
                status=200,
                body={
                    "data": [],
                    "meta": {"total": 0, "current_page": 1, "last_page": 1, "per_page": 25},
                }
            )
        )

        # Act
        result = self.sdk.servers.list()

        # Assert
        assert result is not None
        assert len(result.result.data) == 0

    def test_list_servers_api_error(self):
        """Should handle API errors"""
        # Arrange
        self.mock_client.mock_response(
            "GET",
            "/servers",
            MockResponse(
                status=500,
                body={
                    "error": {
                        "message": "Internal server error",
                        "code": "internal_error",
                    },
                }
            )
        )

        # Act & Assert
        with pytest.raises(Exception):
            self.sdk.servers.list()

    def test_create_server(self):
        """Should create a new server"""
        # Arrange
        self.mock_client.mock_response(
            "POST",
            "/servers",
            MockResponse(status=201, body={"data": mock_server})
        )

        # Act
        result = self.sdk.servers.create(
            data=mock_server_create_request
        )

        # Assert
        assert result is not None
        assert result.data.id == "srv_test123"
        assert result.data.attributes.hostname == "test-server-01"
        assert result.data.attributes.status == "on"
        assert self.mock_client.verify_request("POST", "/servers")

    def test_create_server_validation_error(self):
        """Should handle validation errors"""
        # Arrange
        self.mock_client.mock_response(
            "POST",
            "/servers",
            MockResponse(
                status=422,
                body={
                    "error": {
                        "message": "Validation failed",
                        "code": "validation_error",
                        "errors": [
                            {"field": "hostname", "message": "Hostname is required"},
                        ],
                    },
                }
            )
        )

        # Act & Assert
        with pytest.raises(Exception):
            self.sdk.servers.create(
                data={
                    "data": {
                        **mock_server_create_request,
                        "attributes": {
                            **mock_server_create_request["attributes"],
                            "hostname": "",
                        },
                    }
                }
            )

    def test_get_server_by_id(self):
        """Should retrieve a server by ID"""
        # Arrange
        self.mock_client.mock_response(
            "GET",
            "/servers/srv_test123",
            MockResponse(status=200, body={"data": mock_server})
        )

        # Act
        result = self.sdk.servers.get(server_id="srv_test123")

        # Assert
        assert result is not None
        assert result.data.id == "srv_test123"
        assert result.data.attributes.hostname == "test-server-01"
        assert result.data.attributes.status == "on"
        assert self.mock_client.verify_request("GET", "/servers/srv_test123")

    def test_get_server_not_found(self):
        """Should handle server not found"""
        # Arrange
        self.mock_client.mock_response(
            "GET",
            "/servers/nonexistent",
            MockResponse(
                status=404,
                body={
                    "error": {
                        "message": "Server not found",
                        "code": "not_found",
                    },
                }
            )
        )

        # Act & Assert
        with pytest.raises(Exception):
            self.sdk.servers.get(server_id="nonexistent")

    def test_update_server(self):
        """Should update a server"""
        # Arrange
        updated_server = {
            **mock_server,
            "attributes": {
                **mock_server["attributes"],
                "hostname": "updated-server-01",
            },
        }

        self.mock_client.mock_response(
            "PATCH",
            "/servers/srv_test123",
            MockResponse(status=200, body={"data": updated_server})
        )

        # Act
        result = self.sdk.servers.update(
            server_id="srv_test123",
            data={
                "data": {
                    "attributes": {
                        "hostname": "updated-server-01",
                    },
                },
            }
        )

        # Assert
        assert result is not None
        assert result.data.attributes.hostname == "updated-server-01"
        assert self.mock_client.verify_request("PATCH", "/servers/srv_test123")

    def test_delete_server(self):
        """Should delete a server"""
        # Arrange
        self.mock_client.mock_response(
            "DELETE",
            "/servers/srv_test123",
            MockResponse(status=204)
        )

        # Act
        self.sdk.servers.delete(server_id="srv_test123")

        # Assert: Should complete without errors
        assert self.mock_client.verify_request("DELETE", "/servers/srv_test123")

    def test_delete_nonexistent_server(self):
        """Should handle delete of non-existent server"""
        # Arrange
        self.mock_client.mock_response(
            "DELETE",
            "/servers/nonexistent",
            MockResponse(
                status=404,
                body={
                    "error": {
                        "message": "Server not found",
                        "code": "not_found",
                    },
                }
            )
        )

        # Act & Assert
        with pytest.raises(Exception):
            self.sdk.servers.delete(server_id="nonexistent")

    def test_unauthorized_request(self):
        """Should handle unauthorized request"""
        # Arrange
        self.mock_client.mock_response(
            "GET",
            "/servers",
            MockResponse(
                status=401,
                body={
                    "error": {
                        "message": "Invalid API key",
                        "code": "unauthorized",
                    },
                }
            )
        )

        # Act & Assert
        with pytest.raises(Exception):
            self.sdk.servers.list()

    def test_rate_limiting(self):
        """Should handle rate limiting"""
        # Arrange
        self.mock_client.mock_response(
            "GET",
            "/servers",
            MockResponse(
                status=429,
                body={
                    "error": {
                        "message": "Rate limit exceeded",
                        "code": "rate_limit_exceeded",
                        "retry_after": 60,
                    },
                },
                headers={"retry-after": "60"},
            )
        )

        # Act & Assert
        with pytest.raises(Exception):
            self.sdk.servers.list()
