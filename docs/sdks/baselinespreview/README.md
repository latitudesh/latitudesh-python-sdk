# BaselinesPreview

## Overview

Preview. Available to teams with the `baselines_api` feature flag. The shape of these endpoints may change before general availability.

### Available Operations

* [get_baselines](#get_baselines) - List baselines
* [create_baseline](#create_baseline) - Create baseline
* [get_baseline](#get_baseline) - Retrieve baseline
* [destroy_baseline](#destroy_baseline) - Delete baseline

## get_baselines

**Preview.** Available to teams with the `baselines_api` feature flag. The shape of this
endpoint may change before general availability.

List all baselines in the team. A baseline records the configuration you expect your
servers to be delivered with — plan, SSH keys, user data, disk layout and BIOS settings.


### Example Usage

<!-- UsageSnippet language="python" operationID="get-baselines" method="get" path="/baselines" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.baselines_preview.get_baselines()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Baselines](../../models/baselines.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_baseline

**Preview.** Available to teams with the `baselines_api` feature flag.

Create a baseline in the team. A baseline can target all servers, a custom set (when the
plan is not yet known), or one or more specific platforms. When it targets platforms, the
disk layout is validated by the same rules a deploy applies — against the smallest of the
selected platforms — so a baseline that saves here can be dispatched verbatim.


### Example Usage

<!-- UsageSnippet language="python" operationID="create-baseline" method="post" path="/baselines" example="Created" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.baselines_preview.create_baseline(data={
        "type": latitudesh_python_sdk.CreateBaselineBaselinesPreviewType.BASELINES,
        "attributes": {
            "name": "web-fleet-v3",
            "description": "Standard build for the public web tier",
            "target_type": latitudesh_python_sdk.CreateBaselineBaselinesPreviewTargetType.PLATFORMS,
            "operating_system": "ubuntu_22_04_x64_lts",
            "platforms": [
                "g3-l40s-small-76",
            ],
            "ssh_key_ids": [
                "ssh_RLYV8DZ2D5QoE",
            ],
            "user_data_id": "ud_r0MK4O4kDa95w",
            "disk_layout": [
                {
                    "role": latitudesh_python_sdk.BaselineDiskLayoutGroupRole.OS,
                    "count": 2,
                    "raid_level": latitudesh_python_sdk.RaidLevel.RAID_1,
                },
                {
                    "role": latitudesh_python_sdk.BaselineDiskLayoutGroupRole.STORAGE,
                    "count": 2,
                    "filesystem": latitudesh_python_sdk.Filesystem.EXT4,
                    "mount_point": "/data",
                },
            ],
            "bios": {},
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `data`                                                                                                    | [Optional[models.CreateBaselineBaselinesPreviewData]](../../models/createbaselinebaselinespreviewdata.md) | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[models.Baseline](../../models/baseline.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_baseline

**Preview.** Available to teams with the `baselines_api` feature flag.

Retrieve a single baseline.


### Example Usage

<!-- UsageSnippet language="python" operationID="get-baseline" method="get" path="/baselines/{baseline_id}" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.baselines_preview.get_baseline(baseline_id="bl_6059EqYkOQj8p")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `baseline_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Baseline ID                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Baseline](../../models/baseline.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## destroy_baseline

**Preview.** Available to teams with the `baselines_api` feature flag.

Delete a baseline.


### Example Usage

<!-- UsageSnippet language="python" operationID="destroy-baseline" method="delete" path="/baselines/{baseline_id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.baselines_preview.destroy_baseline(baseline_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `baseline_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Baseline ID                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |