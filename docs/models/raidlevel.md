# RaidLevel

RAID level for the group. Only valid for the 'os' and 'storage' roles; 'raid-10' is storage-only, needs at least 4 disks, and is applied only at locations with the `raid_ten` feature

## Example Usage

```python
from latitudesh_python_sdk.models import RaidLevel

value = RaidLevel.RAID_0
```


## Values

| Name      | Value     |
| --------- | --------- |
| `RAID_0`  | raid-0    |
| `RAID_1`  | raid-1    |
| `RAID_10` | raid-10   |