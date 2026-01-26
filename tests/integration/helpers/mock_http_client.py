"""
Mock HTTP Client for Integration Tests

This mock client intercepts HTTP requests and returns predefined responses
to simulate API behavior without making actual network calls.
"""

import json
import re
from typing import Any, Dict, List, Optional, Pattern, Union
from dataclasses import dataclass
import httpx


@dataclass
class MockResponse:
    """Mock response configuration"""
    status: int
    headers: Optional[Dict[str, str]] = None
    body: Optional[Any] = None


@dataclass
class MockRequest:
    """Recorded request information"""
    method: str
    url: str
    headers: Optional[Dict[str, str]] = None
    body: Optional[Any] = None


class MockHTTPClient:
    """
    Mock HTTP Client for testing

    This client intercepts HTTP requests and returns predefined mock responses
    instead of making actual network calls.
    """

    def __init__(self):
        self.responses: Dict[str, List[MockResponse]] = {}
        self.requests: List[MockRequest] = []

    def mock_response(
        self,
        method: str,
        url_pattern: Union[str, Pattern],
        response: MockResponse
    ) -> None:
        """
        Register a mock response for a specific endpoint

        Args:
            method: HTTP method (GET, POST, etc.)
            url_pattern: URL pattern to match (string or regex)
            response: MockResponse to return
        """
        key = f"{method}:{str(url_pattern)}"
        if key not in self.responses:
            self.responses[key] = []
        self.responses[key].append(response)

    def get_transport(self) -> httpx.MockTransport:
        """
        Get a mock transport for httpx client

        Returns:
            httpx.MockTransport instance
        """
        def handler(request: httpx.Request) -> httpx.Response:
            # Record the request
            self.requests.append(MockRequest(
                method=request.method,
                url=str(request.url),
                headers=dict(request.headers),
                body=request.content.decode() if request.content else None
            ))

            # Find matching mock response
            mock_response = self._find_mock_response(request.method, str(request.url))

            if not mock_response:
                raise ValueError(
                    f"No mock response configured for {request.method} {request.url}"
                )

            # Create response
            headers = mock_response.headers or {
                'content-type': 'application/vnd.api+json'
            }

            content = (
                json.dumps(mock_response.body).encode()
                if mock_response.body is not None
                else b""
            )

            return httpx.Response(
                status_code=mock_response.status,
                headers=headers,
                content=content
            )

        return httpx.MockTransport(handler)

    def _find_mock_response(self, method: str, url: str) -> Optional[MockResponse]:
        """
        Find a matching mock response for the given method and URL

        Args:
            method: HTTP method
            url: Request URL

        Returns:
            MockResponse if found, None otherwise
        """
        for key, responses in self.responses.items():
            mock_method, mock_url = key.split(':', 1)

            if mock_method != method:
                continue

            # Check if URL matches (either exact match or regex)
            matches = False
            if mock_url.startswith('/') and not mock_url.startswith('//'):
                # Simple string matching
                matches = mock_url in url
            else:
                # Try regex matching
                try:
                    pattern = re.compile(mock_url)
                    matches = pattern.search(url) is not None
                except re.error:
                    # If not a valid regex, try exact match
                    matches = mock_url == url

            if matches and responses:
                return responses.pop(0)  # Return and remove first response

        return None

    def get_requests(self) -> List[MockRequest]:
        """Get all recorded requests"""
        return list(self.requests)

    def get_last_request(self) -> Optional[MockRequest]:
        """Get the last recorded request"""
        return self.requests[-1] if self.requests else None

    def reset(self) -> None:
        """Clear all mock responses and recorded requests"""
        self.responses.clear()
        self.requests.clear()

    def verify_request(self, method: str, url_pattern: Union[str, Pattern]) -> bool:
        """
        Verify that a request was made

        Args:
            method: HTTP method to verify
            url_pattern: URL pattern to match (string or regex)

        Returns:
            True if matching request was found, False otherwise
        """
        for req in self.requests:
            if req.method != method:
                continue

            if isinstance(url_pattern, str):
                if url_pattern in req.url:
                    return True
            elif isinstance(url_pattern, Pattern):
                if url_pattern.search(req.url):
                    return True

        return False

    def count_requests(
        self,
        method: Optional[str] = None,
        url_pattern: Optional[Union[str, Pattern]] = None
    ) -> int:
        """
        Count requests matching the criteria

        Args:
            method: Optional HTTP method filter
            url_pattern: Optional URL pattern filter

        Returns:
            Number of matching requests
        """
        count = 0
        for req in self.requests:
            if method and req.method != method:
                continue

            if url_pattern:
                if isinstance(url_pattern, str):
                    if url_pattern not in req.url:
                        continue
                elif isinstance(url_pattern, Pattern):
                    if not url_pattern.search(req.url):
                        continue

            count += 1

        return count
