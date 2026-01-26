"""
Mock data for integration tests
"""

from typing import Any, Dict, List


# Servers
mock_server = {
    "id": "srv_test123",
    "type": "servers",
    "attributes": {
        "hostname": "test-server-01",
        "label": "Test Server",
        "status": "on",
        "role": "Bare Metal",
        "site": "sao-paulo",
        "locked": False,
        "rescue": False,
        "primary_ipv4": "192.0.2.1",
        "primary_ipv6": "2001:db8::1",
        "created_at": "2024-01-01T00:00:00Z",
        "scheduled_deletion_at": None,
        "plan": {
            "id": "c3.small.x86",
            "name": "c3.small.x86",
            "slug": "c3-small-x86",
        },
        "operating_system": {
            "name": "Ubuntu 22.04 LTS x64",
            "slug": "ubuntu_22_04_x64_lts",
            "version": "22.04",
        },
        "region": {
            "city": "São Paulo",
            "country": "BR",
            "site": {
                "id": "site_sao_paulo",
                "name": "São Paulo",
                "slug": "sao-paulo",
                "facility": "Facility A",
                "rack_id": "rack-01",
            },
        },
        "specs": {
            "cpu": "4 cores",
            "disk": "480 GB",
            "ram": "16 GB",
            "nic": "1 Gbps",
            "gpu": None,
        },
        "project": {
            "id": "proj_test123",
            "name": "Test Project",
            "slug": "test-project",
        },
    },
}

mock_server_list = {
    "data": [
        mock_server,
        {
            **mock_server,
            "id": "srv_test456",
            "attributes": {
                **mock_server["attributes"],
                "hostname": "test-server-02",
                "label": "Test Server 2",
                "primary_ipv4": "192.0.2.2",
            },
        },
    ],
    "meta": {
        "total": 2,
        "current_page": 1,
        "last_page": 1,
        "per_page": 25,
    },
}

mock_server_create_request = {
    "type": "servers",
    "attributes": {
        "project": "proj_test123",
        "plan": "c3-small-x86",
        "operating_system": "ubuntu_22_04_x64_lts",
        "hostname": "test-server-01",
        "site": "SAO",
    },
}

# Projects
mock_project = {
    "id": "proj_test123",
    "type": "projects",
    "attributes": {
        "name": "Test Project",
        "slug": "test-project",
        "description": "A test project for integration tests",
        "billing_type": "Monthly",
        "billing_method": "Normal",
        "cost": "0.00",
        "environment": "Development",
        "stats": {
            "ip_addresses": 2,
            "prefixes": 0,
            "servers": 1,
            "containers": 0,
            "vlans": 1,
        },
        "billing": {
            "subscription_id": "sub_test123",
            "type": "monthly",
            "method": "normal",
        },
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-01T00:00:00Z",
    },
}

mock_project_list = {
    "data": [
        mock_project,
        {
            "id": "proj_test456",
            "type": "projects",
            "attributes": {
                "name": "Production Project",
                "slug": "production-project",
                "description": "Production environment project",
                "billing_type": "Monthly",
                "billing_method": "Normal",
                "cost": "150.00",
                "environment": "Production",
                "stats": {
                    "ip_addresses": 10,
                    "prefixes": 1,
                    "servers": 5,
                    "containers": 2,
                    "vlans": 3,
                },
                "billing": {
                    "subscription_id": "sub_test456",
                    "type": "monthly",
                    "method": "normal",
                },
                "created_at": "2024-01-02T00:00:00Z",
                "updated_at": "2024-01-15T00:00:00Z",
            },
        },
    ],
    "meta": {
        "total": 2,
        "current_page": 1,
        "last_page": 1,
        "per_page": 25,
    },
}

# API Keys
mock_api_key = {
    "id": "apikey_test123",
    "type": "api_keys",
    "attributes": {
        "name": "Test API Key",
        "api_version": "v1",
        "token_last_slice": "abc12",
        "read_only": False,
        "allowed_ips": ["192.168.1.1", "10.0.0.0/24"],
        "last_used_at": "2024-01-15T10:30:00Z",
        "user": {
            "id": "user_test123",
            "email": "test@example.com",
        },
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-01T00:00:00Z",
    },
}

mock_api_key_list = {
    "data": [
        mock_api_key,
        {
            "id": "apikey_test456",
            "type": "api_keys",
            "attributes": {
                "name": "Production API Key",
                "api_version": "v1",
                "token_last_slice": "xyz78",
                "read_only": True,
                "allowed_ips": None,
                "last_used_at": "2024-01-20T14:45:00Z",
                "user": {
                    "id": "user_test456",
                    "email": "prod@example.com",
                },
                "created_at": "2024-01-10T00:00:00Z",
                "updated_at": "2024-01-20T00:00:00Z",
            },
        },
    ],
}

