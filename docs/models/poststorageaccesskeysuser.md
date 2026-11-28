# PostStorageAccessKeysUser

Provider-side IAM user the access key belongs to.


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `user_id`                                                    | *Optional[Any]*                                              | :heavy_minus_sign:                                           | Provider user ID (a string for Wasabi, an integer for VAST). |
| `username`                                                   | *Optional[str]*                                              | :heavy_minus_sign:                                           | Provider user name.                                          |
| `arn`                                                        | *Optional[str]*                                              | :heavy_minus_sign:                                           | Provider user ARN or identifier.                             |