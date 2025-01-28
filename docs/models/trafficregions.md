# TrafficRegions


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `region_slug`                                                | *Optional[str]*                                              | :heavy_minus_sign:                                           | N/A                                                          |
| `total_inbound_gb`                                           | *Optional[int]*                                              | :heavy_minus_sign:                                           | Value in GB                                                  |
| `total_outbound_gb`                                          | *Optional[int]*                                              | :heavy_minus_sign:                                           | Value in GB                                                  |
| `total_inbound_95th_percentile_mbps`                         | *Optional[float]*                                            | :heavy_minus_sign:                                           | Value in MBps                                                |
| `total_outbound_95th_percentile_mbps`                        | *Optional[float]*                                            | :heavy_minus_sign:                                           | Value in MBps                                                |
| `data`                                                       | List[[models.TrafficDataData](../models/trafficdatadata.md)] | :heavy_minus_sign:                                           | N/A                                                          |