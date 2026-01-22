# Servers

## Overview

### Available Operations

* [list](#list) - List all Servers
* [create](#create) - Deploy Server
* [get](#get) - Retrieve a Server
* [update](#update) - Update Server
* [delete](#delete) - Remove Server
* [get_deploy_config](#get_deploy_config) - Retrieve Deploy Config
* [update_deploy_config](#update_deploy_config) - Update Deploy Config
* [lock](#lock) - Lock the server
* [unlock](#unlock) - Unlock the server
* [create_out_of_band_connection](#create_out_of_band_connection) - Start Out of Band Connection
* [list_out_of_band_connections](#list_out_of_band_connections) - List Out of Band Connections
* [actions](#actions) - Run Server Action
* [create_ipmi_session](#create_ipmi_session) - Generate IPMI credentials
* [start_rescue_mode](#start_rescue_mode) - Puts a Server in rescue mode
* [exit_rescue_mode](#exit_rescue_mode) - Exits rescue mode for a Server
* [schedule_deletion](#schedule_deletion) - Schedule the server deletion
* [unschedule_deletion](#unschedule_deletion) - Unschedule the server deletion
* [reinstall](#reinstall) - Run Server Reinstall

## list

Returns a list of all servers belonging to the team.


### Example Usage

<!-- UsageSnippet language="python" operationID="get-servers" method="get" path="/servers" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.list(filter_project="proj_g1mbDwrZqLv5B", filter_region="SAO", filter_ram_eql=32, filter_ram_gte=40, filter_ram_lte=40, filter_tags="tag_pjAkRjVzw0tlYBA2WX1eHzW7w79,tag_yARk1KLJAvslWY7k5wNBCaKEV7e", page_size=20, page_number=1)

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

Deploy Server

### Example Usage

<!-- UsageSnippet language="python" operationID="create-server" method="post" path="/servers" -->
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

<!-- UsageSnippet language="python" operationID="get-server" method="get" path="/servers/{server_id}" -->
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

Update Server

### Example Usage

<!-- UsageSnippet language="python" operationID="update-server" method="patch" path="/servers/{server_id}" -->
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

Remove Server

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

Retrieve Deploy Config

### Example Usage

<!-- UsageSnippet language="python" operationID="get-server-deploy-config" method="get" path="/servers/{server_id}/deploy_config" -->
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

Update Deploy Config

### Example Usage

<!-- UsageSnippet language="python" operationID="update-server-deploy-config" method="patch" path="/servers/{server_id}/deploy_config" -->
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

### Example Usage

<!-- UsageSnippet language="python" operationID="server-lock" method="post" path="/servers/{server_id}/lock" -->
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

### Example Usage

<!-- UsageSnippet language="python" operationID="server-unlock" method="post" path="/servers/{server_id}/unlock" -->
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

Start Out of Band Connection

### Example Usage

<!-- UsageSnippet language="python" operationID="create-server-out-of-band" method="post" path="/servers/{server_id}/out_of_band_connection" -->
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

List Out of Band Connections

### Example Usage

<!-- UsageSnippet language="python" operationID="get-server-out-of-band" method="get" path="/servers/{server_id}/out_of_band_connection" -->
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


### Example Usage

<!-- UsageSnippet language="python" operationID="create-server-action" method="post" path="/servers/{server_id}/actions" -->
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


### Example Usage

<!-- UsageSnippet language="python" operationID="create-ipmi-session" method="post" path="/servers/{server_id}/remote_access" -->
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

### Example Usage

<!-- UsageSnippet language="python" operationID="server-start-rescue-mode" method="post" path="/servers/{server_id}/rescue_mode" -->
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

### Example Usage

<!-- UsageSnippet language="python" operationID="server-exit-rescue-mode" method="post" path="/servers/{server_id}/exit_rescue_mode" -->
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

### Example Usage

<!-- UsageSnippet language="python" operationID="server-schedule-deletion" method="post" path="/servers/{server_id}/schedule_deletion" -->
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

### Example Usage

<!-- UsageSnippet language="python" operationID="create-server-reinstall" method="post" path="/servers/{server_id}/reinstall" -->
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