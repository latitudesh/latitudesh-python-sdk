# VirtualMachineUpdatePayloadBilling

Target billing cycle. Upgrades only (hourly → monthly → yearly); downgrades and reserved-project changes return 422.

## Example Usage

```python
from latitudesh_python_sdk.models import VirtualMachineUpdatePayloadBilling

value = VirtualMachineUpdatePayloadBilling.HOURLY
```


## Values

| Name      | Value     |
| --------- | --------- |
| `HOURLY`  | hourly    |
| `MONTHLY` | monthly   |
| `YEARLY`  | yearly    |