# FilesystemAttachmentDataStatus

Whether the server is attached to the filesystem storage network. "attaching"/"detaching" while an attach or detach runs, "failed" when it gave up.

## Example Usage

```python
from latitudesh_python_sdk.models import FilesystemAttachmentDataStatus

value = FilesystemAttachmentDataStatus.ATTACHING
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `ATTACHING` | attaching   |
| `ATTACHED`  | attached    |
| `DETACHING` | detaching   |
| `DETACHED`  | detached    |
| `FAILED`    | failed      |