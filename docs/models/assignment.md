# Assignment

Server assignment information. Returns an empty object when the IP is not assigned to an active server (e.g., when the server is decommissioning or deleted). The hostname is null when the assigned server has no hostname set.


## Fields

| Field                   | Type                    | Required                | Description             |
| ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| `server_id`             | *Optional[str]*         | :heavy_minus_sign:      | N/A                     |
| `hostname`              | *OptionalNullable[str]* | :heavy_minus_sign:      | N/A                     |
| `assigned_at`           | *OptionalNullable[str]* | :heavy_minus_sign:      | N/A                     |