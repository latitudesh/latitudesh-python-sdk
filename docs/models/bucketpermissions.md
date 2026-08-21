# BucketPermissions


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `bucket_id`                                                            | *str*                                                                  | :heavy_check_mark:                                                     | Bucket (object storage) ID to grant access to.                         |
| `permission`                                                           | [models.Permission](../models/permission.md)                           | :heavy_check_mark:                                                     | `readonly` grants read-only access; `rw` grants read and write access. |