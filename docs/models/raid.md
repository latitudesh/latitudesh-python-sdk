# Raid

Expected RAID level with the default disk layout (data array on 4+ disk servers, the OS on 2-3 disk servers). Mutually exclusive with disk_layout

## Example Usage

```python
from latitudesh_python_sdk.models import Raid

value = Raid.RAID_0
```


## Values

| Name      | Value     |
| --------- | --------- |
| `RAID_0`  | raid-0    |
| `RAID_1`  | raid-1    |
| `RAID_10` | raid-10   |