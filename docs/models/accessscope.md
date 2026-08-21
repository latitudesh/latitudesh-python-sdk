# AccessScope

`fullaccess` grants access to all of the project's buckets. `limited_access` restricts the key to the buckets listed in `bucket_permissions`.

## Example Usage

```python
from latitudesh_python_sdk.models import AccessScope

value = AccessScope.FULLACCESS
```


## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `FULLACCESS`     | fullaccess       |
| `LIMITED_ACCESS` | limited_access   |