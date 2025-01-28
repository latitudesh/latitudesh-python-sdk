# TrafficSDK
(*traffic*)

## Overview

### Available Operations

* [get_traffic_consumption](#get_traffic_consumption) - Retrieve Traffic consumption
* [get_traffic_quota](#get_traffic_quota) - Retrieve Traffic Quota

## get_traffic_consumption

Retrieve Traffic consumption

### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.traffic.get_traffic_consumption(filter_date_gte="2024-12-24T18:28:59Z", filter_date_lte="2025-01-24T18:28:59Z", filter_server=185, filter_project=299)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `filter_date_gte`                                                                                                                | *str*                                                                                                                            | :heavy_check_mark:                                                                                                               | The start timestamp to retrieve the traffic. You must provide in ISO8601 format. Example: filter[date][gte]=2024-04-01T00:00:00Z |
| `filter_date_lte`                                                                                                                | *str*                                                                                                                            | :heavy_check_mark:                                                                                                               | The end timestamp to retrieve the traffic. You must provide in ISO8601 format. Example: filter[date][gte]=2024-04-31T23:59:59Z   |
| `filter_server`                                                                                                                  | *Optional[int]*                                                                                                                  | :heavy_minus_sign:                                                                                                               | N/A                                                                                                                              |
| `filter_project`                                                                                                                 | *Optional[int]*                                                                                                                  | :heavy_minus_sign:                                                                                                               | N/A                                                                                                                              |
| `retries`                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                 | :heavy_minus_sign:                                                                                                               | Configuration to override the default retry behavior of the client.                                                              |

### Response

**[models.Traffic](../../models/traffic.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_traffic_quota

Retrieve Traffic Quota

### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.traffic.get_traffic_quota()

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

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ErrorObject | 503                | application/json   |
| models.APIError    | 4XX, 5XX           | \*/\*              |