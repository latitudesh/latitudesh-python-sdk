# SshKeys

## Overview

### Available Operations

* [~~list_for_project~~](#list_for_project) - List all Project SSH Keys :warning: **Deprecated**
* [~~create~~](#create) - Create a Project SSH Key :warning: **Deprecated**
* [~~get~~](#get) - Retrieve a Project SSH Key :warning: **Deprecated**
* [~~update~~](#update) - Update a Project SSH Key :warning: **Deprecated**
* [~~delete~~](#delete) - Delete a Project SSH Key :warning: **Deprecated**
* [get_ssh_keys](#get_ssh_keys) - List all SSH Keys
* [post_ssh_key](#post_ssh_key) - Create a SSH Key
* [get_ssh_key](#get_ssh_key) - Retrieve a SSH Key
* [put_ssh_key](#put_ssh_key) - Update a SSH Key
* [delete_ssh_key](#delete_ssh_key) - Delete a SSH Key

## ~~list_for_project~~

List all SSH Keys in the project. These keys can be used to access servers after deploy and reinstall actions.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-project-ssh-keys" method="get" path="/projects/{project_id}/ssh_keys" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.ssh_keys.list_for_project(project_id="proj_5AEmq7wMqBkWX", filter_tags="tag_5wKQ2Y9eoAi5plr4zlQ6tjl6rEw,tag_8GKKZ6B9MbtYl4K09gj4fXy9Nneg")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                   | Type                                                                                                                        | Required                                                                                                                    | Description                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `project_id`                                                                                                                | *str*                                                                                                                       | :heavy_check_mark:                                                                                                          | Project ID or Slug                                                                                                          |
| `filter_tags`                                                                                                               | *Optional[str]*                                                                                                             | :heavy_minus_sign:                                                                                                          | The tags ids to filter by, separated by comma, e.g. `filter[tags]=tag_1,tag_2`will return ssh keys with `tag_1` AND `tag_2` |
| `retries`                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                            | :heavy_minus_sign:                                                                                                          | Configuration to override the default retry behavior of the client.                                                         |

### Response

**[models.SSHKeys](../../models/sshkeys.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## ~~create~~

Allow you create SSH Keys in a project. These keys can be used to access servers after deploy and reinstall actions.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="post-project-ssh-key" method="post" path="/projects/{project_id}/ssh_keys" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.ssh_keys.create(project_id="proj_059EqYE2qQj8p", data={
        "type": latitudesh_python_sdk.PostProjectSSHKeySSHKeysType.SSH_KEYS,
        "attributes": {
            "name": "SSH Key",
            "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDOLFnjGP3Jsh1usHNS2EILgfqZNC9pOvNqBZqxH+qNAdZdQCzy2csMuiq+ZwLA8Mm4Vo5CvSgBHs/kuZRUKyTl+79YUMZIj8PhHzL4XbdqX1ZnAIklHWcJaveB0+UXLEPKGzFIFq+FkuwtiXQsVe5NnSpIDYgpzhqEs38NsnXvsubKphGUdARDhaxvMdUUl4YsAtLHKMzSyIvE6xwfTtIVwA9bZt/8GoBzrn9px9PEcf25Rgd2NhOYs3WYcZuwvRmfcFdi2vGhVqTPqL9n16R/n5jknxHYrTyqWNxJdpdvg2YqXpN7vnFNoOjYFD6EahJ0pF/+WL4tPCIkLfoaVaSx",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `project_id`                                                                        | *str*                                                                               | :heavy_check_mark:                                                                  | Project ID or Slug                                                                  |
| `data`                                                                              | [models.PostProjectSSHKeySSHKeysData](../../models/postprojectsshkeysshkeysdata.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.PostProjectSSHKeyResponseBody](../../models/postprojectsshkeyresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## ~~get~~

List all SSH Keys in the project. These keys can be used to access servers after deploy and reinstall actions.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-project-ssh-key" method="get" path="/projects/{project_id}/ssh_keys/{ssh_key_id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.ssh_keys.get(project_id="proj_kjQwdE0XOYNVP", ssh_key_id="ssh_zGr47qlMDAg0m")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Project ID or Slug                                                  |
| `ssh_key_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetProjectSSHKeyResponseBody](../../models/getprojectsshkeyresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## ~~update~~

Allow you update SSH Key in a project. These keys can be used to access servers after deploy and reinstall actions.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="put-project-ssh-key" method="patch" path="/projects/{project_id}/ssh_keys/{ssh_key_id}" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.ssh_keys.update(project_id="proj_v9BVDaR3ORm1W", ssh_key_id="ssh_zlkg1DegdvZE5", data={
        "id": "ssh_zlkg1DegdvZE5",
        "type": latitudesh_python_sdk.PutProjectSSHKeySSHKeysType.SSH_KEYS,
        "attributes": {
            "tags": [
                "tag_rB7B21L1QbiJ6yWYxQLmHWJE3GmR",
                "tag_57nzyG0Bn3c5wooyYyeLH1w9kmN",
            ],
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `project_id`                                                                      | *str*                                                                             | :heavy_check_mark:                                                                | Project ID or Slug                                                                |
| `ssh_key_id`                                                                      | *str*                                                                             | :heavy_check_mark:                                                                | N/A                                                                               |
| `data`                                                                            | [models.PutProjectSSHKeySSHKeysData](../../models/putprojectsshkeysshkeysdata.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.PutProjectSSHKeyResponseBody](../../models/putprojectsshkeyresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## ~~delete~~

Allow you remove SSH Keys in a project. Remove a SSH Key from the project won't revoke the SSH Keys access for previously deploy and reinstall actions.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-project-ssh-key" method="delete" path="/projects/{project_id}/ssh_keys/{ssh_key_id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.ssh_keys.delete(project_id="proj_LA73qk4wDaJ2o", ssh_key_id="ssh_7vYAZqGBdMQ94")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Project ID or Slug                                                  |
| `ssh_key_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_ssh_keys

List all SSH Keys in the project. These keys can be used to access servers after deploy and reinstall actions.


### Example Usage

<!-- UsageSnippet language="python" operationID="get-ssh-keys" method="get" path="/ssh_keys" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.ssh_keys.get_ssh_keys(filter_tags="tag_A06EMPEmKXhKBNKgWrv0CRZMN5a,tag_P7xlGZzYNZF4w3YXRrYMU7AjQEAX")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                   | Type                                                                                                                        | Required                                                                                                                    | Description                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `filter_project`                                                                                                            | *Optional[str]*                                                                                                             | :heavy_minus_sign:                                                                                                          | Project ID or slug                                                                                                          |
| `filter_scope`                                                                                                              | *Optional[str]*                                                                                                             | :heavy_minus_sign:                                                                                                          | Filter by scope: `project` (has projects), `team` (no projects), or empty (all)                                             |
| `filter_tags`                                                                                                               | *Optional[str]*                                                                                                             | :heavy_minus_sign:                                                                                                          | The tags ids to filter by, separated by comma, e.g. `filter[tags]=tag_1,tag_2`will return ssh keys with `tag_1` AND `tag_2` |
| `retries`                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                            | :heavy_minus_sign:                                                                                                          | Configuration to override the default retry behavior of the client.                                                         |

### Response

**[models.SSHKeys](../../models/sshkeys.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## post_ssh_key

Allows you create SSH Keys. These keys can be used to access servers after deploy and reinstall actions.


### Example Usage

<!-- UsageSnippet language="python" operationID="post-ssh-key" method="post" path="/ssh_keys" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.ssh_keys.post_ssh_key(data={
        "type": latitudesh_python_sdk.PostSSHKeySSHKeysType.SSH_KEYS,
        "attributes": {
            "name": "SSH Key",
            "project": "proj_z2A3DV4wdnawP",
            "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDOLFnjGP3Jsh1usHNS2EILgfqZNC9pOvNqBZqxH+qNAdZdQCzy2csMuiq+ZwLA8Mm4Vo5CvSgBHs/kuZRUKyTl+79YUMZIj8PhHzL4XbdqX1ZnAIklHWcJaveB0+UXLEPKGzFIFq+FkuwtiXQsVe5NnSpIDYgpzhqEs38NsnXvsubKphGUdARDhaxvMdUUl4YsAtLHKMzSyIvE6xwfTtIVwA9bZt/8GoBzrn9px9PEcf25Rgd2NhOYs3WYcZuwvRmfcFdi2vGhVqTPqL9n16R/n5jknxHYrTyqWNxJdpdvg2YqXpN7vnFNoOjYFD6EahJ0pF/+WL4tPCIkLfoaVaSx",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `data`                                                                | [models.PostSSHKeySSHKeysData](../../models/postsshkeysshkeysdata.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.PostSSHKeyResponseBody](../../models/postsshkeyresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_ssh_key

List all SSH Keys in the project. These keys can be used to access servers after deploy and reinstall actions.


### Example Usage

<!-- UsageSnippet language="python" operationID="get-ssh-key" method="get" path="/ssh_keys/{ssh_key_id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.ssh_keys.get_ssh_key(ssh_key_id="ssh_LYV8DZ12q5QoE")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ssh_key_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetSSHKeyResponseBody](../../models/getsshkeyresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## put_ssh_key

Allows you update SSH Key in a project. These keys can be used to access servers after deploy and reinstall actions.


### Example Usage

<!-- UsageSnippet language="python" operationID="put-ssh-key" method="patch" path="/ssh_keys/{ssh_key_id}" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.ssh_keys.put_ssh_key(ssh_key_id="ssh_GnzRD5xAqM5yw", data={
        "id": "ssh_GnzRD5xAqM5yw",
        "type": latitudesh_python_sdk.PutSSHKeySSHKeysType.SSH_KEYS,
        "attributes": {
            "tags": [
                "tag_JLA906BzyKHLyVJbJr8NH3QQbev",
                "tag_Yy7PJ68y22FoQyBppnW7FjNGX1k",
            ],
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ssh_key_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `data`                                                              | [models.PutSSHKeySSHKeysData](../../models/putsshkeysshkeysdata.md) | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PutSSHKeyResponseBody](../../models/putsshkeyresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete_ssh_key

Allows you remove SSH Keys in a project. Remove a SSH Key from the project won't revoke the SSH Keys access for previously deploy and reinstall actions.


### Example Usage

<!-- UsageSnippet language="python" operationID="delete-ssh-key" method="delete" path="/ssh_keys/{ssh_key_id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.ssh_keys.delete_ssh_key(ssh_key_id="ssh_KXgRdRa3Ov9k5")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ssh_key_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |