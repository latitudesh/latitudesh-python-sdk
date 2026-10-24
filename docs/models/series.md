# Series


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `timestamp`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Start of the bucket (UTC)                                            |
| `models`                                                             | Dict[str, [models.Models](../models/models.md)]                      | :heavy_minus_sign:                                                   | Usage in the bucket keyed by model ID                                |