# VirtualMachineRestores

## Overview

### Available Operations

* [list_virtual_machine_scoped_restores](#list_virtual_machine_scoped_restores) - List a backup's restores
* [create_virtual_machine_restore](#create_virtual_machine_restore) - Create VM restore
* [list_backup_restores](#list_backup_restores) - List a backup's restores (top-level backup path)
* [list_virtual_machine_restores](#list_virtual_machine_restores) - List all VM restores
* [create_virtual_machine_restore_flat](#create_virtual_machine_restore_flat) - Create VM restore (flat)
* [get_virtual_machine_restore](#get_virtual_machine_restore) - Get VM restore

## list_virtual_machine_scoped_restores

Lists the restores created from the given backup.


### Example Usage

<!-- UsageSnippet language="python" operationID="list-virtual-machine-scoped-restores" method="get" path="/virtual_machines/{virtual_machine_id}/backups/{backup_id}/restores" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.virtual_machine_restores.list_virtual_machine_scoped_restores(virtual_machine_id="<id>", backup_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `virtual_machine_id`                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `backup_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.VirtualMachineRestores](../../models/virtualmachinerestores.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## create_virtual_machine_restore

Restores a backup into a new Virtual Machine. Optionally accepts a `name` for the restored VM and a target `site` slug to restore into another region.


### Example Usage

<!-- UsageSnippet language="python" operationID="create-virtual-machine-restore" method="post" path="/virtual_machines/{virtual_machine_id}/backups/{backup_id}/restores" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.virtual_machine_restores.create_virtual_machine_restore(virtual_machine_id="<id>", backup_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `virtual_machine_id`                                                                                  | *str*                                                                                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `backup_id`                                                                                           | *str*                                                                                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `data`                                                                                                | [Optional[models.VirtualMachineRestorePayloadData]](../../models/virtualmachinerestorepayloaddata.md) | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.VirtualMachineRestore](../../models/virtualmachinerestore.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## list_backup_restores

Lists the restores created from the given backup, reached via the top-level backup path.


### Example Usage

<!-- UsageSnippet language="python" operationID="list-backup-restores" method="get" path="/virtual_machine_backups/{backup_id}/restores" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.virtual_machine_restores.list_backup_restores(backup_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `backup_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.VirtualMachineRestores](../../models/virtualmachinerestores.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## list_virtual_machine_restores

Lists every restore that belongs to the authenticated team.


### Example Usage

<!-- UsageSnippet language="python" operationID="list-virtual-machine-restores" method="get" path="/virtual_machine_restores" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.virtual_machine_restores.list_virtual_machine_restores()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.VirtualMachineRestores](../../models/virtualmachinerestores.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## create_virtual_machine_restore_flat

Restores the backup referenced in the body into a new Virtual Machine. Optionally accepts a `name` for the restored VM and a target `site` slug to restore into another region.


### Example Usage

<!-- UsageSnippet language="python" operationID="create-virtual-machine-restore-flat" method="post" path="/virtual_machine_restores" example="FeatureNotEnabled" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.virtual_machine_restores.create_virtual_machine_restore_flat()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `data`                                                                                                | [Optional[models.VirtualMachineRestorePayloadData]](../../models/virtualmachinerestorepayloaddata.md) | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.VirtualMachineRestore](../../models/virtualmachinerestore.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## get_virtual_machine_restore

Get VM restore

### Example Usage

<!-- UsageSnippet language="python" operationID="get-virtual-machine-restore" method="get" path="/virtual_machine_restores/{id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.virtual_machine_restores.get_virtual_machine_restore(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.VirtualMachineRestore](../../models/virtualmachinerestore.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |