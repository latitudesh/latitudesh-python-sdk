"""
Integration tests for Projects resource
Tests CRUD operations: list, create, update, delete
"""

import pytest
from tests.integration.helpers import (
    setup_test,
    mock_project,
    mock_project_list,
    MockResponse,
)


class TestProjectsCRUDOperations:
    """Integration tests for Projects CRUD operations"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test client before each test"""
        self.sdk, self.mock_client, self.reset = setup_test()
        self.reset()
        yield

    def test_list_all_projects(self):
        """Should list all projects"""
        # Arrange: Mock the list endpoint
        self.mock_client.mock_response(
            "GET",
            "/projects",
            MockResponse(status=200, body=mock_project_list)
        )

        # Act: Call list method
        result = self.sdk.projects.list()

        # Assert: Verify pagination works correctly
        assert result is not None
        assert result.result is not None
        assert len(result.result.data) == 2
        assert result.result.data[0].id == "proj_test123"
        assert result.result.data[0].attributes.name == "Test Project"
        assert result.result.data[0].attributes.slug == "test-project"
        assert result.result.data[1].id == "proj_test456"

    def test_list_empty_projects(self):
        """Should handle empty project list"""
        # Arrange: Mock empty response
        self.mock_client.mock_response(
            "GET",
            "/projects",
            MockResponse(
                status=200,
                body={
                    "data": [],
                    "meta": {
                        "total": 0,
                        "current_page": 1,
                        "last_page": 1,
                        "per_page": 25,
                    },
                }
            )
        )

        # Act
        result = self.sdk.projects.list()

        # Assert
        assert result is not None
        assert len(result.result.data) == 0

    def test_list_projects_with_pagination(self):
        """Should support pagination parameters"""
        # Arrange
        self.mock_client.mock_response(
            "GET",
            "/projects",
            MockResponse(
                status=200,
                body={
                    "data": [],
                    "meta": {
                        "total": 0,
                        "current_page": 1,
                        "last_page": 1,
                        "per_page": 10,
                    },
                }
            )
        )

        # Act: Request projects with specific page size
        result = self.sdk.projects.list(page_size=10)

        # Assert
        assert result is not None
        assert self.mock_client.verify_request("GET", "/projects")

    def test_filter_projects_by_name(self):
        """Should filter projects by name"""
        # Arrange
        self.mock_client.mock_response(
            "GET",
            "/projects",
            MockResponse(
                status=200,
                body={
                    "data": [mock_project],
                    "meta": {
                        "total": 1,
                        "current_page": 1,
                        "last_page": 1,
                        "per_page": 25,
                    },
                }
            )
        )

        # Act
        result = self.sdk.projects.list(filter_name="Test Project")

        # Assert
        assert result is not None
        assert len(result.result.data) == 1
        assert result.result.data[0].attributes.name == "Test Project"

    def test_filter_projects_by_environment(self):
        """Should filter projects by environment"""
        # Arrange
        self.mock_client.mock_response(
            "GET",
            "/projects",
            MockResponse(
                status=200,
                body={
                    "data": [mock_project_list["data"][1]],
                    "meta": {
                        "total": 1,
                        "current_page": 1,
                        "last_page": 1,
                        "per_page": 25,
                    },
                }
            )
        )

        # Act
        result = self.sdk.projects.list(filter_environment="Production")

        # Assert
        assert result is not None
        assert len(result.result.data) == 1
        assert result.result.data[0].attributes.environment == "Production"

    def test_create_new_project(self):
        """Should create a new project"""
        # Arrange
        new_project = {
            "id": "proj_new123",
            "type": "projects",
            "attributes": {
                "name": "New Project",
                "slug": "new-project",
                "description": "A newly created project",
                "billing_type": "Hourly",
                "environment": "Staging",
                "created_at": "2024-01-03T00:00:00Z",
                "updated_at": "2024-01-03T00:00:00Z",
            },
        }

        self.mock_client.mock_response(
            "POST",
            "/projects",
            MockResponse(status=201, body={"data": new_project})
        )

        # Act
        result = self.sdk.projects.create(
            data={
                "type": "projects",
                "attributes": {
                    "name": "New Project",
                    "provisioning_type": "on_demand",
                    "description": "A newly created project",
                    "environment": "Staging",
                },
            }
        )

        # Assert
        assert result is not None
        assert result.data.id == "proj_new123"
        assert result.data.attributes.name == "New Project"
        assert result.data.attributes.slug == "new-project"
        assert result.data.attributes.environment == "Staging"

    def test_create_project_minimal_fields(self):
        """Should create project with minimal required fields"""
        # Arrange
        minimal_project = {
            "id": "proj_minimal123",
            "type": "projects",
            "attributes": {
                "name": "Minimal Project",
                "slug": "minimal-project",
                "created_at": "2024-01-03T00:00:00Z",
                "updated_at": "2024-01-03T00:00:00Z",
            },
        }

        self.mock_client.mock_response(
            "POST",
            "/projects",
            MockResponse(status=201, body={"data": minimal_project})
        )

        # Act
        result = self.sdk.projects.create(
            data={
                "type": "projects",
                "attributes": {
                    "name": "Minimal Project",
                    "provisioning_type": "on_demand",
                },
            }
        )

        # Assert
        assert result is not None
        assert result.data.id == "proj_minimal123"
        assert result.data.attributes.name == "Minimal Project"

    def test_create_project_validation_error(self):
        """Should handle validation error on create"""
        # Arrange
        self.mock_client.mock_response(
            "POST",
            "/projects",
            MockResponse(
                status=422,
                body={
                    "errors": [
                        {
                            "status": "422",
                            "title": "Validation Error",
                            "detail": "Name is required",
                        },
                    ],
                }
            )
        )

        # Act & Assert
        with pytest.raises(Exception):
            self.sdk.projects.create(
                data={
                    "data": {
                        "type": "projects",
                        "attributes": {
                            "name": "",
                        },
                    }
                }
            )

    def test_update_project_name_and_description(self):
        """Should update project name and description"""
        # Arrange
        updated_project = {
            **mock_project,
            "attributes": {
                **mock_project["attributes"],
                "name": "Updated Project Name",
                "description": "Updated description",
                "updated_at": "2024-01-05T00:00:00Z",
            },
        }

        self.mock_client.mock_response(
            "PATCH",
            "/projects/proj_test123",
            MockResponse(status=200, body={"data": updated_project})
        )

        # Act
        result = self.sdk.projects.update(
            project_id="proj_test123",
            data={
                "id": "proj_test123",
                "type": "projects",
                "attributes": {
                    "name": "Updated Project Name",
                    "description": "Updated description",
                },
            }
        )

        # Assert
        assert result is not None
        assert result.data.id == "proj_test123"
        assert result.data.attributes.name == "Updated Project Name"
        assert result.data.attributes.description == "Updated description"

    def test_update_project_environment(self):
        """Should update project environment"""
        # Arrange
        updated_project = {
            **mock_project,
            "attributes": {
                **mock_project["attributes"],
                "environment": "Production",
                "updated_at": "2024-01-05T00:00:00Z",
            },
        }

        self.mock_client.mock_response(
            "PATCH",
            "/projects/proj_test123",
            MockResponse(status=200, body={"data": updated_project})
        )

        # Act
        result = self.sdk.projects.update(
            project_id="proj_test123",
            data={
                "id": "proj_test123",
                "type": "projects",
                "attributes": {
                    "environment": "Production",
                },
            }
        )

        # Assert
        assert result is not None
        assert result.data.attributes.environment == "Production"

    def test_update_project_not_found(self):
        """Should handle not found error on update"""
        # Arrange
        self.mock_client.mock_response(
            "PATCH",
            "/projects/proj_nonexistent",
            MockResponse(
                status=404,
                body={
                    "errors": [
                        {
                            "status": "404",
                            "title": "Not Found",
                            "detail": "Project not found",
                        },
                    ],
                }
            )
        )

        # Act & Assert
        with pytest.raises(Exception):
            self.sdk.projects.update(
                project_id="proj_nonexistent",
                data={
                    "data": {
                        "type": "projects",
                        "attributes": {
                            "name": "Updated Name",
                        },
                    }
                }
            )

    def test_delete_project(self):
        """Should delete a project"""
        # Arrange
        self.mock_client.mock_response(
            "DELETE",
            "/projects/proj_test123",
            MockResponse(status=204, body=None)
        )

        # Act
        self.sdk.projects.delete(project_id="proj_test123")

        # Assert: Should complete without errors
        assert self.mock_client.verify_request("DELETE", "/projects/proj_test123")

    def test_delete_project_not_found(self):
        """Should handle not found error on delete"""
        # Arrange
        self.mock_client.mock_response(
            "DELETE",
            "/projects/proj_nonexistent",
            MockResponse(
                status=404,
                body={
                    "errors": [
                        {
                            "status": "404",
                            "title": "Not Found",
                            "detail": "Project not found",
                        },
                    ],
                }
            )
        )

        # Act & Assert
        with pytest.raises(Exception):
            self.sdk.projects.delete(project_id="proj_nonexistent")

    def test_delete_project_with_resources(self):
        """Should handle forbidden error when project has resources"""
        # Arrange
        self.mock_client.mock_response(
            "DELETE",
            "/projects/proj_test123",
            MockResponse(
                status=403,
                body={
                    "errors": [
                        {
                            "status": "403",
                            "title": "Forbidden",
                            "detail": "Cannot delete project with active resources",
                        },
                    ],
                }
            )
        )

        # Act & Assert
        with pytest.raises(Exception):
            self.sdk.projects.delete(project_id="proj_test123")

    def test_project_statistics(self):
        """Should return project statistics"""
        # Arrange
        self.mock_client.mock_response(
            "GET",
            "/projects",
            MockResponse(
                status=200,
                body={
                    "data": [mock_project],
                    "meta": {
                        "total": 1,
                        "current_page": 1,
                        "last_page": 1,
                        "per_page": 25,
                    },
                }
            )
        )

        # Act
        result = self.sdk.projects.list()

        # Assert
        project = result.result.data[0]
        assert project.attributes.stats is not None
        assert project.attributes.stats.ip_addresses == 2
        assert project.attributes.stats.servers == 1
        assert project.attributes.stats.vlans == 1
        assert project.attributes.stats.containers == 0
        assert project.attributes.stats.prefixes == 0
