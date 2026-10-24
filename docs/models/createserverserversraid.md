# CreateServerServersRaid

RAID mode for the server. Set to 'raid-0' for RAID 0, 'raid-1' for RAID 1, 'raid-10' for RAID 10 on the data disks (only at locations with the `raid_ten` feature), or omit/null for no RAID configuration

## Example Usage

```python
from latitudesh_python_sdk.models import CreateServerServersRaid

value = CreateServerServersRaid.RAID_0
```


## Values

| Name      | Value     |
| --------- | --------- |
| `RAID_0`  | raid-0    |
| `RAID_1`  | raid-1    |
| `RAID_10` | raid-10   |