# ManagedDatabases

## Overview

### Available Operations

* [show_managed_database_metrics](#show_managed_database_metrics) - Show managed database metrics

## show_managed_database_metrics

Show managed database metrics

### Example Usage

<!-- UsageSnippet language="python" operationID="show-managed-database-metrics" method="get" path="/managed_databases/{managed_database_id}/metrics" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.managed_databases.show_managed_database_metrics(managed_database_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `managed_database_id`                                                                                                                        | *str*                                                                                                                                        | :heavy_check_mark:                                                                                                                           | Managed database ID                                                                                                                          |
| `period`                                                                                                                                     | *Optional[int]*                                                                                                                              | :heavy_minus_sign:                                                                                                                           | Time window in seconds. One of 1800, 3600, 21600, 86400, 604800 (default 1800).                                                              |
| `queries`                                                                                                                                    | *Optional[str]*                                                                                                                              | :heavy_minus_sign:                                                                                                                           | Comma-separated metrics to fetch. Defaults to all: cpuUsage, memoryUsage, tpsUsage, maxConnections, deadlocks, blockedQueries, databaseSize. |
| `retries`                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                             | :heavy_minus_sign:                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                          |

### Response

**[models.ShowManagedDatabaseMetricsResponseBody](../../models/showmanageddatabasemetricsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |