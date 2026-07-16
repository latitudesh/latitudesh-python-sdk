# VirtualMachineBackups

## Overview

### Available Operations

* [list_virtual_machine_scoped_backups](#list_virtual_machine_scoped_backups) - List a VM's backups
* [create_virtual_machine_backup](#create_virtual_machine_backup) - Create VM backup
* [list_virtual_machine_backups](#list_virtual_machine_backups) - List all VM backups
* [create_virtual_machine_backup_top_level](#create_virtual_machine_backup_top_level) - Create VM backup (top-level)
* [get_virtual_machine_backup](#get_virtual_machine_backup) - Get VM backup
* [delete_virtual_machine_backup](#delete_virtual_machine_backup) - Delete VM backup

## list_virtual_machine_scoped_backups

Lists the backups of the given Virtual Machine.


### Example Usage

<!-- UsageSnippet language="python" operationID="list-virtual-machine-scoped-backups" method="get" path="/virtual_machines/{virtual_machine_id}/backups" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.virtual_machine_backups.list_virtual_machine_scoped_backups(virtual_machine_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `virtual_machine_id`                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.VirtualMachineBackups](../../models/virtualmachinebackups.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## create_virtual_machine_backup

Triggers a backup of the given Virtual Machine.


### Example Usage

<!-- UsageSnippet language="python" operationID="create-virtual-machine-backup" method="post" path="/virtual_machines/{virtual_machine_id}/backups" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.virtual_machine_backups.create_virtual_machine_backup(virtual_machine_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `virtual_machine_id`                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.VirtualMachineBackup](../../models/virtualmachinebackup.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## list_virtual_machine_backups

Lists every backup that belongs to the authenticated team.


### Example Usage

<!-- UsageSnippet language="python" operationID="list-virtual-machine-backups" method="get" path="/virtual_machine_backups" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.virtual_machine_backups.list_virtual_machine_backups()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.VirtualMachineBackups](../../models/virtualmachinebackups.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## create_virtual_machine_backup_top_level

Triggers a backup of the Virtual Machine referenced in the body.


### Example Usage

<!-- UsageSnippet language="python" operationID="create-virtual-machine-backup-top-level" method="post" path="/virtual_machine_backups" example="FeatureNotEnabled" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.virtual_machine_backups.create_virtual_machine_backup_top_level()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `data`                                                                                              | [Optional[models.VirtualMachineBackupPayloadData]](../../models/virtualmachinebackuppayloaddata.md) | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[models.VirtualMachineBackup](../../models/virtualmachinebackup.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## get_virtual_machine_backup

Get VM backup

### Example Usage

<!-- UsageSnippet language="python" operationID="get-virtual-machine-backup" method="get" path="/virtual_machine_backups/{id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.virtual_machine_backups.get_virtual_machine_backup(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.VirtualMachineBackup](../../models/virtualmachinebackup.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## delete_virtual_machine_backup

Archives and deletes a Virtual Machine backup. Work runs asynchronously and returns 202 Accepted. Only `Ready` or `Failed` backups can be deleted, and not while a restore from the backup is in progress.


### Example Usage

<!-- UsageSnippet language="python" operationID="delete-virtual-machine-backup" method="delete" path="/virtual_machine_backups/{id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.virtual_machine_backups.delete_virtual_machine_backup(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.VirtualMachineBackup](../../models/virtualmachinebackup.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |