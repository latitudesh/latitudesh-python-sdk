# BlockStorage

## Overview

### Available Operations

* [list_volumes](#list_volumes) - List volumes
* [create_volume](#create_volume) - Create volume
* [retrieve_volume](#retrieve_volume) - Retrieve volume
* [delete_volume](#delete_volume) - Delete volume
* [~~mount_volume~~](#mount_volume) - Mount volume (deprecated) :warning: **Deprecated**
* [map_volume](#map_volume) - Map volume
* [unmap_volume](#unmap_volume) - Unmap volume

## list_volumes

Lists all the volumes from a team.

### Example Usage

<!-- UsageSnippet language="python" operationID="list-volumes" method="get" path="/storage/volumes" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.block_storage.list_volumes(filter_project="proj_WeGoqA5AqP7nz")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `filter_project`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The project ID or Slug to filter by                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListVolumesResponseBody](../../models/listvolumesresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_volume

Allows you to add persistent storage to a project. These volumes can be used to store data across your servers.

### Example Usage

<!-- UsageSnippet language="python" operationID="create-volume" method="post" path="/storage/volumes" example="Created" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.block_storage.create_volume(data={
        "type": latitudesh_python_sdk.CreateVolumeBlockStorageType.VOLUMES,
        "attributes": {
            "project": "proj_enPbqoZ6dA2MQ",
            "name": "my-data",
            "region": "DAL",
            "size_in_gb": 1500,
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `data`                                                                              | [models.CreateVolumeBlockStorageData](../../models/createvolumeblockstoragedata.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.CreateVolumeResponseBody](../../models/createvolumeresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## retrieve_volume

Shows details of a specific volume.

### Example Usage

<!-- UsageSnippet language="python" operationID="retrieve-volume" method="get" path="/storage/volumes/{id}" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.block_storage.retrieve_volume(id="vol_aKXgRdR3qv9k5")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The volume ID                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RetrieveVolumeResponseBody](../../models/retrievevolumeresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete_volume

Allows you to remove a volume from a project.

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-volume" method="delete" path="/storage/volumes/{id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.block_storage.delete_volume(id="<id>")

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

## ~~mount_volume~~

Mounts a volume by adding the client to an allowed list

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="mount-volume" method="post" path="/storage/volumes/{id}/mount" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.block_storage.mount_volume(id="<id>", data={
        "type": latitudesh_python_sdk.MountVolumeType.VOLUMES,
        "attributes": {
            "nqn": "nqn.2024-01.com.example:server01",
        },
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Volume ID                                                           |
| `data`                                                              | [models.MountVolumeData](../../models/mountvolumedata.md)           | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## map_volume

Maps a high performance volume to a server over NVMe-TCP.

### Example Usage

<!-- UsageSnippet language="python" operationID="map-volume" method="post" path="/storage/volumes/{id}/map" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.block_storage.map_volume(id="<id>", data={
        "type": latitudesh_python_sdk.MapVolumeBlockStorageType.VOLUMES,
        "attributes": {
            "server_id": "sv_abcd1234",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `id`                                                                          | *str*                                                                         | :heavy_check_mark:                                                            | Volume ID                                                                     |
| `data`                                                                        | [models.MapVolumeBlockStorageData](../../models/mapvolumeblockstoragedata.md) | :heavy_check_mark:                                                            | N/A                                                                           |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.MapVolumeResponseBody](../../models/mapvolumeresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## unmap_volume

Unmaps a high performance volume from the server it is currently mapped to.

### Example Usage

<!-- UsageSnippet language="python" operationID="unmap-volume" method="post" path="/storage/volumes/{id}/unmap" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.block_storage.unmap_volume(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Volume ID                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UnmapVolumeResponseBody](../../models/unmapvolumeresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |