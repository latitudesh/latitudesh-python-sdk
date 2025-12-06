# Roles

## Overview

### Available Operations

* [list](#list) - List all Roles
* [get](#get) - Retrieve Role

## list

Returns a list of all roles that can be assigned to users


### Example Usage

<!-- UsageSnippet language="python" operationID="get-roles" method="get" path="/roles" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.roles.list(page_size=20, page_number=1)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Number of items to return per page                                  |
| `page_number`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Page number to return (starts at 1)                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetRolesResponse](../../models/getrolesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get

Retrieve Role

### Example Usage

<!-- UsageSnippet language="python" operationID="get-role-id" method="get" path="/roles/{role_id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.roles.get(role_id="role_LMmAD8vldwop2")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `role_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Role](../../models/role.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |