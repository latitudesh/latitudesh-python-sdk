# ElasticIPDataServer

The server this Elastic IP is assigned to. Returns null when the Elastic IP is not assigned to a server or when the assigned server is not active (e.g., decommissioning or deleted).


## Fields

| Field                   | Type                    | Required                | Description             |
| ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| `id`                    | *Optional[str]*         | :heavy_minus_sign:      | N/A                     |
| `hostname`              | *Optional[str]*         | :heavy_minus_sign:      | N/A                     |
| `primary_ipv4`          | *Optional[str]*         | :heavy_minus_sign:      | N/A                     |
| `operating_system`      | *OptionalNullable[str]* | :heavy_minus_sign:      | N/A                     |