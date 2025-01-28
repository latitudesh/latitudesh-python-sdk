# TeamsMembers
(*teams_members*)

## Overview

### Available Operations

* [get_team_members](#get_team_members) - List all Team Members
* [post_team_members](#post_team_members) - Add a Team Member
* [destroy_team_member](#destroy_team_member) - Remove a Team Member

## get_team_members

List all Team Members

### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.teams_members.get_team_members()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TeamMembers](../../models/teammembers.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## post_team_members

Add a Team Member

### Example Usage

```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.teams_members.post_team_members(request={
        "data": {
            "type": latitudesh_python_sdk.PostTeamMembersType.MEMBERSHIPS,
            "attributes": {
                "email": "dian_davis@connelly-yost.test",
                "role": latitudesh_python_sdk.PostTeamMembersRole.COLLABORATOR,
                "first_name": "Ramon",
                "last_name": "Stracke",
            },
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `request`                                                                       | [models.PostTeamMembersRequestBody](../../models/postteammembersrequestbody.md) | :heavy_check_mark:                                                              | The request object to use for the request.                                      |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.Membership](../../models/membership.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ErrorObject | 403, 422           | application/json   |
| models.APIError    | 4XX, 5XX           | \*/\*              |

## destroy_team_member

Remove a Team Member

### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.teams_members.destroy_team_member(user_id="user_Gr47qlE1DAg0m")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The user ID                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ErrorObject | 404                | application/json   |
| models.APIError    | 4XX, 5XX           | \*/\*              |