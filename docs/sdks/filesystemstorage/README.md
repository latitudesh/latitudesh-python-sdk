# FilesystemStorage

## Overview

### Available Operations

* [create_filesystem](#create_filesystem) - Create filesystem
* [list_filesystems](#list_filesystems) - List filesystems
* [delete_filesystem](#delete_filesystem) - Delete filesystem
* [update_filesystem](#update_filesystem) - Update filesystem
* [get_filesystem_attachment](#get_filesystem_attachment) - Get filesystem attachment
* [attach_filesystem](#attach_filesystem) - Attach filesystem to server
* [detach_filesystem](#detach_filesystem) - Detach filesystem from server

## create_filesystem

Allows you to add persistent storage to a project. These filesystems can be used to store data across your servers.

### Example Usage: Created

<!-- UsageSnippet language="python" operationID="create-filesystem" method="post" path="/storage/filesystems" example="Created" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.filesystem_storage.create_filesystem(data={
        "type": latitudesh_python_sdk.CreateFilesystemFilesystemStorageType.FILESYSTEMS,
        "attributes": {
            "project": "proj_lkg1De6ROvZE5",
            "name": "my-data",
            "region": "NYC",
            "protocols": [
                latitudesh_python_sdk.CreateFilesystemProtocols.NFS3,
            ],
        },
    })

    # Handle response
    print(res)

```
### Example Usage: LocationUnavailable

<!-- UsageSnippet language="python" operationID="create-filesystem" method="post" path="/storage/filesystems" example="LocationUnavailable" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.filesystem_storage.create_filesystem(data={
        "type": latitudesh_python_sdk.CreateFilesystemFilesystemStorageType.FILESYSTEMS,
        "attributes": {
            "project": "<value>",
            "name": "<value>",
            "region": "<value>",
            "protocols": [
                latitudesh_python_sdk.CreateFilesystemProtocols.NFS4,
            ],
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Storage creation frozen

<!-- UsageSnippet language="python" operationID="create-filesystem" method="post" path="/storage/filesystems" example="Storage creation frozen" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.filesystem_storage.create_filesystem(data={
        "type": latitudesh_python_sdk.CreateFilesystemFilesystemStorageType.FILESYSTEMS,
        "attributes": {
            "project": "<value>",
            "name": "<value>",
            "region": "<value>",
            "protocols": [
                latitudesh_python_sdk.CreateFilesystemProtocols.NFS4,
            ],
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `data`                                                                                                | [models.CreateFilesystemFilesystemStorageData](../../models/createfilesystemfilesystemstoragedata.md) | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.CreateFilesystemResponseBody](../../models/createfilesystemresponsebody.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 422                      | application/vnd.api+json |
| models.ErrorObject       | 503                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## list_filesystems

Lists all the filesystems from a team.

### Example Usage

<!-- UsageSnippet language="python" operationID="list-filesystems" method="get" path="/storage/filesystems" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.filesystem_storage.list_filesystems(filter_project="small-rubber-shirt")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `filter_project`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The project ID or Slug to filter by                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Filesystems](../../models/filesystems.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete_filesystem

Allows you to remove a filesystem from a project.

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-filesystem" method="delete" path="/storage/filesystems/{filesystem_id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    latitudesh.filesystem_storage.delete_filesystem(filesystem_id="<id>")

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

### Example Usage

<!-- UsageSnippet language="python" operationID="update-filesystem" method="patch" path="/storage/filesystems/{filesystem_id}" example="Success" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.filesystem_storage.update_filesystem(filesystem_id="fs_7vYAZqGBdMQ94", data={
        "id": "fs_7vYAZqGBdMQ94",
        "type": latitudesh_python_sdk.UpdateFilesystemFilesystemStorageType.FILESYSTEMS,
        "attributes": {
            "size_in_gb": 1501,
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `filesystem_id`                                                                                       | *str*                                                                                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `data`                                                                                                | [models.UpdateFilesystemFilesystemStorageData](../../models/updatefilesystemfilesystemstoragedata.md) | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.UpdateFilesystemResponseBody](../../models/updatefilesystemresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_filesystem_attachment

Returns whether a server is attached to the storage network the filesystem is served on. Poll it after attaching: once the status is "attached", configure the returned storage network on the server and mount the filesystem.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-filesystem-attachment" method="get" path="/storage/filesystems/{filesystem_id}/attach" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.filesystem_storage.get_filesystem_attachment(filesystem_id="<id>", server_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `filesystem_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | Filesystem ID                                                       |
| `server_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Server ID                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetFilesystemAttachmentResponseBody](../../models/getfilesystemattachmentresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## attach_filesystem

Attaches a running server to the private storage network the filesystem is served on, so it can mount the filesystem. The attach runs asynchronously and is idempotent.

### Example Usage

<!-- UsageSnippet language="python" operationID="attach-filesystem" method="post" path="/storage/filesystems/{filesystem_id}/attach" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    latitudesh.filesystem_storage.attach_filesystem(filesystem_id="<id>", data={
        "type": latitudesh_python_sdk.AttachFilesystemFilesystemStorageType.FILESYSTEMS,
        "attributes": {
            "server_id": "sv_abcd1234",
        },
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `filesystem_id`                                                                                       | *str*                                                                                                 | :heavy_check_mark:                                                                                    | Filesystem ID                                                                                         |
| `data`                                                                                                | [models.AttachFilesystemFilesystemStorageData](../../models/attachfilesystemfilesystemstoragedata.md) | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## detach_filesystem

Detaches a server from the storage network the filesystem is served on, removing its storage IP and VLAN. The network stays while a volume is still mapped to the server, since volumes use the same network. The detach runs asynchronously: poll GET .../attach for its status.

### Example Usage

<!-- UsageSnippet language="python" operationID="detach-filesystem" method="post" path="/storage/filesystems/{filesystem_id}/detach" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    latitudesh.filesystem_storage.detach_filesystem(filesystem_id="<id>", data={
        "type": latitudesh_python_sdk.DetachFilesystemFilesystemStorageType.FILESYSTEMS,
        "attributes": {
            "server_id": "sv_abcd1234",
        },
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `filesystem_id`                                                                                       | *str*                                                                                                 | :heavy_check_mark:                                                                                    | Filesystem ID                                                                                         |
| `data`                                                                                                | [models.DetachFilesystemFilesystemStorageData](../../models/detachfilesystemfilesystemstoragedata.md) | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |