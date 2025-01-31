# UserDataSDK
(*user_data*)

## Overview

### Available Operations

* [get_project_users_data](#get_project_users_data) - List all Project User Data
* [post_project_user_data](#post_project_user_data) - Create a Project User Data
* [get_project_user_data](#get_project_user_data) - Retrieve a Project User Data
* [put_project_user_data](#put_project_user_data) - Update a Project User Data
* [delete_project_user_data](#delete_project_user_data) - Delete a Project User Data

## get_project_users_data

List all Users Data in the project. These scripts can be used to configure servers with user data.


### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.user_data.get_project_users_data(project_id="proj_Gr47qlMADAg0m")

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

**[models.GetProjectUsersDataResponseBody](../../models/getprojectusersdataresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## post_project_user_data

Allows you to create User Data in a project, which can be used to perform custom setup on your servers after deploy and reinstall.


### Example Usage

```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.user_data.post_project_user_data(project_id="proj_VE1Wd3GadXnZJ", data={
        "type": latitudesh_python_sdk.PostProjectUserDataType.USER_DATA,
        "attributes": {
            "description": "User Data description",
            "content": "I2Nsb3VkLWNvbmZpZwpydW5jbWQ6CiAtIFsgdG91Y2gsICAvaG9tZS91YnVudHUvdGVzdCBd",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `project_id`                                                              | *str*                                                                     | :heavy_check_mark:                                                        | Project ID or Slug                                                        |
| `data`                                                                    | [models.PostProjectUserDataData](../../models/postprojectuserdatadata.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.UserData](../../models/userdata.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_project_user_data

Get User Data in the project. These scripts can be used to configure servers with user data.


### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.user_data.get_project_user_data(project_id="proj_kjQwdEa7dYNVP", user_data_id="ud_Ee8pKq05DWAob")

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

**[models.UserData](../../models/userdata.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## put_project_user_data

Allow you update User Data in a project.


### Example Usage

```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.user_data.put_project_user_data(project_id="proj_vYAZqG44DMQ94", user_data_id="ud_GlxWpD6KOm6rk", data={
        "id": "ud_GlxWpD6KOm6rk",
        "type": latitudesh_python_sdk.PutProjectUserDataType.USER_DATA,
        "attributes": {
            "content": "I2Nsb3VkLWNvbmZpZwpydW5jbWQ6CiAtIFsgdG91Y2gsICAvaG9tZS91YnVudHUvdGVzdCBd",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `project_id`                                                            | *str*                                                                   | :heavy_check_mark:                                                      | Project ID or Slug                                                      |
| `user_data_id`                                                          | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `data`                                                                  | [models.PutProjectUserDataData](../../models/putprojectuserdatadata.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.UserData](../../models/userdata.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete_project_user_data

Allow you remove User Data in a project.


### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.user_data.delete_project_user_data(project_id="proj_QraYDPA3OpjwW", user_data_id="123")

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