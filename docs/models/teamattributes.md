# TeamAttributes


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `name`                                                     | *Optional[str]*                                            | :heavy_minus_sign:                                         | N/A                                                        |
| `slug`                                                     | *Optional[str]*                                            | :heavy_minus_sign:                                         | N/A                                                        |
| `description`                                              | *Optional[str]*                                            | :heavy_minus_sign:                                         | N/A                                                        |
| `address`                                                  | *Optional[str]*                                            | :heavy_minus_sign:                                         | N/A                                                        |
| `currency`                                                 | *Optional[str]*                                            | :heavy_minus_sign:                                         | N/A                                                        |
| `created_at`                                               | *Optional[str]*                                            | :heavy_minus_sign:                                         | N/A                                                        |
| `updated_at`                                               | *Optional[str]*                                            | :heavy_minus_sign:                                         | N/A                                                        |
| `enforce_mfa`                                              | *Optional[bool]*                                           | :heavy_minus_sign:                                         | N/A                                                        |
| `users`                                                    | List[[models.UserInclude](../models/userinclude.md)]       | :heavy_minus_sign:                                         | N/A                                                        |
| `projects`                                                 | List[[models.ProjectInclude](../models/projectinclude.md)] | :heavy_minus_sign:                                         | N/A                                                        |
| `owner`                                                    | [Optional[models.UserInclude]](../models/userinclude.md)   | :heavy_minus_sign:                                         | N/A                                                        |
| `billing`                                                  | [Optional[models.TeamBilling]](../models/teambilling.md)   | :heavy_minus_sign:                                         | N/A                                                        |
| `feature_flags`                                            | List[*str*]                                                | :heavy_minus_sign:                                         | N/A                                                        |