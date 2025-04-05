# ServersSDK
(*servers*)

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

```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.list(filter_project="proj_W6Q2D9lGqKLpr", filter_region="SAO", filter_ram_eql=32, filter_ram_gte=40, filter_ram_lte=40, filter_tags="tag_EVZVklJKJpUXr3eZ46ylUoEJXZP")

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

## create

Deploy Server

### Example Usage

```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.create(request={
        "data": {
            "type": latitudesh_python_sdk.CreateServerServersType.SERVERS,
            "attributes": {
                "project": "proj_LGXPdWK8dnNWk",
                "plan": latitudesh_python_sdk.CreateServerServersPlan.C2_SMALL_X86,
                "site": latitudesh_python_sdk.CreateServerServersSite.SAO,
                "operating_system": latitudesh_python_sdk.CreateServerServersOperatingSystem.UBUNTU_22_04_X64_LTS,
                "hostname": "BRC1",
            },
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `request`                                                                               | [models.CreateServerServersRequestBody](../../models/createserverserversrequestbody.md) | :heavy_check_mark:                                                                      | The request object to use for the request.                                              |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.Server](../../models/server.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 400, 402, 422            | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## get

Returns a server that belongs to the team.


### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.get(server_id="sv_RMLydp70OQKr1")

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

```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.servers.update(server_id="sv_Gr47qleMDAg0m")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `server_id`                                                                                     | *str*                                                                                           | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `id`                                                                                            | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `type`                                                                                          | [Optional[models.UpdateServerServersType]](../../models/updateserverserverstype.md)             | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `attributes`                                                                                    | [Optional[models.UpdateServerServersAttributes]](../../models/updateserverserversattributes.md) | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ServerError       | 400, 422                 | application/vnd.api+json |
| models.ErrorObject       | 402, 423                 | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## delete

Remove Server

### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.servers.delete(server_id="sv_GMy1Db3NON50m")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `server_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The server ID                                                       |
| `reason`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The reason for deleting the server                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 406, 422            | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## get_deploy_config

Retrieve Deploy Config

### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.get_deploy_config(server_id="sv_xkjQwdENqYNVP")

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

```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.update_deploy_config(server_id="sv_Z8rodmnGq1jLB", type_=latitudesh_python_sdk.UpdateServerDeployConfigServersType.DEPLOY_CONFIG)

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

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 406                 | application/vnd.api+json |
| models.DeployConfigError | 422                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## lock

Locks the server. A locked server cannot be deleted or modified and no actions can be performed on it.

### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.lock(server_id="sv_w49QDBmQqagKb")

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

## unlock

Unlocks the server. A locked server cannot be deleted or modified and no actions can be performed on it.

### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.unlock(server_id="sv_LMmAD8E4Owop2")

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

## create_out_of_band_connection

Start Out of Band Connection

### Example Usage

```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.create_out_of_band_connection(server_id="sv_RMLydpoXOQKr1", data={
        "type": latitudesh_python_sdk.CreateServerOutOfBandServersType.OUT_OF_BAND,
        "attributes": {
            "ssh_key_id": "ssh_NGnzRD5ADM5yw",
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

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 404                 | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## list_out_of_band_connections

List Out of Band Connections

### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.list_out_of_band_connections(server_id="sv_059EqYX2dQj8p")

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

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 404                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## actions

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

    res = latitudesh.servers.actions(server_id="sv_z2A3DVpQdnawP", data={
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

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

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

    res = latitudesh.servers.create_ipmi_session(server_id="sv_0MK4O44ROa95w")

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

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 404, 422            | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## start_rescue_mode

Starts rescue mode on a given server.

### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.start_rescue_mode(server_id="sv_pbV0DgjKq4AWz")

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

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 406                 | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## exit_rescue_mode

Exits rescue mode on a given server.

### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.exit_rescue_mode(server_id="sv_QraYDP15OpjwW")

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

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 406                 | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## schedule_deletion

Schedules the server to be removed at the end of the billing cycle.

### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.servers.schedule_deletion(server_id="sv_yQrJdNMGO30gv")

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

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 406, 423            | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## unschedule_deletion

Unschedules the server removal at the end of the billing cycle.

### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.servers.unschedule_deletion(server_id="sv_1R3zq2JxqWxyn")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `server_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## reinstall

Run Server Reinstall

### Example Usage

```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.servers.reinstall(server_id="sv_GMy1Db2NDN50m", data={
        "type": latitudesh_python_sdk.CreateServerReinstallServersType.REINSTALLS,
        "attributes": {
            "operating_system": latitudesh_python_sdk.CreateServerReinstallServersOperatingSystem.UBUNTU_22_04_X64_LTS,
            "hostname": "BRC1",
            "partitions": [
                {
                    "size_in_gb": 300,
                    "path": "/",
                    "filesystem_type": "ext4",
                },
            ],
            "ssh_keys": [
                "35",
            ],
            "user_data": 10,
            "raid": latitudesh_python_sdk.CreateServerReinstallServersRaid.RAID_1,
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

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 404, 422            | application/vnd.api+json |
| models.ServerError       | 423                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |