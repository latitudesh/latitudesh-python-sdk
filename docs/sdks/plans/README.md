# Plans
(*plans*)

## Overview

### Available Operations

* [list](#list) - List all Plans
* [get](#get) - Retrieve a Plan
* [list_bandwidth](#list_bandwidth) - List all bandwidth plans
* [update_bandwidth](#update_bandwidth) - Buy or remove bandwidth packages
* [get_containers_plans](#get_containers_plans) - List containers plans
* [get_containers_plan](#get_containers_plan) - Retrieve container plan
* [list_storage](#list_storage) - List all Storage Plans
* [list_vm_plans](#list_vm_plans) - List all Virtual Machines Plans

## list

Lists all plans. Availability by region is included in `attributes.regions.locations.available[*]` node for a given plan.


### Example Usage

<!-- UsageSnippet language="python" operationID="get-plans" method="get" path="/plans" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.plans.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                | Type                                                                                                                                                                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `filter_name`                                                                                                                                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                       | The plan name to filter by                                                                                                                                                                                                                                                                                                                                               |
| `filter_slug`                                                                                                                                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                       | The plan slug to filter by                                                                                                                                                                                                                                                                                                                                               |
| `filter_location`                                                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                       | The location of the site to filter by                                                                                                                                                                                                                                                                                                                                    |
| `filter_stock_level`                                                                                                                                                                                                                                                                                                                                                     | [Optional[models.FilterStockLevel]](../../models/filterstocklevel.md)                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                       | The stock level at the site to filter by                                                                                                                                                                                                                                                                                                                                 |
| `filter_in_stock`                                                                                                                                                                                                                                                                                                                                                        | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                       | The stock available at the site to filter by                                                                                                                                                                                                                                                                                                                             |
| `filter_gpu`                                                                                                                                                                                                                                                                                                                                                             | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                       | Filter by the existence of an associated GPU                                                                                                                                                                                                                                                                                                                             |
| `filter_ram`                                                                                                                                                                                                                                                                                                                                                             | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                       | The ram size in Gigabytes to filter by, should be used with the following options:<br/>                              [eql] to filter for values equal to the provided value.<br/>                              [gte] to filter for values greater or equal to the provided value.<br/>                              [lte] to filter by values lower or equal to the provided value. |
| `filter_disk`                                                                                                                                                                                                                                                                                                                                                            | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                       | The disk size in Gigabytes to filter by, should be used with the following options:<br/>                              [eql] to filter for values equal to the provided value.<br/>                              [gte] to filter for values greater or equal to the provided value.<br/>                              [lte] to filter by values lower or equal to the provided value. |
| `retries`                                                                                                                                                                                                                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                      |

### Response

**[models.GetPlansResponseBody](../../models/getplansresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get

Retrieve a Plan

### Example Usage

<!-- UsageSnippet language="python" operationID="get-plan" method="get" path="/plans/{plan_id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.plans.get(plan_id="plan_m5xyZOnNOWM0l")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `plan_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Plan](../../models/plan.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_bandwidth

Lists all bandwidth plans.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-bandwidth-plans" method="get" path="/plans/bandwidth" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.plans.list_bandwidth(api_version="2023-06-01", page_size=20, page_number=1)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `api_version`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `filter_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The plan ID to filter by                                            |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Number of items to return per page                                  |
| `page_number`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Page number to return (starts at 1)                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetBandwidthPlansResponse](../../models/getbandwidthplansresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_bandwidth

Allows to increase or decrease bandwidth packages. Only admins and owners can request.


### Example Usage

<!-- UsageSnippet language="python" operationID="update-plans-bandwidth" method="post" path="/plans/bandwidth" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.plans.update_bandwidth(data={
        "type": latitudesh_python_sdk.UpdatePlansBandwidthPlansType.BANDWIDTH_PACKAGES,
        "attributes": {
            "project": "proj_z2A3DVZ3DnawP",
            "quantity": 5,
            "region_slug": "brazil",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `data`                                                                                          | [Optional[models.UpdatePlansBandwidthPlansData]](../../models/updateplansbandwidthplansdata.md) | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.BandwidthPackages](../../models/bandwidthpackages.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_containers_plans

Lists all containers plans.


### Example Usage

<!-- UsageSnippet language="python" operationID="get-containers-plans" method="get" path="/plans/containers" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.plans.get_containers_plans()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                             | Type                                                                                                                                                                                                                                                                                                                                                                                  | Required                                                                                                                                                                                                                                                                                                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `filter_name`                                                                                                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                    | The plan name to filter by                                                                                                                                                                                                                                                                                                                                                            |
| `filter_slug`                                                                                                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                    | The plan slug to filter by                                                                                                                                                                                                                                                                                                                                                            |
| `filter_location`                                                                                                                                                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                    | The location of the site to filter by                                                                                                                                                                                                                                                                                                                                                 |
| `filter_stock_level`                                                                                                                                                                                                                                                                                                                                                                  | [Optional[models.QueryParamFilterStockLevel]](../../models/queryparamfilterstocklevel.md)                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                    | Filter by the level of containers availability                                                                                                                                                                                                                                                                                                                                        |
| `filter_in_stock`                                                                                                                                                                                                                                                                                                                                                                     | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                    | The stock available at the site to filter by                                                                                                                                                                                                                                                                                                                                          |
| `filter_gpu`                                                                                                                                                                                                                                                                                                                                                                          | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                    | Filter by the existence of an associated GPU                                                                                                                                                                                                                                                                                                                                          |
| `filter_ram`                                                                                                                                                                                                                                                                                                                                                                          | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                    | The ram size in Gigabytes to filter by, should be used with the following options:<br/>                              [eql] to filter for values equal to the provided value.<br/>                              [gte] to filter for values greater or equal to the provided value.<br/>                              [lte] to filter by values lower or equal to the provided value.   |
| `filter_ephemeral_storage`                                                                                                                                                                                                                                                                                                                                                            | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                    | The ephemeral_storage size in Gigabytes to filter by, should be used with the following options:<br/>                              [eql] to filter for values equal to the provided value.<br/>                              [gte] to filter for values greater or equal to the provided value.<br/>                              [lte] to filter by values lower or equal to the provided value. |
| `retries`                                                                                                                                                                                                                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                   |

### Response

**[models.GetContainersPlansResponseBody](../../models/getcontainersplansresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_containers_plan

Retrieve a container plan.


### Example Usage

<!-- UsageSnippet language="python" operationID="get-containers-plan" method="get" path="/plans/containers/{plan_id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.plans.get_containers_plan(plan_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `plan_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The Plan ID                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ContainerPlanData](../../models/containerplandata.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_storage

List all Storage Plans

### Example Usage

<!-- UsageSnippet language="python" operationID="get-storage-plans" method="get" path="/plans/storage" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.plans.list_storage()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.StoragePlans](../../models/storageplans.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_vm_plans

List all Virtual Machines Plans

### Example Usage

<!-- UsageSnippet language="python" operationID="get-vm-plans" method="get" path="/plans/virtual_machines" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.plans.list_vm_plans()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.VirtualMachinePlans](../../models/virtualmachineplans.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |