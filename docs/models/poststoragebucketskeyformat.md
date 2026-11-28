# PostStorageBucketsKeyFormat

Format of the log object keys. Defaults to SIMPLE_PREFIX.

## Example Usage

```python
from latitudesh_python_sdk.models import PostStorageBucketsKeyFormat

value = PostStorageBucketsKeyFormat.SIMPLE_PREFIX
```


## Values

| Name                               | Value                              |
| ---------------------------------- | ---------------------------------- |
| `SIMPLE_PREFIX`                    | SIMPLE_PREFIX                      |
| `PARTITIONED_PREFIX_EVENT_TIME`    | PARTITIONED_PREFIX_EVENT_TIME      |
| `PARTITIONED_PREFIX_DELIVERY_TIME` | PARTITIONED_PREFIX_DELIVERY_TIME   |