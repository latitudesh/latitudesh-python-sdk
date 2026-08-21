# GetStorageUsageRequest


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `filter_project`                                                             | *str*                                                                        | :heavy_check_mark:                                                           | Project ID or Slug                                                           |
| `filter_storage_id`                                                          | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | Restrict the result to a single storage. Accepts the storage/bucket ID       |
| `filter_start_date`                                                          | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_minus_sign:                                                           | Defaults to yesterday                                                        |
| `filter_end_date`                                                            | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_minus_sign:                                                           | Defaults to today; clamped to today when a future date is given              |