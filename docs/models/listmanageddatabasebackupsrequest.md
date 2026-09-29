# ListManagedDatabaseBackupsRequest


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `managed_database_id`                                                     | *str*                                                                     | :heavy_check_mark:                                                        | Managed database ID                                                       |
| `phase`                                                                   | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | Filter backups by phase. Use 'completed' to return only finished backups. |