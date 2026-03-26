# Servers

## Overview

### Available Operations

* [list](#list) - List servers
* [create](#create) - Create server
* [get](#get) - Retrieve server
* [update](#update) - Update server
* [delete](#delete) - Remove server
* [get_deploy_config](#get_deploy_config) - Retrieve deploy config
* [update_deploy_config](#update_deploy_config) - Update deploy config
* [lock](#lock) - Lock server
* [unlock](#unlock) - Unlock server
* [create_out_of_band_connection](#create_out_of_band_connection) - Create out-of-band connection
* [list_out_of_band_connections](#list_out_of_band_connections) - List out-of-band connections
* [actions](#actions) - Run power action
* [create_ipmi_session](#create_ipmi_session) - Create IPMI credentials
* [start_rescue_mode](#start_rescue_mode) - Put server in rescue mode
* [exit_rescue_mode](#exit_rescue_mode) - Exits rescue mode
* [schedule_deletion](#schedule_deletion) - Schedule server deletion
* [unschedule_deletion](#unschedule_deletion) - Unschedule server deletion
* [reinstall](#reinstall) - Run Server Reinstall

## list

Returns a list of all servers belonging to the team.


### Example Usage: Filtered by multiple tags

<!-- UsageSnippet language="python" operationID="get-servers" method="get" path="/servers" example="Filtered by multiple tags" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.list(filter_tags="tag_3lg8RjPJL7HK4jYBbLmxC0ZR0yVX,tag_5JgXW7Wyr6i5V85g2Y2MFWL8bXA", page_size=20, page_number=1)

    while res is not None:
        # Handle items

        res = res.next()

```
### Example Usage: Success

<!-- UsageSnippet language="python" operationID="get-servers" method="get" path="/servers" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.list(filter_tags="tag_pjAkRjVzw0tlYBA2WX1eHzW7w79,tag_yARk1KLJAvslWY7k5wNBCaKEV7e", page_size=20, page_number=1)

    while res is not None:
        # Handle items

        res = res.next()

```
### Example Usage: when no filters

<!-- UsageSnippet language="python" operationID="get-servers" method="get" path="/servers" example="when no filters" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.list(page_size=20, page_number=1)

    while res is not None:
        # Handle items

        res = res.next()

```
### Example Usage: when project filter

<!-- UsageSnippet language="python" operationID="get-servers" method="get" path="/servers" example="when project filter" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.list(filter_project="proj_g1mbDwrZqLv5B", page_size=20, page_number=1)

    while res is not None:
        # Handle items

        res = res.next()

```
### Example Usage: when region filter

<!-- UsageSnippet language="python" operationID="get-servers" method="get" path="/servers" example="when region filter" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.list(filter_region="SAO", page_size=20, page_number=1)

    while res is not None:
        # Handle items

        res = res.next()

```
### Example Usage: when trying to filter by tag

<!-- UsageSnippet language="python" operationID="get-servers" method="get" path="/servers" example="when trying to filter by tag" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.list(filter_tags="tag_0yrQNVQRLwHy0XwEGM6ESwLrW2PA", page_size=20, page_number=1)

    while res is not None:
        # Handle items

        res = res.next()

```
### Example Usage: with a `eql` filter

<!-- UsageSnippet language="python" operationID="get-servers" method="get" path="/servers" example="with a `eql` filter" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.list(filter_ram_eql=32, page_size=20, page_number=1)

    while res is not None:
        # Handle items

        res = res.next()

```
### Example Usage: with a `gte` filter

<!-- UsageSnippet language="python" operationID="get-servers" method="get" path="/servers" example="with a `gte` filter" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.list(filter_ram_gte=40, page_size=20, page_number=1)

    while res is not None:
        # Handle items

        res = res.next()

```
### Example Usage: with a `lte` filter

<!-- UsageSnippet language="python" operationID="get-servers" method="get" path="/servers" example="with a `lte` filter" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.list(filter_ram_lte=40, page_size=20, page_number=1)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                          | Type                                                                                                                                                                                                                                                                                                                                                                               | Required                                                                                                                                                                                                                                                                                                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `filter_project`                                                                                                                                                                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                 | The project ID or Slug to filter by                                                                                                                                                                                                                                                                                                                                                |
| `filter_region`                                                                                                                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                 | The region Slug to filter by                                                                                                                                                                                                                                                                                                                                                       |
| `filter_hostname`                                                                                                                                                                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                 | The hostname of server to filter by                                                                                                                                                                                                                                                                                                                                                |
| `filter_created_at_gte`                                                                                                                                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                 | The created at greater than equal date to filter by                                                                                                                                                                                                                                                                                                                                |
| `filter_created_at_lte`                                                                                                                                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                 | The created at less than equal date to filter by                                                                                                                                                                                                                                                                                                                                   |
| `filter_label`                                                                                                                                                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                 | The label of server to filter by                                                                                                                                                                                                                                                                                                                                                   |
| `filter_status`                                                                                                                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                 | The status of server to filter by                                                                                                                                                                                                                                                                                                                                                  |
| `filter_plan`                                                                                                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                 | The platform/plan name of the server to filter by                                                                                                                                                                                                                                                                                                                                  |
| `filter_gpu`                                                                                                                                                                                                                                                                                                                                                                       | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                 | Filter by the existence of an associated GPU                                                                                                                                                                                                                                                                                                                                       |
| `filter_ram_eql`                                                                                                                                                                                                                                                                                                                                                                   | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                 | Filter servers with RAM size (in GB) equals the provided value.                                                                                                                                                                                                                                                                                                                    |
| `filter_ram_gte`                                                                                                                                                                                                                                                                                                                                                                   | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                 | Filter servers with RAM size (in GB) greater than or equal the provided value.                                                                                                                                                                                                                                                                                                     |
| `filter_ram_lte`                                                                                                                                                                                                                                                                                                                                                                   | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                 | Filter servers with RAM size (in GB) less than or equal the provided value.                                                                                                                                                                                                                                                                                                        |
| `filter_disk`                                                                                                                                                                                                                                                                                                                                                                      | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                 | The disk size in Gigabytes to filter by, should be used with the following options:<br/>                              [eql] to filter for values equal to the provided value.<br/>                              [gte] to filter for values greater than or equal to the provided value.<br/>                              [lte] to filter by values lower than or equal to the provided value. |
| `filter_tags`                                                                                                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                 | The tags IDs to filter by, separated by comma, e.g. `filter[tags]=tag_1,tag_2`will return servers with `tag_1` AND `tag_2`                                                                                                                                                                                                                                                         |
| `extra_fields_servers`                                                                                                                                                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                 | The `credentials` are provided as extra attributes that are lazy loaded. To request it, just set `extra_fields[servers]=credentials` in the query string.                                                                                                                                                                                                                          |
| `page_size`                                                                                                                                                                                                                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                 | Number of items to return per page                                                                                                                                                                                                                                                                                                                                                 |
| `page_number`                                                                                                                                                                                                                                                                                                                                                                      | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                 | Page number to return (starts at 1)                                                                                                                                                                                                                                                                                                                                                |
| `retries`                                                                                                                                                                                                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                |

### Response

**[models.GetServersResponse](../../models/getserversresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create

Create server

### Example Usage: Created

<!-- UsageSnippet language="python" operationID="create-server" method="post" path="/servers" example="Created" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.create(data={
        "type": latitudesh_python_sdk.CreateServerServersType.SERVERS,
        "attributes": {
            "project": "proj_lxWpD699qm6rk",
            "plan": latitudesh_python_sdk.CreateServerServersPlan.C2_SMALL_X86,
            "site": latitudesh_python_sdk.CreateServerServersSite.ASH,
            "operating_system": latitudesh_python_sdk.CreateServerServersOperatingSystem.UBUNTU_22_04_X64_LTS,
            "hostname": "BRC1",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Payment Required

<!-- UsageSnippet language="python" operationID="create-server" method="post" path="/servers" example="Payment Required" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.create(data={
        "type": latitudesh_python_sdk.CreateServerServersType.SERVERS,
        "attributes": {
            "project": "proj_kjQwdEMXdYNVP",
            "plan": latitudesh_python_sdk.CreateServerServersPlan.C2_SMALL_X86,
            "site": latitudesh_python_sdk.CreateServerServersSite.SAO,
            "operating_system": latitudesh_python_sdk.CreateServerServersOperatingSystem.UBUNTU_22_04_X64_LTS,
            "hostname": "BRC1",
            "billing": latitudesh_python_sdk.CreateServerServersBilling.MONTHLY,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Unpermited parameter

<!-- UsageSnippet language="python" operationID="create-server" method="post" path="/servers" example="Unpermited parameter" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.create(data={
        "type": latitudesh_python_sdk.CreateServerServersType.SERVERS,
        "attributes": {},
    })

    # Handle response
    print(res)

```
### Example Usage: Unprocessable Entity

<!-- UsageSnippet language="python" operationID="create-server" method="post" path="/servers" example="Unprocessable Entity" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.create(data={
        "type": latitudesh_python_sdk.CreateServerServersType.SERVERS,
        "attributes": {
            "project": "proj_RMLydp9XqQKr1",
            "plan": latitudesh_python_sdk.CreateServerServersPlan.C2_SMALL_X86,
            "site": latitudesh_python_sdk.CreateServerServersSite.SAO,
            "operating_system": latitudesh_python_sdk.CreateServerServersOperatingSystem.UBUNTU_22_04_X64_LTS,
            "hostname": "BRC1",
            "ssh_keys": [
                "ssh_93YjJOLydvZ87",
            ],
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `data`                                                                              | [Optional[models.CreateServerServersData]](../../models/createserverserversdata.md) | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.Server](../../models/server.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get

Returns a server that belongs to the team.


### Example Usage

<!-- UsageSnippet language="python" operationID="get-server" method="get" path="/servers/{server_id}" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.get(server_id="sv_VE1Wd3aXDXnZJ")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                | Type                                                                                                                                                     | Required                                                                                                                                                 | Description                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `server_id`                                                                                                                                              | *str*                                                                                                                                                    | :heavy_check_mark:                                                                                                                                       | The Server ID                                                                                                                                            |
| `extra_fields_servers`                                                                                                                                   | *Optional[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                       | The `credentials` are provided as extra attributes that is lazy loaded. To request it, just set `extra_fields[servers]=credentials` in the query string. |
| `retries`                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                         | :heavy_minus_sign:                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                      |

### Response

**[models.Server](../../models/server.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update

Update server

### Example Usage: Locked server

<!-- UsageSnippet language="python" operationID="update-server" method="patch" path="/servers/{server_id}" example="Locked server" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.update(server_id="sv_g1mbDwrZqLv5B", data={
        "id": "sv_g1mbDwrZqLv5B",
        "type": latitudesh_python_sdk.UpdateServerServersType.SERVERS,
        "attributes": {
            "billing": latitudesh_python_sdk.UpdateServerServersBilling.HOURLY,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Payment Required

<!-- UsageSnippet language="python" operationID="update-server" method="patch" path="/servers/{server_id}" example="Payment Required" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.update(server_id="sv_1ZJrdxe4qg4LV", data={
        "id": "sv_1ZJrdxe4qg4LV",
        "type": latitudesh_python_sdk.UpdateServerServersType.SERVERS,
        "attributes": {
            "billing": latitudesh_python_sdk.UpdateServerServersBilling.MONTHLY,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Reserved project

<!-- UsageSnippet language="python" operationID="update-server" method="patch" path="/servers/{server_id}" example="Reserved project" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.update(server_id="sv_w49QDBaQqagKb", data={
        "id": "sv_w49QDBaQqagKb",
        "type": latitudesh_python_sdk.UpdateServerServersType.SERVERS,
        "attributes": {
            "billing": latitudesh_python_sdk.UpdateServerServersBilling.HOURLY,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Success

<!-- UsageSnippet language="python" operationID="update-server" method="patch" path="/servers/{server_id}" example="Success" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.update(server_id="sv_yQrJdNAGO30gv", data={
        "id": "sv_yQrJdNAGO30gv",
        "type": latitudesh_python_sdk.UpdateServerServersType.SERVERS,
        "attributes": {
            "project": "proj_yQrJdNMGO30gv",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Unpermitted parameter

<!-- UsageSnippet language="python" operationID="update-server" method="patch" path="/servers/{server_id}" example="Unpermitted parameter" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.update(server_id="sv_3YjJOLLNOvZ87", data={
        "id": "sv_3YjJOLLNOvZ87",
        "type": latitudesh_python_sdk.UpdateServerServersType.SERVERS,
        "attributes": {
            "billing": latitudesh_python_sdk.UpdateServerServersBilling.MONTHLY,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Unprocessable Entity

<!-- UsageSnippet language="python" operationID="update-server" method="patch" path="/servers/{server_id}" example="Unprocessable Entity" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.update(server_id="sv_vYAZqGNJdMQ94", data={
        "id": "sv_vYAZqGNJdMQ94",
        "type": latitudesh_python_sdk.UpdateServerServersType.SERVERS,
        "attributes": {
            "billing": latitudesh_python_sdk.UpdateServerServersBilling.MONTHLY,
            "project": "new-project",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: when server has additional ips

<!-- UsageSnippet language="python" operationID="update-server" method="patch" path="/servers/{server_id}" example="when server has additional ips" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.update(server_id="sv_W6Q2D9lGqKLpr", data={
        "id": "sv_W6Q2D9lGqKLpr",
        "type": latitudesh_python_sdk.UpdateServerServersType.SERVERS,
        "attributes": {
            "billing": latitudesh_python_sdk.UpdateServerServersBilling.YEARLY,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: when server has vlan assignments

<!-- UsageSnippet language="python" operationID="update-server" method="patch" path="/servers/{server_id}" example="when server has vlan assignments" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.update(server_id="sv_LMmAD8k4qwop2", data={
        "id": "sv_LMmAD8k4qwop2",
        "type": latitudesh_python_sdk.UpdateServerServersType.SERVERS,
        "attributes": {
            "billing": latitudesh_python_sdk.UpdateServerServersBilling.YEARLY,
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                             | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           | Example                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `server_id`                                                                                                           | *str*                                                                                                                 | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |                                                                                                                       |
| `data`                                                                                                                | [Optional[models.UpdateServerServersData]](../../models/updateserverserversdata.md)                                   | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   | {<br/>"data": {<br/>"id": "sv_81EVOtR1N4J2Z",<br/>"type": "servers",<br/>"attributes": {<br/>"hostname": "new-hostname",<br/>"tags": []<br/>}<br/>}<br/>} |
| `retries`                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                      | :heavy_minus_sign:                                                                                                    | Configuration to override the default retry behavior of the client.                                                   |                                                                                                                       |

### Response

**[models.Server](../../models/server.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete

Remove server

### Example Usage

<!-- UsageSnippet language="python" operationID="destroy-server" method="delete" path="/servers/{server_id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.servers.delete(server_id="sv_WeGoqAZNDP7nz")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `server_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The server ID                                                       |
| `reason`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The reason for deleting the server                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_deploy_config

Retrieve deploy config

### Example Usage

<!-- UsageSnippet language="python" operationID="get-server-deploy-config" method="get" path="/servers/{server_id}/deploy_config" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.get_deploy_config(server_id="sv_pRMLydp0dQKr1")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `server_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The Server ID                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeployConfig](../../models/deployconfig.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_deploy_config

Update deploy config

### Example Usage: Forbidden

<!-- UsageSnippet language="python" operationID="update-server-deploy-config" method="patch" path="/servers/{server_id}/deploy_config" example="Forbidden" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.update_deploy_config(server_id="sv_kjQwdEmXdYNVP", type_=latitudesh_python_sdk.UpdateServerDeployConfigServersType.DEPLOY_CONFIG)

    # Handle response
    print(res)

```
### Example Usage: Not Acceptable

<!-- UsageSnippet language="python" operationID="update-server-deploy-config" method="patch" path="/servers/{server_id}/deploy_config" example="Not Acceptable" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.update_deploy_config(server_id="sv_5AEmq7xMDBkWX", type_=latitudesh_python_sdk.UpdateServerDeployConfigServersType.DEPLOY_CONFIG)

    # Handle response
    print(res)

```
### Example Usage: Success

<!-- UsageSnippet language="python" operationID="update-server-deploy-config" method="patch" path="/servers/{server_id}/deploy_config" example="Success" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.update_deploy_config(server_id="sv_lkg1DeYLDvZE5", type_=latitudesh_python_sdk.UpdateServerDeployConfigServersType.DEPLOY_CONFIG)

    # Handle response
    print(res)

```
### Example Usage: Unprocessable Entity

<!-- UsageSnippet language="python" operationID="update-server-deploy-config" method="patch" path="/servers/{server_id}/deploy_config" example="Unprocessable Entity" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.update_deploy_config(server_id="sv_Gr47ql4vqAg0m", type_=latitudesh_python_sdk.UpdateServerDeployConfigServersType.DEPLOY_CONFIG)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                               | Type                                                                                                                    | Required                                                                                                                | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `server_id`                                                                                                             | *str*                                                                                                                   | :heavy_check_mark:                                                                                                      | The Server ID                                                                                                           |
| `type`                                                                                                                  | [models.UpdateServerDeployConfigServersType](../../models/updateserverdeployconfigserverstype.md)                       | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `attributes`                                                                                                            | [Optional[models.UpdateServerDeployConfigServersAttributes]](../../models/updateserverdeployconfigserversattributes.md) | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `retries`                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                        | :heavy_minus_sign:                                                                                                      | Configuration to override the default retry behavior of the client.                                                     |

### Response

**[models.DeployConfig](../../models/deployconfig.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## lock

Locks the server. A locked server cannot be deleted or modified and no actions can be performed on it.

### Example Usage: Forbidden

<!-- UsageSnippet language="python" operationID="server-lock" method="post" path="/servers/{server_id}/lock" example="Forbidden" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.lock(server_id="sv_VE1Wd3rXOXnZJ")

    # Handle response
    print(res)

```
### Example Usage: Not Found

<!-- UsageSnippet language="python" operationID="server-lock" method="post" path="/servers/{server_id}/lock" example="Not Found" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.lock(server_id="invalid")

    # Handle response
    print(res)

```
### Example Usage: Ok

<!-- UsageSnippet language="python" operationID="server-lock" method="post" path="/servers/{server_id}/lock" example="Ok" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.lock(server_id="sv_059EqYX2dQj8p")

    # Handle response
    print(res)

```
### Example Usage: Success

<!-- UsageSnippet language="python" operationID="server-lock" method="post" path="/servers/{server_id}/lock" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.lock(server_id="sv_pbV0DgjKq4AWz")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `server_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Server](../../models/server.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## unlock

Unlocks the server. A locked server cannot be deleted or modified and no actions can be performed on it.

### Example Usage: Forbidden

<!-- UsageSnippet language="python" operationID="server-unlock" method="post" path="/servers/{server_id}/unlock" example="Forbidden" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.unlock(server_id="sv_A05EdQM4dvKYQ")

    # Handle response
    print(res)

```
### Example Usage: Not Found

<!-- UsageSnippet language="python" operationID="server-unlock" method="post" path="/servers/{server_id}/unlock" example="Not Found" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.unlock(server_id="invalid")

    # Handle response
    print(res)

```
### Example Usage: Ok

<!-- UsageSnippet language="python" operationID="server-unlock" method="post" path="/servers/{server_id}/unlock" example="Ok" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.unlock(server_id="sv_aNmodjoyqbE8W")

    # Handle response
    print(res)

```
### Example Usage: Success

<!-- UsageSnippet language="python" operationID="server-unlock" method="post" path="/servers/{server_id}/unlock" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.unlock(server_id="sv_e8pKq0xYqWAob")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `server_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Server](../../models/server.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_out_of_band_connection

Create out-of-band connection

### Example Usage: Created

<!-- UsageSnippet language="python" operationID="create-server-out-of-band" method="post" path="/servers/{server_id}/out_of_band_connection" example="Created" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.create_out_of_band_connection(server_id="sv_8NkvdyGKDeLpx", data={
        "type": latitudesh_python_sdk.CreateServerOutOfBandServersType.OUT_OF_BAND,
        "attributes": {
            "ssh_key_id": "ssh_3YjJOLMydvZ87",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Forbidden

<!-- UsageSnippet language="python" operationID="create-server-out-of-band" method="post" path="/servers/{server_id}/out_of_band_connection" example="Forbidden" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.create_out_of_band_connection(server_id="sv_lkg1DeYLDvZE5", data={
        "type": latitudesh_python_sdk.CreateServerOutOfBandServersType.OUT_OF_BAND,
        "attributes": {
            "ssh_key_id": "ssh_aKXgRdR3qv9k5",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Not found

<!-- UsageSnippet language="python" operationID="create-server-out-of-band" method="post" path="/servers/{server_id}/out_of_band_connection" example="Not found" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.create_out_of_band_connection(server_id="invalid-server", data={
        "type": latitudesh_python_sdk.CreateServerOutOfBandServersType.OUT_OF_BAND,
        "attributes": {
            "ssh_key_id": "ssh_m1R3zq2bqWxyn",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: when the server is being provisioned

<!-- UsageSnippet language="python" operationID="create-server-out-of-band" method="post" path="/servers/{server_id}/out_of_band_connection" example="when the server is being provisioned" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.create_out_of_band_connection(server_id="sv_0MK4O44ROa95w", data={
        "type": latitudesh_python_sdk.CreateServerOutOfBandServersType.OUT_OF_BAND,
        "attributes": {
            "ssh_key_id": "ssh_vGMy1DbgON50m",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `server_id`                                                                                 | *str*                                                                                       | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `data`                                                                                      | [models.CreateServerOutOfBandServersData](../../models/createserveroutofbandserversdata.md) | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.OutOfBandConnection](../../models/outofbandconnection.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_out_of_band_connections

List out-of-band connections

### Example Usage

<!-- UsageSnippet language="python" operationID="get-server-out-of-band" method="get" path="/servers/{server_id}/out_of_band_connection" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.list_out_of_band_connections(server_id="sv_GnzRD5lvqM5yw")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `server_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The Server ID                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OutOfBandConnection](../../models/outofbandconnection.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## actions

Performs an action on a given server:
- `power_on`
- `power_off`
- `reboot`


### Example Usage: Created

<!-- UsageSnippet language="python" operationID="create-server-action" method="post" path="/servers/{server_id}/actions" example="Created" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.actions(server_id="sv_WVQJDMVBORbyE", data={
        "type": latitudesh_python_sdk.CreateServerActionServersType.ACTIONS,
        "attributes": {
            "action": latitudesh_python_sdk.CreateServerActionAction.REBOOT,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Forbidden

<!-- UsageSnippet language="python" operationID="create-server-action" method="post" path="/servers/{server_id}/actions" example="Forbidden" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.actions(server_id="sv_e8pKq0xYqWAob", data={
        "type": latitudesh_python_sdk.CreateServerActionServersType.ACTIONS,
        "attributes": {
            "action": latitudesh_python_sdk.CreateServerActionAction.POWER_OFF,
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `server_id`                                                                           | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `data`                                                                                | [models.CreateServerActionServersData](../../models/createserveractionserversdata.md) | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.ServerAction](../../models/serveraction.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_ipmi_session

Generates IPMI credentials for a given server. Remote access creates a VPN connection to the internal network of your server so you can connect to its IPMI.
You will have to use a VPN client such as https://openvpn.net to connect. See `VPN Sessions` API to create a VPN connection.

Related guide: https://docs.latitude.sh/docs/ipmi


### Example Usage: Created

<!-- UsageSnippet language="python" operationID="create-ipmi-session" method="post" path="/servers/{server_id}/remote_access" example="Created" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.create_ipmi_session(server_id="sv_Qkm7dXaRq8nZV")

    # Handle response
    print(res)

```
### Example Usage: Not found

<!-- UsageSnippet language="python" operationID="create-ipmi-session" method="post" path="/servers/{server_id}/remote_access" example="Not found" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.create_ipmi_session(server_id="invalid")

    # Handle response
    print(res)

```
### Example Usage: Unprocessable entity

<!-- UsageSnippet language="python" operationID="create-ipmi-session" method="post" path="/servers/{server_id}/remote_access" example="Unprocessable entity" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.create_ipmi_session(server_id="sv_yQrJdNMGO30gv")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `server_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.IpmiSession](../../models/ipmisession.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## start_rescue_mode

Starts rescue mode on a given server.

### Example Usage: Created

<!-- UsageSnippet language="python" operationID="server-start-rescue-mode" method="post" path="/servers/{server_id}/rescue_mode" example="Created" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.start_rescue_mode(server_id="sv_WeGoqAWNOP7nz")

    # Handle response
    print(res)

```
### Example Usage: Not Acceptable

<!-- UsageSnippet language="python" operationID="server-start-rescue-mode" method="post" path="/servers/{server_id}/rescue_mode" example="Not Acceptable" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.start_rescue_mode(server_id="sv_GnzRD5lvqM5yw")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `server_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ServerRescue](../../models/serverrescue.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## exit_rescue_mode

Exits rescue mode on a given server.

### Example Usage: Not Acceptable

<!-- UsageSnippet language="python" operationID="server-exit-rescue-mode" method="post" path="/servers/{server_id}/exit_rescue_mode" example="Not Acceptable" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.exit_rescue_mode(server_id="sv_WVQJDMVBORbyE")

    # Handle response
    print(res)

```
### Example Usage: Success

<!-- UsageSnippet language="python" operationID="server-exit-rescue-mode" method="post" path="/servers/{server_id}/exit_rescue_mode" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.exit_rescue_mode(server_id="sv_3YjJOLQNdvZ87")

    # Handle response
    print(res)

```
### Example Usage: if the server is entering rescue mode

<!-- UsageSnippet language="python" operationID="server-exit-rescue-mode" method="post" path="/servers/{server_id}/exit_rescue_mode" example="if the server is entering rescue mode" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.exit_rescue_mode(server_id="sv_1R3zq2JxqWxyn")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `server_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ServerRescue](../../models/serverrescue.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## schedule_deletion

Schedules the server to be removed at the end of the billing cycle.

### Example Usage: Created

<!-- UsageSnippet language="python" operationID="server-schedule-deletion" method="post" path="/servers/{server_id}/schedule_deletion" example="Created" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.schedule_deletion(server_id="sv_g1mbDwBZqLv5B")

    # Handle response
    print(res)

```
### Example Usage: when request deletion time is invalid

<!-- UsageSnippet language="python" operationID="server-schedule-deletion" method="post" path="/servers/{server_id}/schedule_deletion" example="when request deletion time is invalid" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.schedule_deletion(server_id="sv_Qkm7dXaRq8nZV")

    # Handle response
    print(res)

```
### Example Usage: when server is locked

<!-- UsageSnippet language="python" operationID="server-schedule-deletion" method="post" path="/servers/{server_id}/schedule_deletion" example="when server is locked" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.schedule_deletion(server_id="sv_5xyZOnLMqWM0l")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `server_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ServerScheduleDeletion](../../models/serverscheduledeletion.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## unschedule_deletion

Unschedules the server removal at the end of the billing cycle.

### Example Usage

<!-- UsageSnippet language="python" operationID="server-unschedule-deletion" method="delete" path="/servers/{server_id}/schedule_deletion" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.servers.unschedule_deletion(server_id="sv_Z8rodmJGq1jLB")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `server_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## reinstall

Run Server Reinstall

### Example Usage: Created

<!-- UsageSnippet language="python" operationID="create-server-reinstall" method="post" path="/servers/{server_id}/reinstall" example="Created" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.servers.reinstall(server_id="sv_aNmodj6ydbE8W", data={
        "type": latitudesh_python_sdk.CreateServerReinstallServersType.REINSTALLS,
        "attributes": {
            "operating_system": latitudesh_python_sdk.CreateServerReinstallServersOperatingSystem.IPXE,
            "hostname": "BRC1",
            "ipxe": "https://some-host.com/image.ipxe",
        },
    })

    # Use the SDK ...

```
### Example Usage: Forbidden

<!-- UsageSnippet language="python" operationID="create-server-reinstall" method="post" path="/servers/{server_id}/reinstall" example="Forbidden" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.servers.reinstall(server_id="sv_LGXPdWK8dnNWk", data={
        "type": latitudesh_python_sdk.CreateServerReinstallServersType.REINSTALLS,
        "attributes": {
            "operating_system": latitudesh_python_sdk.CreateServerReinstallServersOperatingSystem.UBUNTU_22_04_X64_LTS,
            "hostname": "BRC1",
        },
    })

    # Use the SDK ...

```
### Example Usage: Locked server

<!-- UsageSnippet language="python" operationID="create-server-reinstall" method="post" path="/servers/{server_id}/reinstall" example="Locked server" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.servers.reinstall(server_id="sv_Gr47qlKvdAg0m", data={
        "type": latitudesh_python_sdk.CreateServerReinstallServersType.REINSTALLS,
        "attributes": {
            "operating_system": latitudesh_python_sdk.CreateServerReinstallServersOperatingSystem.UBUNTU_22_04_X64_LTS,
            "hostname": "BRC1",
            "ssh_keys": [
                "37",
            ],
            "user_data": "19",
            "raid": latitudesh_python_sdk.CreateServerReinstallServersRaid.RAID_1,
        },
    })

    # Use the SDK ...

```
### Example Usage: Not Found

<!-- UsageSnippet language="python" operationID="create-server-reinstall" method="post" path="/servers/{server_id}/reinstall" example="Not Found" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.servers.reinstall(server_id="sv_0L6WO1m1OPlXy", data={
        "type": latitudesh_python_sdk.CreateServerReinstallServersType.REINSTALLS,
        "attributes": {
            "operating_system": latitudesh_python_sdk.CreateServerReinstallServersOperatingSystem.UBUNTU_22_04_X64_LTS,
            "hostname": "BRC1",
            "ssh_keys": [
                "36",
            ],
            "user_data": "12",
            "raid": latitudesh_python_sdk.CreateServerReinstallServersRaid.RAID_1,
        },
    })

    # Use the SDK ...

```
### Example Usage: Unprocessable Entity

<!-- UsageSnippet language="python" operationID="create-server-reinstall" method="post" path="/servers/{server_id}/reinstall" example="Unprocessable Entity" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.servers.reinstall(server_id="sv_RMLydp9XqQKr1", data={
        "type": latitudesh_python_sdk.CreateServerReinstallServersType.REINSTALLS,
        "attributes": {
            "operating_system": latitudesh_python_sdk.CreateServerReinstallServersOperatingSystem.WINDOWS_SERVER_2019_STD_V1,
            "hostname": "BRC1",
            "raid": latitudesh_python_sdk.CreateServerReinstallServersRaid.RAID_0,
        },
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `server_id`                                                                                 | *str*                                                                                       | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `data`                                                                                      | [models.CreateServerReinstallServersData](../../models/createserverreinstallserversdata.md) | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |