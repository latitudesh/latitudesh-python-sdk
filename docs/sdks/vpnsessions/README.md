# VpnSessions

## Overview

### Available Operations

* [list](#list) - List all Active VPN Sessions
* [create](#create) - Create a VPN Session
* [refresh_password](#refresh_password) - Refresh a VPN Session
* [delete](#delete) - Delete a VPN Session

## list

List all Active VPN Sessions

### Example Usage

<!-- UsageSnippet language="python" operationID="get-vpn-sessions" method="get" path="/vpn_sessions" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.vpn_sessions.list(filter_location=latitudesh_python_sdk.FilterLocation.SAO)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `filter_location`                                                   | [Optional[models.FilterLocation]](../../models/filterlocation.md)   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetVpnSessionsResponseBody](../../models/getvpnsessionsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create

Creates a new VPN Session.
`NOTE:` The VPN credentials are only listed ONCE upon creation. They can however be refreshed or deleted.


### Example Usage

<!-- UsageSnippet language="python" operationID="post-vpn-session" method="post" path="/vpn_sessions" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.vpn_sessions.create(data={
        "attributes": {
            "site": latitudesh_python_sdk.PostVpnSessionVpnSessionsSite.SAO,
            "server_id": "sv_wg3ZDrKyO5QlP",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `data`                                                                                          | [Optional[models.PostVpnSessionVpnSessionsData]](../../models/postvpnsessionvpnsessionsdata.md) | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.VpnSessionWithPassword](../../models/vpnsessionwithpassword.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## refresh_password

Refreshing an existing VPN Session will create new credentials for that session


### Example Usage

<!-- UsageSnippet language="python" operationID="put-vpn-session" method="patch" path="/vpn_sessions/{vpn_session_id}/refresh_password" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.vpn_sessions.refresh_password(vpn_session_id="vpn_6VE1Wd37dXnZJ")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `vpn_session_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.VpnSessionWithPassword](../../models/vpnsessionwithpassword.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete

Deletes an existing VPN Session.


### Example Usage

<!-- UsageSnippet language="python" operationID="delete-vpn-session" method="delete" path="/vpn_sessions/{vpn_session_id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.vpn_sessions.delete(vpn_session_id="invalid")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `vpn_session_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |