# ServerDataPublicNetwork

**Preview.** Available to teams with public networks enabled. The public network this server is attached onto, or null. Fetch full details from GET /public_networks/{id}.


## Fields

| Field                   | Type                    | Required                | Description             | Example                 |
| ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| `id`                    | *Optional[str]*         | :heavy_minus_sign:      | N/A                     | pn_2aBcDeFgH            |
| `ipv4`                  | *OptionalNullable[str]* | :heavy_minus_sign:      | N/A                     | 10.90.0.0/26            |
| `ipv6`                  | *OptionalNullable[str]* | :heavy_minus_sign:      | N/A                     | 2001:db8::/64           |