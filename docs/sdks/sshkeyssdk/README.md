# SSHKeysSDK
(*ssh_keys*)

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

```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.ssh_keys.list_for_project(project_id="proj_lxWpD6a9qm6rk", filter_tags="tag_JzoXbwJ7KgFM2J4wALjXHbVrjX4")

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

```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.ssh_keys.create(project_id="proj_wg3ZDrMyq5QlP", data={
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

```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.ssh_keys.get(project_id="proj_k0RyqvrJqW36X", ssh_key_id="ssh_j0L6WO1QOPlXy")

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

```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.ssh_keys.update(project_id="proj_5xyZOnMvDWM0l", ssh_key_id="ssh_5AEmq71XOBkWX", data={
        "id": "ssh_5AEmq71XOBkWX",
        "type": latitudesh_python_sdk.PutProjectSSHKeySSHKeysType.SSH_KEYS,
        "attributes": {
            "tags": [
                "tag_yle6pegwz1hlpaP3EPMkt7zgpX3",
                "tag_z6Qarmr4r4c3lxAmbwkYSVpNv62",
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

```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.ssh_keys.delete(project_id="proj_KN4ydzeXOVob3", ssh_key_id="ssh_kjQwdEGNDYNVP")

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

```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.ssh_keys.get_ssh_keys()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                   | Type                                                                                                                        | Required                                                                                                                    | Description                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `filter_tags`                                                                                                               | *Optional[str]*                                                                                                             | :heavy_minus_sign:                                                                                                          | The tags ids to filter by, separated by comma, e.g. `filter[tags]=tag_1,tag_2`will return ssh keys with `tag_1` AND `tag_2` |
| `retries`                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                            | :heavy_minus_sign:                                                                                                          | Configuration to override the default retry behavior of the client.                                                         |

### Response

**[models.SSHKeys](../../models/sshkeys.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## post_ssh_key

Allow you create SSH Keys in a project. These keys can be used to access servers after deploy and reinstall actions.


### Example Usage

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

```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.ssh_keys.get_ssh_key(ssh_key_id="ssh_zGr47qlMDAg0m")

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

Allow you update SSH Key in a project. These keys can be used to access servers after deploy and reinstall actions.


### Example Usage

```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.ssh_keys.put_ssh_key(ssh_key_id="ssh_ez2A3DVldnawP", data={
        "id": "ssh_ez2A3DVldnawP",
        "type": latitudesh_python_sdk.PutSSHKeySSHKeysType.SSH_KEYS,
        "attributes": {
            "tags": [
                "tag_jj4Xpjj143f0Z5JM8Zp1TKpM6a9",
                "tag_6P4w2joLYGSpxlGZ6zrkSe6WJoe",
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

Allow you remove SSH Keys in a project. Remove a SSH Key from the project won't revoke the SSH Keys access for previously deploy and reinstall actions.


### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.ssh_keys.delete_ssh_key(ssh_key_id="ssh_zlkg1DegdvZE5")

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