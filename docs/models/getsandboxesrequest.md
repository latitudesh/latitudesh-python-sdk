# GetSandboxesRequest


## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `project_id`                                                  | *str*                                                         | :heavy_check_mark:                                            | ID of the project whose sandboxes are listed                  |
| `page_token`                                                  | *Optional[str]*                                               | :heavy_minus_sign:                                            | Token returned in `meta.next_page_token` by the previous page |