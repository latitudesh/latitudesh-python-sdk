# IpAddresses

## Overview

### Available Operations

* [list](#list) - List IPs
* [get](#get) - Retrieve an IP

## list

List all Management and Additional IP Addresses.
 • Management IPs are IPs that are used for the management IP of a device.
   This is a public IP address that a device is born and dies with. It never changes during the lifecycle of the device.
 • Additional IPs are individual IPs that can be added to a device as an additional IP that can be used.


### Example Usage: Success

<!-- UsageSnippet language="python" operationID="get-ips" method="get" path="/ips" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.ip_addresses.list(page_size=20, page_number=1)

    while res is not None:
        # Handle items

        res = res.next()

```
### Example Usage: when a project ID filter is provided 

<!-- UsageSnippet language="python" operationID="get-ips" method="get" path="/ips" example="when a project ID filter is provided " -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.ip_addresses.list(filter_project="59", page_size=20, page_number=1)

    while res is not None:
        # Handle items

        res = res.next()

```
### Example Usage: when filtering by a server that does not have assigned IPs

<!-- UsageSnippet language="python" operationID="get-ips" method="get" path="/ips" example="when filtering by a server that does not have assigned IPs" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.ip_addresses.list(filter_server="sv_LMmAD8pEDwop2", page_size=20, page_number=1)

    while res is not None:
        # Handle items

        res = res.next()

```
### Example Usage: when filtering by a server that has assigned IPs

<!-- UsageSnippet language="python" operationID="get-ips" method="get" path="/ips" example="when filtering by a server that has assigned IPs" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.ip_addresses.list(filter_server="46", page_size=20, page_number=1)

    while res is not None:
        # Handle items

        res = res.next()

```
### Example Usage: when there are no IPs matching the project filter

<!-- UsageSnippet language="python" operationID="get-ips" method="get" path="/ips" example="when there are no IPs matching the project filter" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.ip_addresses.list(filter_project="63", page_size=20, page_number=1)

    while res is not None:
        # Handle items

        res = res.next()

```
### Example Usage: without filters

<!-- UsageSnippet language="python" operationID="get-ips" method="get" path="/ips" example="without filters" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.ip_addresses.list(page_size=20, page_number=1)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                | Type                                                                                                                                                                     | Required                                                                                                                                                                 | Description                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `filter_server`                                                                                                                                                          | *Optional[str]*                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                       | The server ID to filter by                                                                                                                                               |
| `filter_project`                                                                                                                                                         | *Optional[str]*                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                       | The project ID or Slug to filter by                                                                                                                                      |
| `filter_family`                                                                                                                                                          | [Optional[models.FilterFamily]](../../models/filterfamily.md)                                                                                                            | :heavy_minus_sign:                                                                                                                                                       | The protocol family to filter by                                                                                                                                         |
| `filter_type`                                                                                                                                                            | [Optional[models.FilterType]](../../models/filtertype.md)                                                                                                                | :heavy_minus_sign:                                                                                                                                                       | The protocol type to filter by                                                                                                                                           |
| `filter_location`                                                                                                                                                        | *Optional[str]*                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                       | The site slug to filter by                                                                                                                                               |
| `filter_address`                                                                                                                                                         | *Optional[str]*                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                       | The address of IP to filter by starts_with                                                                                                                               |
| `filter_additional`                                                                                                                                                      | *Optional[bool]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                       | Filter by additional IPs (true) or management IPs (false)                                                                                                                |
| `extra_fields_ip_addresses`                                                                                                                                              | *Optional[str]*                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                       | The `region` and `server` are provided as extra attributes that are lazy loaded. To request it, just set `extra_fields[ip_addresses]=region,server` in the query string. |
| `page_size`                                                                                                                                                              | *Optional[int]*                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                       | Number of items to return per page                                                                                                                                       |
| `page_number`                                                                                                                                                            | *Optional[int]*                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                       | Page number to return (starts at 1)                                                                                                                                      |
| `retries`                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                         | :heavy_minus_sign:                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                      |

### Response

**[models.GetIpsResponse](../../models/getipsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get

Retrieve an IP Address

### Example Usage

<!-- UsageSnippet language="python" operationID="get-ip" method="get" path="/ips/{ip_id}" example="when basic GET" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.ip_addresses.get(ip_id="ip_059EqY7kOQj8p")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                | Type                                                                                                                                                                     | Required                                                                                                                                                                 | Description                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `ip_id`                                                                                                                                                                  | *str*                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                       | The IP Address ID                                                                                                                                                        |
| `extra_fields_ip_addresses`                                                                                                                                              | *Optional[str]*                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                       | The `region` and `server` are provided as extra attributes that are lazy loaded. To request it, just set `extra_fields[ip_addresses]=region,server` in the query string. |
| `retries`                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                         | :heavy_minus_sign:                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                      |

### Response

**[models.IPAddress](../../models/ipaddress.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |