# Storage

## Overview

### Available Operations

* [create_filesystem](#create_filesystem) - Create filesystem
* [list_filesystems](#list_filesystems) - List filesystems
* [delete_filesystem](#delete_filesystem) - Delete filesystem
* [update_filesystem](#update_filesystem) - Update filesystem
* [get_storage_volumes](#get_storage_volumes) - List volumes
* [post_storage_volumes](#post_storage_volumes) - Create volume
* [get_storage_volume](#get_storage_volume) - Retrieve volume
* [delete_storage_volumes](#delete_storage_volumes) - Delete volume
* [post_storage_volumes_mount](#post_storage_volumes_mount) - Mount volume
* [get_storage_objects](#get_storage_objects) - List object storages
* [post_storage_objects](#post_storage_objects) - Create object storage
* [get_storage_object](#get_storage_object) - Retrieve object storage
* [delete_storage_objects](#delete_storage_objects) - Delete object storage

## create_filesystem

Allows you to add persistent storage to a project. These filesystems can be used to store data across your servers.

### Example Usage: Conflict

<!-- UsageSnippet language="python" operationID="post-storage-filesystems" method="post" path="/storage/filesystems" example="Conflict" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.storage.create_filesystem(data={
        "type": latitudesh_python_sdk.PostStorageFilesystemsStorageType.FILESYSTEMS,
        "attributes": {
            "project": "proj_0L6WO19lOPlXy",
            "name": "my-data",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Created

<!-- UsageSnippet language="python" operationID="post-storage-filesystems" method="post" path="/storage/filesystems" example="Created" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.storage.create_filesystem(data={
        "type": latitudesh_python_sdk.PostStorageFilesystemsStorageType.FILESYSTEMS,
        "attributes": {
            "project": "proj_lkg1De6ROvZE5",
            "name": "my-data",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Forbidden

<!-- UsageSnippet language="python" operationID="post-storage-filesystems" method="post" path="/storage/filesystems" example="Forbidden" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.storage.create_filesystem(data={
        "type": latitudesh_python_sdk.PostStorageFilesystemsStorageType.FILESYSTEMS,
        "attributes": {
            "project": "proj_3YjJOLejdvZ87",
            "name": "my-data",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Storage creation frozen

<!-- UsageSnippet language="python" operationID="post-storage-filesystems" method="post" path="/storage/filesystems" example="Storage creation frozen" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.storage.create_filesystem(data={
        "type": latitudesh_python_sdk.PostStorageFilesystemsStorageType.FILESYSTEMS,
        "attributes": {
            "project": "<value>",
            "name": "<value>",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Unprocessable Entity

<!-- UsageSnippet language="python" operationID="post-storage-filesystems" method="post" path="/storage/filesystems" example="Unprocessable Entity" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.storage.create_filesystem(data={
        "type": latitudesh_python_sdk.PostStorageFilesystemsStorageType.FILESYSTEMS,
        "attributes": {
            "project": "proj_pRMLydp0dQKr1",
            "name": "test storage @",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `data`                                                                                        | [models.PostStorageFilesystemsStorageData](../../models/poststoragefilesystemsstoragedata.md) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.PostStorageFilesystemsResponseBody](../../models/poststoragefilesystemsresponsebody.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 503                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## list_filesystems

Lists all the filesystems from a team.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-storage-filesystems" method="get" path="/storage/filesystems" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.storage.list_filesystems(filter_project="small-rubber-shirt")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `filter_project`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The project ID or Slug to filter by                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete_filesystem

Allows you to remove persistent storage from a project.

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-storage-filesystems" method="delete" path="/storage/filesystems/{filesystem_id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.storage.delete_filesystem(filesystem_id="fs_123")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `filesystem_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_filesystem

Allow you to upgrade the size of a filesystem.

### Example Usage: Forbidden

<!-- UsageSnippet language="python" operationID="patch-storage-filesystems" method="patch" path="/storage/filesystems/{filesystem_id}" example="Forbidden" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.storage.update_filesystem(filesystem_id="fs_x1ZJrdx5qg4LV", data={
        "id": "fs_x1ZJrdx5qg4LV",
        "type": latitudesh_python_sdk.PatchStorageFilesystemsStorageType.FILESYSTEMS,
        "attributes": {
            "size_in_gb": 1501,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Success

<!-- UsageSnippet language="python" operationID="patch-storage-filesystems" method="patch" path="/storage/filesystems/{filesystem_id}" example="Success" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.storage.update_filesystem(filesystem_id="fs_7vYAZqGBdMQ94", data={
        "id": "fs_7vYAZqGBdMQ94",
        "type": latitudesh_python_sdk.PatchStorageFilesystemsStorageType.FILESYSTEMS,
        "attributes": {
            "size_in_gb": 1501,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Validation Error

<!-- UsageSnippet language="python" operationID="patch-storage-filesystems" method="patch" path="/storage/filesystems/{filesystem_id}" example="Validation Error" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.storage.update_filesystem(filesystem_id="fs_r0MK4O4kDa95w", data={
        "id": "fs_r0MK4O4kDa95w",
        "type": latitudesh_python_sdk.PatchStorageFilesystemsStorageType.FILESYSTEMS,
        "attributes": {
            "size_in_gb": 1499,
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `filesystem_id`                                                                                 | *str*                                                                                           | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `data`                                                                                          | [models.PatchStorageFilesystemsStorageData](../../models/patchstoragefilesystemsstoragedata.md) | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.PatchStorageFilesystemsResponseBody](../../models/patchstoragefilesystemsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_storage_volumes

Lists all the volumes from a team.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-storage-volumes" method="get" path="/storage/volumes" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.storage.get_storage_volumes(filter_project="proj_WeGoqA5AqP7nz")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `filter_project`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The project ID or Slug to filter by                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetStorageVolumesResponseBody](../../models/getstoragevolumesresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## post_storage_volumes

Allows you to add persistent storage to a project. These volumes can be used to store data across your servers.

### Example Usage: Created

<!-- UsageSnippet language="python" operationID="post-storage-volumes" method="post" path="/storage/volumes" example="Created" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.storage.post_storage_volumes(data={
        "type": latitudesh_python_sdk.PostStorageVolumesStorageType.VOLUMES,
        "attributes": {
            "project": "proj_enPbqoZ6dA2MQ",
            "name": "my-data",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Storage creation frozen

<!-- UsageSnippet language="python" operationID="post-storage-volumes" method="post" path="/storage/volumes" example="Storage creation frozen" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.storage.post_storage_volumes(data={
        "type": latitudesh_python_sdk.PostStorageVolumesStorageType.VOLUMES,
        "attributes": {
            "project": "<value>",
            "name": "<value>",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `data`                                                                                | [models.PostStorageVolumesStorageData](../../models/poststoragevolumesstoragedata.md) | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.PostStorageVolumesResponseBody](../../models/poststoragevolumesresponsebody.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 503                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## get_storage_volume

Shows details of a specific volume storage.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-storage-volume" method="get" path="/storage/volumes/{id}" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.storage.get_storage_volume(id="vol_aKXgRdR3qv9k5")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The volume storage ID                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetStorageVolumeResponseBody](../../models/getstoragevolumeresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete_storage_volumes

Allows you to remove persistent storage from a project.

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-storage-volumes" method="delete" path="/storage/volumes/{id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.storage.delete_storage_volumes(id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## post_storage_volumes_mount

Mounts volume storage by adding the client to an allowed list

### Example Usage

<!-- UsageSnippet language="python" operationID="post-storage-volumes-mount" method="post" path="/storage/volumes/{id}/mount" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.storage.post_storage_volumes_mount(id="<id>", data={
        "type": latitudesh_python_sdk.PostStorageVolumesMountType.VOLUMES,
        "attributes": {
            "nqn": "nqn.2024-01.com.example:server01",
        },
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `id`                                                                              | *str*                                                                             | :heavy_check_mark:                                                                | Volume storage ID                                                                 |
| `data`                                                                            | [models.PostStorageVolumesMountData](../../models/poststoragevolumesmountdata.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

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

    res = latitudesh.storage.get_storage_objects()

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

    res = latitudesh.storage.post_storage_objects(data={
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

    res = latitudesh.storage.post_storage_objects(data={
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

    res = latitudesh.storage.post_storage_objects(data={
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

    res = latitudesh.storage.post_storage_objects(data={
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

    res = latitudesh.storage.post_storage_objects(data={
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

    res = latitudesh.storage.get_storage_object(id="<id>")

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

    latitudesh.storage.delete_storage_objects(id="<id>")

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