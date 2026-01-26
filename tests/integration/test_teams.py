"""
Integration tests for Teams resource
"""

import pytest
from tests.integration.helpers import (
    setup_test,
    mock_team,
    mock_team_list,
    MockResponse,
)


class TestTeamsIntegration:
    """Integration tests for Teams resource"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test client before each test"""
        self.sdk, self.mock_client, self.reset = setup_test()
        self.reset()
        yield

    def test_get_team(self):
        """Should retrieve the current team"""
        # Arrange
        self.mock_client.mock_response(
            "GET",
            "/team",
            MockResponse(status=200, body=mock_team_list)
        )

        # Act
        result = self.sdk.teams.get()

        # Assert
        assert result is not None
        assert result.data is not None
        assert len(result.data) == 1
        assert result.data[0].id == "team_test123"
        assert result.data[0].attributes.name == "Test Team"

    def test_create_team(self):
        """Should create a new team"""
        # Arrange
        new_team = {
            **mock_team,
            "id": "team_new123",
            "attributes": {
                **mock_team["attributes"],
                "name": "New Team",
                "slug": "new-team",
            },
        }

        self.mock_client.mock_response(
            "POST",
            "/team",
            MockResponse(status=201, body={"data": new_team})
        )

        # Act
        result = self.sdk.teams.create(
            data={
                "type": "teams",
                "attributes": {
                    "name": "New Team",
                    "currency": "USD",
                },
            }
        )

        # Assert
        assert result is not None
        assert result.data.id == "team_new123"
        assert result.data.attributes.name == "New Team"

    def test_update_team(self):
        """Should update a team"""
        # Arrange
        updated_team = {
            **mock_team,
            "attributes": {
                **mock_team["attributes"],
                "name": "Updated Team Name",
                "description": "Updated description",
            },
        }

        self.mock_client.mock_response(
            "PATCH",
            "/team/team_test123",
            MockResponse(status=200, body={"data": updated_team})
        )

        # Act
        result = self.sdk.teams.update(
            team_id="team_test123",
            data={
                "id": "team_test123",
                "type": "teams",
                "attributes": {
                    "name": "Updated Team Name",
                    "description": "Updated description",
                },
            }
        )

        # Assert
        assert result is not None
        assert result.data.attributes.name == "Updated Team Name"
        assert result.data.attributes.description == "Updated description"

    def test_team_users(self):
        """Should retrieve team with users"""
        # Arrange
        self.mock_client.mock_response(
            "GET",
            "/team",
            MockResponse(status=200, body=mock_team_list)
        )

        # Act
        result = self.sdk.teams.get()

        # Assert
        assert result.data[0].attributes.users is not None
        assert len(result.data[0].attributes.users) == 1
        assert result.data[0].attributes.users[0].email == "test@example.com"

    def test_team_projects(self):
        """Should retrieve team with projects"""
        # Arrange
        self.mock_client.mock_response(
            "GET",
            "/team",
            MockResponse(status=200, body=mock_team_list)
        )

        # Act
        result = self.sdk.teams.get()

        # Assert
        assert result.data[0].attributes.projects is not None
        assert len(result.data[0].attributes.projects) == 1
        assert result.data[0].attributes.projects[0].id == "proj_test123"

    def test_team_not_found(self):
        """Should handle team not found"""
        # Arrange
        self.mock_client.mock_response(
            "GET",
            "/team",
            MockResponse(
                status=404,
                body={
                    "error": {
                        "message": "Team not found",
                        "code": "not_found",
                    },
                }
            )
        )

        # Act & Assert
        with pytest.raises(Exception):
            self.sdk.teams.get()

    def test_team_mfa_enforcement(self):
        """Should check MFA enforcement status"""
        # Arrange
        self.mock_client.mock_response(
            "GET",
            "/team",
            MockResponse(status=200, body=mock_team_list)
        )

        # Act
        result = self.sdk.teams.get()

        # Assert
        assert result.data[0].attributes.enforce_mfa is False

    def test_team_feature_flags(self):
        """Should retrieve team feature flags"""
        # Arrange
        self.mock_client.mock_response(
            "GET",
            "/team",
            MockResponse(status=200, body=mock_team_list)
        )

        # Act
        result = self.sdk.teams.get()

        # Assert
        assert result.data[0].attributes.feature_flags is not None
        assert len(result.data[0].attributes.feature_flags) == 2
        assert "feature_1" in result.data[0].attributes.feature_flags
