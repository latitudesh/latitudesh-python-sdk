# Inference

## Overview

### Available Operations

* [get_inference_models](#get_inference_models) - List available inference models
* [get_inference_api_keys](#get_inference_api_keys) - List inference API keys
* [post_inference_api_key](#post_inference_api_key) - Create an inference API key
* [delete_inference_api_key](#delete_inference_api_key) - Revoke an inference API key
* [get_inference_usage](#get_inference_usage) - Get inference usage for a project

## get_inference_models

Lists the inference models available through the inference gateway. The id is the canonical model ID — send it verbatim as the "model" value in inference requests. Only enabled models are returned; availability is global unless a model is explicitly scoped by region.


### Example Usage

<!-- UsageSnippet language="python" operationID="get-inference-models" method="get" path="/inference/models" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.inference.get_inference_models(project_id="proj_AoW6vRnwkvLn0")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Project ID or Slug                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.InferenceModels](../../models/inferencemodels.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 401, 404                 | application/vnd.api+json |
| models.ErrorObject       | 503                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## get_inference_api_keys

Lists the project's active inference API keys. The full token is never returned here — only its last characters.


### Example Usage

<!-- UsageSnippet language="python" operationID="get-inference-api-keys" method="get" path="/inference/api_keys" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.inference.get_inference_api_keys(project_id="proj_AoW6vRnwkvLn0")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Project ID or Slug                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.InferenceAPIKeys](../../models/inferenceapikeys.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 401, 404                 | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## post_inference_api_key

Creates an inference API key for the project. The full token is returned ONLY in this response — store it securely.
All active keys for the project can authenticate at the inference control plane. Synchronization is asynchronous: sync_status confirms that the refresh receiver observed the key; it does not acknowledge every region.


### Example Usage

<!-- UsageSnippet language="python" operationID="post-inference-api-key" method="post" path="/inference/api_keys" example="Created" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.inference.post_inference_api_key(data={
        "type": latitudesh_python_sdk.CreateInferenceAPIKeyType.INFERENCE_API_KEYS,
        "attributes": {
            "project_id": "proj_AoW6vRnwkvLn0",
            "name": "Production inference key",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `data`                                                                        | [models.CreateInferenceAPIKeyData](../../models/createinferenceapikeydata.md) | :heavy_check_mark:                                                            | N/A                                                                           |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.PostInferenceAPIKeyResponseBody](../../models/postinferenceapikeyresponsebody.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 404, 422                 | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## delete_inference_api_key

Revokes the inference API key and immediately removes it from active listings while retaining its audit record.
Control-plane removal is asynchronous. Other active keys remain valid. The key stops authorizing new requests after the control plane refreshes or its identity snapshot expires. Revoking an already revoked key succeeds.


### Example Usage

<!-- UsageSnippet language="python" operationID="delete-inference-api-key" method="delete" path="/inference/api_keys/{api_key_id}" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.inference.delete_inference_api_key(project_id="proj_AoW6vRnwkvLn0", api_key_id="aitok_6VE1Wd37dXnZJ")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Project ID or Slug                                                  |
| `api_key_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Inference API key ID                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteInferenceAPIKeyResponseBody](../../models/deleteinferenceapikeyresponsebody.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 404                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## get_inference_usage

Returns the project's inference requests, tokens and estimated cost for the window, per model and as a time series. The estimate uses current model prices.


### Example Usage

<!-- UsageSnippet language="python" operationID="get-inference-usage" method="get" path="/inference/usage" example="Success" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
from latitudesh_python_sdk.utils import parse_datetime
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.inference.get_inference_usage(project_id="proj_AoW6vRnwkvLn0", from_=parse_datetime("2026-10-01T00:00:00Z"), to=parse_datetime("2026-10-02T00:00:00Z"), granularity=latitudesh_python_sdk.Granularity.SIXH)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `project_id`                                                                          | *str*                                                                                 | :heavy_check_mark:                                                                    | Project ID or Slug                                                                    |
| `from_`                                                                               | [date](https://docs.python.org/3/library/datetime.html#date-objects)                  | :heavy_check_mark:                                                                    | Start of the window (inclusive), truncated to whole seconds                           |
| `to`                                                                                  | [date](https://docs.python.org/3/library/datetime.html#date-objects)                  | :heavy_check_mark:                                                                    | End of the window (exclusive), truncated to whole seconds; at most 31 days after from |
| `granularity`                                                                         | [models.Granularity](../../models/granularity.md)                                     | :heavy_check_mark:                                                                    | Size of each series bucket                                                            |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.InferenceUsage](../../models/inferenceusage.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 404, 422            | application/vnd.api+json |
| models.ErrorObject       | 503                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |