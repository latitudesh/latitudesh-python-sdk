# FirewallsSDK
(*firewalls*)

## Overview

### Available Operations

* [create_firewall](#create_firewall) - Create a firewall
* [list_firewalls](#list_firewalls) - List firewalls
* [get_firewall](#get_firewall) - Retrieve Firewall
* [update_firewall](#update_firewall) - Update Firewall
* [delete_firewall](#delete_firewall) - Delete Firewall
* [create_firewall_assignment](#create_firewall_assignment) - Firewall Assignment
* [get_firewall_assignments](#get_firewall_assignments) - Firewall Assignments
* [delete_firewall_assignment](#delete_firewall_assignment) - Delete Firewall Assignment

## create_firewall

Create a firewall

### Example Usage

```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.firewalls.create_firewall(request={
        "data": {
            "type": latitudesh_python_sdk.CreateFirewallFirewallsType.FIREWALLS,
            "attributes": {
                "name": "my-firewall",
                "project": "small-rubber-lamp",
                "rules": [
                    {
                        "from_": "192.168.42.72",
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
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `request`                                                                                       | [models.CreateFirewallFirewallsRequestBody](../../models/createfirewallfirewallsrequestbody.md) | :heavy_check_mark:                                                                              | The request object to use for the request.                                                      |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.Firewall](../../models/firewall.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 422                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## list_firewalls

List firewalls

### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.firewalls.list_firewalls(filter_project="aerodynamic-silk-pants")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `filter_project`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Firewalls](../../models/firewalls.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_firewall

Retrieve a firewall

### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.firewalls.get_firewall(firewall_id="fw_xkjQwdENqYNVP")

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

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 404                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## update_firewall

Update a firewall

### Example Usage

```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.firewalls.update_firewall(firewall_id="fw_VaNmodjeObE8W", data={
        "type": latitudesh_python_sdk.UpdateFirewallFirewallsType.FIREWALLS,
        "attributes": {
            "rules": [

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

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 404, 422                 | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## delete_firewall

Delete a firewall

### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.firewalls.delete_firewall(firewall_id="fw_123")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `firewall_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The Firewall ID                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 404, 422                 | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## create_firewall_assignment

Assign a server to a firewall

### Example Usage

```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.firewalls.create_firewall_assignment(firewall_id="fw_Av9BVDavORm1W", data={
        "type": latitudesh_python_sdk.CreateFirewallAssignmentFirewallsType.FIREWALL_ASSIGNMENTS,
        "attributes": {
            "server_id": "sv_2695BdKrOevVo",
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

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 404, 409, 422       | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## get_firewall_assignments

List servers assigned to a firewall

### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.firewalls.get_firewall_assignments(firewall_id="fw_93YjJOLydvZ87")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `firewall_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The Firewall ID                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.FirewallServer](../../models/firewallserver.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 404                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## delete_firewall_assignment

Remove a server from a firewall

### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.firewalls.delete_firewall_assignment(firewall_id="fw_2695BdKrOevVo", assignment_id="fwasg_6059EqYkOQj8p")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `firewall_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The Firewall ID                                                     |
| `assignment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The Assignment ID                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 404                 | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |