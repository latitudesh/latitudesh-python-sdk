# Billing
(*billing*)

## Overview

### Available Operations

* [get_billing_usage](#get_billing_usage) - List Billing Usage

## get_billing_usage

Returns the billing usage of a project


### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.billing.get_billing_usage(filter_project="proj_RMLydp7XOQKr1", filter_products=[
        "si_9553572a-a415-42d5-b9ff-7d1167c03dce",
        "si_5e33ce0d-863a-4a2c-8789-d0bc9fe0105d",
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