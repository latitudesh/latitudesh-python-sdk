# FirewallsSDK
(*firewalls*)

## Overview

### Available Operations

* [get_all_firewall_assignments](#get_all_firewall_assignments) - List All Firewall Assignments
* [create](#create) - Create a firewall
* [list](#list) - List firewalls
* [get](#get) - Retrieve Firewall
* [update](#update) - Update Firewall
* [delete](#delete) - Delete Firewall
* [assign](#assign) - Firewall Assignment
* [list_assignments](#list_assignments) - Firewall Assignments
* [delete_assignment](#delete_assignment) - Delete Firewall Assignment

## get_all_firewall_assignments

List all firewall assignments

### Example Usage

<!-- UsageSnippet language="python" operationID="get-all-firewall-assignments" method="get" path="/firewalls/assignments" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.firewalls.get_all_firewall_assignments(filter_server="sv_RLYV8DZ2D5QoE", page_size=20, page_number=1)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `filter_server`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The server ID to filter by                                          |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Number of items to return per page                                  |
| `page_number`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Page number to return (starts at 1)                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetAllFirewallAssignmentsResponse](../../models/getallfirewallassignmentsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create

Create a firewall

### Example Usage

<!-- UsageSnippet language="python" operationID="create-firewall" method="post" path="/firewalls" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.firewalls.create(data={
        "type": latitudesh_python_sdk.CreateFirewallFirewallsType.FIREWALLS,
        "attributes": {
            "name": "my-firewall",
            "project": "awesome-granite-chair",
            "rules": [
                {
                    "from_": "192.168.42.73",
                    "to": "192.168.43.51",
                    "protocol": latitudesh_python_sdk.CreateFirewallProtocol.TCP,
                    "port": "80",
                },
                {
                    "from_": "192.168.1.16",
                    "to": "192.168.1.30",
                    "protocol": latitudesh_python_sdk.CreateFirewallProtocol.TCP,
                    "port": "80",
                },
                {
                    "from_": "192.168.1.10",
                    "to": "192.168.1.20",
                    "protocol": latitudesh_python_sdk.CreateFirewallProtocol.UDP,
                    "port": "3000-4000",
                },
            ],
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `data`                                                                            | [models.CreateFirewallFirewallsData](../../models/createfirewallfirewallsdata.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.Firewall](../../models/firewall.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list

List firewalls

### Example Usage

<!-- UsageSnippet language="python" operationID="list-firewalls" method="get" path="/firewalls" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.firewalls.list(filter_project="incredible-bronze-car", page_size=20, page_number=1)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `filter_project`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Number of items to return per page                                  |
| `page_number`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Page number to return (starts at 1)                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListFirewallsResponse](../../models/listfirewallsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get

Retrieve a firewall

### Example Usage

<!-- UsageSnippet language="python" operationID="get-firewall" method="get" path="/firewalls/{firewall_id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.firewalls.get(firewall_id="fw_xkjQwdENqYNVP")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `firewall_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The Firewall ID                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Firewall](../../models/firewall.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update

Update a firewall

### Example Usage

<!-- UsageSnippet language="python" operationID="update-firewall" method="patch" path="/firewalls/{firewall_id}" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.firewalls.update(firewall_id="fw_6A05EdQ1dvKYQ", data={
        "type": latitudesh_python_sdk.UpdateFirewallFirewallsType.FIREWALLS,
        "attributes": {
            "name": "new-name",
            "rules": [
                {
                    "from_": "192.168.42.72",
                    "to": "192.168.43.51",
                    "protocol": latitudesh_python_sdk.UpdateFirewallFirewallsProtocol.TCP,
                    "port": "80",
                },
            ],
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `firewall_id`                                                                     | *str*                                                                             | :heavy_check_mark:                                                                | The Firewall ID                                                                   |
| `data`                                                                            | [models.UpdateFirewallFirewallsData](../../models/updatefirewallfirewallsdata.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.Firewall](../../models/firewall.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete

Delete a firewall

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-firewall" method="delete" path="/firewalls/{firewall_id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.firewalls.delete(firewall_id="fw_123")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `firewall_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The Firewall ID                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## assign

Assign a server to a firewall

### Example Usage

<!-- UsageSnippet language="python" operationID="create-firewall-assignment" method="post" path="/firewalls/{firewall_id}/assignments" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.firewalls.assign(firewall_id="fw_Av9BVDavORm1W", data={
        "type": latitudesh_python_sdk.CreateFirewallAssignmentFirewallsType.FIREWALL_ASSIGNMENTS,
        "attributes": {
            "server_id": "sv_lpbV0DgRq4AWz",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `firewall_id`                                                                                         | *str*                                                                                                 | :heavy_check_mark:                                                                                    | The Firewall ID                                                                                       |
| `data`                                                                                                | [models.CreateFirewallAssignmentFirewallsData](../../models/createfirewallassignmentfirewallsdata.md) | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.FirewallServer](../../models/firewallserver.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_assignments

List servers assigned to a firewall

### Example Usage

<!-- UsageSnippet language="python" operationID="get-firewall-assignments" method="get" path="/firewalls/{firewall_id}/assignments" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.firewalls.list_assignments(firewall_id="fw_z8Nkvdy1deLpx", page_size=20, page_number=1)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `firewall_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The Firewall ID                                                     |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Number of items to return per page                                  |
| `page_number`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Page number to return (starts at 1)                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetFirewallAssignmentsResponse](../../models/getfirewallassignmentsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete_assignment

Remove a server from a firewall

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-firewall-assignment" method="delete" path="/firewalls/{firewall_id}/assignments/{assignment_id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.firewalls.delete_assignment(firewall_id="fw_2695BdKrOevVo", assignment_id="fwasg_6059EqYkOQj8p")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `firewall_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The Firewall ID                                                     |
| `assignment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The Assignment ID                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |