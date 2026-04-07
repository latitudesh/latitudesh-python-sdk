# ControlPlaneStatus

Current status of control plane nodes. 'ready' when control plane is operational, 'scaling' when nodes are being provisioned/removed, 'error' when a control plane node has failed.

## Example Usage

```python
from latitudesh_python_sdk.models import ControlPlaneStatus

value = ControlPlaneStatus.READY
```


## Values

| Name      | Value     |
| --------- | --------- |
| `READY`   | ready     |
| `SCALING` | scaling   |
| `ERROR`   | error     |