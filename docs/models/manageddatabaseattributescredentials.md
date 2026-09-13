# ManagedDatabaseAttributesCredentials


## Fields

| Field                      | Type                       | Required                   | Description                |
| -------------------------- | -------------------------- | -------------------------- | -------------------------- |
| `host`                     | *Optional[str]*            | :heavy_minus_sign:         | N/A                        |
| `http_port`                | *OptionalNullable[int]*    | :heavy_minus_sign:         | N/A                        |
| `tcp_port`                 | *OptionalNullable[int]*    | :heavy_minus_sign:         | N/A                        |
| `port`                     | *OptionalNullable[int]*    | :heavy_minus_sign:         | Postgres NodePort          |
| `database`                 | *OptionalNullable[str]*    | :heavy_minus_sign:         | N/A                        |
| `url`                      | *OptionalNullable[str]*    | :heavy_minus_sign:         | Postgres connection string |
| `username`                 | *Optional[str]*            | :heavy_minus_sign:         | N/A                        |
| `password`                 | *OptionalNullable[str]*    | :heavy_minus_sign:         | N/A                        |