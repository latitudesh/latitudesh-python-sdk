# PostStorageBucketsRetentionMode

Object Lock retention mode applied to new objects. `GOVERNANCE` allows privileged users to override the retention; `COMPLIANCE` cannot be overridden by anyone. Only applies when `locking` is `true`.

## Example Usage

```python
from latitudesh_python_sdk.models import PostStorageBucketsRetentionMode

value = PostStorageBucketsRetentionMode.NONE
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `NONE`       | NONE         |
| `COMPLIANCE` | COMPLIANCE   |
| `GOVERNANCE` | GOVERNANCE   |