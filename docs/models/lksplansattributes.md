# LksPlansAttributes


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `name`                                                       | *Optional[str]*                                              | :heavy_minus_sign:                                           | The name of the plan                                         |
| `slug`                                                       | *Optional[str]*                                              | :heavy_minus_sign:                                           | The slug of the plan, used as the node pool plan             |
| `specs`                                                      | [Optional[models.LksPlansSpecs]](../models/lksplansspecs.md) | :heavy_minus_sign:                                           | N/A                                                          |
| `regions`                                                    | List[[models.LksPlansRegions](../models/lksplansregions.md)] | :heavy_minus_sign:                                           | N/A                                                          |