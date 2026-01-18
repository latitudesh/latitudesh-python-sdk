# Traffic

## Overview

### Available Operations

* [get](#get) - Retrieve Traffic consumption
* [get_quota](#get_quota) - Retrieve Traffic Quota

## get

Retrieve Traffic consumption

### Example Usage

<!-- UsageSnippet language="python" operationID="get-traffic-consumption" method="get" path="/traffic" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.traffic.get(filter_date_gte="2025-12-14T15:57:10Z", filter_date_lte="2026-01-14T15:57:10Z", filter_server="sv_A05EdQ50dvKYQ", filter_project="proj_AW6Q2D9lqKLpr")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `filter_date_gte`                                                                                                                | *str*                                                                                                                            | :heavy_check_mark:                                                                                                               | The start timestamp to retrieve the traffic. You must provide in ISO8601 format. Example: filter[date][gte]=2024-04-01T00:00:00Z |
| `filter_date_lte`                                                                                                                | *str*                                                                                                                            | :heavy_check_mark:                                                                                                               | The end timestamp to retrieve the traffic. You must provide in ISO8601 format. Example: filter[date][gte]=2024-04-31T23:59:59Z   |
| `filter_server`                                                                                                                  | *Optional[str]*                                                                                                                  | :heavy_minus_sign:                                                                                                               | The server id to filter by                                                                                                       |
| `filter_project`                                                                                                                 | *Optional[str]*                                                                                                                  | :heavy_minus_sign:                                                                                                               | The project id to filter by                                                                                                      |
| `retries`                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                 | :heavy_minus_sign:                                                                                                               | Configuration to override the default retry behavior of the client.                                                              |

### Response

**[models.Traffic](../../models/traffic.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_quota

Retrieve Traffic Quota

### Example Usage

<!-- UsageSnippet language="python" operationID="get-traffic-quota" method="get" path="/traffic/quota" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.traffic.get_quota()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `filter_project`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TrafficQuota](../../models/trafficquota.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |