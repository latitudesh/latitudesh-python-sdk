# Traffic

## Overview

### Available Operations

* [get](#get) - Retrieve traffic
* [get_quota](#get_quota) - Retrieve traffic quota

## get

Retrieve traffic

### Example Usage: Success

<!-- UsageSnippet language="python" operationID="get-traffic-consumption" method="get" path="/traffic" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.traffic.get(filter_date_gte="2025-12-14T15:57:10Z", filter_date_lte="2026-01-14T15:57:10Z", filter_server="sv_A05EdQ50dvKYQ")

    # Handle response
    print(res)

```
### Example Usage: when the period filter is the deprecated format

<!-- UsageSnippet language="python" operationID="get-traffic-consumption" method="get" path="/traffic" example="when the period filter is the deprecated format" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.traffic.get(filter_date_gte="2025-04-28T10:40:31Z", filter_date_lte="2025-04-28T18:40:31Z", filter_project="308")

    # Handle response
    print(res)

```
### Example Usage: when the period is less than 1 day

<!-- UsageSnippet language="python" operationID="get-traffic-consumption" method="get" path="/traffic" example="when the period is less than 1 day" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.traffic.get(filter_date_gte="2025-04-28T10:40:31Z", filter_date_lte="2025-04-28T18:40:31Z", filter_server="198")

    # Handle response
    print(res)

```
### Example Usage: with invalid filter

<!-- UsageSnippet language="python" operationID="get-traffic-consumption" method="get" path="/traffic" example="with invalid filter" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.traffic.get(filter_date_gte="invalid", filter_date_lte="invalid")

    # Handle response
    print(res)

```
### Example Usage: with project filter

<!-- UsageSnippet language="python" operationID="get-traffic-consumption" method="get" path="/traffic" example="with project filter" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.traffic.get(filter_date_gte="2025-04-06T21:00:00Z", filter_date_lte="2025-05-06T21:00:00Z", filter_project="proj_AW6Q2D9lqKLpr")

    # Handle response
    print(res)

```
### Example Usage: with server filter

<!-- UsageSnippet language="python" operationID="get-traffic-consumption" method="get" path="/traffic" example="with server filter" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.traffic.get(filter_date_gte="2025-04-06T21:00:00Z", filter_date_lte="2025-05-06T21:00:00Z", filter_server="sv_mw49QDB5qagKb")

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

Retrieve traffic quota

### Example Usage: Success

<!-- UsageSnippet language="python" operationID="get-traffic-quota" method="get" path="/traffic/quota" example="Success" -->
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
### Example Usage: when `billing_method` is `95th percentile`

<!-- UsageSnippet language="python" operationID="get-traffic-quota" method="get" path="/traffic/quota" example="when `billing_method` is `95th percentile`" -->
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
### Example Usage: when `billing_method` is `Normal`

<!-- UsageSnippet language="python" operationID="get-traffic-quota" method="get" path="/traffic/quota" example="when `billing_method` is `Normal`" -->
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