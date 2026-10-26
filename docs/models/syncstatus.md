# SyncStatus

Control-plane refresh observation. Synced confirms the receiver observed an active key; revoked confirms it observed the key absent. Other regions reconcile independently.

## Example Usage

```python
from latitudesh_python_sdk.models import SyncStatus

value = SyncStatus.PENDING
```


## Values

| Name      | Value     |
| --------- | --------- |
| `PENDING` | pending   |
| `SYNCED`  | synced    |
| `FAILED`  | failed    |
| `REVOKED` | revoked   |