# GetStorageAccessKeysData

Access keys grouped by storage class.


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `standard`                                                   | List[[models.Standard](../models/standard.md)]               | :heavy_minus_sign:                                           | Wasabi (standard) access keys.                               |
| `high_performance`                                           | List[[models.HighPerformance](../models/highperformance.md)] | :heavy_minus_sign:                                           | VAST (high_performance) access keys, across all regions.     |