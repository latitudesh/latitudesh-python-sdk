# StorageNetwork

Storage network to configure on the server before mounting the filesystem. Null until the status is "attached".


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `vid`                                                      | *OptionalNullable[int]*                                    | :heavy_minus_sign:                                         | VLAN ID of the storage VLAN.                               |
| `host_cidr`                                                | *Optional[str]*                                            | :heavy_minus_sign:                                         | Storage IP of the server, in CIDR notation.                |
| `gateway`                                                  | *OptionalNullable[str]*                                    | :heavy_minus_sign:                                         | Gateway of the storage network, used for the routes below. |
| `routes`                                                   | List[*str*]                                                | :heavy_minus_sign:                                         | Storage infrastructure prefixes to route via the gateway.  |