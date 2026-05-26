# ObjectStorage

## Overview

### Available Operations

* [get_storage_buckets](#get_storage_buckets) - List object storages
* [post_storage_buckets](#post_storage_buckets) - Create object storage
* [get_storage_bucket](#get_storage_bucket) - Retrieve object storage
* [delete_storage_buckets](#delete_storage_buckets) - Delete object storage

## get_storage_buckets

Lists all object storages from a team.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-storage-buckets" method="get" path="/storage/buckets" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.object_storage.get_storage_buckets()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `filter_project`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The project ID or Slug to filter by                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ObjectStorages](../../models/objectstorages.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## post_storage_buckets

Creates a new object storage bucket for a project.

### Example Usage: Create

<!-- UsageSnippet language="python" operationID="post-storage-buckets" method="post" path="/storage/buckets" example="Create" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.object_storage.post_storage_buckets(data={
        "type": latitudesh_python_sdk.PostStorageBucketsType.OBJECTS,
        "attributes": {
            "project": "proj_6059EqYkOQj8p",
            "name": "my-bucket",
            "region": "DAL",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: CreateScoped

<!-- UsageSnippet language="python" operationID="post-storage-buckets" method="post" path="/storage/buckets" example="CreateScoped" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.object_storage.post_storage_buckets(data={
        "type": latitudesh_python_sdk.PostStorageBucketsType.OBJECTS,
        "attributes": {
            "project": "proj_6059EqYkOQj8p",
            "name": "customer-bucket",
            "region": "DAL",
            "scoped": True,
            "customer": "acme-corp",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Created

<!-- UsageSnippet language="python" operationID="post-storage-buckets" method="post" path="/storage/buckets" example="Created" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.object_storage.post_storage_buckets(data={
        "type": latitudesh_python_sdk.PostStorageBucketsType.OBJECTS,
        "attributes": {
            "project": "<value>",
            "name": "<value>",
            "region": "<value>",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: FeatureNotEnabled

<!-- UsageSnippet language="python" operationID="post-storage-buckets" method="post" path="/storage/buckets" example="FeatureNotEnabled" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.object_storage.post_storage_buckets(data={
        "type": latitudesh_python_sdk.PostStorageBucketsType.OBJECTS,
        "attributes": {
            "project": "<value>",
            "name": "<value>",
            "region": "<value>",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: InsufficientPermissions

<!-- UsageSnippet language="python" operationID="post-storage-buckets" method="post" path="/storage/buckets" example="InsufficientPermissions" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.object_storage.post_storage_buckets(data={
        "type": latitudesh_python_sdk.PostStorageBucketsType.OBJECTS,
        "attributes": {
            "project": "<value>",
            "name": "<value>",
            "region": "<value>",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `data`                                                                  | [models.PostStorageBucketsData](../../models/poststoragebucketsdata.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.PostStorageBucketsResponseBody](../../models/poststoragebucketsresponsebody.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 404, 409, 422       | application/vnd.api+json |
| models.ErrorObject       | 500                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## get_storage_bucket

Shows details of a specific object storage.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-storage-bucket" method="get" path="/storage/buckets/{id}" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.object_storage.get_storage_bucket(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The object storage ID                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetStorageBucketResponseBody](../../models/getstoragebucketresponsebody.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 404                 | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## delete_storage_buckets

Allows you to remove an object storage from a project.

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-storage-buckets" method="delete" path="/storage/buckets/{id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.object_storage.delete_storage_buckets(id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The object storage ID                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 404, 409            | application/vnd.api+json |
| models.ErrorObject       | 500                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |