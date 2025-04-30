# Billing
(*billing*)

## Overview

### Available Operations

* [list_usage](#list_usage) - List Billing Usage

## list_usage

Returns the billing usage of a project


### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.billing.list_usage(filter_project="proj_6059EqYkOQj8p", filter_products=[
        "si_pttmsx3d",
        "si_nmru52ev",
    ], filter_plan="plan.name")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `filter_project`                                                                               | *str*                                                                                          | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `filter_products`                                                                              | List[*str*]                                                                                    | :heavy_minus_sign:                                                                             | Allows to filter the billing usage for specific products. It accepts an array of product ids.<br/> |
| `filter_plan`                                                                                  | *Optional[str]*                                                                                | :heavy_minus_sign:                                                                             | Accepts a plan name and allows to filter the usage for that plan.<br/>                         |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[models.BillingUsage](../../models/billingusage.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |