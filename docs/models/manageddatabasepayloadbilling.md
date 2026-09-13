# ManagedDatabasePayloadBilling

Billing cycle (postgres/clickhouse). Defaults to monthly when omitted.

## Example Usage

```python
from latitudesh_python_sdk.models import ManagedDatabasePayloadBilling

value = ManagedDatabasePayloadBilling.MONTHLY
```


## Values

| Name      | Value     |
| --------- | --------- |
| `MONTHLY` | monthly   |
| `YEARLY`  | yearly    |