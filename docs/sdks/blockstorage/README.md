# BlockStorage

## Overview

### Available Operations

* [get_storage_volumes](#get_storage_volumes) - List volumes
* [post_storage_volumes](#post_storage_volumes) - Create volume
* [get_storage_volume](#get_storage_volume) - Retrieve volume
* [delete_storage_volumes](#delete_storage_volumes) - Delete volume
* [post_storage_volumes_mount](#post_storage_volumes_mount) - Mount volume

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

    res = latitudesh.block_storage.get_storage_volumes(filter_project="proj_WeGoqA5AqP7nz")

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

    res = latitudesh.block_storage.post_storage_volumes(data={
        "type": latitudesh_python_sdk.PostStorageVolumesBlockStorageType.VOLUMES,
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

    res = latitudesh.block_storage.post_storage_volumes(data={
        "type": latitudesh_python_sdk.PostStorageVolumesBlockStorageType.VOLUMES,
        "attributes": {
            "project": "<value>",
            "name": "<value>",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `data`                                                                                          | [models.PostStorageVolumesBlockStorageData](../../models/poststoragevolumesblockstoragedata.md) | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

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

    res = latitudesh.block_storage.get_storage_volume(id="vol_aKXgRdR3qv9k5")

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

    latitudesh.block_storage.delete_storage_volumes(id="<id>")

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

    latitudesh.block_storage.post_storage_volumes_mount(id="<id>", data={
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