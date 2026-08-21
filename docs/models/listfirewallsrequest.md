# ListFirewallsRequest


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `filter_project`                                                         | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | N/A                                                                      |
| `filter_tags`                                                            | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | Comma-separated tag IDs. Returns firewalls that have all the given tags. |
| `page_size`                                                              | *Optional[int]*                                                          | :heavy_minus_sign:                                                       | Number of items to return per page                                       |
| `page_number`                                                            | *Optional[int]*                                                          | :heavy_minus_sign:                                                       | Page number to return (starts at 1)                                      |