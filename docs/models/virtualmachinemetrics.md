# VirtualMachineMetrics


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `metric`                                                     | [Optional[models.Metric]](../models/metric.md)               | :heavy_minus_sign:                                           | N/A                                                          |
| `range`                                                      | [Optional[models.Range]](../models/range.md)                 | :heavy_minus_sign:                                           | N/A                                                          |
| `step`                                                       | *Optional[str]*                                              | :heavy_minus_sign:                                           | Sampling interval between adjacent points (e.g. "15s", "1m") |
| `unit`                                                       | [Optional[models.Unit]](../models/unit.md)                   | :heavy_minus_sign:                                           | Unit applied to every point value                            |
| `points`                                                     | List[[models.Points](../models/points.md)]                   | :heavy_minus_sign:                                           | N/A                                                          |