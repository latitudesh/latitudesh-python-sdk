# RequirementsState

draft while they're being prepared; awaiting_signature to review, change and sign; signed once an owner or administrator signs. Signed requirements are locked: changing them or their node groups answers 409 REQUIREMENTS_SIGNED until your Latitude.sh contact reopens them.

## Example Usage

```python
from latitudesh_python_sdk.models import RequirementsState

value = RequirementsState.DRAFT
```


## Values

| Name                 | Value                |
| -------------------- | -------------------- |
| `DRAFT`              | draft                |
| `AWAITING_SIGNATURE` | awaiting_signature   |
| `SIGNED`             | signed               |