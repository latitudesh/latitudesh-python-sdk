# ServersSDK
(*servers*)

## Overview

### Available Operations

* [get_servers](#get_servers) - List all Servers
* [create_server](#create_server) - Deploy Server
* [get_server](#get_server) - Retrieve a Server
* [update_server](#update_server) - Update Server
* [destroy_server](#destroy_server) - Remove Server
* [get_server_deploy_config](#get_server_deploy_config) - Retrieve Deploy Config
* [update_server_deploy_config](#update_server_deploy_config) - Update Deploy Config
* [server_lock](#server_lock) - Lock the server
* [server_unlock](#server_unlock) - Unlock the server
* [create_server_out_of_band](#create_server_out_of_band) - Start Out of Band Connection
* [get_server_out_of_band](#get_server_out_of_band) - List Out of Band Connections
* [create_server_action](#create_server_action) - Run Server Action
* [create_ipmi_session](#create_ipmi_session) - Generate IPMI credentials
* [server_start_rescue_mode](#server_start_rescue_mode) - Puts a Server in rescue mode
* [server_exit_rescue_mode](#server_exit_rescue_mode) - Exits rescue mode for a Server
* [server_schedule_deletion](#server_schedule_deletion) - Schedule the server deletion
* [server_unschedule_deletion](#server_unschedule_deletion) - Unschedule the server deletion
* [create_server_reinstall](#create_server_reinstall) - Run Server Reinstall

## get_servers

Returns a list of all servers belonging to the team.


### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.get_servers(filter_project="proj_695BdKNeOevVo", filter_region="region-slug", filter_ram_eql=32, filter_ram_gte=40, filter_ram_lte=40, filter_tags="tag_YLNQJ4a0gXfo883Z79X2Crp19AA")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                | Type                                                                                                                                                                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `filter_project`                                                                                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                       | The project ID or Slug to filter by                                                                                                                                                                                                                                                                                                                                      |
| `filter_region`                                                                                                                                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                       | The region Slug to filter by                                                                                                                                                                                                                                                                                                                                             |
| `filter_hostname`                                                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                       | The hostname of server to filter by                                                                                                                                                                                                                                                                                                                                      |
| `filter_created_at_gte`                                                                                                                                                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                       | The created at greater than equal date to filter by                                                                                                                                                                                                                                                                                                                      |
| `filter_created_at_lte`                                                                                                                                                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                       | The created at less than equal date to filter by                                                                                                                                                                                                                                                                                                                         |
| `filter_label`                                                                                                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                       | The label of server to filter by                                                                                                                                                                                                                                                                                                                                         |
| `filter_status`                                                                                                                                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                       | The status of server to filter by                                                                                                                                                                                                                                                                                                                                        |
| `filter_plan`                                                                                                                                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                       | The platform/plan name of the server to filter by                                                                                                                                                                                                                                                                                                                        |
| `filter_gpu`                                                                                                                                                                                                                                                                                                                                                             | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                       | Filter by the existence of an associated GPU                                                                                                                                                                                                                                                                                                                             |
| `filter_ram_eql`                                                                                                                                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                       | Filter servers with RAM size (in GB) equals the provided value.                                                                                                                                                                                                                                                                                                          |
| `filter_ram_gte`                                                                                                                                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                       | Filter servers with RAM size (in GB) greater than or equal the provided value.                                                                                                                                                                                                                                                                                           |
| `filter_ram_lte`                                                                                                                                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                       | Filter servers with RAM size (in GB) less than or equal the provided value.                                                                                                                                                                                                                                                                                              |
| `filter_disk`                                                                                                                                                                                                                                                                                                                                                            | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                       | The disk size in Gigabytes to filter by, should be used with the following options:<br/>                              [eql] to filter for values equal to the provided value.<br/>                              [gte] to filter for values greater or equal to the provided value.<br/>                              [lte] to filter by values lower or equal to the provided value. |
| `filter_tags`                                                                                                                                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                       | The tags ids to filter by, separated by comma, e.g. `filter[tags]=tag_1,tag_2`will return servers with `tag_1` AND `tag_2`                                                                                                                                                                                                                                               |
| `extra_fields_servers`                                                                                                                                                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                       | The `credentials` are provided as extra attributes that is lazy loaded. To request it, just set `extra_fields[servers]=credentials` in the query string.                                                                                                                                                                                                                 |
| `retries`                                                                                                                                                                                                                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                      |

### Response

**[models.Servers](../../models/servers.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_server

Deploy Server

### Example Usage

```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.create_server(request={
        "data": {
            "type": latitudesh_python_sdk.CreateServerType.SERVERS,
            "attributes": {
                "project": "proj_WeGoqAWNOP7nz",
                "plan": latitudesh_python_sdk.CreateServerPlan.C2_SMALL_X86,
                "site": latitudesh_python_sdk.CreateServerSite.SAO,
                "operating_system": latitudesh_python_sdk.CreateServerOperatingSystem.UBUNTU_22_04_X64_LTS,
                "hostname": "BRC1",
            },
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.CreateServerRequestBody](../../models/createserverrequestbody.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.Server](../../models/server.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ErrorObject | 400, 402, 422      | application/json   |
| models.APIError    | 4XX, 5XX           | \*/\*              |

## get_server

Returns a server that belongs to the team.


### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.get_server(server_id="sv_RMLydp70OQKr1")

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

## update_server

Update Server

### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.servers.update_server(server_id="sv_Gr47qleMDAg0m", id="sv_81EVOtR1N4J2Z")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `server_id`                                                                       | *str*                                                                             | :heavy_check_mark:                                                                | N/A                                                                               |
| `id`                                                                              | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | N/A                                                                               |
| `type`                                                                            | [Optional[models.UpdateServerType]](../../models/updateservertype.md)             | :heavy_minus_sign:                                                                | N/A                                                                               |
| `attributes`                                                                      | [Optional[models.UpdateServerAttributes]](../../models/updateserverattributes.md) | :heavy_minus_sign:                                                                | N/A                                                                               |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ServerError | 400                | application/json   |
| models.ErrorObject | 422, 423           | application/json   |
| models.APIError    | 4XX, 5XX           | \*/\*              |

## destroy_server

Remove Server

### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.servers.destroy_server(server_id="sv_1R3zq2rxqWxyn")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `server_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The server ID                                                       |
| `reason`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The reason for deleting the server                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ErrorObject | 403, 406, 422      | application/json   |
| models.APIError    | 4XX, 5XX           | \*/\*              |

## get_server_deploy_config

Retrieve Deploy Config

### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.get_server_deploy_config(server_id="sv_VLMmAD8EOwop2")

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

## update_server_deploy_config

Update Deploy Config

### Example Usage

```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.update_server_deploy_config(server_id="sv_KN4ydzwvqVob3", type_=latitudesh_python_sdk.UpdateServerDeployConfigType.DEPLOY_CONFIG)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `server_id`                                                                                               | *str*                                                                                                     | :heavy_check_mark:                                                                                        | The Server ID                                                                                             |
| `type`                                                                                                    | [models.UpdateServerDeployConfigType](../../models/updateserverdeployconfigtype.md)                       | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `attributes`                                                                                              | [Optional[models.UpdateServerDeployConfigAttributes]](../../models/updateserverdeployconfigattributes.md) | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[models.DeployConfig](../../models/deployconfig.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 406                 | application/json         |
| models.DeployConfigError | 422                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## server_lock

Locks the server. A locked server cannot be deleted or modified and no actions can be performed on it.

### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.server_lock(server_id="sv_3YjJOL5NdvZ87")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `server_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Server1](../../models/server1.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## server_unlock

Unlocks the server. A locked server cannot be deleted or modified and no actions can be performed on it.

### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.server_unlock(server_id="sv_W6Q2D9xGqKLpr")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `server_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Server1](../../models/server1.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_server_out_of_band

Start Out of Band Connection

### Example Usage

```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.create_server_out_of_band(server_id="sv_g1mbDweZdLv5B", data={
        "type": latitudesh_python_sdk.CreateServerOutOfBandType.OUT_OF_BAND,
        "attributes": {
            "ssh_key_id": "ssh_NGnzRD5ADM5yw",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `server_id`                                                                   | *str*                                                                         | :heavy_check_mark:                                                            | N/A                                                                           |
| `data`                                                                        | [models.CreateServerOutOfBandData](../../models/createserveroutofbanddata.md) | :heavy_check_mark:                                                            | N/A                                                                           |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.OutOfBandConnection](../../models/outofbandconnection.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ErrorObject | 403, 404           | application/json   |
| models.APIError    | 4XX, 5XX           | \*/\*              |

## get_server_out_of_band

List Out of Band Connections

### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.get_server_out_of_band(server_id="sv_kjQwdEmXdYNVP")

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

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ErrorObject | 404                | application/json   |
| models.APIError    | 4XX, 5XX           | \*/\*              |

## create_server_action

Performs an action on a given server:
- `power_on`
- `power_off`
- `reboot`


### Example Usage

```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.create_server_action(server_id="sv_A05EdQM4dvKYQ", data={
        "type": latitudesh_python_sdk.CreateServerActionType.ACTIONS,
        "attributes": {
            "action": latitudesh_python_sdk.Action.REBOOT,
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `server_id`                                                             | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `data`                                                                  | [models.CreateServerActionData](../../models/createserveractiondata.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.ServerAction](../../models/serveraction.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ErrorObject | 403                | application/json   |
| models.APIError    | 4XX, 5XX           | \*/\*              |

## create_ipmi_session

Generates IPMI credentials for a given server. Remote access creates a VPN connection to the internal network of your server so you can connect to its IPMI.
You will have to use a VPN client such as https://openvpn.net to connect. See `VPN Sessions` API to create a VPN connection.

Related guide: https://docs.latitude.sh/docs/ipmi


### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.create_ipmi_session(server_id="sv_vYAZqGyJOMQ94")

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

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ErrorObject | 403, 404, 422      | application/json   |
| models.APIError    | 4XX, 5XX           | \*/\*              |

## server_start_rescue_mode

Starts rescue mode on a given server.

### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.server_start_rescue_mode(server_id="sv_LA73qkJwdaJ2o")

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

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ErrorObject | 403, 406           | application/json   |
| models.APIError    | 4XX, 5XX           | \*/\*              |

## server_exit_rescue_mode

Exits rescue mode on a given server.

### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.server_exit_rescue_mode(server_id="sv_e8pKq0xYqWAob")

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

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ErrorObject | 403, 406           | application/json   |
| models.APIError    | 4XX, 5XX           | \*/\*              |

## server_schedule_deletion

Schedules the server to be removed at the end of the billing cycle.

### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.server_schedule_deletion(server_id="sv_lxWpD6WvOm6rk")

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

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ErrorObject | 403, 406, 423      | application/json   |
| models.APIError    | 4XX, 5XX           | \*/\*              |

## server_unschedule_deletion

Unschedules the server removal at the end of the billing cycle.

### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.servers.server_unschedule_deletion(server_id="sv_GnzRD5lvqM5yw")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `server_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ErrorObject | 403                | application/json   |
| models.APIError    | 4XX, 5XX           | \*/\*              |

## create_server_reinstall

Run Server Reinstall

### Example Usage

```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.servers.create_server_reinstall(server_id="sv_KXgRdRRodv9k5", data={
        "type": latitudesh_python_sdk.CreateServerReinstallType.REINSTALLS,
        "attributes": {
            "operating_system": latitudesh_python_sdk.CreateServerReinstallOperatingSystem.UBUNTU_22_04_X64_LTS,
            "hostname": "BRC1",
            "ssh_keys": [
                "35",
            ],
            "user_data": 10,
            "raid": latitudesh_python_sdk.CreateServerReinstallRaid.RAID_1,
        },
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `server_id`                                                                   | *str*                                                                         | :heavy_check_mark:                                                            | N/A                                                                           |
| `data`                                                                        | [models.CreateServerReinstallData](../../models/createserverreinstalldata.md) | :heavy_check_mark:                                                            | N/A                                                                           |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ErrorObject | 403, 404, 422      | application/json   |
| models.ServerError | 423                | application/json   |
| models.APIError    | 4XX, 5XX           | \*/\*              |