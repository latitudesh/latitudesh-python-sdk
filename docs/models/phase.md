# Phase

The current phase of the cluster lifecycle.

## Example Usage

```python
from latitudesh_python_sdk.models import Phase

value = Phase.PENDING

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `PENDING`      | Pending        |
| `PROVISIONING` | Provisioning   |
| `PROVISIONED`  | Provisioned    |
| `UPGRADING`    | Upgrading      |
| `DELETING`     | Deleting       |
| `FAILED`       | Failed         |
| `UNKNOWN`      | Unknown        |