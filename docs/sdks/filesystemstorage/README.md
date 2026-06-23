# FilesystemStorage

## Overview

### Available Operations

* [create_filesystem](#create_filesystem) - Create filesystem
* [list_filesystems](#list_filesystems) - List filesystems
* [delete_filesystem](#delete_filesystem) - Delete filesystem
* [update_filesystem](#update_filesystem) - Update filesystem

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

    res = latitudesh.filesystem_storage.create_filesystem(data={
        "type": latitudesh_python_sdk.PostStorageFilesystemsFilesystemStorageType.FILESYSTEMS,
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

    res = latitudesh.filesystem_storage.create_filesystem(data={
        "type": latitudesh_python_sdk.PostStorageFilesystemsFilesystemStorageType.FILESYSTEMS,
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

    res = latitudesh.filesystem_storage.create_filesystem(data={
        "type": latitudesh_python_sdk.PostStorageFilesystemsFilesystemStorageType.FILESYSTEMS,
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

    res = latitudesh.filesystem_storage.create_filesystem(data={
        "type": latitudesh_python_sdk.PostStorageFilesystemsFilesystemStorageType.FILESYSTEMS,
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

    res = latitudesh.filesystem_storage.create_filesystem(data={
        "type": latitudesh_python_sdk.PostStorageFilesystemsFilesystemStorageType.FILESYSTEMS,
        "attributes": {
            "project": "proj_pRMLydp0dQKr1",
            "name": "test storage @",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `data`                                                                                                            | [models.PostStorageFilesystemsFilesystemStorageData](../../models/poststoragefilesystemsfilesystemstoragedata.md) | :heavy_check_mark:                                                                                                | N/A                                                                                                               |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |

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

    latitudesh.filesystem_storage.list_filesystems(filter_project="small-rubber-shirt")

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

Allows you to remove a filesystem from a project.

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-storage-filesystems" method="delete" path="/storage/filesystems/{filesystem_id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.filesystem_storage.delete_filesystem(filesystem_id="fs_123")

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

    res = latitudesh.filesystem_storage.update_filesystem(filesystem_id="fs_x1ZJrdx5qg4LV", data={
        "id": "fs_x1ZJrdx5qg4LV",
        "type": latitudesh_python_sdk.PatchStorageFilesystemsFilesystemStorageType.FILESYSTEMS,
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

    res = latitudesh.filesystem_storage.update_filesystem(filesystem_id="fs_7vYAZqGBdMQ94", data={
        "id": "fs_7vYAZqGBdMQ94",
        "type": latitudesh_python_sdk.PatchStorageFilesystemsFilesystemStorageType.FILESYSTEMS,
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

    res = latitudesh.filesystem_storage.update_filesystem(filesystem_id="fs_r0MK4O4kDa95w", data={
        "id": "fs_r0MK4O4kDa95w",
        "type": latitudesh_python_sdk.PatchStorageFilesystemsFilesystemStorageType.FILESYSTEMS,
        "attributes": {
            "size_in_gb": 1499,
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                           | Type                                                                                                                | Required                                                                                                            | Description                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `filesystem_id`                                                                                                     | *str*                                                                                                               | :heavy_check_mark:                                                                                                  | N/A                                                                                                                 |
| `data`                                                                                                              | [models.PatchStorageFilesystemsFilesystemStorageData](../../models/patchstoragefilesystemsfilesystemstoragedata.md) | :heavy_check_mark:                                                                                                  | N/A                                                                                                                 |
| `retries`                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                    | :heavy_minus_sign:                                                                                                  | Configuration to override the default retry behavior of the client.                                                 |

### Response

**[models.PatchStorageFilesystemsResponseBody](../../models/patchstoragefilesystemsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |