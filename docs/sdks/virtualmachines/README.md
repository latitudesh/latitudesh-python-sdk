# VirtualMachines

## Overview

### Available Operations

* [create](#create) - Create a Virtual Machine
* [list](#list) - Get Teams Virtual Machines
* [get](#get) - Get a Virtual Machine
* [delete](#delete) - Destroy a Virtual Machine
* [create_virtual_machine_action](#create_virtual_machine_action) - Run Virtual Machine Action

## create

Creates a new Virtual Machine.


### Example Usage

<!-- UsageSnippet language="python" operationID="create-virtual-machine" method="post" path="/virtual_machines" -->
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
            "site": "ASH",
            "project": "enormous-wool-keyboard",
            "billing": latitudesh_python_sdk.VirtualMachinePayloadBilling.MONTHLY,
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

<!-- UsageSnippet language="python" operationID="index-virtual-machine" method="get" path="/virtual_machines" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.virtual_machines.list(extra_fields_virtual_machines="credentials")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                          | Type                                                                                                                                                               | Required                                                                                                                                                           | Description                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `filter_project`                                                                                                                                                   | *Optional[str]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                 | The project ID or Slug to filter by                                                                                                                                |
| `extra_fields_virtual_machines`                                                                                                                                    | *Optional[str]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                 | The `credentials` are provided as extra attributes that are lazy loaded. To request it, just set `extra_fields[virtual_machines]=credentials` in the query string. |
| `retries`                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                   | :heavy_minus_sign:                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get

Show a Virtual Machine.


### Example Usage

<!-- UsageSnippet language="python" operationID="show-virtual-machine" method="get" path="/virtual_machines/{virtual_machine_id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.virtual_machines.get(virtual_machine_id="vm_w5AEmq7XDBkWX")

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

## create_virtual_machine_action

Performs a power action on a given virtual machine:
- `power_on` - Starts the virtual machine
- `power_off` - Stops the virtual machine
- `reboot` - Restarts the virtual machine


### Example Usage

<!-- UsageSnippet language="python" operationID="create-virtual-machine-action" method="post" path="/virtual_machines/{virtual_machine_id}/actions" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.virtual_machines.create_virtual_machine_action(virtual_machine_id="vm_VLMmAD8EOwop2", id="vm_VLMmAD8EOwop2", type_=latitudesh_python_sdk.CreateVirtualMachineActionVirtualMachinesType.VIRTUAL_MACHINES, attributes={
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