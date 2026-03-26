# WorkerStatus

Current status of worker nodes. 'idle' when 0 workers, 'ready' when all workers are ready, 'scaling' when workers are being provisioned/removed, 'error' when a worker has failed.

## Example Usage

```python
from latitudesh_python_sdk.models import WorkerStatus

value = WorkerStatus.IDLE
```


## Values

| Name      | Value     |
| --------- | --------- |
| `IDLE`    | idle      |
| `READY`   | ready     |
| `SCALING` | scaling   |
| `ERROR`   | error     |