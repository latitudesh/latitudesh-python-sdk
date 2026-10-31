# SandboxesPreview

## Overview

Preview. Available to teams with the `sandboxes_api` feature flag. The shape of these endpoints may change before general availability.

### Available Operations

* [get_sandboxes](#get_sandboxes) - List sandboxes
* [create_sandbox](#create_sandbox) - Create sandbox
* [get_sandbox](#get_sandbox) - Retrieve sandbox
* [destroy_sandbox](#destroy_sandbox) - Delete sandbox
* [exec_sandbox](#exec_sandbox) - Run a command in a sandbox

## get_sandboxes

**Preview.** Available to teams with the `sandboxes_api` feature flag. The shape of this
endpoint may change before general availability.

List the sandboxes of a project, up to 100 per page.


### Example Usage

<!-- UsageSnippet language="python" operationID="get-sandboxes" method="get" path="/sandboxes" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.sandboxes_preview.get_sandboxes(project_id="proj_6059EqYkOQj8p")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the project whose sandboxes are listed                        |
| `page_token`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Token returned in `meta.next_page_token` by the previous page       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Sandboxes](../../models/sandboxes.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_sandbox

**Preview.** Available to teams with the `sandboxes_api` feature flag. The shape of this
endpoint may change before general availability.

Create a sandbox in a project.


### Example Usage

<!-- UsageSnippet language="python" operationID="create-sandbox" method="post" path="/sandboxes" example="Created" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.sandboxes_preview.create_sandbox(data={
        "type": latitudesh_python_sdk.CreateSandboxSandboxesPreviewType.SANDBOXES,
        "attributes": {
            "project_id": "proj_6059EqYkOQj8p",
            "name": "sbx-demo",
            "image": "python:3.12",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `data`                                                                                                  | [Optional[models.CreateSandboxSandboxesPreviewData]](../../models/createsandboxsandboxespreviewdata.md) | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[models.Sandbox](../../models/sandbox.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_sandbox

**Preview.** Available to teams with the `sandboxes_api` feature flag.

Retrieve a single sandbox.


### Example Usage

<!-- UsageSnippet language="python" operationID="get-sandbox" method="get" path="/sandboxes/{sandbox_id}" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.sandboxes_preview.get_sandbox(sandbox_id="sbx-demo")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `sandbox_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Sandbox name                                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Sandbox](../../models/sandbox.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## destroy_sandbox

**Preview.** Available to teams with the `sandboxes_api` feature flag.

Delete a sandbox. Deletion completes in the background.


### Example Usage

<!-- UsageSnippet language="python" operationID="destroy-sandbox" method="delete" path="/sandboxes/{sandbox_id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    latitudesh.sandboxes_preview.destroy_sandbox(sandbox_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `sandbox_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Sandbox name                                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## exec_sandbox

**Preview.** Available to teams with the `sandboxes_api` feature flag. The shape of this
endpoint may change before general availability.

Run a command in a sandbox and wait for its output.


### Example Usage

<!-- UsageSnippet language="python" operationID="exec-sandbox" method="post" path="/sandboxes/{sandbox_id}/exec" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.sandboxes_preview.exec_sandbox(sandbox_id="sbx-demo", data={
        "attributes": {
            "command": [
                "python",
                "-V",
            ],
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `sandbox_id`                                                                                        | *str*                                                                                               | :heavy_check_mark:                                                                                  | Sandbox name                                                                                        |
| `data`                                                                                              | [Optional[models.ExecSandboxSandboxesPreviewData]](../../models/execsandboxsandboxespreviewdata.md) | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[models.SandboxExec](../../models/sandboxexec.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |