# ApiKeys

## Overview

### Available Operations

* [list](#list) - List API keys
* [create](#create) - Create API key
* [regenerate](#regenerate) - Rotate API key
* [delete](#delete) - Delete API key
* [update_api_key](#update_api_key) - Update API key settings

## list

Returns a list of all API keys.


### Example Usage

<!-- UsageSnippet language="python" operationID="get-api-keys" method="get" path="/auth/api_keys" example="Success" -->
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

**[models.APIKeys](../../models/apikeys.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create

Create a new API Key that is tied to the current user account. The created API key is only listed ONCE upon creation. It can however be regenerated or deleted.


### Example Usage: API Key Created

<!-- UsageSnippet language="python" operationID="post-api-key" method="post" path="/auth/api_keys" example="API Key Created" -->
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
### Example Usage: Bad Request

<!-- UsageSnippet language="python" operationID="post-api-key" method="post" path="/auth/api_keys" example="Bad Request" -->
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
            "name": "foobar",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Created

<!-- UsageSnippet language="python" operationID="post-api-key" method="post" path="/auth/api_keys" example="Created" -->
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
### Example Usage: Unprocessable Entity

<!-- UsageSnippet language="python" operationID="post-api-key" method="post" path="/auth/api_keys" example="Unprocessable Entity" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.api_keys.create(data={
        "type": latitudesh_python_sdk.CreateAPIKeyType.API_KEYS,
        "attributes": {},
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

Rotate an existing API Key, generating a new token. This invalidates the previous key.
Use PATCH to update settings without rotating the token.


### Example Usage

<!-- UsageSnippet language="python" operationID="rotate-api-key" method="put" path="/auth/api_keys/{api_key_id}" example="Success" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.api_keys.regenerate(api_key_id="tok_x1ZJrdx5qg4LV", data={
        "id": "tok_x1ZJrdx5qg4LV",
        "type": latitudesh_python_sdk.UpdateAPIKeyType.API_KEYS,
        "attributes": {
            "name": "App Token",
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

**[models.RotateAPIKeyResponseBody](../../models/rotateapikeyresponsebody.md)**

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

    latitudesh.api_keys.delete(api_key_id="tok_lQraYDPeOpjwW")

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

## update_api_key

Update API Key settings (name, read_only, allowed_ips) without rotating the token.
Use PUT to rotate the token.


### Example Usage: API Key Not Found

<!-- UsageSnippet language="python" operationID="update-api-key" method="patch" path="/auth/api_keys/{api_key_id}" example="API Key Not Found" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.api_keys.update_api_key(api_key_id="invalid-api-key", data={
        "id": "invalid-api-key",
        "type": latitudesh_python_sdk.UpdateAPIKeyType.API_KEYS,
        "attributes": {
            "name": "App Token",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: API Key Updated

<!-- UsageSnippet language="python" operationID="update-api-key" method="patch" path="/auth/api_keys/{api_key_id}" example="API Key Updated" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.api_keys.update_api_key(api_key_id="tok_pRMLydp0dQKr1", data={
        "id": "tok_pRMLydp0dQKr1",
        "type": latitudesh_python_sdk.UpdateAPIKeyType.API_KEYS,
        "attributes": {
            "name": "App Token",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Bad Request

<!-- UsageSnippet language="python" operationID="update-api-key" method="patch" path="/auth/api_keys/{api_key_id}" example="Bad Request" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.api_keys.update_api_key(api_key_id="tok_w5AEmq7XDBkWX", data={
        "id": "tok_w5AEmq7XDBkWX",
        "type": latitudesh_python_sdk.UpdateAPIKeyType.API_KEYS,
        "attributes": {
            "name": "Name of the API Key",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Success

<!-- UsageSnippet language="python" operationID="update-api-key" method="patch" path="/auth/api_keys/{api_key_id}" example="Success" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.api_keys.update_api_key(api_key_id="tok_zlkg1DegdvZE5", data={
        "id": "tok_zlkg1DegdvZE5",
        "type": latitudesh_python_sdk.UpdateAPIKeyType.API_KEYS,
        "attributes": {
            "name": "App Token",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Success - Update name without rotating token

<!-- UsageSnippet language="python" operationID="update-api-key" method="patch" path="/auth/api_keys/{api_key_id}" example="Success - Update name without rotating token" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.api_keys.update_api_key(api_key_id="tok_lpbV0DgRq4AWz", data={
        "id": "tok_lpbV0DgRq4AWz",
        "type": latitudesh_python_sdk.UpdateAPIKeyType.API_KEYS,
        "attributes": {
            "name": "Updated Name",
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

**[models.UpdateAPIKeyResponseBody](../../models/updateapikeyresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |