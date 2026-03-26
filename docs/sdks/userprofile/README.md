# UserProfile

## Overview

### Available Operations

* [get](#get) - Retrieve profile
* [update](#update) - Update profile
* [list_teams](#list_teams) - List user teams

## get

Retrieve the current user profile


### Example Usage

<!-- UsageSnippet language="python" operationID="get-user-profile" method="get" path="/user/profile" example="Success" -->
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


### Example Usage: Forbidden

<!-- UsageSnippet language="python" operationID="patch-user-profile" method="patch" path="/user/profile/{id}" example="Forbidden" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.user_profile.update(id="user_kLn528op4zIMZ61MzRapu7XnAkL", data={
        "id": "user_kLn528op4zIMZ61MzRapu7XnAkL",
        "type": latitudesh_python_sdk.PatchUserProfileUserProfileType.USERS,
        "attributes": {
            "role": latitudesh_python_sdk.PatchUserProfileUserProfileRole.COLLABORATOR,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Success

<!-- UsageSnippet language="python" operationID="patch-user-profile" method="patch" path="/user/profile/{id}" example="Success" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.user_profile.update(id="user_8PMvy2GL72uKKyXyANEnsjMQYMP", data={
        "id": "user_8PMvy2GL72uKKyXyANEnsjMQYMP",
        "type": latitudesh_python_sdk.PatchUserProfileUserProfileType.USERS,
        "attributes": {
            "role": latitudesh_python_sdk.PatchUserProfileUserProfileRole.COLLABORATOR,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Unprocessable Entity

<!-- UsageSnippet language="python" operationID="patch-user-profile" method="patch" path="/user/profile/{id}" example="Unprocessable Entity" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.user_profile.update(id="user_WeGoqA4ndP7nz", data={
        "id": "user_WeGoqA4ndP7nz",
        "type": latitudesh_python_sdk.PatchUserProfileUserProfileType.USERS,
        "attributes": {},
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


### Example Usage: Success

<!-- UsageSnippet language="python" operationID="get-user-teams" method="get" path="/user/teams" example="Success" -->
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
### Example Usage: when team is older than one month

<!-- UsageSnippet language="python" operationID="get-user-teams" method="get" path="/user/teams" example="when team is older than one month" -->
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
### Example Usage: when team is recent (created within last month)

<!-- UsageSnippet language="python" operationID="get-user-teams" method="get" path="/user/teams" example="when team is recent (created within last month)" -->
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