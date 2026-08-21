# CreatePublicNetworkAttributes


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `project_id`                                                                 | *str*                                                                        | :heavy_check_mark:                                                           | The project to create the public network in                                  |
| `site`                                                                       | *str*                                                                        | :heavy_check_mark:                                                           | The site slug the public network is bound to                                 |
| `size`                                                                       | [models.CreatePublicNetworkSize](../models/createpublicnetworksize.md)       | :heavy_check_mark:                                                           | IPv4 prefix length. Determines how many servers the public network can host. |