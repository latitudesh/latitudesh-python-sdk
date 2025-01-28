# BillingUsageAttributes


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `project`                                                                | [Optional[models.BillingUsageProject]](../models/billingusageproject.md) | :heavy_minus_sign:                                                       | The project in which the returned usage belongs to                       |
| `period`                                                                 | [Optional[models.Period]](../models/period.md)                           | :heavy_minus_sign:                                                       | The period from the returned billing cycle                               |
| `price`                                                                  | *Optional[float]*                                                        | :heavy_minus_sign:                                                       | The total usage price in cents                                           |
| `threshold`                                                              | *Optional[float]*                                                        | :heavy_minus_sign:                                                       | The threshold which we use to charge your usage, in cents                |
| `products`                                                               | List[[models.Products](../models/products.md)]                           | :heavy_minus_sign:                                                       | N/A                                                                      |