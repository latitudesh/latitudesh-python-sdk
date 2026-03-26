# ListElasticIpsRequest


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `filter_project`                                           | *Optional[str]*                                            | :heavy_minus_sign:                                         | The project ID or slug to filter by                        |
| `filter_server`                                            | *Optional[str]*                                            | :heavy_minus_sign:                                         | The server ID to filter by                                 |
| `filter_status`                                            | [Optional[models.FilterStatus]](../models/filterstatus.md) | :heavy_minus_sign:                                         | The status to filter by                                    |
| `page_size`                                                | *Optional[int]*                                            | :heavy_minus_sign:                                         | Number of items to return per page                         |
| `page_number`                                              | *Optional[int]*                                            | :heavy_minus_sign:                                         | Page number to return (starts at 1)                        |