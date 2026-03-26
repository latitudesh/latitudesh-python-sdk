# ElasticIps

## Overview

### Available Operations

* [list_elastic_ips](#list_elastic_ips) - List Elastic IPs
* [create_elastic_ip](#create_elastic_ip) - Create an Elastic IP
* [get_elastic_ip](#get_elastic_ip) - Retrieve an Elastic IP
* [delete_elastic_ip](#delete_elastic_ip) - Release an Elastic IP
* [update_elastic_ip](#update_elastic_ip) - Move an Elastic IP

## list_elastic_ips

List all Elastic IPs for the authenticated team. Elastic IPs are static public IP addresses that can be assigned to servers and moved between servers within the same project.

**Note:** This feature requires the `elastic_ips` feature flag to be enabled for your team. When the flag is disabled, the endpoint returns an empty list.


### Example Usage

<!-- UsageSnippet language="python" operationID="list-elastic-ips" method="get" path="/elastic_ips" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.elastic_ips.list_elastic_ips(page_size=20, page_number=1)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `filter_project`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The project ID or slug to filter by                                 |
| `filter_server`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The server ID to filter by                                          |
| `filter_status`                                                     | [Optional[models.FilterStatus]](../../models/filterstatus.md)       | :heavy_minus_sign:                                                  | The status to filter by                                             |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Number of items to return per page                                  |
| `page_number`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Page number to return (starts at 1)                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListElasticIpsResponse](../../models/listelasticipsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_elastic_ip

Creates a new Elastic IP and assigns it to the specified server. The IP is provisioned asynchronously—the response will show status `configuring` and the `id` will be `null` until provisioning completes.

**Note:** This feature requires the `elastic_ips` feature flag to be enabled for your team. Currently only IPv4 /32 addresses in routed mode are supported.


### Example Usage: Accepted

<!-- UsageSnippet language="python" operationID="create-elastic-ip" method="post" path="/elastic_ips" example="Accepted" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.elastic_ips.create_elastic_ip(data={
        "type": latitudesh_python_sdk.CreateElasticIPType.ELASTIC_IPS,
        "attributes": {
            "project_id": "<id>",
            "server_id": "<id>",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Create

<!-- UsageSnippet language="python" operationID="create-elastic-ip" method="post" path="/elastic_ips" example="Create" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.elastic_ips.create_elastic_ip(data={
        "type": latitudesh_python_sdk.CreateElasticIPType.ELASTIC_IPS,
        "attributes": {
            "project_id": "proj_AoW6vRnwkvLn0",
            "server_id": "sv_2GmAlJ6BXlK1a",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: FeatureNotEnabled

<!-- UsageSnippet language="python" operationID="create-elastic-ip" method="post" path="/elastic_ips" example="FeatureNotEnabled" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.elastic_ips.create_elastic_ip(data={
        "type": latitudesh_python_sdk.CreateElasticIPType.ELASTIC_IPS,
        "attributes": {
            "project_id": "<id>",
            "server_id": "<id>",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `data`                                                              | [models.CreateElasticIPData](../../models/createelasticipdata.md)   | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ElasticIP](../../models/elasticip.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 422                 | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## get_elastic_ip

Returns a single Elastic IP by its ID.

**Note:** This feature requires the `elastic_ips` feature flag to be enabled for your team.


### Example Usage

<!-- UsageSnippet language="python" operationID="get-elastic-ip" method="get" path="/elastic_ips/{elastic_ip_id}" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.elastic_ips.get_elastic_ip(elastic_ip_id="eip_KeQbB4BoO6x10")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `elastic_ip_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The Elastic IP ID                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ElasticIP](../../models/elasticip.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 404                 | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## delete_elastic_ip

Releases an Elastic IP, returning it to the available pool. The IP will transition to `releasing` status before being fully removed.

**Note:** This feature requires the `elastic_ips` feature flag to be enabled for your team. Only Elastic IPs with status `active` or `error` can be released.


### Example Usage

<!-- UsageSnippet language="python" operationID="delete-elastic-ip" method="delete" path="/elastic_ips/{elastic_ip_id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.elastic_ips.delete_elastic_ip(elastic_ip_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `elastic_ip_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The Elastic IP ID                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 404, 422            | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## update_elastic_ip

Moves an Elastic IP to a different server within the same project. The reassignment is performed asynchronously.

**Note:** This feature requires the `elastic_ips` feature flag to be enabled for your team. The Elastic IP must be in `active` status and the target server must belong to the same project.


### Example Usage: FeatureNotEnabled

<!-- UsageSnippet language="python" operationID="update-elastic-ip" method="patch" path="/elastic_ips/{elastic_ip_id}" example="FeatureNotEnabled" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.elastic_ips.update_elastic_ip(elastic_ip_id="<id>", data={
        "type": latitudesh_python_sdk.UpdateElasticIPType.ELASTIC_IPS,
        "attributes": {
            "server_id": "<id>",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Move

<!-- UsageSnippet language="python" operationID="update-elastic-ip" method="patch" path="/elastic_ips/{elastic_ip_id}" example="Move" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.elastic_ips.update_elastic_ip(elastic_ip_id="<id>", data={
        "type": latitudesh_python_sdk.UpdateElasticIPType.ELASTIC_IPS,
        "attributes": {
            "server_id": "sv_oDEBlwBGRO2me",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Success

<!-- UsageSnippet language="python" operationID="update-elastic-ip" method="patch" path="/elastic_ips/{elastic_ip_id}" example="Success" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.elastic_ips.update_elastic_ip(elastic_ip_id="eip_KeQbB4BoO6x10", data={
        "type": latitudesh_python_sdk.UpdateElasticIPType.ELASTIC_IPS,
        "attributes": {
            "server_id": "<id>",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `elastic_ip_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The Elastic IP ID                                                   |
| `data`                                                              | [models.UpdateElasticIPData](../../models/updateelasticipdata.md)   | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ElasticIP](../../models/elasticip.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 404, 422            | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |