# VirtualMachineAttributesFeatures

Features supported by this operating system


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `raid`                                                              | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Whether RAID is supported                                           |
| `ssh_keys`                                                          | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Whether SSH keys are supported                                      |
| `user_data`                                                         | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Whether user data is supported                                      |
| `rescue`                                                            | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Whether rescue mode is supported                                    |
| `arm64`                                                             | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Whether the operating system can be deployed on ARM (arm64) servers |
| `workflow`                                                          | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Whether workflow is supported                                       |