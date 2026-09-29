# ManagedDatabases

## Overview

Managed database instances (PostgreSQL, ClickHouse)

### Available Operations

* [show_managed_database_metrics](#show_managed_database_metrics) - Show managed database metrics
* [list_managed_databases](#list_managed_databases) - List managed databases
* [create_managed_database](#create_managed_database) - Create a managed database
* [show_managed_database](#show_managed_database) - Show a managed database
* [destroy_managed_database](#destroy_managed_database) - Destroy a managed database
* [update_managed_database](#update_managed_database) - Update a managed database
* [list_managed_database_backups](#list_managed_database_backups) - List managed database backups

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

## list_managed_databases

List managed databases

### Example Usage

<!-- UsageSnippet language="python" operationID="list-managed-databases" method="get" path="/managed_databases" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.managed_databases.list_managed_databases(project_id="<id>", engine="postgres")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The project slug to filter databases by                             |                                                                     |
| `engine`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Filter by database engine                                           | postgres                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ManagedDatabases](../../models/manageddatabases.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_managed_database

Create a managed database

### Example Usage

<!-- UsageSnippet language="python" operationID="create-managed-database" method="post" path="/managed_databases" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.managed_databases.create_managed_database(data={
        "type": latitudesh_python_sdk.ManagedDatabasePayloadType.MANAGED_DATABASES,
        "attributes": {
            "name": "my-postgres-db",
            "project_id": "proj_ABC123",
            "region": "ASH",
            "plan": "db.psql.small",
            "engine": "postgres",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `data`                                                                                    | [Optional[models.ManagedDatabasePayloadData]](../../models/manageddatabasepayloaddata.md) | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.ManagedDatabase](../../models/manageddatabase.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## show_managed_database

Show a managed database

### Example Usage

<!-- UsageSnippet language="python" operationID="show-managed-database" method="get" path="/managed_databases/{id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.managed_databases.show_managed_database(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Managed database ID                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ManagedDatabase](../../models/manageddatabase.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## destroy_managed_database

Destroy a managed database

### Example Usage

<!-- UsageSnippet language="python" operationID="destroy-managed-database" method="delete" path="/managed_databases/{id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.managed_databases.destroy_managed_database(id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Managed database ID                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_managed_database

Update a managed database

### Example Usage

<!-- UsageSnippet language="python" operationID="update-managed-database" method="patch" path="/managed_databases/{id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.managed_databases.update_managed_database(id="<id>", data={
        "attributes": {
            "trusted_sources": [
                "203.0.113.0/24",
                "198.51.100.0/24",
            ],
            "parameters": {
                "shared_buffers": "256MB",
                "work_mem": "16MB",
                "effective_cache_size": "1GB",
            },
            "pooler": {
                "enabled": True,
                "default_pool_size": 30,
                "max_client_conn": 200,
            },
            "backup": {
                "enabled": True,
                "schedule": "0 0 0 * * *",
                "s3Endpoint": "https://s3.amazonaws.com",
                "bucketName": "my-db-backups",
                "path": "prod/postgres",
                "retentionPolicy": "7",
            },
            "access_credentials": {
                "access_key_id": "AKIAIOSFODNN7EXAMPLE",
                "secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            },
            "supabase": True,
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `id`                                                                                                  | *str*                                                                                                 | :heavy_check_mark:                                                                                    | Managed database ID                                                                                   |
| `data`                                                                                                | [Optional[models.ManagedDatabaseUpdatePayloadData]](../../models/manageddatabaseupdatepayloaddata.md) | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.ManagedDatabase](../../models/manageddatabase.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_managed_database_backups

List managed database backups

### Example Usage

<!-- UsageSnippet language="python" operationID="list-managed-database-backups" method="get" path="/managed_databases/{managed_database_id}/backups" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.managed_databases.list_managed_database_backups(managed_database_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `managed_database_id`                                                     | *str*                                                                     | :heavy_check_mark:                                                        | Managed database ID                                                       |
| `phase`                                                                   | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | Filter backups by phase. Use 'completed' to return only finished backups. |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.ListManagedDatabaseBackupsResponseBody](../../models/listmanageddatabasebackupsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |