# ControlPlaneStatus

Current status of control plane nodes. 'ready' when control plane is operational, 'scaling' when nodes are being provisioned/removed, 'upgrading' while a Kubernetes version upgrade is rolling through the control plane, 'error' when a control plane node has failed.

## Example Usage

```python
from latitudesh_python_sdk.models import ControlPlaneStatus

value = ControlPlaneStatus.READY

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `READY`     | ready       |
| `SCALING`   | scaling     |
| `UPGRADING` | upgrading   |
| `ERROR`     | error       |