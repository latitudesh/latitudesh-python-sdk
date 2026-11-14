# ChangeClusterRequirementsAttributes

Exactly one of add, add_checks, remove, remove_checks or set. expected and note go with add and set.


## Fields

| Field                                                 | Type                                                  | Required                                              | Description                                           | Example                                               |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `add`                                                 | *Optional[str]*                                       | :heavy_minus_sign:                                    | A requirement to add                                  | storage_fs                                            |
| `add_checks`                                          | List[*str*]                                           | :heavy_minus_sign:                                    | Checks to add at once                                 |                                                       |
| `remove`                                              | *Optional[str]*                                       | :heavy_minus_sign:                                    | A requirement id to remove                            |                                                       |
| `remove_checks`                                       | List[*str*]                                           | :heavy_minus_sign:                                    | Checks to remove at once                              |                                                       |
| `set`                                                 | *Optional[str]*                                       | :heavy_minus_sign:                                    | A requirement id whose expected value or note changes |                                                       |
| `expected`                                            | *OptionalNullable[str]*                               | :heavy_minus_sign:                                    | N/A                                                   |                                                       |
| `note`                                                | *OptionalNullable[str]*                               | :heavy_minus_sign:                                    | N/A                                                   |                                                       |