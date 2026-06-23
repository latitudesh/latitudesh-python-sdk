# DiskLayout


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `count`                                                        | *int*                                                          | :heavy_check_mark:                                             | N/A                                                            |
| `role`                                                         | [models.DeployConfigRole](../models/deployconfigrole.md)       | :heavy_check_mark:                                             | N/A                                                            |
| `raid_level`                                                   | [OptionalNullable[models.RaidLevel]](../models/raidlevel.md)   | :heavy_minus_sign:                                             | N/A                                                            |
| `filesystem`                                                   | [OptionalNullable[models.Filesystem]](../models/filesystem.md) | :heavy_minus_sign:                                             | N/A                                                            |
| `mount_point`                                                  | *OptionalNullable[str]*                                        | :heavy_minus_sign:                                             | N/A                                                            |