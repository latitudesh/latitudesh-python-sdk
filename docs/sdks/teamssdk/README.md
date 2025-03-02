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
            "type": latitudesh_python_sdk.PostTeamTeamsType.TEAMS,
            "attributes": {
                "name": "Name",
                "currency": latitudesh_python_sdk.PostTeamTeamsCurrency.USD,
                "address": "Address",
            },
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.PostTeamTeamsRequestBody](../../models/postteamteamsrequestbody.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.PostTeamResponseBody](../../models/postteamresponsebody.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 406, 422                 | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

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

    res = latitudesh.teams.patch_current_team(team_id="7d6111de-ae7e-41af-9a8c-c5808e6d9807", data={
        "id": "team_pEmgv7yvm7cl6KmKa5GPF3eRYvj",
        "type": latitudesh_python_sdk.PatchCurrentTeamTeamsType.TEAMS,
        "attributes": {
            "address": "Address",
            "name": "Name",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `team_id`                                                                     | *str*                                                                         | :heavy_check_mark:                                                            | N/A                                                                           |
| `data`                                                                        | [models.PatchCurrentTeamTeamsData](../../models/patchcurrentteamteamsdata.md) | :heavy_check_mark:                                                            | N/A                                                                           |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.PatchCurrentTeamResponseBody](../../models/patchcurrentteamresponsebody.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 404                 | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |