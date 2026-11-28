# PublicIPType

How the VM holds its public IP: `direct`, a BGP-announced address on its own NIC (every VM outside a VPC); `floating`, a public address the VPC router maps onto the private address of the VM; null when the VM has no public IP.

## Example Usage

```python
from latitudesh_python_sdk.models import PublicIPType

value = PublicIPType.DIRECT
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `DIRECT`   | direct     |
| `FLOATING` | floating   |