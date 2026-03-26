# PrivateNetworks

## Overview

### Available Operations

* [list](#list) - List VLANs
* [create](#create) - Create VLAN
* [update](#update) - Update VLAN
* [delete_virtual_network](#delete_virtual_network) - Delete VLAN
* [get](#get) - Retrieve VLAN
* [list_assignments](#list_assignments) - List VLAN assignments
* [assign](#assign) - Assign VLAN
* [remove_assignment](#remove_assignment) - Delete VLAN assignment

## list

Lists virtual networks assigned to a project


### Example Usage: Filtered by multiple tags

<!-- UsageSnippet language="python" operationID="get-virtual-networks" method="get" path="/virtual_networks" example="Filtered by multiple tags" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.private_networks.list(filter_tags="tag_5EJXPRJKB3h5XZJjwL42iEx4RWk,tag_Vx53BQnm94UbrgGlay5lFgEJZ8a", page_size=20, page_number=1)

    while res is not None:
        # Handle items

        res = res.next()

```
### Example Usage: List virtual networks filtered by tag

<!-- UsageSnippet language="python" operationID="get-virtual-networks" method="get" path="/virtual_networks" example="List virtual networks filtered by tag" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.private_networks.list(filter_tags="tag_KLmjvaEPE7uL9G9E42pxTrEK96Jn", page_size=20, page_number=1)

    while res is not None:
        # Handle items

        res = res.next()

```
### Example Usage: Success

<!-- UsageSnippet language="python" operationID="get-virtual-networks" method="get" path="/virtual_networks" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.private_networks.list(filter_tags="tag_BZWAJKePr2Fx9kRyyaARImQlXmW,tag_X8yMgb8AZPFrX72lQgrwhBVnPN2", page_size=20, page_number=1)

    while res is not None:
        # Handle items

        res = res.next()

```
### Example Usage: filtered by project

<!-- UsageSnippet language="python" operationID="get-virtual-networks" method="get" path="/virtual_networks" example="filtered by project" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.private_networks.list(filter_project="awesome-copper-clock", page_size=20, page_number=1)

    while res is not None:
        # Handle items

        res = res.next()

```
### Example Usage: filtered by site

<!-- UsageSnippet language="python" operationID="get-virtual-networks" method="get" path="/virtual_networks" example="filtered by site" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.private_networks.list(filter_location="SAO", page_size=20, page_number=1)

    while res is not None:
        # Handle items

        res = res.next()

```
### Example Usage: without filters

<!-- UsageSnippet language="python" operationID="get-virtual-networks" method="get" path="/virtual_networks" example="without filters" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.private_networks.list(page_size=20, page_number=1)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                   | Type                                                                                                                        | Required                                                                                                                    | Description                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `filter_location`                                                                                                           | *Optional[str]*                                                                                                             | :heavy_minus_sign:                                                                                                          | The location slug to filter by                                                                                              |
| `filter_project`                                                                                                            | *Optional[str]*                                                                                                             | :heavy_minus_sign:                                                                                                          | The project id or slug to filter by                                                                                         |
| `filter_tags`                                                                                                               | *Optional[str]*                                                                                                             | :heavy_minus_sign:                                                                                                          | The tags ids to filter by, separated by comma, e.g. `filter[tags]=tag_1,tag_2`will return ssh keys with `tag_1` AND `tag_2` |
| `page_size`                                                                                                                 | *Optional[int]*                                                                                                             | :heavy_minus_sign:                                                                                                          | Number of items to return per page                                                                                          |
| `page_number`                                                                                                               | *Optional[int]*                                                                                                             | :heavy_minus_sign:                                                                                                          | Page number to return (starts at 1)                                                                                         |
| `retries`                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                            | :heavy_minus_sign:                                                                                                          | Configuration to override the default retry behavior of the client.                                                         |

### Response

**[models.GetVirtualNetworksResponse](../../models/getvirtualnetworksresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create

Creates a new Virtual Network.


### Example Usage: Created

<!-- UsageSnippet language="python" operationID="create-virtual-network" method="post" path="/virtual_networks" example="Created" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.private_networks.create(data={
        "type": latitudesh_python_sdk.CreateVirtualNetworkPrivateNetworksType.VIRTUAL_NETWORK,
        "attributes": {
            "description": "São Paulo VLAN",
            "site": latitudesh_python_sdk.CreateVirtualNetworkPrivateNetworksSite.MIA,
            "project": "ergonomic-steel-bag",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: validation error

<!-- UsageSnippet language="python" operationID="create-virtual-network" method="post" path="/virtual_networks" example="validation error" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.private_networks.create(data={
        "type": latitudesh_python_sdk.CreateVirtualNetworkPrivateNetworksType.VIRTUAL_NETWORK,
        "attributes": {
            "description": "São Paulo VLAN",
            "project": "<value>",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: when the project has reached max_vlans

<!-- UsageSnippet language="python" operationID="create-virtual-network" method="post" path="/virtual_networks" example="when the project has reached max_vlans" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.private_networks.create(data={
        "type": latitudesh_python_sdk.CreateVirtualNetworkPrivateNetworksType.VIRTUAL_NETWORK,
        "attributes": {
            "description": "São Paulo VLAN",
            "site": latitudesh_python_sdk.CreateVirtualNetworkPrivateNetworksSite.MIA,
            "project": "lightweight-rubber-shirt",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: when the user is allowed to create

<!-- UsageSnippet language="python" operationID="create-virtual-network" method="post" path="/virtual_networks" example="when the user is allowed to create" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.private_networks.create(data={
        "type": latitudesh_python_sdk.CreateVirtualNetworkPrivateNetworksType.VIRTUAL_NETWORK,
        "attributes": {
            "description": "São Paulo VLAN",
            "site": latitudesh_python_sdk.CreateVirtualNetworkPrivateNetworksSite.MIA,
            "project": "enormous-paper-clock",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `data`                                                                                                    | [models.CreateVirtualNetworkPrivateNetworksData](../../models/createvirtualnetworkprivatenetworksdata.md) | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[models.VirtualNetwork](../../models/virtualnetwork.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update

Update a Virtual Network.


### Example Usage: Success

<!-- UsageSnippet language="python" operationID="update-virtual-network" method="patch" path="/virtual_networks/{vlan_id}" example="Success" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.private_networks.update(vlan_id="vlan_VaNmodjeObE8W", data={
        "id": "vlan_VaNmodjeObE8W",
        "type": latitudesh_python_sdk.UpdateVirtualNetworkPrivateNetworksType.VIRTUAL_NETWORKS,
        "attributes": {
            "tags": [
                "tag_RjLvG6oe84IAw7BxxEGaFAXK4l4",
                "tag_lpPQ21kXEYfb9az3jRoVIVw4RBk",
            ],
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Tag not updated

<!-- UsageSnippet language="python" operationID="update-virtual-network" method="patch" path="/virtual_networks/{vlan_id}" example="Tag not updated" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.private_networks.update(vlan_id="vlan_6059EqYkOQj8p", data={
        "id": "<id>",
        "type": latitudesh_python_sdk.UpdateVirtualNetworkPrivateNetworksType.VIRTUAL_NETWORKS,
        "attributes": {
            "tags": [
                "invalid-tag",
            ],
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Unpermited parameter

<!-- UsageSnippet language="python" operationID="update-virtual-network" method="patch" path="/virtual_networks/{vlan_id}" example="Unpermited parameter" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.private_networks.update(vlan_id="vlan_w5AEmq7XDBkWX", data={
        "id": "<id>",
        "type": latitudesh_python_sdk.UpdateVirtualNetworkPrivateNetworksType.VIRTUAL_NETWORKS,
        "attributes": {},
    })

    # Handle response
    print(res)

```
### Example Usage: when the user is allowed to update virtual networks

<!-- UsageSnippet language="python" operationID="update-virtual-network" method="patch" path="/virtual_networks/{vlan_id}" example="when the user is allowed to update virtual networks" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.private_networks.update(vlan_id="vlan_zGr47qlMDAg0m", data={
        "id": "<id>",
        "type": latitudesh_python_sdk.UpdateVirtualNetworkPrivateNetworksType.VIRTUAL_NETWORKS,
        "attributes": {},
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `vlan_id`                                                                                                 | *str*                                                                                                     | :heavy_check_mark:                                                                                        | The Virtual Network ID                                                                                    |
| `data`                                                                                                    | [models.UpdateVirtualNetworkPrivateNetworksData](../../models/updatevirtualnetworkprivatenetworksdata.md) | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[models.VirtualNetwork](../../models/virtualnetwork.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete_virtual_network

Delete virtual network


### Example Usage

<!-- UsageSnippet language="python" operationID="destroy-virtual-network" method="delete" path="/virtual_networks/{vlan_id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.private_networks.delete_virtual_network(vlan_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `vlan_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The virtual network ID                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get

Retrieve a Virtual Network.


### Example Usage: List private networks

<!-- UsageSnippet language="python" operationID="get-virtual-network" method="get" path="/virtual_networks/{vlan_id}" example="List private networks" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.private_networks.get(vlan_id="vlan_W6Q2D9ordKLpr")

    # Handle response
    print(res)

```
### Example Usage: Success

<!-- UsageSnippet language="python" operationID="get-virtual-network" method="get" path="/virtual_networks/{vlan_id}" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.private_networks.get(vlan_id="vlan_W6Q2D9ordKLpr")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `vlan_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Virtual Network ID                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.VirtualNetwork](../../models/virtualnetwork.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_assignments

Returns a list of all servers assigned to virtual networks.


### Example Usage: Success

<!-- UsageSnippet language="python" operationID="get-virtual-networks-assignments" method="get" path="/virtual_networks/assignments" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.private_networks.list_assignments(page_size=20, page_number=1)

    while res is not None:
        # Handle items

        res = res.next()

```
### Example Usage: when filtering by server_id

<!-- UsageSnippet language="python" operationID="get-virtual-networks-assignments" method="get" path="/virtual_networks/assignments" example="when filtering by server_id" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.private_networks.list_assignments(filter_server="217", page_size=20, page_number=1)

    while res is not None:
        # Handle items

        res = res.next()

```
### Example Usage: when filtering by vid

<!-- UsageSnippet language="python" operationID="get-virtual-networks-assignments" method="get" path="/virtual_networks/assignments" example="when filtering by vid" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.private_networks.list_assignments(filter_vid="8", page_size=20, page_number=1)

    while res is not None:
        # Handle items

        res = res.next()

```
### Example Usage: when no filters are applied

<!-- UsageSnippet language="python" operationID="get-virtual-networks-assignments" method="get" path="/virtual_networks/assignments" example="when no filters are applied" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.private_networks.list_assignments(page_size=20, page_number=1)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `filter_server`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The server ID to filter by                                          |
| `filter_vid`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The vlan ID to filter by                                            |
| `filter_virtual_network_id`                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The virtual network ID to filter by                                 |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Number of items to return per page                                  |
| `page_number`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Page number to return (starts at 1)                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetVirtualNetworksAssignmentsResponse](../../models/getvirtualnetworksassignmentsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## assign

Assign VLAN

### Example Usage: Created

<!-- UsageSnippet language="python" operationID="assign-server-virtual-network" method="post" path="/virtual_networks/assignments" example="Created" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.private_networks.assign(data={
        "type": latitudesh_python_sdk.AssignServerVirtualNetworkPrivateNetworksType.VIRTUAL_NETWORK_ASSIGNMENT,
        "attributes": {
            "server_id": "sv_5xyZOn5vDWM0l",
            "virtual_network_id": "vlan_Z8rodmpGO1jLB",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Forbidden

<!-- UsageSnippet language="python" operationID="assign-server-virtual-network" method="post" path="/virtual_networks/assignments" example="Forbidden" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.private_networks.assign(data={
        "type": latitudesh_python_sdk.AssignServerVirtualNetworkPrivateNetworksType.VIRTUAL_NETWORK_ASSIGNMENT,
        "attributes": {
            "server_id": "sv_LYV8DZ61D5QoE",
            "virtual_network_id": "vlan_3YjJOLBjqvZ87",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: validation error

<!-- UsageSnippet language="python" operationID="assign-server-virtual-network" method="post" path="/virtual_networks/assignments" example="validation error" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.private_networks.assign(data={
        "type": latitudesh_python_sdk.AssignServerVirtualNetworkPrivateNetworksType.VIRTUAL_NETWORK_ASSIGNMENT,
        "attributes": {
            "server_id": "<id>",
            "virtual_network_id": "<id>",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                       | Type                                                                                                                            | Required                                                                                                                        | Description                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `data`                                                                                                                          | [Optional[models.AssignServerVirtualNetworkPrivateNetworksData]](../../models/assignservervirtualnetworkprivatenetworksdata.md) | :heavy_minus_sign:                                                                                                              | N/A                                                                                                                             |
| `retries`                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                | :heavy_minus_sign:                                                                                                              | Configuration to override the default retry behavior of the client.                                                             |

### Response

**[models.VirtualNetworkAssignment](../../models/virtualnetworkassignment.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## remove_assignment

Allow you to remove a Virtual Network assignment.


### Example Usage

<!-- UsageSnippet language="python" operationID="delete-virtual-networks-assignments" method="delete" path="/virtual_networks/assignments/{assignment_id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.private_networks.remove_assignment(assignment_id="vnasg_LA73qk8WDaJ2o")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `assignment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |