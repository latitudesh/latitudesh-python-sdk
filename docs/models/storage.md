# Storage

Storage consumption metrics


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `consumed`                                                                               | *Optional[int]*                                                                          | :heavy_minus_sign:                                                                       | Billed storage usage for the current period                                              |
| `current`                                                                                | *Optional[int]*                                                                          | :heavy_minus_sign:                                                                       | Latest recorded storage usage (last datapoint)                                           |
| `unit`                                                                                   | [Optional[models.GetStorageBucketMetricsUnit]](../models/getstoragebucketmetricsunit.md) | :heavy_minus_sign:                                                                       | Unit of measurement for storage                                                          |