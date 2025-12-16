# Projects

## Overview

### Available Operations

* [list](#list) - List all Projects
* [create](#create) - Create a Project
* [update](#update) - Update a Project
* [delete](#delete) - Delete a Project

## list

Returns a list of all projects for the current team


### Example Usage

<!-- UsageSnippet language="python" operationID="get-projects" method="get" path="/projects" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.projects.list(filter_tags="tag_GGXAB6PNQbU285ZYLP3wt3ZQyXW,tag_xR2B8J4W81TBL6YRGPJaCQRkVyn", page_size=20, page_number=1)

    while res is not None:
        # Handle items

        res = res.next()

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
| `page_size`                                                                                                                                                                                                                                   | *Optional[int]*                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                            | Number of items to return per page                                                                                                                                                                                                            |
| `page_number`                                                                                                                                                                                                                                 | *Optional[int]*                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                            | Page number to return (starts at 1)                                                                                                                                                                                                           |
| `retries`                                                                                                                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                                                                                                                           |

### Response

**[models.GetProjectsResponse](../../models/getprojectsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create

Create a Project

### Example Usage

<!-- UsageSnippet language="python" operationID="create-project" method="post" path="/projects" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.projects.create(data={
        "type": latitudesh_python_sdk.CreateProjectProjectsType.PROJECTS,
        "attributes": {
            "name": "Kshlerin, Hand and Beer",
            "provisioning_type": latitudesh_python_sdk.CreateProjectProvisioningType.ON_DEMAND,
            "description": "Thick slices of French toast bread, brown sugar, half-and-half and vanilla, topped with powdered sugar. With two eggs served any style, and your choice of smoked bacon or smoked ham.",
            "environment": latitudesh_python_sdk.CreateProjectProjectsEnvironment.DEVELOPMENT,
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `data`                                                                                  | [Optional[models.CreateProjectProjectsData]](../../models/createprojectprojectsdata.md) | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.CreateProjectResponseBody](../../models/createprojectresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update

Update a Project

### Example Usage

<!-- UsageSnippet language="python" operationID="update-project" method="patch" path="/projects/{project_id}" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.projects.update(project_id="proj_WVQJDMMwDRbyE", data={
        "id": "proj_WVQJDMMwDRbyE",
        "type": latitudesh_python_sdk.UpdateProjectProjectsType.PROJECTS,
        "attributes": {
            "tags": [
                "tag_xNrKWa1ZaMtBKwaZnYaMTBE2XQb",
                "tag_Ge9E4oboPgILP5e9aKNAUB4Gaw5",
            ],
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `project_id`                                                                  | *str*                                                                         | :heavy_check_mark:                                                            | The project ID or Slug                                                        |
| `data`                                                                        | [models.UpdateProjectProjectsData](../../models/updateprojectprojectsdata.md) | :heavy_check_mark:                                                            | N/A                                                                           |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.UpdateProjectResponseBody](../../models/updateprojectresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete

Delete a Project

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-project" method="delete" path="/projects/{project_id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.projects.delete(project_id="invalid")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The project ID or Slug                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |