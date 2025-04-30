# UserDataSDK
(*user_data*)

## Overview

### Available Operations

* [list_project_user_data](#list_project_user_data) - List all Project User Data
* [create](#create) - Create a Project User Data
* [get_project_user_data](#get_project_user_data) - Retrieve a Project User Data
* [update](#update) - Update a Project User Data
* [delete](#delete) - Delete a Project User Data

## list_project_user_data

List all Users Data in the project. These scripts can be used to configure servers with user data.


### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.user_data.list_project_user_data(project_id="proj_z2A3DV4wdnawP")

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

## create

Allows you to create User Data in a project, which can be used to perform custom setup on your servers after deploy and reinstall.


### Example Usage

```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.user_data.create(project_id="proj_1ZJrdxvyDg4LV", data={
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

    res = latitudesh.user_data.get_project_user_data(project_id="proj_vYAZqG44DMQ94", user_data_id="ud_lQraYDPeOpjwW")

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

## update

Allow you update User Data in a project.


### Example Usage

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

**[models.UserData](../../models/userdata.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete

Allow you remove User Data in a project.


### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.user_data.delete(project_id="proj_GnzRD5X6qM5yw", user_data_id="123")

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