# ProjectsSDK
(*projects*)

## Overview

### Available Operations

* [get_projects](#get_projects) - List all Projects
* [create_project](#create_project) - Create a Project
* [update_project](#update_project) - Update a Project
* [delete_project](#delete_project) - Delete a Project

## get_projects

Returns a list of all projects for the current team


### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.projects.get_projects(filter_tags="tag_3neyM8YlxMuKkm2AgPVMcamM2yv")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                     | Type                                                                                                                                                                                                                                          | Required                                                                                                                                                                                                                                      | Description                                                                                                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `filter_name`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                            | The project name to filter by                                                                                                                                                                                                                 |
| `filter_slug`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                            | The project slug to filter by                                                                                                                                                                                                                 |
| `filter_description`                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                            | The project description to filter by                                                                                                                                                                                                          |
| `filter_billing_type`                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                            | The billing type to filter by                                                                                                                                                                                                                 |
| `filter_environment`                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                            | The environment to filter by                                                                                                                                                                                                                  |
| `filter_tags`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                            | The tags ids to filter by, separated by comma, e.g. `filter[tags]=tag_1,tag_2`will return projects with `tag_1` AND `tag_2`                                                                                                                   |
| `extra_fields_projects`                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                            | The `last_renewal_date` and `next_renewal_date` are provided as extra attributes that show previous and future billing cycle dates. To request it, just set `extra_fields[projects]=last_renewal_date,next_renewal_date` in the query string. |
| `retries`                                                                                                                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                                                                                                                           |

### Response

**[models.Projects](../../models/projects.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_project

Create a Project

### Example Usage

```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.projects.create_project(request={
        "data": {
            "type": latitudesh_python_sdk.CreateProjectType.PROJECTS,
            "attributes": {
                "name": "Ward Inc",
                "provisioning_type": latitudesh_python_sdk.ProvisioningType.ON_DEMAND,
                "description": "Breaded fried chicken with waffles. Served with maple syrup.",
                "environment": latitudesh_python_sdk.CreateProjectEnvironment.DEVELOPMENT,
            },
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.CreateProjectRequestBody](../../models/createprojectrequestbody.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.CreateProjectResponseBody](../../models/createprojectresponsebody.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ErrorObject | 400, 403, 422      | application/json   |
| models.APIError    | 4XX, 5XX           | \*/\*              |

## update_project

Update a Project

### Example Usage

```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.projects.update_project(project_id="proj_v9BVDal3qRm1W", data={
        "type": latitudesh_python_sdk.UpdateProjectType.PROJECTS,
        "attributes": {
            "tags": [
                "tag_x4mmPZJ4N6UB7XjXP6mEuBz4r9Y",
                "tag_NGo0yaojbAt8ljQ1MooEIrrBLjg",
            ],
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The project ID or Slug                                              |
| `data`                                                              | [models.UpdateProjectData](../../models/updateprojectdata.md)       | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpdateProjectResponseBody](../../models/updateprojectresponsebody.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ErrorObject | 403, 404, 422      | application/json   |
| models.APIError    | 4XX, 5XX           | \*/\*              |

## delete_project

Delete a Project

### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.projects.delete_project(project_id="invalid")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The project ID or Slug                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ErrorObject | 403, 404, 422      | application/json   |
| models.APIError    | 4XX, 5XX           | \*/\*              |