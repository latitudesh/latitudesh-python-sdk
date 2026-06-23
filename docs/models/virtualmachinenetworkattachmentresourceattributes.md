# VirtualMachineNetworkAttachmentResourceAttributes


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `virtual_network_id`                                        | *Optional[str]*                                             | :heavy_minus_sign:                                          | The encoded VLAN id_hash                                    |
| `vid`                                                       | *Optional[int]*                                             | :heavy_minus_sign:                                          | The 802.1Q VLAN ID                                          |
| `pending_restart`                                           | *Optional[bool]*                                            | :heavy_minus_sign:                                          | True if the attachment requires a VM restart to take effect |