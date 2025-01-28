# TrafficAttributes


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `from_date`                                                | *Optional[int]*                                            | :heavy_minus_sign:                                         | The start timestamp. Must be a unix timestamp              |
| `to_date`                                                  | *Optional[int]*                                            | :heavy_minus_sign:                                         | The end timestamp. Must be a unix timestamp                |
| `regions`                                                  | List[[models.TrafficRegions](../models/trafficregions.md)] | :heavy_minus_sign:                                         | N/A                                                        |
| `total_inbound_gb`                                         | *Optional[int]*                                            | :heavy_minus_sign:                                         | Value in GB                                                |
| `total_outbound_gb`                                        | *Optional[int]*                                            | :heavy_minus_sign:                                         | Value in GB                                                |
| `total_inbound_95th_percentile_mbps`                       | *Optional[float]*                                          | :heavy_minus_sign:                                         | Value in MBps                                              |
| `total_outbound_95th_percentile_mbps`                      | *Optional[float]*                                          | :heavy_minus_sign:                                         | Value in MBps                                              |