# KubernetesClusterDataPhase

The current phase of the cluster lifecycle. 'Upgrading' is reported while a Kubernetes version upgrade is rolling through the cluster.

## Example Usage

```python
from latitudesh_python_sdk.models import KubernetesClusterDataPhase

value = KubernetesClusterDataPhase.PENDING

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `PENDING`      | Pending        |
| `PROVISIONING` | Provisioning   |
| `PROVISIONED`  | Provisioned    |
| `UPGRADING`    | Upgrading      |
| `DELETING`     | Deleting       |
| `FAILED`       | Failed         |
| `UNKNOWN`      | Unknown        |