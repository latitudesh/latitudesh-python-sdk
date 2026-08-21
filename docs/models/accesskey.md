# AccessKey

The newly created access key. The secret is included only in this create response and cannot be retrieved again. Field names depend on the provider: `standard` (Wasabi) returns `access_key_id` and `secret_access_key`; `high_performance` (VAST) returns `access_key` and `secret_key`.


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `access_key_id`                                            | *Optional[str]*                                            | :heavy_minus_sign:                                         | Access key ID (standard / Wasabi).                         |
| `secret_access_key`                                        | *Optional[str]*                                            | :heavy_minus_sign:                                         | Secret access key (standard / Wasabi). Returned only once. |
| `access_key`                                               | *Optional[str]*                                            | :heavy_minus_sign:                                         | Access key ID (high_performance / VAST).                   |
| `secret_key`                                               | *Optional[str]*                                            | :heavy_minus_sign:                                         | Secret key (high_performance / VAST). Returned only once.  |
| `name`                                                     | *Optional[str]*                                            | :heavy_minus_sign:                                         | Access key name.                                           |
| `status`                                                   | *Optional[str]*                                            | :heavy_minus_sign:                                         | Access key status (e.g., `Active`).                        |
| `username`                                                 | *Optional[str]*                                            | :heavy_minus_sign:                                         | Underlying IAM user the key belongs to.                    |