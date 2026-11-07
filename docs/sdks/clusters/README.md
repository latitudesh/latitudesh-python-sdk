# Clusters

## Overview

Projects that have a GPU cluster only. Every operation answers 404 PROJECT_NOT_A_CLUSTER for a project without one.

### Available Operations

* [get_project_cluster_requirements](#get_project_cluster_requirements) - Get cluster requirements
* [update_project_cluster_requirements](#update_project_cluster_requirements) - Change cluster requirements
* [sign_project_cluster_requirements](#sign_project_cluster_requirements) - Sign cluster requirements
* [get_project_cluster_requirement_signoffs](#get_project_cluster_requirement_signoffs) - List cluster requirement sign-offs
* [get_project_cluster_node_groups](#get_project_cluster_node_groups) - List cluster node groups
* [create_project_cluster_node_group](#create_project_cluster_node_group) - Create a cluster node group
* [delete_project_cluster_node_group](#delete_project_cluster_node_group) - Delete a cluster node group
* [update_project_cluster_node_group](#update_project_cluster_node_group) - Update a cluster node group

## get_project_cluster_requirements

Shows your cluster's requirements for review: the requirements and what is expected of each, the node groups, the version to sign and who signed. Only available for projects that have a GPU cluster; any other project answers 404 PROJECT_NOT_A_CLUSTER. While the requirements are a draft, their content is empty.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-project-cluster-requirements" method="get" path="/projects/{project_id}/cluster/requirements" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.clusters.get_project_cluster_requirements(project_id="proj_lxWpD699qm6rk")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The ID or slug of a project that has a GPU cluster                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ClusterRequirements](../../models/clusterrequirements.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_project_cluster_requirements

Applies one change to your requirements: add or remove a requirement or the checks of a block, or set what a requirement expects. Signed requirements need to be signed again. Only available for projects that have a GPU cluster; any other project answers 404 PROJECT_NOT_A_CLUSTER. Needs an owner, administrator or collaborator.

### Example Usage

<!-- UsageSnippet language="python" operationID="update-project-cluster-requirements" method="patch" path="/projects/{project_id}/cluster/requirements" example="Success" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.clusters.update_project_cluster_requirements(project_id="proj_lxWpD699qm6rk", data={
        "type": latitudesh_python_sdk.ChangeClusterRequirementsType.CLUSTER_REQUIREMENTS,
        "attributes": {
            "add": "storage_fs",
            "expected": "xfs",
            "note": "Scratch",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `project_id`                                                                          | *str*                                                                                 | :heavy_check_mark:                                                                    | The ID or slug of a project that has a GPU cluster                                    |
| `data`                                                                                | [models.ChangeClusterRequirementsData](../../models/changeclusterrequirementsdata.md) | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.ClusterRequirements](../../models/clusterrequirements.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## sign_project_cluster_requirements

Signs the requirements as you, for the requirements_version you were shown. A version that no longer matches the requirements is refused. Only available for projects that have a GPU cluster; any other project answers 404 PROJECT_NOT_A_CLUSTER. Needs an owner or administrator.

### Example Usage

<!-- UsageSnippet language="python" operationID="sign-project-cluster-requirements" method="post" path="/projects/{project_id}/cluster/requirements/sign" example="Created" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.clusters.sign_project_cluster_requirements(project_id="proj_lxWpD699qm6rk", data={
        "type": latitudesh_python_sdk.SignClusterRequirementsType.CLUSTER_REQUIREMENTS,
        "attributes": {
            "requirements_version": "3f1c9b2e7a4d8c06b5e9f2a1d7c3e8b04a6f9d2c1b7e5a3f8d0c4b6e2a9f7d1c",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `project_id`                                                                      | *str*                                                                             | :heavy_check_mark:                                                                | The ID or slug of a project that has a GPU cluster                                |
| `data`                                                                            | [models.SignClusterRequirementsData](../../models/signclusterrequirementsdata.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.ClusterRequirements](../../models/clusterrequirements.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_project_cluster_requirement_signoffs

Lists who signed the requirements and when, newest first. Only available for projects that have a GPU cluster; any other project answers 404 PROJECT_NOT_A_CLUSTER.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-project-cluster-requirement-signoffs" method="get" path="/projects/{project_id}/cluster/requirements/signoffs" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.clusters.get_project_cluster_requirement_signoffs(project_id="proj_lxWpD699qm6rk")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The ID or slug of a project that has a GPU cluster                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ClusterRequirementSignoffs](../../models/clusterrequirementsignoffs.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_project_cluster_node_groups

Lists your cluster's node groups. Only available for projects that have a GPU cluster; any other project answers 404 PROJECT_NOT_A_CLUSTER. While the requirements are a draft, the list is empty.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-project-cluster-node-groups" method="get" path="/projects/{project_id}/cluster/node_groups" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.clusters.get_project_cluster_node_groups(project_id="proj_lxWpD699qm6rk")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The ID or slug of a project that has a GPU cluster                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ClusterNodeGroups](../../models/clusternodegroups.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_project_cluster_node_group

Adds a node group to your cluster. Only available for projects that have a GPU cluster; any other project answers 404 PROJECT_NOT_A_CLUSTER. Signed requirements need to be signed again. Needs an owner, administrator or collaborator.

### Example Usage

<!-- UsageSnippet language="python" operationID="create-project-cluster-node-group" method="post" path="/projects/{project_id}/cluster/node_groups" example="Created" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.clusters.create_project_cluster_node_group(project_id="proj_lxWpD699qm6rk", data={
        "type": latitudesh_python_sdk.CreateClusterNodeGroupType.CLUSTER_NODE_GROUPS,
        "attributes": {
            "name": "login",
            "kind": latitudesh_python_sdk.CreateClusterNodeGroupKind.CPU,
            "plan": "g4-b300-large",
            "server_count": 2,
            "os": "rocky_9_x64",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `project_id`                                                                    | *str*                                                                           | :heavy_check_mark:                                                              | The ID or slug of a project that has a GPU cluster                              |
| `data`                                                                          | [models.CreateClusterNodeGroupData](../../models/createclusternodegroupdata.md) | :heavy_check_mark:                                                              | N/A                                                                             |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.ClusterNodeGroup](../../models/clusternodegroup.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete_project_cluster_node_group

Removes one of your cluster's node groups. Only available for projects that have a GPU cluster; any other project answers 404 PROJECT_NOT_A_CLUSTER. Signed requirements need to be signed again. Needs an owner, administrator or collaborator.

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-project-cluster-node-group" method="delete" path="/projects/{project_id}/cluster/node_groups/{id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    latitudesh.clusters.delete_project_cluster_node_group(project_id="proj_lxWpD699qm6rk", id="7")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The ID or slug of a project that has a GPU cluster                  |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The node group ID                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_project_cluster_node_group

Changes the attributes sent of one of your cluster's node groups. Only available for projects that have a GPU cluster; any other project answers 404 PROJECT_NOT_A_CLUSTER. Signed requirements need to be signed again. Needs an owner, administrator or collaborator.

### Example Usage

<!-- UsageSnippet language="python" operationID="update-project-cluster-node-group" method="patch" path="/projects/{project_id}/cluster/node_groups/{id}" example="Success" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.clusters.update_project_cluster_node_group(project_id="proj_lxWpD699qm6rk", id="7", data={
        "type": latitudesh_python_sdk.UpdateClusterNodeGroupType.CLUSTER_NODE_GROUPS,
        "attributes": {
            "server_count": 32,
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `project_id`                                                                    | *str*                                                                           | :heavy_check_mark:                                                              | The ID or slug of a project that has a GPU cluster                              |
| `id`                                                                            | *str*                                                                           | :heavy_check_mark:                                                              | The node group ID                                                               |
| `data`                                                                          | [models.UpdateClusterNodeGroupData](../../models/updateclusternodegroupdata.md) | :heavy_check_mark:                                                              | N/A                                                                             |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.ClusterNodeGroup](../../models/clusternodegroup.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |