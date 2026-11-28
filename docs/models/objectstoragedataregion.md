# ObjectStorageDataRegion

Region information where the object storage is located


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `id`                                                                                 | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | Region identifier                                                                    |
| `city`                                                                               | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | City identifier                                                                      |
| `country`                                                                            | *OptionalNullable[str]*                                                              | :heavy_minus_sign:                                                                   | Country name                                                                         |
| `site`                                                                               | [OptionalNullable[models.ObjectStorageDataSite]](../models/objectstoragedatasite.md) | :heavy_minus_sign:                                                                   | N/A                                                                                  |