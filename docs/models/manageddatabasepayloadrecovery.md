# ManagedDatabasePayloadRecovery

Restore from a source database backup (postgres only). Required: Managed Databases no longer accepts new databases, only restores.


## Fields

| Field                  | Type                   | Required               | Description            |
| ---------------------- | ---------------------- | ---------------------- | ---------------------- |
| `source_database_name` | *str*                  | :heavy_check_mark:     | N/A                    |
| `backup_id`            | *Optional[str]*        | :heavy_minus_sign:     | N/A                    |