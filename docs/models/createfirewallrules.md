# CreateFirewallRules


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `from_`                                                                        | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | N/A                                                                            |
| `to`                                                                           | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | N/A                                                                            |
| `protocol`                                                                     | [Optional[models.CreateFirewallProtocol]](../models/createfirewallprotocol.md) | :heavy_minus_sign:                                                             | N/A                                                                            |
| `port`                                                                         | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | Port number or range (e.g., "80", "80-443")                                    |