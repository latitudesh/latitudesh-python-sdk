# Block

NVMe-TCP block mapping of a high performance volume. Null for volumes that are not mapped to a server.


## Fields

| Field                                     | Type                                      | Required                                  | Description                               |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `nqn`                                     | *OptionalNullable[str]*                   | :heavy_minus_sign:                        | NVMe Qualified Name of the mapped server. |
| `nsid`                                    | *OptionalNullable[int]*                   | :heavy_minus_sign:                        | NVMe namespace ID of the mapping.         |
| `server_id`                               | *OptionalNullable[str]*                   | :heavy_minus_sign:                        | ID of the server the volume is mapped to. |