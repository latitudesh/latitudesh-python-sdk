# UserProfile

## Overview

### Available Operations

* [get](#get) - Get user profile
* [update](#update) - Update User Profile
* [list_teams](#list_teams) - List User Teams

## get

Retrieve the current user profile


### Example Usage

<!-- UsageSnippet language="python" operationID="get-user-profile" method="get" path="/user/profile" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.user_profile.get()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetUserProfileResponseBody](../../models/getuserprofileresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update

Update the current user profile


### Example Usage

<!-- UsageSnippet language="python" operationID="patch-user-profile" method="patch" path="/user/profile/{id}" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.user_profile.update(id="user_lGJBgAxbgeUJ4yZj56wmfrK4vag", data={
        "id": "user_lGJBgAxbgeUJ4yZj56wmfrK4vag",
        "type": latitudesh_python_sdk.PatchUserProfileUserProfileType.USERS,
        "attributes": {
            "role": latitudesh_python_sdk.PatchUserProfileUserProfileRole.COLLABORATOR,
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `id`                                                                                      | *str*                                                                                     | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `data`                                                                                    | [models.PatchUserProfileUserProfileData](../../models/patchuserprofileuserprofiledata.md) | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.PatchUserProfileResponseBody](../../models/patchuserprofileresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_teams

Returns a list of all teams the user belongs to


### Example Usage

<!-- UsageSnippet language="python" operationID="get-user-teams" method="get" path="/user/teams" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.user_profile.list_teams()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UserTeams](../../models/userteams.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |