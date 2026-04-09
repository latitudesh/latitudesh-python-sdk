# KubernetesClusterUpdateResponseStatus

The update status. 'scaling' indicates nodes are being added or removed. 'upgrading' indicates a version upgrade is in progress. 'unchanged' indicates no change was needed.

## Example Usage

```python
from latitudesh_python_sdk.models import KubernetesClusterUpdateResponseStatus

value = KubernetesClusterUpdateResponseStatus.SCALING
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `SCALING`   | scaling     |
| `UPGRADING` | upgrading   |
| `UNCHANGED` | unchanged   |