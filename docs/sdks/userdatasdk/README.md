# UserData

## Overview

### Available Operations

* [~~list_project_user_data~~](#list_project_user_data) - List all Project User Data :warning: **Deprecated**
* [~~create~~](#create) - Create a Project User Data :warning: **Deprecated**
* [~~get_project_user_data~~](#get_project_user_data) - Retrieve a Project User Data :warning: **Deprecated**
* [~~update~~](#update) - Update a Project User Data :warning: **Deprecated**
* [~~delete~~](#delete) - Delete a Project User Data :warning: **Deprecated**
* [get_users_data](#get_users_data) - List all User Data
* [post_user_data](#post_user_data) - Create an User Data
* [get_user_data](#get_user_data) - Retrieve an User Data
* [patch_user_data](#patch_user_data) - Update an User Data
* [delete_user_data](#delete_user_data) - Delete an User Data

## ~~list_project_user_data~~

List all Users Data in the project. These scripts can be used to configure servers with user data.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-project-users-data" method="get" path="/projects/{project_id}/user_data" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.user_data.list_project_user_data(project_id="proj_RMLydp7XOQKr1", extra_fields_user_data="decoded_content")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `project_id`                                                                                | *str*                                                                                       | :heavy_check_mark:                                                                          | Project ID or Slug                                                                          |
| `extra_fields_user_data`                                                                    | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | The `decoded_content` is provided as an extra attribute that shows content in decoded form. |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.UserData](../../models/userdata.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## ~~create~~

Allows you to create User Data in a project, which can be used to perform custom setup on your servers after deploy and reinstall.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="post-project-user-data" method="post" path="/projects/{project_id}/user_data" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.user_data.create(project_id="proj_kjQwdE0XOYNVP", data={
        "type": latitudesh_python_sdk.PostProjectUserDataUserDataType.USER_DATA,
        "attributes": {
            "description": "User Data description",
            "content": "I2Nsb3VkLWNvbmZpZwpydW5jbWQ6CiAtIFsgdG91Y2gsICAvaG9tZS91YnVudHUvdGVzdCBd",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `project_id`                                                                              | *str*                                                                                     | :heavy_check_mark:                                                                        | Project ID or Slug                                                                        |
| `data`                                                                                    | [models.PostProjectUserDataUserDataData](../../models/postprojectuserdatauserdatadata.md) | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.UserDataObject](../../models/userdataobject.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## ~~get_project_user_data~~

Get User Data in the project. These scripts can be used to configure servers with user data.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-project-user-data" method="get" path="/projects/{project_id}/user_data/{user_data_id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.user_data.get_project_user_data(project_id="proj_Gr47qlevDAg0m", user_data_id="ud_VLMmAD8EOwop2", extra_fields_user_data="decoded_content")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `project_id`                                                                                | *str*                                                                                       | :heavy_check_mark:                                                                          | Project ID or Slug                                                                          |
| `user_data_id`                                                                              | *str*                                                                                       | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `extra_fields_user_data`                                                                    | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | The `decoded_content` is provided as an extra attribute that shows content in decoded form. |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.UserDataObject](../../models/userdataobject.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## ~~update~~

Allow you update User Data in a project.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="put-project-user-data" method="patch" path="/projects/{project_id}/user_data/{user_data_id}" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.user_data.update(project_id="proj_e8pKq0aKDWAob", user_data_id="ud_2695BdKrOevVo", data={
        "id": "ud_2695BdKrOevVo",
        "type": latitudesh_python_sdk.PutProjectUserDataUserDataType.USER_DATA,
        "attributes": {
            "content": "I2Nsb3VkLWNvbmZpZwpydW5jbWQ6CiAtIFsgdG91Y2gsICAvaG9tZS91YnVudHUvdGVzdCBd",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `project_id`                                                                            | *str*                                                                                   | :heavy_check_mark:                                                                      | Project ID or Slug                                                                      |
| `user_data_id`                                                                          | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `data`                                                                                  | [models.PutProjectUserDataUserDataData](../../models/putprojectuserdatauserdatadata.md) | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.UserDataObject](../../models/userdataobject.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## ~~delete~~

Allow you remove User Data in a project.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-project-user-data" method="delete" path="/projects/{project_id}/user_data/{user_data_id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.user_data.delete(project_id="proj_x1ZJrdx5qg4LV", user_data_id="123")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Project ID or Slug                                                  |
| `user_data_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_users_data

List all Users Data in the project. These scripts can be used to configure servers with user data.


### Example Usage

<!-- UsageSnippet language="python" operationID="get-users-data" method="get" path="/user_data" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.user_data.get_users_data(extra_fields_user_data="decoded_content")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `filter_project`                                                                            | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | Project ID or slug                                                                          |
| `extra_fields_user_data`                                                                    | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | The `decoded_content` is provided as an extra attribute that shows content in decoded form. |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.UserData](../../models/userdata.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## post_user_data

Allows you to create User Data in a team, which can be used to perform custom setup on your servers after deploy and reinstall.


### Example Usage

<!-- UsageSnippet language="python" operationID="post-user-data" method="post" path="/user_data" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.user_data.post_user_data(data={
        "type": latitudesh_python_sdk.PostUserDataUserDataType.USER_DATA,
        "attributes": {
            "description": "User Data description",
            "project": "proj_AW6Q2D9lqKLpr",
            "content": "I2Nsb3VkLWNvbmZpZwpydW5jbWQ6CiAtIFsgdG91Y2gsICAvaG9tZS91YnVudHUvdGVzdCBd",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `data`                                                                      | [models.PostUserDataUserDataData](../../models/postuserdatauserdatadata.md) | :heavy_check_mark:                                                          | N/A                                                                         |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.UserDataObject](../../models/userdataobject.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_user_data

Get User Data in the project. These scripts can be used to configure servers with user data.


### Example Usage

<!-- UsageSnippet language="python" operationID="get-user-data" method="get" path="/user_data/{user_data_id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.user_data.get_user_data(user_data_id="ud_1Qkm7dXzD8nZV", extra_fields_user_data="decoded_content")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `user_data_id`                                                                              | *str*                                                                                       | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `extra_fields_user_data`                                                                    | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | The `decoded_content` is provided as an extra attribute that shows content in decoded form. |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.UserDataObject](../../models/userdataobject.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## patch_user_data

Allow you update User Data in a team.


### Example Usage

<!-- UsageSnippet language="python" operationID="patch-user-data" method="patch" path="/user_data/{user_data_id}" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.user_data.patch_user_data(user_data_id="ud_Av9BVDavORm1W", data={
        "id": "ud_Av9BVDavORm1W",
        "type": latitudesh_python_sdk.PatchUserDataUserDataType.USER_DATA,
        "attributes": {
            "content": "I2Nsb3VkLWNvbmZpZwpydW5jbWQ6CiAtIFsgdG91Y2gsICAvaG9tZS91YnVudHUvdGVzdCBd",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `user_data_id`                                                                | *str*                                                                         | :heavy_check_mark:                                                            | N/A                                                                           |
| `data`                                                                        | [models.PatchUserDataUserDataData](../../models/patchuserdatauserdatadata.md) | :heavy_check_mark:                                                            | N/A                                                                           |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.UserDataObject](../../models/userdataobject.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete_user_data

Delete an User Data

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-user-data" method="delete" path="/user_data/{user_data_id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.user_data.delete_user_data(user_data_id="123")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_data_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |