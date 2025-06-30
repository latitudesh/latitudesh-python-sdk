# APIKeys
(*api_keys*)

## Overview

### Available Operations

* [list](#list) - List API Keys
* [create](#create) - Create API Key
* [regenerate](#regenerate) - Regenerate API Key
* [delete](#delete) - Delete API Key

## list

Returns a list of all API keys from the team members


### Example Usage

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

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 400, 422                 | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## regenerate

Regenerate an existing API Key that is tied to the current user. This overrides the previous key.


### Example Usage

```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.api_keys.regenerate(api_key_id="tok_pRMLydp0dQKr1", data={
        "id": "tok_pRMLydp0dQKr1",
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

**[models.UpdateAPIKeyResponseBody](../../models/updateapikeyresponsebody.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 400, 404                 | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## delete

Delete an existing API Key. Once deleted, the API Key can no longer be used to access the API.


### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.api_keys.delete(api_key_id="tok_xkjQwdENqYNVP")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `api_key_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 404                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |