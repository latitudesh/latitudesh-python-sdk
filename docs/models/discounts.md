# Discounts


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              | Example                                                  |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `description`                                            | *str*                                                    | :heavy_check_mark:                                       | Description of the discount                              | Monthly Discount - Accelerate                            |
| `type`                                                   | [models.BillingUsageType](../models/billingusagetype.md) | :heavy_check_mark:                                       | Type of discount (percentage or fixed amount)            |                                                          |
| `value`                                                  | *float*                                                  | :heavy_check_mark:                                       | Value of the discount (percentage or amount)             | 5                                                        |