# Plans
mock_plan = {
    "id": "c3.small.x86",
    "type": "plans",
    "attributes": {
        "slug": "c3-small-x86",
        "name": "c3.small.x86",
        "features": ["ssh", "raid", "user_data"],
        "specs": {
            "cpu": {
                "type": "Intel Xeon E3",
                "clock": 3.4,
                "cores": 4,
                "count": 1,
            },
            "memory": {
                "total": 16,
            },
            "nics": [
                {
                    "type": "1Gbps",
                    "count": 2,
                },
            ],
            "drives": [
                {
                    "type": "SSD",
                    "size": "480 GB",
                    "count": 2,
                },
            ],
        },
        "regions": [
            {
                "name": "São Paulo",
                "deploys_instantly": ["sao-paulo-1", "sao-paulo-2"],
                "locations": {
                    "available": ["sao-paulo-1", "sao-paulo-2"],
                    "in_stock": ["sao-paulo-1"],
                },
                "stock_level": "high",
            },
        ],
    },
}

mock_plan_list = {
    "data": [mock_plan],
}

# Teams
mock_team = {
    "id": "team_test123",
    "attributes": {
        "name": "Test Team",
        "slug": "test-team",
        "description": "A test team for integration tests",
        "address": "123 Test Street, Test City",
        "currency": "USD",
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-01T00:00:00Z",
        "enforce_mfa": False,
        "users": [
            {
                "id": "user_test123",
                "email": "test@example.com",
                "first_name": "Test",
                "last_name": "User",
                "role": {
                    "id": "role_admin",
                    "name": "admin",
                    "created_at": "2024-01-01T00:00:00Z",
                    "updated_at": "2024-01-01T00:00:00Z",
                },
            },
        ],
        "projects": [
            {
                "id": "proj_test123",
                "name": "Test Project",
                "slug": "test-project",
            },
        ],
        "owner": {
            "id": "user_test123",
            "email": "test@example.com",
            "first_name": "Test",
            "last_name": "User",
            "role": {
                "id": "role_owner",
                "name": "owner",
                "created_at": "2024-01-01T00:00:00Z",
                "updated_at": "2024-01-01T00:00:00Z",
            },
        },
        "billing": {
            "id": "billing_test123",
            "customer_billing_id": "cus_test123",
        },
        "feature_flags": ["feature_1", "feature_2"],
    },
}

mock_team_list = {
    "data": [mock_team],
    "meta": {},
}

# User Data
mock_user_data = {
    "data": {
        "id": "userdata_test123",
        "type": "user_data",
        "attributes": {
            "description": "Test User Data Script",
            "content": "#!/bin/bash\necho \"Hello World\"\napt-get update\napt-get install -y nginx",
            "project": {
                "id": "proj_test123",
                "name": "Test Project",
                "slug": "test-project",
            },
            "created_at": "2024-01-01T00:00:00Z",
            "updated_at": "2024-01-01T00:00:00Z",
        },
    },
    "meta": {},
}

mock_user_data_list = {
    "data": [
        {
            "data": {
                "id": "userdata_test123",
                "type": "user_data",
                "attributes": {
                    "description": "Test User Data Script",
                    "content": "#!/bin/bash\necho \"Hello World\"\napt-get update\napt-get install -y nginx",
                    "project": {
                        "id": "proj_test123",
                        "name": "Test Project",
                        "slug": "test-project",
                    },
                    "created_at": "2024-01-01T00:00:00Z",
                    "updated_at": "2024-01-01T00:00:00Z",
                },
            },
            "meta": {},
        },
    ],
    "meta": {},
}

# Error responses
mock_error = {
    "error": {
        "message": "Resource not found",
        "code": "not_found",
    },
}

mock_validation_error = {
    "error": {
        "message": "Validation failed",
        "code": "validation_error",
        "errors": [
            {
                "field": "hostname",
                "message": "Hostname is required",
            },
        ],
    },
}

mock_rate_limit_error = {
    "error": {
        "message": "Rate limit exceeded",
        "code": "rate_limit_exceeded",
        "retry_after": 60,
    },
}


def create_mock_servers(count: int) -> List[Dict[str, Any]]:
    """
    Create multiple mock server objects

    Args:
        count: Number of mock servers to create

    Returns:
        List of mock server dictionaries
    """
    servers = []
    for i in range(count):
        server = {
            **mock_server,
            "id": f"srv_test{i + 1}",
            "attributes": {
                **mock_server["attributes"],
                "hostname": f"test-server-{str(i + 1).zfill(2)}",
                "label": f"Test Server {i + 1}",
                "primary_ipv4": f"192.0.2.{i + 1}",
            },
        }
        servers.append(server)
    return servers


def create_paginated_response(
    data: List[Any],
    page: int = 1,
    per_page: int = 25
) -> Dict[str, Any]:
    """
    Create a paginated response

    Args:
        data: List of data items
        page: Current page number
        per_page: Items per page

    Returns:
        Paginated response dictionary
    """
    start = (page - 1) * per_page
    end = start + per_page
    page_data = data[start:end]

    return {
        "data": page_data,
        "meta": {
            "total": len(data),
            "current_page": page,
            "last_page": (len(data) + per_page - 1) // per_page,
            "per_page": per_page,
        },
    }
