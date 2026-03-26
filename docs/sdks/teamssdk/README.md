# Teams

## Overview

### Available Operations

* [get](#get) - Retrieve team
* [create](#create) - Create team
* [update](#update) - Update team

## get

Retrieve team

### Example Usage: Success

<!-- UsageSnippet language="python" operationID="get-team" method="get" path="/team" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.teams.get()

    # Handle response
    print(res)

```
### Example Usage: when team is older than one month

<!-- UsageSnippet language="python" operationID="get-team" method="get" path="/team" example="when team is older than one month" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.teams.get()

    # Handle response
    print(res)

```
### Example Usage: when team is recent (created within last month)

<!-- UsageSnippet language="python" operationID="get-team" method="get" path="/team" example="when team is recent (created within last month)" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.teams.get()

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

## create

Create team

### Example Usage: Created

<!-- UsageSnippet language="python" operationID="post-team" method="post" path="/team" example="Created" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.teams.create(data={
        "type": latitudesh_python_sdk.PostTeamTeamsType.TEAMS,
        "attributes": {
            "name": "Name",
            "currency": latitudesh_python_sdk.PostTeamTeamsCurrency.USD,
            "address": "Address",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Not Acceptable

<!-- UsageSnippet language="python" operationID="post-team" method="post" path="/team" example="Not Acceptable" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.teams.create(data={
        "type": latitudesh_python_sdk.PostTeamTeamsType.TEAMS,
        "attributes": {
            "name": "Name",
            "currency": latitudesh_python_sdk.PostTeamTeamsCurrency.USD,
            "address": "Address",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Unprocessable Entity

<!-- UsageSnippet language="python" operationID="post-team" method="post" path="/team" example="Unprocessable Entity" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.teams.create(data={
        "type": latitudesh_python_sdk.PostTeamTeamsType.TEAMS,
        "attributes": {
            "name": "",
            "currency": latitudesh_python_sdk.PostTeamTeamsCurrency.BRL,
            "address": "",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `data`                                                              | [models.PostTeamTeamsData](../../models/postteamteamsdata.md)       | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PostTeamResponseBody](../../models/postteamresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update

Update team

### Example Usage: Forbidden

<!-- UsageSnippet language="python" operationID="patch-current-team" method="patch" path="/team/{team_id}" example="Forbidden" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.teams.update(team_id="7107c56e-31be-45e4-9376-a905f204d08a", data={
        "id": "team_8Wj589lRWNCK1gAje2pAfXmag5jg",
        "type": latitudesh_python_sdk.PatchCurrentTeamTeamsType.TEAMS,
        "attributes": {
            "address": "Address",
            "name": "Name",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Not Found

<!-- UsageSnippet language="python" operationID="patch-current-team" method="patch" path="/team/{team_id}" example="Not Found" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.teams.update(team_id="c7a799cc-bb1c-42e3-aaf9-a76b10f5c1ac", data={
        "id": "c7a799cc-bb1c-42e3-aaf9-a76b10f5c1ac",
        "type": latitudesh_python_sdk.PatchCurrentTeamTeamsType.TEAMS,
        "attributes": {
            "address": "Address",
            "name": "Name",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Success

<!-- UsageSnippet language="python" operationID="patch-current-team" method="patch" path="/team/{team_id}" example="Success" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.teams.update(team_id="team_bVJM4y6m4VCyy101JzA3szlVGRb", data={
        "id": "team_bVJM4y6m4VCyy101JzA3szlVGRb",
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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |