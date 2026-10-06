# PublicNetworkDataRole

gateway: reserved for the network gateway; server: a server on the network; elastic_ip: an elastic IP; reserved: held in IPAM but not by a server, including addresses you reserved; available: free to use

## Example Usage

```python
from latitudesh_python_sdk.models import PublicNetworkDataRole

value = PublicNetworkDataRole.GATEWAY
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `GATEWAY`    | gateway      |
| `SERVER`     | server       |
| `ELASTIC_IP` | elastic_ip   |
| `RESERVED`   | reserved     |
| `AVAILABLE`  | available    |