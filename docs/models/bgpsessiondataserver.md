# BgpSessionDataServer

The server announcing the Elastic IP over BGP. Null when the announcer could not be resolved to a server record.


## Fields

| Field                   | Type                    | Required                | Description             |
| ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| `id`                    | *Optional[str]*         | :heavy_minus_sign:      | N/A                     |
| `hostname`              | *Optional[str]*         | :heavy_minus_sign:      | N/A                     |
| `primary_ipv4`          | *OptionalNullable[str]* | :heavy_minus_sign:      | N/A                     |
| `operating_system`      | *OptionalNullable[str]* | :heavy_minus_sign:      | N/A                     |