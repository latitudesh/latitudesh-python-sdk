"""
Integration tests for User Data resource
"""

import pytest
from tests.integration.helpers import (
    setup_test,
    mock_user_data,
    mock_user_data_list,
    MockResponse,
)


class TestUserDataIntegration:
    """Integration tests for User Data resource"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test client before each test"""
        self.sdk, self.mock_client, self.reset = setup_test()
        self.reset()
        yield

    def test_list_project_user_data(self):
        """Should list user data scripts for a project"""
        # Arrange
        self.mock_client.mock_response(
            "GET",
            "/projects/proj_test123/user_data",
            MockResponse(status=200, body=mock_user_data_list)
        )

        # Act
        result = self.sdk.user_data.list_project_user_data(project_id="proj_test123")

        # Assert
        assert result is not None

    def test_create_user_data(self):
        """Should create a new user data script"""
        # Arrange
        new_user_data = {
            **mock_user_data,
            "data": {
                **mock_user_data["data"],
                "id": "userdata_new123",
                "attributes": {
                    **mock_user_data["data"]["attributes"],
                    "description": "New User Data Script",
                },
            },
        }

        self.mock_client.mock_response(
            "POST",
            "/user_data",
            MockResponse(status=201, body=new_user_data)
        )

        # Act
        result = self.sdk.user_data.create(
            project_id="proj_test123",
            data={
                "type": "user_data",
                "attributes": {
                    "description": "New User Data Script",
                    "content": "#!/bin/bash\necho 'New script'",
                },
            }
        )

        # Assert
        assert result is not None

    def test_get_user_data(self):
        """Should retrieve a user data script"""
        # Arrange
        self.mock_client.mock_response(
            "GET",
            "/user_data/userdata_test123",
            MockResponse(status=200, body=mock_user_data)
        )

        # Act
        result = self.sdk.user_data.get_user_data(user_data_id="userdata_test123")

        # Assert
        assert result is not None
        assert result.data.id == "userdata_test123"
        assert result.data.attributes.description == "Test User Data Script"

    def test_update_user_data(self):
        """Should update a user data script"""
        # Arrange
        updated_user_data = {
            **mock_user_data,
            "data": {
                **mock_user_data["data"],
                "attributes": {
                    **mock_user_data["data"]["attributes"],
                    "description": "Updated User Data Script",
                },
            },
        }

        self.mock_client.mock_response(
            "PATCH",
            "/user_data/userdata_test123",
            MockResponse(status=200, body=updated_user_data)
        )

        # Act
        result = self.sdk.user_data.patch_user_data(
            user_data_id="userdata_test123",
            data={
                "id": "userdata_test123",
                "type": "user_data",
                "attributes": {
                    "description": "Updated User Data Script",
                },
            }
        )

        # Assert
        assert result is not None

    def test_delete_user_data(self):
        """Should delete a user data script"""
        # Arrange
        self.mock_client.mock_response(
            "DELETE",
            "/user_data/userdata_test123",
            MockResponse(status=204)
        )

        # Act
        self.sdk.user_data.delete_user_data(user_data_id="userdata_test123")

        # Assert
        assert self.mock_client.verify_request("DELETE", "/user_data/userdata_test123")

    def test_user_data_not_found(self):
        """Should handle user data not found"""
        # Arrange
        self.mock_client.mock_response(
            "GET",
            "/user_data/nonexistent",
            MockResponse(
                status=404,
                body={
                    "error": {
                        "message": "User data not found",
                        "code": "not_found",
                    },
                }
            )
        )

        # Act & Assert
        with pytest.raises(Exception):
            self.sdk.user_data.get_user_data(user_data_id="nonexistent")

    def test_user_data_content(self):
        """Should retrieve user data script content"""
        # Arrange
        self.mock_client.mock_response(
            "GET",
            "/user_data/userdata_test123",
            MockResponse(status=200, body=mock_user_data)
        )

        # Act
        result = self.sdk.user_data.get_user_data(user_data_id="userdata_test123")

        # Assert
        assert result.data.attributes.content is not None
        assert "#!/bin/bash" in result.data.attributes.content
        assert "apt-get update" in result.data.attributes.content

    def test_user_data_project_association(self):
        """Should verify user data project association"""
        # Arrange
        self.mock_client.mock_response(
            "GET",
            "/user_data/userdata_test123",
            MockResponse(status=200, body=mock_user_data)
        )

        # Act
        result = self.sdk.user_data.get_user_data(user_data_id="userdata_test123")

        # Assert
        assert result.data.attributes.project is not None
        assert result.data.attributes.project.id == "proj_test123"
        assert result.data.attributes.project.name == "Test Project"
