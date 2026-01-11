# ApiKeys

## Overview

### Available Operations

* [list](#list) - List API keys
* [create](#create) - Create API key
* [regenerate](#regenerate) - Rotate API key
* [delete](#delete) - Delete API key
* [patch_api_key](#patch_api_key) - Update API key settings

## list

Returns a list of all API keys.


### Example Usage

<!-- UsageSnippet language="python" operationID="get-api-keys" method="get" path="/auth/api_keys" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.api_keys.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.APIKey](../../models/apikey.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create

Create a new API Key that is tied to the current user account. The created API key is only listed ONCE upon creation. It can however be regenerated or deleted.


### Example Usage

<!-- UsageSnippet language="python" operationID="post-api-key" method="post" path="/auth/api_keys" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.api_keys.create(data={
        "type": latitudesh_python_sdk.CreateAPIKeyType.API_KEYS,
        "attributes": {
            "name": "App Token",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `data`                                                              | [Optional[models.Data]](../../models/data.md)                       | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PostAPIKeyResponseBody](../../models/postapikeyresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## regenerate

Rotate (regenerate) an API key's token and optionally update its settings. This generates a new token and invalidates the previous one. To update settings without rotating the token, use the PATCH endpoint instead.


### Example Usage

<!-- UsageSnippet language="python" operationID="update-api-key" method="put" path="/auth/api_keys/{api_key_id}" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.api_keys.regenerate(api_key_id="tok_zlkg1DegdvZE5", data={
        "id": "tok_zlkg1DegdvZE5",
        "type": latitudesh_python_sdk.UpdateAPIKeyType.API_KEYS,
        "attributes": {
            "name": "App Token",
        },
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `api_key_id`                                                          | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `data`                                                                | [Optional[models.UpdateAPIKeyData]](../../models/updateapikeydata.md) | :heavy_minus_sign:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete

Delete an existing API Key. Once deleted, the API Key can no longer be used to access the API.


### Example Usage

<!-- UsageSnippet language="python" operationID="delete-api-key" method="delete" path="/auth/api_keys/{api_key_id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.api_keys.delete(api_key_id="tok_x1ZJrdx5qg4LV")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `api_key_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## patch_api_key

Update an API key's settings (name, read_only, allowed_ips) without regenerating the token. To rotate the token, use the PUT endpoint instead.


### Example Usage

<!-- UsageSnippet language="python" operationID="patch-api-key" method="patch" path="/auth/api_keys/{api_key_id}" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.api_keys.patch_api_key(api_key_id="tok_zlkg1DegdvZE5", data={
        "id": "tok_zlkg1DegdvZE5",
        "type": latitudesh_python_sdk.UpdateAPIKeyType.API_KEYS,
        "attributes": {
            "name": "Updated Token Name",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `api_key_id`                                                          | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `data`                                                                | [Optional[models.UpdateAPIKeyData]](../../models/updateapikeydata.md) | :heavy_minus_sign:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.PatchAPIKeyResponseBody](../../models/patchapikeyresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |