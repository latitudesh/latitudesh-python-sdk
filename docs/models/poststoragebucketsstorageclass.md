# PostStorageBucketsStorageClass

Backend storage tier. `standard` is the default S3-compatible tier. `high_performance` is a lower-latency, higher-throughput tier available in select regions only.

## Example Usage

```python
from latitudesh_python_sdk.models import PostStorageBucketsStorageClass

value = PostStorageBucketsStorageClass.STANDARD
```


## Values

| Name               | Value              |
| ------------------ | ------------------ |
| `STANDARD`         | standard           |
| `HIGH_PERFORMANCE` | high_performance   |