# KubernetesClusters

## Overview

### Available Operations

* [list_kubernetes_clusters](#list_kubernetes_clusters) - List Kubernetes Clusters
* [create_kubernetes_cluster](#create_kubernetes_cluster) - Create a Kubernetes Cluster
* [get_kubernetes_cluster](#get_kubernetes_cluster) - Get a Kubernetes Cluster
* [delete_kubernetes_cluster](#delete_kubernetes_cluster) - Delete a Kubernetes Cluster
* [update_kubernetes_cluster](#update_kubernetes_cluster) - Scale Kubernetes Cluster Workers
* [get_kubernetes_cluster_kubeconfig](#get_kubernetes_cluster_kubeconfig) - Get Kubernetes Cluster Kubeconfig

## list_kubernetes_clusters

Lists all Kubernetes clusters for a project.


### Example Usage: EmptyList

<!-- UsageSnippet language="python" operationID="list-kubernetes-clusters" method="get" path="/kubernetes_clusters" example="EmptyList" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.kubernetes_clusters.list_kubernetes_clusters(project_id="<id>")

    # Handle response
    print(res)

```
### Example Usage: Success

<!-- UsageSnippet language="python" operationID="list-kubernetes-clusters" method="get" path="/kubernetes_clusters" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.kubernetes_clusters.list_kubernetes_clusters(project_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The project ID to filter clusters by                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.KubernetesClusters](../../models/kubernetesclusters.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 400, 401, 403            | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## create_kubernetes_cluster

Creates a new managed Kubernetes cluster. Maximum of 1 cluster per project.

Cluster names must follow Kubernetes naming rules: lowercase alphanumeric characters or hyphens, must start and end with an alphanumeric character, and be at most 63 characters long.


### Example Usage: Created

<!-- UsageSnippet language="python" operationID="create-kubernetes-cluster" method="post" path="/kubernetes_clusters" example="Created" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.kubernetes_clusters.create_kubernetes_cluster(data={
        "type": latitudesh_python_sdk.CreateKubernetesClusterType.KUBERNETES_CLUSTERS,
        "attributes": {
            "name": "my-cluster",
            "project_id": "proj_6059EqYkOQj8p",
            "site": "SAN3",
            "plan": "c2-small-x86",
            "ssh_keys": [
                "ssh_VkE1DwV37dnZJ",
            ],
        },
    })

    # Handle response
    print(res)

```
### Example Usage: InvalidSshKeys

<!-- UsageSnippet language="python" operationID="create-kubernetes-cluster" method="post" path="/kubernetes_clusters" example="InvalidSshKeys" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.kubernetes_clusters.create_kubernetes_cluster(data={
        "type": latitudesh_python_sdk.CreateKubernetesClusterType.KUBERNETES_CLUSTERS,
        "attributes": {
            "project_id": "<id>",
            "site": "<value>",
            "plan": "<value>",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: ValidationError

<!-- UsageSnippet language="python" operationID="create-kubernetes-cluster" method="post" path="/kubernetes_clusters" example="ValidationError" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.kubernetes_clusters.create_kubernetes_cluster(data={
        "type": latitudesh_python_sdk.CreateKubernetesClusterType.KUBERNETES_CLUSTERS,
        "attributes": {
            "project_id": "<id>",
            "site": "<value>",
            "plan": "<value>",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `data`                                                                            | [models.CreateKubernetesClusterData](../../models/createkubernetesclusterdata.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.KubernetesClusterCreateResponse](../../models/kubernetesclustercreateresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 400, 403, 422            | application/vnd.api+json |
| models.ErrorObject       | 503                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## get_kubernetes_cluster

Retrieves detailed information about a Kubernetes cluster including its status, control plane, worker node details, and individual node information.


### Example Usage: Provisioning

<!-- UsageSnippet language="python" operationID="get-kubernetes-cluster" method="get" path="/kubernetes_clusters/{kubernetes_cluster_id}" example="Provisioning" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.kubernetes_clusters.get_kubernetes_cluster(kubernetes_cluster_id="<id>")

    # Handle response
    print(res)

```
### Example Usage: Success

<!-- UsageSnippet language="python" operationID="get-kubernetes-cluster" method="get" path="/kubernetes_clusters/{kubernetes_cluster_id}" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.kubernetes_clusters.get_kubernetes_cluster(kubernetes_cluster_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `kubernetes_cluster_id`                                                                                   | *str*                                                                                                     | :heavy_check_mark:                                                                                        | The cluster ID (format: kc_<hash>) or cluster name. Both formats are accepted for backward compatibility. |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[models.KubernetesCluster](../../models/kubernetescluster.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 401, 403, 404            | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## delete_kubernetes_cluster

Deletes a Kubernetes cluster. This action is irreversible and will destroy all cluster resources.


### Example Usage

<!-- UsageSnippet language="python" operationID="delete-kubernetes-cluster" method="delete" path="/kubernetes_clusters/{kubernetes_cluster_id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.kubernetes_clusters.delete_kubernetes_cluster(kubernetes_cluster_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `kubernetes_cluster_id`                                                                                   | *str*                                                                                                     | :heavy_check_mark:                                                                                        | The cluster ID (format: kc_<hash>) or cluster name. Both formats are accepted for backward compatibility. |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 401, 403, 404, 422       | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## update_kubernetes_cluster

Scales the worker nodes of a Kubernetes cluster. The cluster must be in `Provisioned` phase to accept updates.

When scaling up, the API validates that sufficient server stock is available for the requested delta (e.g., scaling from 2 to 5 workers checks for 3 available servers).

When scaling from 0 workers, you must provide a `worker_plan` since there is no existing configuration to inherit the plan from.

Returns 202 Accepted when a scaling operation is triggered. Poll the GET endpoint to monitor progress. Returns 200 OK if the requested worker count matches the current count (no-op).


### Example Usage: InvalidWorkerCountType

<!-- UsageSnippet language="python" operationID="update-kubernetes-cluster" method="patch" path="/kubernetes_clusters/{kubernetes_cluster_id}" example="InvalidWorkerCountType" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.kubernetes_clusters.update_kubernetes_cluster(kubernetes_cluster_id="<id>", data={
        "type": latitudesh_python_sdk.UpdateKubernetesClusterType.KUBERNETES_CLUSTERS,
        "attributes": {
            "worker_count": 204185,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: MissingWorkerCount

<!-- UsageSnippet language="python" operationID="update-kubernetes-cluster" method="patch" path="/kubernetes_clusters/{kubernetes_cluster_id}" example="MissingWorkerCount" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.kubernetes_clusters.update_kubernetes_cluster(kubernetes_cluster_id="<id>", data={
        "type": latitudesh_python_sdk.UpdateKubernetesClusterType.KUBERNETES_CLUSTERS,
        "attributes": {
            "worker_count": 204185,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: ScaleDown

<!-- UsageSnippet language="python" operationID="update-kubernetes-cluster" method="patch" path="/kubernetes_clusters/{kubernetes_cluster_id}" example="ScaleDown" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.kubernetes_clusters.update_kubernetes_cluster(kubernetes_cluster_id="<id>", data={
        "type": latitudesh_python_sdk.UpdateKubernetesClusterType.KUBERNETES_CLUSTERS,
        "attributes": {
            "worker_count": 2,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: ScaleFromZero

<!-- UsageSnippet language="python" operationID="update-kubernetes-cluster" method="patch" path="/kubernetes_clusters/{kubernetes_cluster_id}" example="ScaleFromZero" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.kubernetes_clusters.update_kubernetes_cluster(kubernetes_cluster_id="<id>", data={
        "type": latitudesh_python_sdk.UpdateKubernetesClusterType.KUBERNETES_CLUSTERS,
        "attributes": {
            "worker_count": 3,
            "worker_plan": "c3-small-x86",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: ScaleToZero

<!-- UsageSnippet language="python" operationID="update-kubernetes-cluster" method="patch" path="/kubernetes_clusters/{kubernetes_cluster_id}" example="ScaleToZero" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.kubernetes_clusters.update_kubernetes_cluster(kubernetes_cluster_id="<id>", data={
        "type": latitudesh_python_sdk.UpdateKubernetesClusterType.KUBERNETES_CLUSTERS,
        "attributes": {
            "worker_count": 0,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: ScaleUp

<!-- UsageSnippet language="python" operationID="update-kubernetes-cluster" method="patch" path="/kubernetes_clusters/{kubernetes_cluster_id}" example="ScaleUp" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.kubernetes_clusters.update_kubernetes_cluster(kubernetes_cluster_id="<id>", data={
        "type": latitudesh_python_sdk.UpdateKubernetesClusterType.KUBERNETES_CLUSTERS,
        "attributes": {
            "worker_count": 5,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Unchanged

<!-- UsageSnippet language="python" operationID="update-kubernetes-cluster" method="patch" path="/kubernetes_clusters/{kubernetes_cluster_id}" example="Unchanged" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.kubernetes_clusters.update_kubernetes_cluster(kubernetes_cluster_id="<id>", data={
        "type": latitudesh_python_sdk.UpdateKubernetesClusterType.KUBERNETES_CLUSTERS,
        "attributes": {
            "worker_count": 204185,
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `kubernetes_cluster_id`                                                                                   | *str*                                                                                                     | :heavy_check_mark:                                                                                        | The cluster ID (format: kc_<hash>) or cluster name. Both formats are accepted for backward compatibility. |
| `data`                                                                                                    | [models.UpdateKubernetesClusterData](../../models/updatekubernetesclusterdata.md)                         | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[models.KubernetesClusterUpdateResponse](../../models/kubernetesclusterupdateresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 400, 403, 404, 422       | application/vnd.api+json |
| models.ErrorObject       | 503                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## get_kubernetes_cluster_kubeconfig

Retrieves the kubeconfig file for a Kubernetes cluster. The kubeconfig is only available once the cluster is fully provisioned.


### Example Usage

<!-- UsageSnippet language="python" operationID="get-kubernetes-cluster-kubeconfig" method="get" path="/kubernetes_clusters/{kubernetes_cluster_id}/kubeconfig" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.kubernetes_clusters.get_kubernetes_cluster_kubeconfig(kubernetes_cluster_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `kubernetes_cluster_id`                                                                                   | *str*                                                                                                     | :heavy_check_mark:                                                                                        | The cluster ID (format: kc_<hash>) or cluster name. Both formats are accepted for backward compatibility. |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[models.KubernetesClusterKubeconfig](../../models/kubernetesclusterkubeconfig.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 401, 403, 404            | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |