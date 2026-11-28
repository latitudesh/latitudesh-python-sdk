# ObjectStorage

## Overview

### Available Operations

* [get_storage_usage](#get_storage_usage) - List storage usage
* [get_storage_access_keys](#get_storage_access_keys) - List access keys
* [post_storage_access_keys](#post_storage_access_keys) - Create access key
* [delete_storage_access_keys_username](#delete_storage_access_keys_username) - Delete access key
* [get_storage_bucket_access_keys](#get_storage_bucket_access_keys) - List bucket access keys
* [get_storage_buckets](#get_storage_buckets) - List buckets
* [post_storage_buckets](#post_storage_buckets) - Create bucket
* [get_storage_bucket](#get_storage_bucket) - Retrieve bucket
* [delete_storage_buckets](#delete_storage_buckets) - Delete bucket
* [patch_storage_buckets](#patch_storage_buckets) - Update bucket
* [get_storage_bucket_lifecycle_rules](#get_storage_bucket_lifecycle_rules) - List lifecycle rules
* [post_storage_bucket_lifecycle_rules](#post_storage_bucket_lifecycle_rules) - Create lifecycle rule
* [get_storage_bucket_lifecycle_rule](#get_storage_bucket_lifecycle_rule) - Retrieve lifecycle rule
* [delete_storage_bucket_lifecycle_rule](#delete_storage_bucket_lifecycle_rule) - Delete lifecycle rule
* [patch_storage_bucket_lifecycle_rule](#patch_storage_bucket_lifecycle_rule) - Update lifecycle rule
* [get_storage_bucket_metrics](#get_storage_bucket_metrics) - Retrieve bucket metrics

## get_storage_usage

Returns daily object storage usage for a project. Each row reports the canonical usage in bytes for a single storage on a given day, plus the provider-reported raw value.


### Example Usage

<!-- UsageSnippet language="python" operationID="get-storage-usage" method="get" path="/storage/usage" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.object_storage.get_storage_usage(filter_project="proj_5AEmq7wMqBkWX", filter_storage_id="bkt_6VE1Wd37dXnZJ")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `filter_project`                                                             | *str*                                                                        | :heavy_check_mark:                                                           | Project ID or Slug                                                           |
| `filter_storage_id`                                                          | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | Restrict the result to a single storage. Accepts the storage/bucket ID       |
| `filter_start_date`                                                          | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_minus_sign:                                                           | Defaults to yesterday                                                        |
| `filter_end_date`                                                            | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_minus_sign:                                                           | Defaults to today; clamped to today when a future date is given              |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[models.StorageUsage](../../models/storageusage.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_storage_access_keys

Lists object storage access keys for a project, grouped by storage class. Secrets are never returned by this endpoint.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-storage-access-keys" method="get" path="/storage/access_keys" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.object_storage.get_storage_access_keys(project="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Project ID or slug to list access keys for.                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetStorageAccessKeysResponseBody](../../models/getstorageaccesskeysresponsebody.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 404                 | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## post_storage_access_keys

Creates an object storage IAM access key for a project. The secret is returned only once, in this response, and cannot be retrieved again. The provider is selected by `storage_class`: `standard` provisions the key on Wasabi and `high_performance` provisions it on VAST.

### Example Usage: Created

<!-- UsageSnippet language="python" operationID="post-storage-access-keys" method="post" path="/storage/access_keys" example="Created" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.object_storage.post_storage_access_keys(data={
        "type": latitudesh_python_sdk.PostStorageAccessKeysObjectStorageType.ACCESS_KEYS,
        "attributes": {
            "project": "<value>",
            "storage_class": latitudesh_python_sdk.PostStorageAccessKeysObjectStorageStorageClass.HIGH_PERFORMANCE,
            "name": "<value>",
            "access_scope": latitudesh_python_sdk.PostStorageAccessKeysAccessScope.LIMITED_ACCESS,
            "region": "<value>",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: FullAccess

<!-- UsageSnippet language="python" operationID="post-storage-access-keys" method="post" path="/storage/access_keys" example="FullAccess" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.object_storage.post_storage_access_keys(data={
        "type": latitudesh_python_sdk.PostStorageAccessKeysObjectStorageType.ACCESS_KEYS,
        "attributes": {
            "project": "proj_6059EqYkOQj8p",
            "storage_class": latitudesh_python_sdk.PostStorageAccessKeysObjectStorageStorageClass.STANDARD,
            "name": "my-access-key",
            "access_scope": latitudesh_python_sdk.PostStorageAccessKeysAccessScope.FULLACCESS,
            "region": "DAL",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: LimitedAccess

<!-- UsageSnippet language="python" operationID="post-storage-access-keys" method="post" path="/storage/access_keys" example="LimitedAccess" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.object_storage.post_storage_access_keys(data={
        "type": latitudesh_python_sdk.PostStorageAccessKeysObjectStorageType.ACCESS_KEYS,
        "attributes": {
            "project": "proj_6059EqYkOQj8p",
            "storage_class": latitudesh_python_sdk.PostStorageAccessKeysObjectStorageStorageClass.STANDARD,
            "name": "my-limited-key",
            "access_scope": latitudesh_python_sdk.PostStorageAccessKeysAccessScope.LIMITED_ACCESS,
            "region": "DAL",
            "bucket_permissions": [
                {
                    "bucket_id": "bkt_6VE1Wd37dXnZJ",
                    "permission": latitudesh_python_sdk.PostStorageAccessKeysPermission.READONLY,
                },
                {
                    "bucket_id": "bkt_7WF2Xe48eYoAK",
                    "permission": latitudesh_python_sdk.PostStorageAccessKeysPermission.RW,
                },
            ],
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Unauthorized

<!-- UsageSnippet language="python" operationID="post-storage-access-keys" method="post" path="/storage/access_keys" example="Unauthorized" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.object_storage.post_storage_access_keys(data={
        "type": latitudesh_python_sdk.PostStorageAccessKeysObjectStorageType.ACCESS_KEYS,
        "attributes": {
            "project": "<value>",
            "storage_class": latitudesh_python_sdk.PostStorageAccessKeysObjectStorageStorageClass.HIGH_PERFORMANCE,
            "name": "<value>",
            "access_scope": latitudesh_python_sdk.PostStorageAccessKeysAccessScope.LIMITED_ACCESS,
            "region": "<value>",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `data`                                                                                                  | [models.PostStorageAccessKeysObjectStorageData](../../models/poststorageaccesskeysobjectstoragedata.md) | :heavy_check_mark:                                                                                      | N/A                                                                                                     |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[models.PostStorageAccessKeysResponseBody](../../models/poststorageaccesskeysresponsebody.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 404, 422            | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## delete_storage_access_keys_username

Permanently deletes an object storage access key and its associated provider-side credentials. Deletion cannot be undone: it revokes the key's credentials and removes the key from the storage provider. For `standard` (Wasabi) keys, the IAM user is removed from each of the project's bucket policies, all of the user's access keys are revoked, and the IAM user is deleted. For `high_performance` (VAST) keys, the VAST user's S3 keys are revoked, its attached S3 policies are deleted, and the VAST user is removed.

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-storage-access-keys-username" method="delete" path="/storage/access_keys/{username}/{storage_class}" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    latitudesh.object_storage.delete_storage_access_keys_username(username="Earline_Dooley27", storage_class=latitudesh_python_sdk.PathParamStorageClass.HIGH_PERFORMANCE, project="<value>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                        | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `username`                                                                                                                                       | *str*                                                                                                                                            | :heavy_check_mark:                                                                                                                               | Name of the access key to delete.                                                                                                                |
| `storage_class`                                                                                                                                  | [models.PathParamStorageClass](../../models/pathparamstorageclass.md)                                                                            | :heavy_check_mark:                                                                                                                               | Backend storage tier of the access key. `standard` targets Wasabi; `high_performance` targets VAST.                                              |
| `project`                                                                                                                                        | *str*                                                                                                                                            | :heavy_check_mark:                                                                                                                               | Project ID or slug the access key belongs to.                                                                                                    |
| `region`                                                                                                                                         | *Optional[str]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | Region slug (e.g., `DAL`, `SAO2`). Required for `high_performance` (VAST) keys to select the VAST cluster; ignored for `standard` (Wasabi) keys. |
| `retries`                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                 | :heavy_minus_sign:                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                              |

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 404                 | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## get_storage_bucket_access_keys

Lists IAM access keys associated with an object storage bucket. Secrets are never returned by this endpoint.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-storage-bucket-access-keys" method="get" path="/storage/buckets/{id}/access_keys" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.object_storage.get_storage_bucket_access_keys(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The object storage (bucket) ID                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetStorageBucketAccessKeysResponseBody](../../models/getstoragebucketaccesskeysresponsebody.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 404                 | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## get_storage_buckets

Lists all object storages from a team.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-storage-buckets" method="get" path="/storage/buckets" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.object_storage.get_storage_buckets(page_size=50, page_number=1)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `filter_project`                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                  | The project ID or Slug to filter by                                                                                                                                                                                                 |
| `filter_name`                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                  | The name to filter by (case-insensitive exact match)                                                                                                                                                                                |
| `page_size`                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                  | Number of items to return per page                                                                                                                                                                                                  |
| `page_number`                                                                                                                                                                                                                       | *Optional[int]*                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                  | Page number to return (starts at 1)                                                                                                                                                                                                 |
| `stats_total`                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                  | Request aggregate stats in the response `meta`. Use `count` to get the total number of records, returned as `meta.stats.total.count`.                                                                                               |
| `extra_fields_object_storages`                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                  | The `credentials` are provided as extra attributes that are lazy loaded. Only storages where the requesting user is the creator will include them. To request, set `extra_fields[object_storages]=credentials` in the query string. |
| `retries`                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                 |

### Response

**[models.GetStorageBucketsResponse](../../models/getstoragebucketsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## post_storage_buckets

Creates a new object storage bucket for a project.

### Example Usage: Create

<!-- UsageSnippet language="python" operationID="post-storage-buckets" method="post" path="/storage/buckets" example="Create" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.object_storage.post_storage_buckets(data={
        "type": latitudesh_python_sdk.PostStorageBucketsObjectStorageType.OBJECTS,
        "attributes": {
            "project": "proj_6059EqYkOQj8p",
            "name": "my-bucket",
            "region": "DAL",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: CreateScoped

<!-- UsageSnippet language="python" operationID="post-storage-buckets" method="post" path="/storage/buckets" example="CreateScoped" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.object_storage.post_storage_buckets(data={
        "type": latitudesh_python_sdk.PostStorageBucketsObjectStorageType.OBJECTS,
        "attributes": {
            "project": "proj_6059EqYkOQj8p",
            "name": "customer-bucket",
            "region": "DAL",
            "scoped": True,
            "customer": "acme-corp",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Created

<!-- UsageSnippet language="python" operationID="post-storage-buckets" method="post" path="/storage/buckets" example="Created" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.object_storage.post_storage_buckets(data={
        "type": latitudesh_python_sdk.PostStorageBucketsObjectStorageType.OBJECTS,
        "attributes": {
            "project": "<value>",
            "name": "<value>",
            "region": "<value>",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: FeatureNotEnabled

<!-- UsageSnippet language="python" operationID="post-storage-buckets" method="post" path="/storage/buckets" example="FeatureNotEnabled" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.object_storage.post_storage_buckets(data={
        "type": latitudesh_python_sdk.PostStorageBucketsObjectStorageType.OBJECTS,
        "attributes": {
            "project": "<value>",
            "name": "<value>",
            "region": "<value>",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: InsufficientPermissions

<!-- UsageSnippet language="python" operationID="post-storage-buckets" method="post" path="/storage/buckets" example="InsufficientPermissions" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.object_storage.post_storage_buckets(data={
        "type": latitudesh_python_sdk.PostStorageBucketsObjectStorageType.OBJECTS,
        "attributes": {
            "project": "<value>",
            "name": "<value>",
            "region": "<value>",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `data`                                                                                            | [models.PostStorageBucketsObjectStorageData](../../models/poststoragebucketsobjectstoragedata.md) | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Response

**[models.PostStorageBucketsResponseBody](../../models/poststoragebucketsresponsebody.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 404, 409, 422       | application/vnd.api+json |
| models.ErrorObject       | 500                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## get_storage_bucket

Shows details of a specific object storage.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-storage-bucket" method="get" path="/storage/buckets/{id}" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.object_storage.get_storage_bucket(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                            | Type                                                                                                                                                                                                 | Required                                                                                                                                                                                             | Description                                                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                 | *str*                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                   | The object storage ID                                                                                                                                                                                |
| `extra_fields_object_storages`                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                   | The `credentials` are provided as extra attributes that are lazy loaded. Only the storage creator may request them. To request, set `extra_fields[object_storages]=credentials` in the query string. |
| `retries`                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                  |

### Response

**[models.GetStorageBucketResponseBody](../../models/getstoragebucketresponsebody.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 404                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## delete_storage_buckets

Allows you to remove an object storage from a project.

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-storage-buckets" method="delete" path="/storage/buckets/{id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    latitudesh.object_storage.delete_storage_buckets(id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The object storage ID                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 404, 409            | application/vnd.api+json |
| models.ErrorObject       | 500                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## patch_storage_buckets

Updates versioning, locking and bucket logging settings for an object storage bucket.

### Example Usage

<!-- UsageSnippet language="python" operationID="patch-storage-buckets" method="patch" path="/storage/buckets/{id}" example="OK" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.object_storage.patch_storage_buckets(id="bucket_KXgRdRyoOv9k5", data={
        "type": latitudesh_python_sdk.PatchStorageBucketsObjectStorageType.OBJECTS,
        "attributes": {
            "versioning": True,
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `id`                                                                                                | *str*                                                                                               | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `data`                                                                                              | [models.PatchStorageBucketsObjectStorageData](../../models/patchstoragebucketsobjectstoragedata.md) | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[models.PatchStorageBucketsResponseBody](../../models/patchstoragebucketsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_storage_bucket_lifecycle_rules

Lists all lifecycle rules for a specific object storage bucket.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-storage-bucket-lifecycle-rules" method="get" path="/storage/buckets/{bucket_id}/lifecycle_rules" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.object_storage.get_storage_bucket_lifecycle_rules(bucket_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `bucket_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The object storage bucket ID                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LifecycleRules](../../models/lifecyclerules.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 404                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## post_storage_bucket_lifecycle_rules

Creates a new lifecycle rule for an object storage bucket. Lifecycle rules automate object expiration based on age.

### Example Usage: Create

<!-- UsageSnippet language="python" operationID="post-storage-bucket-lifecycle-rules" method="post" path="/storage/buckets/{bucket_id}/lifecycle_rules" example="Create" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.object_storage.post_storage_bucket_lifecycle_rules(bucket_id="<id>", data={
        "type": latitudesh_python_sdk.PostStorageBucketLifecycleRulesObjectStorageType.LIFECYCLE_RULES,
        "attributes": {
            "name": "delete-old-logs",
            "prefix": "logs/",
            "expiration_days": 30,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: CreateWithAllOptions

<!-- UsageSnippet language="python" operationID="post-storage-bucket-lifecycle-rules" method="post" path="/storage/buckets/{bucket_id}/lifecycle_rules" example="CreateWithAllOptions" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.object_storage.post_storage_bucket_lifecycle_rules(bucket_id="<id>", data={
        "type": latitudesh_python_sdk.PostStorageBucketLifecycleRulesObjectStorageType.LIFECYCLE_RULES,
        "attributes": {
            "name": "full-cleanup-rule",
            "prefix": "temp/",
            "expiration_days": 30,
            "noncurrent_days": 14,
            "abort_mpu_days_after_initiation": 7,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Created

<!-- UsageSnippet language="python" operationID="post-storage-bucket-lifecycle-rules" method="post" path="/storage/buckets/{bucket_id}/lifecycle_rules" example="Created" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.object_storage.post_storage_bucket_lifecycle_rules(bucket_id="<id>", data={
        "type": latitudesh_python_sdk.PostStorageBucketLifecycleRulesObjectStorageType.LIFECYCLE_RULES,
        "attributes": {
            "name": "<value>",
            "expiration_days": 69486,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: FeatureNotEnabled

<!-- UsageSnippet language="python" operationID="post-storage-bucket-lifecycle-rules" method="post" path="/storage/buckets/{bucket_id}/lifecycle_rules" example="FeatureNotEnabled" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.object_storage.post_storage_bucket_lifecycle_rules(bucket_id="<id>", data={
        "type": latitudesh_python_sdk.PostStorageBucketLifecycleRulesObjectStorageType.LIFECYCLE_RULES,
        "attributes": {
            "name": "<value>",
            "expiration_days": 69486,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: InsufficientPermissions

<!-- UsageSnippet language="python" operationID="post-storage-bucket-lifecycle-rules" method="post" path="/storage/buckets/{bucket_id}/lifecycle_rules" example="InsufficientPermissions" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.object_storage.post_storage_bucket_lifecycle_rules(bucket_id="<id>", data={
        "type": latitudesh_python_sdk.PostStorageBucketLifecycleRulesObjectStorageType.LIFECYCLE_RULES,
        "attributes": {
            "name": "<value>",
            "expiration_days": 69486,
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                   | Type                                                                                                                        | Required                                                                                                                    | Description                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `bucket_id`                                                                                                                 | *str*                                                                                                                       | :heavy_check_mark:                                                                                                          | The object storage bucket ID                                                                                                |
| `data`                                                                                                                      | [models.PostStorageBucketLifecycleRulesObjectStorageData](../../models/poststoragebucketlifecyclerulesobjectstoragedata.md) | :heavy_check_mark:                                                                                                          | N/A                                                                                                                         |
| `retries`                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                            | :heavy_minus_sign:                                                                                                          | Configuration to override the default retry behavior of the client.                                                         |

### Response

**[models.PostStorageBucketLifecycleRulesResponseBody](../../models/poststoragebucketlifecyclerulesresponsebody.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 404, 409, 422       | application/vnd.api+json |
| models.ErrorObject       | 500                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## get_storage_bucket_lifecycle_rule

Retrieves details of a specific lifecycle rule.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-storage-bucket-lifecycle-rule" method="get" path="/storage/buckets/{bucket_id}/lifecycle_rules/{id}" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.object_storage.get_storage_bucket_lifecycle_rule(bucket_id="<id>", id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `bucket_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The object storage bucket ID                                        |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The lifecycle rule ID                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetStorageBucketLifecycleRuleResponseBody](../../models/getstoragebucketlifecycleruleresponsebody.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 404                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## delete_storage_bucket_lifecycle_rule

Deletes a lifecycle rule from an object storage bucket.

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-storage-bucket-lifecycle-rule" method="delete" path="/storage/buckets/{bucket_id}/lifecycle_rules/{id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    latitudesh.object_storage.delete_storage_bucket_lifecycle_rule(bucket_id="<id>", id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `bucket_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The object storage bucket ID                                        |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The lifecycle rule ID                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 404                 | application/vnd.api+json |
| models.ErrorObject       | 500                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## patch_storage_bucket_lifecycle_rule

Updates an existing lifecycle rule for an object storage bucket.

### Example Usage: FeatureNotEnabled

<!-- UsageSnippet language="python" operationID="patch-storage-bucket-lifecycle-rule" method="patch" path="/storage/buckets/{bucket_id}/lifecycle_rules/{id}" example="FeatureNotEnabled" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.object_storage.patch_storage_bucket_lifecycle_rule(bucket_id="<id>", id="<id>", data={
        "type": latitudesh_python_sdk.PatchStorageBucketLifecycleRuleObjectStorageType.LIFECYCLE_RULES,
        "attributes": {
            "name": "<value>",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: InsufficientPermissions

<!-- UsageSnippet language="python" operationID="patch-storage-bucket-lifecycle-rule" method="patch" path="/storage/buckets/{bucket_id}/lifecycle_rules/{id}" example="InsufficientPermissions" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.object_storage.patch_storage_bucket_lifecycle_rule(bucket_id="<id>", id="<id>", data={
        "type": latitudesh_python_sdk.PatchStorageBucketLifecycleRuleObjectStorageType.LIFECYCLE_RULES,
        "attributes": {
            "name": "<value>",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Success

<!-- UsageSnippet language="python" operationID="patch-storage-bucket-lifecycle-rule" method="patch" path="/storage/buckets/{bucket_id}/lifecycle_rules/{id}" example="Success" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.object_storage.patch_storage_bucket_lifecycle_rule(bucket_id="<id>", id="<id>", data={
        "type": latitudesh_python_sdk.PatchStorageBucketLifecycleRuleObjectStorageType.LIFECYCLE_RULES,
        "attributes": {
            "name": "<value>",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Update

<!-- UsageSnippet language="python" operationID="patch-storage-bucket-lifecycle-rule" method="patch" path="/storage/buckets/{bucket_id}/lifecycle_rules/{id}" example="Update" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.object_storage.patch_storage_bucket_lifecycle_rule(bucket_id="<id>", id="<id>", data={
        "type": latitudesh_python_sdk.PatchStorageBucketLifecycleRuleObjectStorageType.LIFECYCLE_RULES,
        "attributes": {
            "name": "delete-old-logs",
            "enabled": False,
            "expiration_days": 60,
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                   | Type                                                                                                                        | Required                                                                                                                    | Description                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `bucket_id`                                                                                                                 | *str*                                                                                                                       | :heavy_check_mark:                                                                                                          | The object storage bucket ID                                                                                                |
| `id`                                                                                                                        | *str*                                                                                                                       | :heavy_check_mark:                                                                                                          | The lifecycle rule ID                                                                                                       |
| `data`                                                                                                                      | [models.PatchStorageBucketLifecycleRuleObjectStorageData](../../models/patchstoragebucketlifecycleruleobjectstoragedata.md) | :heavy_check_mark:                                                                                                          | N/A                                                                                                                         |
| `retries`                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                            | :heavy_minus_sign:                                                                                                          | Configuration to override the default retry behavior of the client.                                                         |

### Response

**[models.PatchStorageBucketLifecycleRuleResponseBody](../../models/patchstoragebucketlifecycleruleresponsebody.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 403, 404, 422            | application/vnd.api+json |
| models.ErrorObject       | 500                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## get_storage_bucket_metrics

Retrieves usage metrics for a specific object storage bucket, including storage consumption and estimated cost for the current billing period.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-storage-bucket-metrics" method="get" path="/storage/buckets/{bucket_id}/metrics" example="Success" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER"),
) as latitudesh:

    res = latitudesh.object_storage.get_storage_bucket_metrics(bucket_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `bucket_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The object storage bucket ID                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetStorageBucketMetricsResponseBody](../../models/getstoragebucketmetricsresponsebody.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 404                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |