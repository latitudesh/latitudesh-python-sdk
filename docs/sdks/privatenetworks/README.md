# PrivateNetworks
(*private_networks*)

## Overview

### Available Operations

* [list](#list) - List all Virtual Networks
* [create](#create) - Create a Virtual Network
* [update](#update) - Update a Virtual Network
* [delete_virtual_network](#delete_virtual_network) - Delete a Virtual Network
* [get](#get) - Retrieve a Virtual Network
* [list_assignments](#list_assignments) - List all servers assigned to virtual networks
* [assign](#assign) - Assign Virtual network
* [remove_assignment](#remove_assignment) - Delete Virtual Network Assignment

## list

Lists virtual networks assigned to a project


### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.private_networks.list(filter_location="SAO", filter_project="awesome-copper-clock", filter_tags="tag_KLmjvaEPE7uL9G9E42pxTrEK96Jn", page_size=20, page_number=1)

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


### Example Usage

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

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 422                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## update

Update a Virtual Network.


### Example Usage

```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.private_networks.update(vlan_id="vlan_zGr47qlMDAg0m", data={
        "type": latitudesh_python_sdk.UpdateVirtualNetworkPrivateNetworksType.VIRTUAL_NETWORKS,
        "attributes": {},
    }, id="vlan_81EVOtR1N4J2Z")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `vlan_id`                                                                                                 | *str*                                                                                                     | :heavy_check_mark:                                                                                        | The Virtual Network ID                                                                                    |
| `data`                                                                                                    | [models.UpdateVirtualNetworkPrivateNetworksData](../../models/updatevirtualnetworkprivatenetworksdata.md) | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `id`                                                                                                      | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[models.VirtualNetwork](../../models/virtualnetwork.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.VirtualNetworkError | 403                        | application/vnd.api+json   |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete_virtual_network

Delete virtual network


### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.private_networks.delete_virtual_network(vlan_id=793185)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `vlan_id`                                                           | *int*                                                               | :heavy_check_mark:                                                  | The virtual network ID                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 406                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## get

Retrieve a Virtual Network.


### Example Usage

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

**[models.GetVirtualNetworkResponseBody](../../models/getvirtualnetworkresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_assignments

Returns a list of all servers assigned to virtual networks.


### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.private_networks.list_assignments(filter_server="217", filter_vid="8", page_size=20, page_number=1)

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

Assign Virtual network

### Example Usage

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
            "server_id": "sv_pbV0DgQGd4AWz",
            "virtual_network_id": "vlan_059EqYe2qQj8p",
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

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 422                 | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## remove_assignment

Allow you to remove a Virtual Network assignment.


### Example Usage

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

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 423                 | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |