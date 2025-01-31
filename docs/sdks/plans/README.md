# Plans
(*plans*)

## Overview

### Available Operations

* [get_plans](#get_plans) - List all Plans
* [get_plan](#get_plan) - Retrieve a Plan
* [get_bandwidth_plans](#get_bandwidth_plans) - List all bandwidth plans
* [update_plans_bandwidth](#update_plans_bandwidth) - Buy or remove bandwidth packages
* [get_storage_plans](#get_storage_plans) - List all Storage Plans

## get_plans

Lists all plans. Availability by region is included in `attributes.regions.locations.available[*]` node for a given plan.


### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.plans.get_plans()

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

## get_plan

Retrieve a Plan

### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.plans.get_plan(plan_id="plan_VE1Wd3aXDXnZJ")

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

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ErrorObject | 404                | application/json   |
| models.APIError    | 4XX, 5XX           | \*/\*              |

## get_bandwidth_plans

Lists all bandwidth plans.

### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.plans.get_bandwidth_plans()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `api_version`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `filter_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The plan ID to filter by                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.BandwidthPlans](../../models/bandwidthplans.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_plans_bandwidth

Allow to increase or decrease bandwidth packages. Only admins and owners can request.


### Example Usage

```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.plans.update_plans_bandwidth(request={
        "data": {
            "type": latitudesh_python_sdk.UpdatePlansBandwidthType.BANDWIDTH_PACKAGES,
            "attributes": {
                "project": "proj_QraYDPQNOpjwW",
                "quantity": 5,
                "region_slug": "brazil",
            },
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `request`                                                                                 | [models.UpdatePlansBandwidthRequestBody](../../models/updateplansbandwidthrequestbody.md) | :heavy_check_mark:                                                                        | The request object to use for the request.                                                |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.BandwidthPackages](../../models/bandwidthpackages.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ErrorObject | 403                | application/json   |
| models.APIError    | 4XX, 5XX           | \*/\*              |

## get_storage_plans

List all Storage Plans

### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.plans.get_storage_plans()

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