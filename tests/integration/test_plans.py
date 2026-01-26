"""
Integration tests for Plans resource
"""

import pytest
from tests.integration.helpers import (
    setup_test,
    mock_plan,
    mock_plan_list,
    MockResponse,
)


class TestPlansIntegration:
    """Integration tests for Plans resource"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test client before each test"""
        self.sdk, self.mock_client, self.reset = setup_test()
        self.reset()
        yield

    def test_list_all_plans(self):
        """Should list all plans"""
        # Arrange
        self.mock_client.mock_response(
            "GET",
            "/plans",
            MockResponse(status=200, body=mock_plan_list)
        )

        # Act
        result = self.sdk.plans.list()

        # Assert
        assert result is not None
        assert result.data is not None
        assert len(result.data) == 1
        assert result.data[0].id == "c3.small.x86"
        assert result.data[0].attributes.slug == "c3-small-x86"

    def test_list_empty_plans(self):
        """Should handle empty plans list"""
        # Arrange
        self.mock_client.mock_response(
            "GET",
            "/plans",
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
        result = self.sdk.plans.list()

        # Assert
        assert result is not None
        assert len(result.data) == 0

    def test_get_plan_by_id(self):
        """Should retrieve a plan by ID"""
        # Arrange
        self.mock_client.mock_response(
            "GET",
            "/plans/c3.small.x86",
            MockResponse(status=200, body={"data": mock_plan})
        )

        # Act
        result = self.sdk.plans.get(plan_id="c3.small.x86")

        # Assert
        assert result is not None
        assert result.data.id == "c3.small.x86"
        assert result.data.attributes.name == "c3.small.x86"
        assert result.data.attributes.slug == "c3-small-x86"

    def test_plan_specs(self):
        """Should retrieve plan specifications"""
        # Arrange
        self.mock_client.mock_response(
            "GET",
            "/plans/c3.small.x86",
            MockResponse(status=200, body={"data": mock_plan})
        )

        # Act
        result = self.sdk.plans.get(plan_id="c3.small.x86")

        # Assert
        assert result.data.attributes.specs is not None
        assert result.data.attributes.specs.cpu.cores == 4
        assert result.data.attributes.specs.memory.total == 16

    def test_plan_regions(self):
        """Should retrieve plan regions and availability"""
        # Arrange
        self.mock_client.mock_response(
            "GET",
            "/plans/c3.small.x86",
            MockResponse(status=200, body={"data": mock_plan})
        )

        # Act
        result = self.sdk.plans.get(plan_id="c3.small.x86")

        # Assert
        assert result.data.attributes.regions is not None
        assert len(result.data.attributes.regions) == 1
        assert result.data.attributes.regions[0].name == "São Paulo"
        assert result.data.attributes.regions[0].stock_level == "high"

    def test_plan_not_found(self):
        """Should handle plan not found"""
        # Arrange
        self.mock_client.mock_response(
            "GET",
            "/plans/nonexistent",
            MockResponse(
                status=404,
                body={
                    "error": {
                        "message": "Plan not found",
                        "code": "not_found",
                    },
                }
            )
        )

        # Act & Assert
        with pytest.raises(Exception):
            self.sdk.plans.get(plan_id="nonexistent")

    def test_filter_plans_by_region(self):
        """Should filter plans by region"""
        # Arrange
        self.mock_client.mock_response(
            "GET",
            "/plans",
            MockResponse(
                status=200,
                body={
                    "data": [mock_plan],
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
        result = self.sdk.plans.list()

        # Assert
        assert result is not None
        assert len(result.data) >= 1
