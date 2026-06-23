# ShowVirtualMachineMetricsRequest


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `virtual_machine_id`                                             | *str*                                                            | :heavy_check_mark:                                               | N/A                                                              |
| `metric`                                                         | [models.QueryParamMetric](../models/queryparammetric.md)         | :heavy_check_mark:                                               | N/A                                                              |
| `range`                                                          | [Optional[models.QueryParamRange]](../models/queryparamrange.md) | :heavy_minus_sign:                                               | N/A                                                              |
| `force_refresh`                                                  | *Optional[bool]*                                                 | :heavy_minus_sign:                                               | N/A                                                              |