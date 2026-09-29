# Lks

## Overview

### Available Operations

* [list_lks_clusters](#list_lks_clusters) - List LKS clusters
* [create_lks_cluster](#create_lks_cluster) - Create an LKS cluster
* [get_lks_cluster](#get_lks_cluster) - Get an LKS cluster
* [delete_lks_cluster](#delete_lks_cluster) - Delete an LKS cluster
* [update_lks_cluster](#update_lks_cluster) - Update an LKS cluster
* [get_lks_cluster_kubeconfig](#get_lks_cluster_kubeconfig) - Get the cluster kubeconfig
* [list_lks_node_pools](#list_lks_node_pools) - List node pools
* [create_lks_node_pool](#create_lks_node_pool) - Create a node pool
* [get_lks_node_pool](#get_lks_node_pool) - Get a node pool
* [delete_lks_node_pool](#delete_lks_node_pool) - Delete a node pool
* [update_lks_node_pool](#update_lks_node_pool) - Update a node pool
* [list_lks_available_versions](#list_lks_available_versions) - List available Kubernetes versions
* [list_lks_sites](#list_lks_sites) - List sites available for LKS

## list_lks_clusters

Lists every LKS cluster of a project. The response is not paginated; `meta.total` is the number of clusters returned.


### Example Usage: Empty

<!-- UsageSnippet language="python" operationID="list-lks-clusters" method="get" path="/lks/clusters" example="Empty" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.lks.list_lks_clusters(project_id="proj_6059EqYkOQj8p")

    # Handle response
    print(res)

```
### Example Usage: OneCluster

<!-- UsageSnippet language="python" operationID="list-lks-clusters" method="get" path="/lks/clusters" example="OneCluster" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.lks.list_lks_clusters(project_id="proj_6059EqYkOQj8p")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    | Example                                                                        |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `project_id`                                                                   | *str*                                                                          | :heavy_check_mark:                                                             | Project `id_hash` or slug. Required — clusters are always scoped to a project. | proj_6059EqYkOQj8p                                                             |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |                                                                                |

### Response

**[models.LksClusters](../../models/lksclusters.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 404                 | application/vnd.api+json |
| models.ErrorObject       | 502                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## create_lks_cluster

Creates an LKS cluster. The cluster is the control plane only — worker capacity is added separately through node pools (`POST /lks/clusters/{cluster_id}/nodepools`).

`site` must be one of the slugs returned by `GET /lks/sites`, and `kubernetes_version` must be a patch listed by `GET /lks/available_versions` with `available_for_creation: true`.

The cluster is returned immediately with `status: "provisioning"`. Poll `GET /lks/clusters/{id}` until `status` is `ready`, then fetch the kubeconfig.


### Example Usage: InsufficientPermissions

<!-- UsageSnippet language="python" operationID="create-lks-cluster" method="post" path="/lks/clusters" example="InsufficientPermissions" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.lks.create_lks_cluster(data={
        "type": latitudesh_python_sdk.CreateLksClusterType.LKS_CLUSTERS,
        "attributes": {
            "name": "<value>",
            "project_id": "<id>",
            "site": "<value>",
            "kubernetes_version": "1.36.3",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Minimal

<!-- UsageSnippet language="python" operationID="create-lks-cluster" method="post" path="/lks/clusters" example="Minimal" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.lks.create_lks_cluster(data={
        "type": latitudesh_python_sdk.CreateLksClusterType.LKS_CLUSTERS,
        "attributes": {
            "name": "production",
            "project_id": "proj_6059EqYkOQj8p",
            "site": "DAL2",
            "kubernetes_version": "1.36.3",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Provisioning

<!-- UsageSnippet language="python" operationID="create-lks-cluster" method="post" path="/lks/clusters" example="Provisioning" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.lks.create_lks_cluster(data={
        "type": latitudesh_python_sdk.CreateLksClusterType.LKS_CLUSTERS,
        "attributes": {
            "name": "<value>",
            "project_id": "<id>",
            "site": "<value>",
            "kubernetes_version": "1.36.3",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: WithNetworkOverrides

<!-- UsageSnippet language="python" operationID="create-lks-cluster" method="post" path="/lks/clusters" example="WithNetworkOverrides" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.lks.create_lks_cluster(data={
        "type": latitudesh_python_sdk.CreateLksClusterType.LKS_CLUSTERS,
        "attributes": {
            "name": "production",
            "project_id": "proj_6059EqYkOQj8p",
            "site": "DAL2",
            "kubernetes_version": "1.36.3",
            "description": "Main production cluster",
            "network": {
                "pod_cidrs": [
                    "10.70.0.0/16",
                ],
                "service_cidrs": [
                    "10.71.0.0/16",
                ],
                "node_cidrs": [
                    "10.72.0.0/24",
                ],
            },
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `data`                                                              | [models.CreateLksClusterData](../../models/createlksclusterdata.md) | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LksCluster](../../models/lkscluster.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 404, 422            | application/vnd.api+json |
| models.ErrorObject       | 502                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## get_lks_cluster

Retrieves a single LKS cluster.

`status` is an open enum sourced from the platform controller — `provisioning`, `ready`, `updating`, `scaling`, `upgrading`, `paused`, `deleting` and `deleted` are the values in use today, and new ones may appear without notice. `reason` and `message` carry the machine-readable and human-readable detail behind the current `status`.


### Example Usage: Provisioning

<!-- UsageSnippet language="python" operationID="get-lks-cluster" method="get" path="/lks/clusters/{id}" example="Provisioning" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.lks.get_lks_cluster(id="<id>")

    # Handle response
    print(res)

```
### Example Usage: Ready

<!-- UsageSnippet language="python" operationID="get-lks-cluster" method="get" path="/lks/clusters/{id}" example="Ready" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.lks.get_lks_cluster(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The cluster ID (format: `lksc_<hash>`).                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LksCluster](../../models/lkscluster.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 404                 | application/vnd.api+json |
| models.ErrorObject       | 502                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## delete_lks_cluster

Marks the cluster for deletion. The call returns as soon as the tombstone is written; the platform then tears the cluster and its node pools down asynchronously. A cluster that is already deleted, or that is paused, rejects the request.


### Example Usage

<!-- UsageSnippet language="python" operationID="delete-lks-cluster" method="delete" path="/lks/clusters/{id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.lks.delete_lks_cluster(id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The cluster ID (format: `lksc_<hash>`).                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 404, 409            | application/vnd.api+json |
| models.ErrorObject       | 502                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## update_lks_cluster

Renames a cluster, edits its description, or upgrades the control plane. At least one of `name`, `description` or `kubernetes_version` must be provided.

Setting a newer `kubernetes_version` consents to a control-plane upgrade; the value must be a patch listed by `GET /lks/available_versions` with `available_for_upgrade: true` and must not be lower than the current one. Node pools are upgraded separately and must never run a patch newer than the control plane.

The cluster must be idle: a cluster that is provisioning, updating, scaling, upgrading, paused or deleting rejects the request with 409.


### Example Usage: InsufficientPermissions

<!-- UsageSnippet language="python" operationID="update-lks-cluster" method="patch" path="/lks/clusters/{id}" example="InsufficientPermissions" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.lks.update_lks_cluster(id="<id>", data={
        "type": latitudesh_python_sdk.UpdateLksClusterType.LKS_CLUSTERS,
        "attributes": {
            "kubernetes_version": "1.37.2",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Rename

<!-- UsageSnippet language="python" operationID="update-lks-cluster" method="patch" path="/lks/clusters/{id}" example="Rename" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.lks.update_lks_cluster(id="<id>", data={
        "type": latitudesh_python_sdk.UpdateLksClusterType.LKS_CLUSTERS,
        "attributes": {
            "name": "production-eu",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: UpgradeControlPlane

<!-- UsageSnippet language="python" operationID="update-lks-cluster" method="patch" path="/lks/clusters/{id}" example="UpgradeControlPlane" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.lks.update_lks_cluster(id="<id>", data={
        "type": latitudesh_python_sdk.UpdateLksClusterType.LKS_CLUSTERS,
        "attributes": {
            "kubernetes_version": "1.37.2",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Upgrading

<!-- UsageSnippet language="python" operationID="update-lks-cluster" method="patch" path="/lks/clusters/{id}" example="Upgrading" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.lks.update_lks_cluster(id="<id>", data={
        "type": latitudesh_python_sdk.UpdateLksClusterType.LKS_CLUSTERS,
        "attributes": {
            "kubernetes_version": "1.37.2",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The cluster ID (format: `lksc_<hash>`).                             |
| `data`                                                              | [models.UpdateLksClusterData](../../models/updatelksclusterdata.md) | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LksCluster](../../models/lkscluster.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 404, 409, 422       | application/vnd.api+json |
| models.ErrorObject       | 502                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## get_lks_cluster_kubeconfig

Returns the kubeconfig for the cluster. It only exists once the control plane is up, so this endpoint answers 409 `NOT_READY` while the cluster is still provisioning — poll `GET /lks/clusters/{id}` until `kubeconfig_url` is set.


### Example Usage

<!-- UsageSnippet language="python" operationID="get-lks-cluster-kubeconfig" method="get" path="/lks/clusters/{id}/kubeconfig" example="Ready" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.lks.get_lks_cluster_kubeconfig(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The cluster ID (format: `lksc_<hash>`).                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LksClusterKubeconfig](../../models/lksclusterkubeconfig.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 404, 409            | application/vnd.api+json |
| models.ErrorObject       | 502                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## list_lks_node_pools

Lists every node pool of an LKS cluster. The response is not paginated; `meta.total` is the number of node pools returned.


### Example Usage

<!-- UsageSnippet language="python" operationID="list-lks-node-pools" method="get" path="/lks/clusters/{cluster_id}/nodepools" example="OnePool" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.lks.list_lks_node_pools(cluster_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `cluster_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The cluster ID (format: `lksc_<hash>`).                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LksNodePools](../../models/lksnodepools.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 404                 | application/vnd.api+json |
| models.ErrorObject       | 502                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## create_lks_node_pool

Adds a node pool to an LKS cluster. The platform provisions `count` servers of `plan` from stock, so both fields are required.

`kubernetes_version` defaults to the control-plane patch and may never be newer than it. `max_pods_per_node` is set once, here — it cannot be changed later.


### Example Usage: InsufficientPermissions

<!-- UsageSnippet language="python" operationID="create-lks-node-pool" method="post" path="/lks/clusters/{cluster_id}/nodepools" example="InsufficientPermissions" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.lks.create_lks_node_pool(cluster_id="<id>", data={
        "type": latitudesh_python_sdk.CreateLksNodePoolType.LKS_NODE_POOLS,
        "attributes": {
            "plan": "<value>",
            "count": 973849,
            "kubernetes_version": "1.36.3",
            "max_pods_per_node": 110,
            "taints": [
                {
                    "key": "dedicated",
                    "value": "gpu",
                    "effect": latitudesh_python_sdk.Effect.NO_SCHEDULE,
                },
            ],
        },
    })

    # Handle response
    print(res)

```
### Example Usage: OnDemand

<!-- UsageSnippet language="python" operationID="create-lks-node-pool" method="post" path="/lks/clusters/{cluster_id}/nodepools" example="OnDemand" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.lks.create_lks_node_pool(cluster_id="<id>", data={
        "type": latitudesh_python_sdk.CreateLksNodePoolType.LKS_NODE_POOLS,
        "attributes": {
            "plan": "c2-small-x86",
            "count": 2,
            "name": "pool-a",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Provisioning

<!-- UsageSnippet language="python" operationID="create-lks-node-pool" method="post" path="/lks/clusters/{cluster_id}/nodepools" example="Provisioning" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.lks.create_lks_node_pool(cluster_id="<id>", data={
        "type": latitudesh_python_sdk.CreateLksNodePoolType.LKS_NODE_POOLS,
        "attributes": {
            "plan": "<value>",
            "count": 973849,
            "kubernetes_version": "1.36.3",
            "max_pods_per_node": 110,
            "taints": [
                {
                    "key": "dedicated",
                    "value": "gpu",
                    "effect": latitudesh_python_sdk.Effect.NO_SCHEDULE,
                },
            ],
        },
    })

    # Handle response
    print(res)

```
### Example Usage: WithLabelsAndTaints

<!-- UsageSnippet language="python" operationID="create-lks-node-pool" method="post" path="/lks/clusters/{cluster_id}/nodepools" example="WithLabelsAndTaints" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.lks.create_lks_node_pool(cluster_id="<id>", data={
        "type": latitudesh_python_sdk.CreateLksNodePoolType.LKS_NODE_POOLS,
        "attributes": {
            "plan": "g3-xlarge-x86",
            "count": 3,
            "max_pods_per_node": 250,
            "name": "gpu",
            "labels": {
                "workload": "training",
            },
            "taints": [
                {
                    "key": "dedicated",
                    "value": "gpu",
                    "effect": latitudesh_python_sdk.Effect.NO_SCHEDULE,
                },
            ],
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `cluster_id`                                                          | *str*                                                                 | :heavy_check_mark:                                                    | The cluster ID (format: `lksc_<hash>`).                               |
| `data`                                                                | [models.CreateLksNodePoolData](../../models/createlksnodepooldata.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.LksNodePool](../../models/lksnodepool.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 404, 422            | application/vnd.api+json |
| models.ErrorObject       | 502                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## get_lks_node_pool

Retrieves a single node pool of an LKS cluster. `ready_nodes` reports how many of the pool's `count` nodes have joined the cluster.


### Example Usage

<!-- UsageSnippet language="python" operationID="get-lks-node-pool" method="get" path="/lks/clusters/{cluster_id}/nodepools/{id}" example="Ready" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.lks.get_lks_node_pool(cluster_id="<id>", id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `cluster_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The cluster ID (format: `lksc_<hash>`).                             |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The node pool ID (format: `lksnp_<hash>`).                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LksNodePool](../../models/lksnodepool.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 404                 | application/vnd.api+json |
| models.ErrorObject       | 502                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## delete_lks_node_pool

Marks the node pool for deletion. The call returns as soon as the tombstone is written; the platform then drains and releases the nodes asynchronously.


### Example Usage

<!-- UsageSnippet language="python" operationID="delete-lks-node-pool" method="delete" path="/lks/clusters/{cluster_id}/nodepools/{id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.lks.delete_lks_node_pool(cluster_id="<id>", id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `cluster_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The cluster ID (format: `lksc_<hash>`).                             |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The node pool ID (format: `lksnp_<hash>`).                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 404, 409            | application/vnd.api+json |
| models.ErrorObject       | 502                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## update_lks_node_pool

Scales, renames, upgrades or re-labels a node pool. At least one attribute must be provided.

`labels` and `taints` are declarative replacements, not merges: omit the field to leave it untouched, send the whole map/list to replace it, or send `{}` / `[]` to clear it.

A newer `kubernetes_version` rolls a node-recreating upgrade; it must not be lower than the pool's current patch nor newer than the control-plane patch. `max_pods_per_node` is immutable — a PATCH that carries it is rejected with 422 even if the value is unchanged.

The node pool must be idle: one that is provisioning, updating, scaling, upgrading, paused or deleting rejects the request with 409.


### Example Usage: ClearTaints

<!-- UsageSnippet language="python" operationID="update-lks-node-pool" method="patch" path="/lks/clusters/{cluster_id}/nodepools/{id}" example="ClearTaints" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.lks.update_lks_node_pool(cluster_id="<id>", id="<id>", data={
        "type": latitudesh_python_sdk.UpdateLksNodePoolType.LKS_NODE_POOLS,
        "attributes": {
            "taints": [],
        },
    })

    # Handle response
    print(res)

```
### Example Usage: InsufficientPermissions

<!-- UsageSnippet language="python" operationID="update-lks-node-pool" method="patch" path="/lks/clusters/{cluster_id}/nodepools/{id}" example="InsufficientPermissions" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.lks.update_lks_node_pool(cluster_id="<id>", id="<id>", data={
        "type": latitudesh_python_sdk.UpdateLksNodePoolType.LKS_NODE_POOLS,
        "attributes": {
            "taints": [
                {
                    "key": "dedicated",
                    "value": "gpu",
                    "effect": latitudesh_python_sdk.Effect.NO_SCHEDULE,
                },
            ],
        },
    })

    # Handle response
    print(res)

```
### Example Usage: ReplaceLabels

<!-- UsageSnippet language="python" operationID="update-lks-node-pool" method="patch" path="/lks/clusters/{cluster_id}/nodepools/{id}" example="ReplaceLabels" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.lks.update_lks_node_pool(cluster_id="<id>", id="<id>", data={
        "type": latitudesh_python_sdk.UpdateLksNodePoolType.LKS_NODE_POOLS,
        "attributes": {
            "labels": {
                "env": "prod",
            },
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Scale

<!-- UsageSnippet language="python" operationID="update-lks-node-pool" method="patch" path="/lks/clusters/{cluster_id}/nodepools/{id}" example="Scale" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.lks.update_lks_node_pool(cluster_id="<id>", id="<id>", data={
        "type": latitudesh_python_sdk.UpdateLksNodePoolType.LKS_NODE_POOLS,
        "attributes": {
            "count": 4,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Scaling

<!-- UsageSnippet language="python" operationID="update-lks-node-pool" method="patch" path="/lks/clusters/{cluster_id}/nodepools/{id}" example="Scaling" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.lks.update_lks_node_pool(cluster_id="<id>", id="<id>", data={
        "type": latitudesh_python_sdk.UpdateLksNodePoolType.LKS_NODE_POOLS,
        "attributes": {
            "taints": [
                {
                    "key": "dedicated",
                    "value": "gpu",
                    "effect": latitudesh_python_sdk.Effect.NO_SCHEDULE,
                },
            ],
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Upgrade

<!-- UsageSnippet language="python" operationID="update-lks-node-pool" method="patch" path="/lks/clusters/{cluster_id}/nodepools/{id}" example="Upgrade" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.lks.update_lks_node_pool(cluster_id="<id>", id="<id>", data={
        "type": latitudesh_python_sdk.UpdateLksNodePoolType.LKS_NODE_POOLS,
        "attributes": {
            "kubernetes_version": "1.36.3",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `cluster_id`                                                          | *str*                                                                 | :heavy_check_mark:                                                    | The cluster ID (format: `lksc_<hash>`).                               |
| `id`                                                                  | *str*                                                                 | :heavy_check_mark:                                                    | The node pool ID (format: `lksnp_<hash>`).                            |
| `data`                                                                | [models.UpdateLksNodePoolData](../../models/updatelksnodepooldata.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.LksNodePool](../../models/lksnodepool.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 404, 409, 422       | application/vnd.api+json |
| models.ErrorObject       | 502                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## list_lks_available_versions

Lists the Kubernetes patches the platform offers, with their lifecycle flags. Use a version with `available_for_creation: true` when creating a cluster or a node pool, and one with `available_for_upgrade: true` when upgrading. Exactly one entry has `default: true`.


### Example Usage

<!-- UsageSnippet language="python" operationID="list-lks-available-versions" method="get" path="/lks/available_versions" example="TwoVersions" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.lks.list_lks_available_versions()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LksKubernetesVersions](../../models/lkskubernetesversions.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 502                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## list_lks_sites

Lists the sites that can host an LKS cluster, one entry per site. Pass an entry's `id` (the site slug) as `site` when creating a cluster. `country` is null when the underlying site has no region assigned.


### Example Usage

<!-- UsageSnippet language="python" operationID="list-lks-sites" method="get" path="/lks/sites" example="TwoSites" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.lks.list_lks_sites()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LksSites](../../models/lkssites.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 502                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |