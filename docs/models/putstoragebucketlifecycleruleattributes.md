# PutStorageBucketLifecycleRuleAttributes


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `name`                                                                | *str*                                                                 | :heavy_check_mark:                                                    | Name of the lifecycle rule                                            |
| `enabled`                                                             | *Optional[bool]*                                                      | :heavy_minus_sign:                                                    | Whether the rule is active                                            |
| `prefix`                                                              | *OptionalNullable[str]*                                               | :heavy_minus_sign:                                                    | Object key prefix to filter which objects the rule applies to         |
| `expiration_days`                                                     | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | Number of days after object creation when the object expires          |
| `noncurrent_days`                                                     | *OptionalNullable[int]*                                               | :heavy_minus_sign:                                                    | Number of days after which noncurrent object versions expire          |
| `abort_mpu_days_after_initiation`                                     | *OptionalNullable[int]*                                               | :heavy_minus_sign:                                                    | Number of days after initiation to abort incomplete multipart uploads |