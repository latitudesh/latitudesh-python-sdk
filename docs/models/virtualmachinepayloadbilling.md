# VirtualMachinePayloadBilling

Billing cycle for the VM. The supported set is validated per-project (on_demand vs reserved). Defaults to the project's default billing when omitted.

## Example Usage

```python
from latitudesh_python_sdk.models import VirtualMachinePayloadBilling

value = VirtualMachinePayloadBilling.HOURLY
```


## Values

| Name      | Value     |
| --------- | --------- |
| `HOURLY`  | hourly    |
| `MONTHLY` | monthly   |
| `YEARLY`  | yearly    |