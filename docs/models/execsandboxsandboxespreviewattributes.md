# ExecSandboxSandboxesPreviewAttributes


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `command`                                               | List[*str*]                                             | :heavy_check_mark:                                      | Command and arguments to run                            |
| `environment`                                           | Dict[str, *str*]                                        | :heavy_minus_sign:                                      | Environment variables set for the command               |
| `workdir`                                               | *Optional[str]*                                         | :heavy_minus_sign:                                      | Working directory for the command                       |
| `timeout_seconds`                                       | *Optional[int]*                                         | :heavy_minus_sign:                                      | Maximum run time of the command. Defaults to 30 seconds |