# ObjectStorage

## Overview

### Available Operations

* [get_storage_objects](#get_storage_objects) - List object storages
* [post_storage_objects](#post_storage_objects) - Create object storage
* [get_storage_object](#get_storage_object) - Retrieve object storage
* [delete_storage_objects](#delete_storage_objects) - Delete object storage

## get_storage_objects

Lists all object storages from a team.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-storage-objects" method="get" path="/storage/objects" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.object_storage.get_storage_objects()

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

## post_storage_objects

Creates a new object storage bucket for a project.

### Example Usage: Create

<!-- UsageSnippet language="python" operationID="post-storage-objects" method="post" path="/storage/objects" example="Create" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.object_storage.post_storage_objects(data={
        "type": latitudesh_python_sdk.PostStorageObjectsType.OBJECTS,
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

<!-- UsageSnippet language="python" operationID="post-storage-objects" method="post" path="/storage/objects" example="CreateScoped" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.object_storage.post_storage_objects(data={
        "type": latitudesh_python_sdk.PostStorageObjectsType.OBJECTS,
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

<!-- UsageSnippet language="python" operationID="post-storage-objects" method="post" path="/storage/objects" example="Created" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.object_storage.post_storage_objects(data={
        "type": latitudesh_python_sdk.PostStorageObjectsType.OBJECTS,
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

<!-- UsageSnippet language="python" operationID="post-storage-objects" method="post" path="/storage/objects" example="FeatureNotEnabled" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.object_storage.post_storage_objects(data={
        "type": latitudesh_python_sdk.PostStorageObjectsType.OBJECTS,
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

<!-- UsageSnippet language="python" operationID="post-storage-objects" method="post" path="/storage/objects" example="InsufficientPermissions" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.object_storage.post_storage_objects(data={
        "type": latitudesh_python_sdk.PostStorageObjectsType.OBJECTS,
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
| `data`                                                                  | [models.PostStorageObjectsData](../../models/poststorageobjectsdata.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.PostStorageObjectsResponseBody](../../models/poststorageobjectsresponsebody.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 404, 409, 422       | application/vnd.api+json |
| models.ErrorObject       | 500                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## get_storage_object

Shows details of a specific object storage.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-storage-object" method="get" path="/storage/objects/{id}" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.object_storage.get_storage_object(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The object storage ID                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetStorageObjectResponseBody](../../models/getstorageobjectresponsebody.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 404                 | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## delete_storage_objects

Allows you to remove an object storage from a project.

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-storage-objects" method="delete" path="/storage/objects/{id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.object_storage.delete_storage_objects(id="<id>")

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
| models.ErrorObject       | 403, 404                 | application/vnd.api+json |
| models.ErrorObject       | 500                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |