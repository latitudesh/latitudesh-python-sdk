# PlanDataAttributes


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `slug`                                                         | *Optional[str]*                                                | :heavy_minus_sign:                                             | N/A                                                            |
| `name`                                                         | *Optional[str]*                                                | :heavy_minus_sign:                                             | N/A                                                            |
| `features`                                                     | List[[models.PlanDataFeatures](../models/plandatafeatures.md)] | :heavy_minus_sign:                                             | List of available features for the plan                        |
| `specs`                                                        | [Optional[models.Specs]](../models/specs.md)                   | :heavy_minus_sign:                                             | N/A                                                            |
| `regions`                                                      | List[[models.PlanDataRegions](../models/plandataregions.md)]   | :heavy_minus_sign:                                             | N/A                                                            |