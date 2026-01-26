"""
Integration tests for API Keys resource
"""

import pytest
from tests.integration.helpers import (
    setup_test,
    mock_api_key,
    mock_api_key_list,
    MockResponse,
)


class TestAPIKeysIntegration:
    """Integration tests for API Keys resource"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test client before each test"""
        self.sdk, self.mock_client, self.reset = setup_test()
        self.reset()
        yield

    def test_list_all_api_keys(self):
        """Should list all API keys"""
        # Arrange
        self.mock_client.mock_response(
            "GET",
            "/auth/api_keys",
            MockResponse(status=200, body=mock_api_key_list)
        )

        # Act
        result = self.sdk.api_keys.list()

        # Assert
        assert result is not None
        assert result.data is not None
        assert len(result.data) == 2
        assert result.data[0].id == "apikey_test123"
        assert result.data[0].attributes.name == "Test API Key"

    def test_list_empty_api_keys(self):
        """Should handle empty API keys list"""
        # Arrange
        self.mock_client.mock_response(
            "GET",
            "/auth/api_keys",
            MockResponse(status=200, body={"data": []})
        )

        # Act
        result = self.sdk.api_keys.list()

        # Assert
        assert result is not None
        assert len(result.data) == 0

    def test_create_api_key(self):
        """Should create a new API key"""
        # Arrange
        new_api_key = {
            **mock_api_key,
            "id": "apikey_new123",
            "attributes": {
                **mock_api_key["attributes"],
                "name": "New API Key",
                "token": "lat_test_new_key_123456789",
            },
        }

        self.mock_client.mock_response(
            "POST",
            "/auth/api_keys",
            MockResponse(status=201, body={"data": new_api_key})
        )

        # Act
        result = self.sdk.api_keys.create(
            data={
                "type": "api_keys",
                "attributes": {
                    "name": "New API Key",
                },
            }
        )

        # Assert
        assert result is not None
        assert result.data.id == "apikey_new123"
        assert result.data.attributes.name == "New API Key"

    def test_delete_api_key(self):
        """Should delete an API key"""
        # Arrange
        self.mock_client.mock_response(
            "DELETE",
            "/auth/api_keys/apikey_test123",
            MockResponse(status=200, body={})
        )

        # Act
        self.sdk.api_keys.delete(api_key_id="apikey_test123")

        # Assert
        assert self.mock_client.verify_request("DELETE", "/auth/api_keys/apikey_test123")

    def test_api_key_not_found(self):
        """Should handle API key not found"""
        # Arrange
        self.mock_client.mock_response(
            "DELETE",
            "/auth/api_keys/nonexistent",
            MockResponse(
                status=404,
                body={
                    "error": {
                        "message": "API key not found",
                        "code": "not_found",
                    },
                }
            )
        )

        # Act & Assert
        with pytest.raises(Exception):
            self.sdk.api_keys.delete(api_key_id="nonexistent")
