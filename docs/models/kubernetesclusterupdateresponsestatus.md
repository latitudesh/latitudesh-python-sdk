# KubernetesClusterUpdateResponseStatus

The update status. 'scaling' indicates worker nodes are being added or removed. 'unchanged' indicates the requested worker_count matches the current count.

## Example Usage

```python
from latitudesh_python_sdk.models import KubernetesClusterUpdateResponseStatus

value = KubernetesClusterUpdateResponseStatus.SCALING
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `SCALING`   | scaling     |
| `UNCHANGED` | unchanged   |