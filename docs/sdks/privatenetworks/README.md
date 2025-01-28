# PrivateNetworks
(*private_networks*)

## Overview

### Available Operations

* [get_virtual_networks](#get_virtual_networks) - List all Virtual Networks
* [create_virtual_network](#create_virtual_network) - Create a Virtual Network
* [update_virtual_network](#update_virtual_network) - Update a Virtual Network
* [destroy_virtual_network](#destroy_virtual_network) - Delete a Virtual Network
* [get_virtual_network](#get_virtual_network) - Retrieve a Virtual Network
* [get_virtual_networks_assignments](#get_virtual_networks_assignments) - List all servers assigned to virtual networks
* [assign_server_virtual_network](#assign_server_virtual_network) - Assign Virtual network
* [delete_virtual_networks_assignments](#delete_virtual_networks_assignments) - Delete Virtual Network Assignment

## get_virtual_networks

Lists virtual networks assigned to a project


### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.private_networks.get_virtual_networks(filter_location="SAO", filter_project="awesome-cotton-bag", filter_tags="tag_9Mk835MMXPcEjlrgop7Js5XAZ20")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                   | Type                                                                                                                        | Required                                                                                                                    | Description                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `filter_location`                                                                                                           | *Optional[str]*                                                                                                             | :heavy_minus_sign:                                                                                                          | The location slug to filter by                                                                                              |
| `filter_project`                                                                                                            | *Optional[str]*                                                                                                             | :heavy_minus_sign:                                                                                                          | The project id or slug to filter by                                                                                         |
| `filter_tags`                                                                                                               | *Optional[str]*                                                                                                             | :heavy_minus_sign:                                                                                                          | The tags ids to filter by, separated by comma, e.g. `filter[tags]=tag_1,tag_2`will return ssh keys with `tag_1` AND `tag_2` |
| `retries`                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                            | :heavy_minus_sign:                                                                                                          | Configuration to override the default retry behavior of the client.                                                         |

### Response

**[models.VirtualNetworks](../../models/virtualnetworks.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_virtual_network

Creates a new Virtual Network.


### Example Usage

```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.private_networks.create_virtual_network(request={
        "data": {
            "type": latitudesh_python_sdk.CreateVirtualNetworkType.VIRTUAL_NETWORK,
            "attributes": {
                "description": "São Paulo VLAN",
                "project": "awesome-copper-car",
                "site": latitudesh_python_sdk.CreateVirtualNetworkSite.MIA,
            },
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `request`                                                                                 | [models.CreateVirtualNetworkRequestBody](../../models/createvirtualnetworkrequestbody.md) | :heavy_check_mark:                                                                        | The request object to use for the request.                                                |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.VirtualNetwork](../../models/virtualnetwork.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ErrorObject | 422                | application/json   |
| models.APIError    | 4XX, 5XX           | \*/\*              |

## update_virtual_network

Update a Virtual Network.


### Example Usage

```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.private_networks.update_virtual_network(vlan_id="vlan_pRMLydp0dQKr1", data={
        "type": latitudesh_python_sdk.UpdateVirtualNetworkType.VIRTUAL_NETWORKS,
        "attributes": {
            "description": "Test virtual network update",
        },
    }, id="vlan_81EVOtR1N4J2Z")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `vlan_id`                                                                   | *str*                                                                       | :heavy_check_mark:                                                          | The Virtual Network ID                                                      |
| `data`                                                                      | [models.UpdateVirtualNetworkData](../../models/updatevirtualnetworkdata.md) | :heavy_check_mark:                                                          | N/A                                                                         |
| `id`                                                                        | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | N/A                                                                         |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.VirtualNetwork](../../models/virtualnetwork.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.VirtualNetworkError | 403                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## destroy_virtual_network

Delete virtual network


### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.private_networks.destroy_virtual_network(vlan_id=invalid-id)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `vlan_id`                                                           | *int*                                                               | :heavy_check_mark:                                                  | The virtual network ID                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ErrorObject | 406                | application/json   |
| models.APIError    | 4XX, 5XX           | \*/\*              |

## get_virtual_network

Retrieve a Virtual Network.


### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.private_networks.get_virtual_network(vlan_id="vlan_W6Q2D9ordKLpr")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `vlan_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Virtual Network ID                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetVirtualNetworkResponseBody](../../models/getvirtualnetworkresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_virtual_networks_assignments

Returns a list of all servers assigned to virtual networks.


### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.private_networks.get_virtual_networks_assignments(filter_server="206", filter_vid="8")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `filter_server`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The server ID to filter by                                          |
| `filter_vid`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The vlan ID to filter by                                            |
| `filter_virtual_network_id`                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The virtual network ID to filter by                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.VirtualNetworkAssignments](../../models/virtualnetworkassignments.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## assign_server_virtual_network

Assign Virtual network

### Example Usage

```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.private_networks.assign_server_virtual_network(request={
        "data": {
            "type": latitudesh_python_sdk.AssignServerVirtualNetworkType.VIRTUAL_NETWORK_ASSIGNMENT,
            "attributes": {
                "server_id": "sv_059EqYVjDQj8p",
                "virtual_network_id": vlan_g1mbDwG0DLv5B,
            },
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `request`                                                                                             | [models.AssignServerVirtualNetworkRequestBody](../../models/assignservervirtualnetworkrequestbody.md) | :heavy_check_mark:                                                                                    | The request object to use for the request.                                                            |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.VirtualNetworkAssignment](../../models/virtualnetworkassignment.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ErrorObject | 403, 422           | application/json   |
| models.APIError    | 4XX, 5XX           | \*/\*              |

## delete_virtual_networks_assignments

Allow you to remove a Virtual Network assignment.


### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.private_networks.delete_virtual_networks_assignments(assignment_id="vnasg_695BdKagDevVo")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `assignment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ErrorObject | 403, 423           | application/json   |
| models.APIError    | 4XX, 5XX           | \*/\*              |