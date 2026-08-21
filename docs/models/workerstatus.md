# WorkerStatus

Current status of worker nodes. 'idle' when 0 workers, 'ready' when all workers are ready, 'scaling' when workers are being provisioned/removed, 'upgrading' while a Kubernetes version upgrade is rolling through the workers, 'error' when a worker has failed.

## Example Usage

```python
from latitudesh_python_sdk.models import WorkerStatus

value = WorkerStatus.IDLE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `IDLE`      | idle        |
| `READY`     | ready       |
| `SCALING`   | scaling     |
| `UPGRADING` | upgrading   |
| `ERROR`     | error       |