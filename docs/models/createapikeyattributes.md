# CreateAPIKeyAttributes


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `name`                                                                             | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | Name of the API Key                                                                |
| `read_only`                                                                        | *Optional[bool]*                                                                   | :heavy_minus_sign:                                                                 | Whether the API Key is read-only. Read-only keys can only perform GET requests.    |
| `allowed_ips`                                                                      | List[*str*]                                                                        | :heavy_minus_sign:                                                                 | List of allowed IP addresses or CIDR ranges (e.g., "192.168.1.100", "10.0.0.0/24") |