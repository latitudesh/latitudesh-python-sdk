# TeamsSDK
(*teams*)

## Overview

### Available Operations

* [get_team](#get_team) - Retrieve the team
* [post_team](#post_team) - Create a team
* [patch_current_team](#patch_current_team) - Update a team

## get_team

Retrieve the team

### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.teams.get_team()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Teams](../../models/teams.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## post_team

Create a team

### Example Usage

```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.teams.post_team(request={
        "data": {
            "type": latitudesh_python_sdk.PostTeamType.TEAMS,
            "attributes": {
                "name": "Name",
                "currency": latitudesh_python_sdk.PostTeamCurrency.USD,
                "address": "Address",
            },
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.PostTeamRequestBody](../../models/postteamrequestbody.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PostTeamResponseBody](../../models/postteamresponsebody.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ErrorObject | 406, 422           | application/json   |
| models.APIError    | 4XX, 5XX           | \*/\*              |

## patch_current_team

Update a team

### Example Usage

```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.teams.patch_current_team(team_id="49d41738-140a-4ee5-991e-c708f208e050", data={
        "id": "team_2zLy9LxYpgH4Le2LGN02fMwNX9Xg",
        "type": latitudesh_python_sdk.PatchCurrentTeamType.TEAMS,
        "attributes": {
            "address": "Address",
            "name": "Name",
            "currency": latitudesh_python_sdk.PatchCurrentTeamCurrency.USD,
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `team_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `data`                                                              | [models.PatchCurrentTeamData](../../models/patchcurrentteamdata.md) | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PatchCurrentTeamResponseBody](../../models/patchcurrentteamresponsebody.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ErrorObject | 403, 404           | application/json   |
| models.APIError    | 4XX, 5XX           | \*/\*              |