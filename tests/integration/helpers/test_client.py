"""
Test client setup utilities
"""

from typing import Optional, Tuple
import httpx
from latitudesh_python_sdk import Latitudesh
from .mock_http_client import MockHTTPClient


class LatitudeTestClient:
    """Latitude test client wrapper"""

    def __init__(
        self,
        sdk: Latitudesh,
        mock_client: MockHTTPClient,
        http_client: httpx.Client
    ):
        self.sdk = sdk
        self.mock_client = mock_client
        self.http_client = http_client

    def reset(self) -> None:
        """Reset mock client state"""
        self.mock_client.reset()

    def close(self) -> None:
        """Close HTTP client"""
        self.http_client.close()


def create_test_client(
    api_key: Optional[str] = None,
    server_url: Optional[str] = None
) -> LatitudeTestClient:
    """
    Create a test SDK instance with mock HTTP client

    Args:
        api_key: Optional API key (defaults to 'test-api-key')
        server_url: Optional server URL (defaults to 'https://api.latitude.sh')

    Returns:
        LatitudeTestClient instance
    """
    mock_client = MockHTTPClient()

    # Create httpx client with mock transport
    http_client = httpx.Client(
        transport=mock_client.get_transport(),
        base_url=server_url or 'https://api.latitude.sh'
    )

    # Create SDK instance with mock client
    sdk = Latitudesh(
        bearer=api_key or 'test-api-key',
        server_url=server_url or 'https://api.latitude.sh',
        client=http_client
    )

    return LatitudeTestClient(sdk, mock_client, http_client)


def setup_test() -> Tuple[Latitudesh, MockHTTPClient, callable]:
    """
    Setup common test utilities

    Returns:
        Tuple of (sdk, mock_client, reset_function)
    """
    test_client = create_test_client()

    return test_client.sdk, test_client.mock_client, test_client.reset
