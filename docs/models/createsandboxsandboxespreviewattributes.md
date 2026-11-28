# CreateSandboxSandboxesPreviewAttributes


## Fields

| Field                                                                       | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `project_id`                                                                | *str*                                                                       | :heavy_check_mark:                                                          | ID of the project that owns the sandbox                                     |
| `name`                                                                      | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | Name of the sandbox. Generated when omitted                                 |
| `image`                                                                     | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | Container image to run. Defaults to the Latitude sandbox image when omitted |
| `environment`                                                               | Dict[str, *str*]                                                            | :heavy_minus_sign:                                                          | Environment variables set in the sandbox                                    |