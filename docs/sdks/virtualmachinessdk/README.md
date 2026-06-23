# VirtualMachines

## Overview

### Available Operations

* [create](#create) - Create VM
* [list](#list) - List VMs
* [get](#get) - Retrieve VM
* [delete](#delete) - Destroy VM
* [update_virtual_machine](#update_virtual_machine) - Update VM
* [create_virtual_machine_action](#create_virtual_machine_action) - Run VM power action
* [show_virtual_machine_metrics](#show_virtual_machine_metrics) - Retrieve VM metrics
* [list_virtual_machine_network_attachments](#list_virtual_machine_network_attachments) - List VM network attachments
* [create_virtual_machine_network_attachment](#create_virtual_machine_network_attachment) - Attach a network to a VM
* [destroy_virtual_machine_network_attachment](#destroy_virtual_machine_network_attachment) - Detach a network from a VM

## create

Creates a new Virtual Machine.


### Example Usage: Conflict

<!-- UsageSnippet language="python" operationID="create-virtual-machine" method="post" path="/virtual_machines" example="Conflict" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.virtual_machines.create(data={
        "type": latitudesh_python_sdk.VirtualMachinePayloadType.VIRTUAL_MACHINES,
        "attributes": {
            "name": "my-new-vm",
            "project": "intelligent-paper-table",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Created

<!-- UsageSnippet language="python" operationID="create-virtual-machine" method="post" path="/virtual_machines" example="Created" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.virtual_machines.create(data={
        "type": latitudesh_python_sdk.VirtualMachinePayloadType.VIRTUAL_MACHINES,
        "attributes": {
            "name": "my-new-vm",
            "project": "lightweight-leather-lamp",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: CreatedWithOS

<!-- UsageSnippet language="python" operationID="create-virtual-machine" method="post" path="/virtual_machines" example="CreatedWithOS" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.virtual_machines.create(data={
        "type": latitudesh_python_sdk.VirtualMachinePayloadType.VIRTUAL_MACHINES,
        "attributes": {
            "name": "my-new-vm",
            "project": "lightweight-leather-lamp",
            "operating_system": "ubuntu_24_04_x64_lts",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: CreatedWithUserData

<!-- UsageSnippet language="python" operationID="create-virtual-machine" method="post" path="/virtual_machines" example="CreatedWithUserData" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.virtual_machines.create(data={
        "type": latitudesh_python_sdk.VirtualMachinePayloadType.VIRTUAL_MACHINES,
        "attributes": {
            "name": "my-new-vm",
            "project": "lightweight-leather-lamp",
            "user_data": "ud_abc123",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Unprocessable Entity

<!-- UsageSnippet language="python" operationID="create-virtual-machine" method="post" path="/virtual_machines" example="Unprocessable Entity" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.virtual_machines.create(data={
        "type": latitudesh_python_sdk.VirtualMachinePayloadType.VIRTUAL_MACHINES,
        "attributes": {
            "name": "My new-vm",
            "project": "mediocre-wool-knife",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `data`                                                                                  | [Optional[models.VirtualMachinePayloadData]](../../models/virtualmachinepayloaddata.md) | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.VirtualMachine](../../models/virtualmachine.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list

Show all Team's Virtual Machines.


### Example Usage

<!-- UsageSnippet language="python" operationID="index-virtual-machine" method="get" path="/virtual_machines" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.virtual_machines.list(extra_fields_virtual_machines="credentials")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                         | Type                                                                                                                                                                              | Required                                                                                                                                                                          | Description                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `filter_project`                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                | The project ID or Slug to filter by                                                                                                                                               |
| `filter_tags`                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                | The tag IDs to filter by, separated by comma, e.g. `filter[tags]=tag_1,tag_2` will return VMs with `tag_1` AND `tag_2`.                                                           |
| `extra_fields_virtual_machines`                                                                                                                                                   | *Optional[str]*                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                | Comma-separated extra attributes that are lazy-loaded. Supported values: `credentials`, `pending_restart`. Example: `extra_fields[virtual_machines]=credentials,pending_restart`. |
| `retries`                                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                                               |

### Response

**[models.VirtualMachines](../../models/virtualmachines.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get

Show a Virtual Machine.


### Example Usage

<!-- UsageSnippet language="python" operationID="show-virtual-machine" method="get" path="/virtual_machines/{virtual_machine_id}" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.virtual_machines.get(virtual_machine_id="vm_7vYAZqGBdMQ94")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `virtual_machine_id`                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.VirtualMachine](../../models/virtualmachine.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete

Destroys a Virtual Machine.


### Example Usage

<!-- UsageSnippet language="python" operationID="destroy-virtual-machine" method="delete" path="/virtual_machines/{virtual_machine_id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.virtual_machines.delete(virtual_machine_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `virtual_machine_id`                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_virtual_machine

Updates a Virtual Machine's display name (hostname).


### Example Usage

<!-- UsageSnippet language="python" operationID="update-virtual-machine" method="patch" path="/virtual_machines/{virtual_machine_id}" example="Success" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.virtual_machines.update_virtual_machine(virtual_machine_id="vm_7vYAZqGBdMQ94", data={
        "type": latitudesh_python_sdk.VirtualMachineUpdatePayloadType.VIRTUAL_MACHINES,
        "id": "vm_7vYAZqGBdMQ94",
        "attributes": {
            "name": "my-updated-vm",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `virtual_machine_id`                                                                      | *str*                                                                                     | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `data`                                                                                    | [models.VirtualMachineUpdatePayloadData](../../models/virtualmachineupdatepayloaddata.md) | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.VirtualMachine](../../models/virtualmachine.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_virtual_machine_action

Performs a power action on a given virtual machine:
- `power_on` - Starts the virtual machine
- `power_off` - Stops the virtual machine
- `reboot` - Restarts the virtual machine


### Example Usage

<!-- UsageSnippet language="python" operationID="create-virtual-machine-action" method="post" path="/virtual_machines/{virtual_machine_id}/actions" example="Created" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.virtual_machines.create_virtual_machine_action(virtual_machine_id="vm_5LA73qkjdaJ2o", id="vm_5LA73qkjdaJ2o", type_=latitudesh_python_sdk.CreateVirtualMachineActionVirtualMachinesType.VIRTUAL_MACHINES, attributes={
        "action": latitudesh_python_sdk.CreateVirtualMachineActionVirtualMachinesAction.REBOOT,
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                         | Type                                                                                                                              | Required                                                                                                                          | Description                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `virtual_machine_id`                                                                                                              | *str*                                                                                                                             | :heavy_check_mark:                                                                                                                | N/A                                                                                                                               |
| `id`                                                                                                                              | *str*                                                                                                                             | :heavy_check_mark:                                                                                                                | N/A                                                                                                                               |
| `type`                                                                                                                            | [models.CreateVirtualMachineActionVirtualMachinesType](../../models/createvirtualmachineactionvirtualmachinestype.md)             | :heavy_check_mark:                                                                                                                | N/A                                                                                                                               |
| `attributes`                                                                                                                      | [models.CreateVirtualMachineActionVirtualMachinesAttributes](../../models/createvirtualmachineactionvirtualmachinesattributes.md) | :heavy_check_mark:                                                                                                                | N/A                                                                                                                               |
| `retries`                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                  | :heavy_minus_sign:                                                                                                                | Configuration to override the default retry behavior of the client.                                                               |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## show_virtual_machine_metrics

Retrieve a time series for a single metric of a Virtual Machine.

### Example Usage

<!-- UsageSnippet language="python" operationID="show-virtual-machine-metrics" method="get" path="/virtual_machines/{virtual_machine_id}/metrics" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.virtual_machines.show_virtual_machine_metrics(virtual_machine_id="<id>", metric=latitudesh_python_sdk.QueryParamMetric.MEMORY)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `virtual_machine_id`                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `metric`                                                            | [models.QueryParamMetric](../../models/queryparammetric.md)         | :heavy_check_mark:                                                  | N/A                                                                 |
| `range`                                                             | [Optional[models.QueryParamRange]](../../models/queryparamrange.md) | :heavy_minus_sign:                                                  | N/A                                                                 |
| `force_refresh`                                                     | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.VirtualMachineMetrics](../../models/virtualmachinemetrics.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_virtual_machine_network_attachments

Lists the secondary network attachments currently configured for a Virtual Machine.


### Example Usage

<!-- UsageSnippet language="python" operationID="list-virtual-machine-network-attachments" method="get" path="/virtual_machines/{virtual_machine_id}/network_attachments" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.virtual_machines.list_virtual_machine_network_attachments(virtual_machine_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `virtual_machine_id`                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.VirtualMachineNetworkAttachments](../../models/virtualmachinenetworkattachments.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_virtual_machine_network_attachment

Attaches a virtual network (VLAN) to a Virtual Machine. Work runs asynchronously and returns 202 Accepted.


### Example Usage

<!-- UsageSnippet language="python" operationID="create-virtual-machine-network-attachment" method="post" path="/virtual_machines/{virtual_machine_id}/network_attachments" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.virtual_machines.create_virtual_machine_network_attachment(virtual_machine_id="<id>", data={
        "type": latitudesh_python_sdk.VirtualMachineNetworkAttachmentCreatePayloadType.VIRTUAL_MACHINE_NETWORK_ATTACHMENTS,
        "attributes": {
            "virtual_network_id": "<id>",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                   | Type                                                                                                                        | Required                                                                                                                    | Description                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `virtual_machine_id`                                                                                                        | *str*                                                                                                                       | :heavy_check_mark:                                                                                                          | N/A                                                                                                                         |
| `data`                                                                                                                      | [models.VirtualMachineNetworkAttachmentCreatePayloadData](../../models/virtualmachinenetworkattachmentcreatepayloaddata.md) | :heavy_check_mark:                                                                                                          | N/A                                                                                                                         |
| `retries`                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                            | :heavy_minus_sign:                                                                                                          | Configuration to override the default retry behavior of the client.                                                         |

### Response

**[models.CreateVirtualMachineNetworkAttachmentResponseBody](../../models/createvirtualmachinenetworkattachmentresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## destroy_virtual_machine_network_attachment

Detaches a virtual network (VLAN) from a Virtual Machine. Work runs asynchronously and returns 202 Accepted.


### Example Usage

<!-- UsageSnippet language="python" operationID="destroy-virtual-machine-network-attachment" method="delete" path="/virtual_machines/{virtual_machine_id}/network_attachments/{id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.virtual_machines.destroy_virtual_machine_network_attachment(virtual_machine_id="<id>", id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `virtual_machine_id`                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The VLAN id_hash to detach                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DestroyVirtualMachineNetworkAttachmentResponseBody](../../models/destroyvirtualmachinenetworkattachmentresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |