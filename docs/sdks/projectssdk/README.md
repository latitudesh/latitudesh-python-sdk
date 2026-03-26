# Projects

## Overview

### Available Operations

* [list](#list) - List projects
* [create](#create) - Create project
* [update](#update) - Update project
* [delete](#delete) - Delete project

## list

Returns a list of all projects for the current team


### Example Usage: Filtered by multiple tags

<!-- UsageSnippet language="python" operationID="get-projects" method="get" path="/projects" example="Filtered by multiple tags" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.projects.list(filter_tags="tag_bg6v8Kz52LHyg0okmVREI6mnKM2,tag_PzXjAnK7MLfpMPzprQ3wSn4rG5P", page_size=20, page_number=1)

    while res is not None:
        # Handle items

        res = res.next()

```
### Example Usage: Filtered by tag

<!-- UsageSnippet language="python" operationID="get-projects" method="get" path="/projects" example="Filtered by tag" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.projects.list(filter_tags="tag_R3YGrW8m0NSAm0l5Wp6XTnnww9r", page_size=20, page_number=1)

    while res is not None:
        # Handle items

        res = res.next()

```
### Example Usage: Success

<!-- UsageSnippet language="python" operationID="get-projects" method="get" path="/projects" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.projects.list(filter_tags="tag_GXeww714mRF2gZ05lnKgU8emo5RE,tag_QQkaK9JnV6tWwPG3pmLviXveVK0Y", page_size=20, page_number=1)

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

Create project

### Example Usage: Bad Request

<!-- UsageSnippet language="python" operationID="create-project" method="post" path="/projects" example="Bad Request" -->
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
            "name": "Collins LLC",
            "provisioning_type": latitudesh_python_sdk.CreateProjectProvisioningType.ON_DEMAND,
            "description": "Granny Smith apples mixed with brown sugar and butter filling, in a flaky all-butter crust, with ice cream.",
            "environment": latitudesh_python_sdk.CreateProjectProjectsEnvironment.DEVELOPMENT,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Created

<!-- UsageSnippet language="python" operationID="create-project" method="post" path="/projects" example="Created" -->
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
            "name": "Bailey and Sons",
            "provisioning_type": latitudesh_python_sdk.CreateProjectProvisioningType.ON_DEMAND,
            "description": "Thick slices of French toast bread, brown sugar, half-and-half and vanilla, topped with powdered sugar. With two eggs served any style, and your choice of smoked bacon or smoked ham.",
            "environment": latitudesh_python_sdk.CreateProjectProjectsEnvironment.DEVELOPMENT,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Forbidden

<!-- UsageSnippet language="python" operationID="create-project" method="post" path="/projects" example="Forbidden" -->
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
            "name": "Morissette, Zieme and Botsford",
            "provisioning_type": latitudesh_python_sdk.CreateProjectProvisioningType.ON_DEMAND,
            "description": "Three egg omelet with Roquefort cheese, chives, and ham. With a side of roasted potatoes, and your choice of toast or croissant.",
            "environment": latitudesh_python_sdk.CreateProjectProjectsEnvironment.DEVELOPMENT,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Success

<!-- UsageSnippet language="python" operationID="create-project" method="post" path="/projects" example="Success" -->
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
            "name": "Cormier-Corkery",
            "provisioning_type": latitudesh_python_sdk.CreateProjectProvisioningType.ON_DEMAND,
            "description": "Thick slices of French toast bread, brown sugar, half-and-half and vanilla, topped with powdered sugar. With two eggs served any style, and your choice of smoked bacon or smoked ham.",
            "environment": latitudesh_python_sdk.CreateProjectProjectsEnvironment.DEVELOPMENT,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Unprocessable Entity

<!-- UsageSnippet language="python" operationID="create-project" method="post" path="/projects" example="Unprocessable Entity" -->
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
            "name": "123",
            "provisioning_type": latitudesh_python_sdk.CreateProjectProvisioningType.RESERVED,
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

Update project

### Example Usage: Forbidden

<!-- UsageSnippet language="python" operationID="update-project" method="patch" path="/projects/{project_id}" example="Forbidden" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.projects.update(project_id="proj_0MoLqJmGd57pY", data={
        "id": "proj_0MoLqJmGd57pY",
        "type": latitudesh_python_sdk.UpdateProjectProjectsType.PROJECTS,
        "attributes": {
            "name": "Moore-Durgan",
            "description": "Sequi occaecati eaque exercitationem.",
            "environment": latitudesh_python_sdk.UpdateProjectProjectsEnvironment.PRODUCTION,
            "bandwidth_alert": True,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Not found

<!-- UsageSnippet language="python" operationID="update-project" method="patch" path="/projects/{project_id}" example="Not found" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.projects.update(project_id="invalid-id", data={
        "id": "invalid-id",
        "type": latitudesh_python_sdk.UpdateProjectProjectsType.PROJECTS,
        "attributes": {
            "name": "Moore-Durgan",
            "description": "Sequi occaecati eaque exercitationem.",
            "environment": latitudesh_python_sdk.UpdateProjectProjectsEnvironment.PRODUCTION,
            "bandwidth_alert": True,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Success

<!-- UsageSnippet language="python" operationID="update-project" method="patch" path="/projects/{project_id}" example="Success" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.projects.update(project_id="proj_Gr47qleMDAg0m", data={
        "id": "proj_Gr47qleMDAg0m",
        "type": latitudesh_python_sdk.UpdateProjectProjectsType.PROJECTS,
        "attributes": {
            "tags": [
                "tag_VgrmvzlEGJhbGYv0z8YzHLa9PKV",
                "tag_PEAMyKnQZEHpGAWKMpB6F7EVYyYj",
            ],
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Tag not updated

<!-- UsageSnippet language="python" operationID="update-project" method="patch" path="/projects/{project_id}" example="Tag not updated" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.projects.update(project_id="proj_Z8rodm2Yq1jLB", data={
        "id": "proj_Z8rodm2Yq1jLB",
        "type": latitudesh_python_sdk.UpdateProjectProjectsType.PROJECTS,
        "attributes": {
            "tags": [
                "invalid-tag",
            ],
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Unprocessable Entity

<!-- UsageSnippet language="python" operationID="update-project" method="patch" path="/projects/{project_id}" example="Unprocessable Entity" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.projects.update(project_id="proj_5xyZOnoNdWM0l", data={
        "id": "proj_5xyZOnoNdWM0l",
        "type": latitudesh_python_sdk.UpdateProjectProjectsType.PROJECTS,
        "attributes": {
            "name": "123",
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

Delete project

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