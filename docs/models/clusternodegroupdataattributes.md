# ClusterNodeGroupDataAttributes


## Fields

| Field                                             | Type                                              | Required                                          | Description                                       | Example                                           |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| `name`                                            | *Optional[str]*                                   | :heavy_minus_sign:                                | N/A                                               | gpu-workers                                       |
| `kind`                                            | [Optional[models.Kind]](../models/kind.md)        | :heavy_minus_sign:                                | N/A                                               | gpu                                               |
| `plan`                                            | *OptionalNullable[str]*                           | :heavy_minus_sign:                                | The plan slug; null while no plan is set          | g4-b300-large                                     |
| `plan_name`                                       | *OptionalNullable[str]*                           | :heavy_minus_sign:                                | N/A                                               | g4.b300.large                                     |
| `server_count`                                    | *Optional[int]*                                   | :heavy_minus_sign:                                | N/A                                               | 16                                                |
| `os`                                              | *OptionalNullable[str]*                           | :heavy_minus_sign:                                | The operating system slug; null while none is set | ubuntu_24_04_x64_lts                              |