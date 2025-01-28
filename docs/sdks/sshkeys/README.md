# SSHKeys
(*ssh_keys*)

## Overview

### Available Operations

* [get_project_ssh_keys](#get_project_ssh_keys) - List all Project SSH Keys
* [post_project_ssh_key](#post_project_ssh_key) - Create a Project SSH Key
* [get_project_ssh_key](#get_project_ssh_key) - Retrieve a Project SSH Key
* [put_project_ssh_key](#put_project_ssh_key) - Update a Project SSH Key
* [delete_project_ssh_key](#delete_project_ssh_key) - Delete a Project SSH Key

## get_project_ssh_keys

List all SSH Keys in the project. These keys can be used to access servers after deploy and reinstall actions.


### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.ssh_keys.get_project_ssh_keys(project_id="proj_v9BVDaN5ORm1W", filter_tags="tag_K3oJoeZZzxcjJjkRAYNetrEAbJgj")

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

**[models.SSHKey](../../models/sshkey.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## post_project_ssh_key

Allow you create SSH Keys in a project. These keys can be used to access servers after deploy and reinstall actions.


### Example Usage

```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.ssh_keys.post_project_ssh_key(project_id="proj_e8pKq0BGOWAob", data={
        "type": latitudesh_python_sdk.PostProjectSSHKeyType.SSH_KEYS,
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
| `project_id`                                                          | *str*                                                                 | :heavy_check_mark:                                                    | Project ID or Slug                                                    |
| `data`                                                                | [models.PostProjectSSHKeyData](../../models/postprojectsshkeydata.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.PostProjectSSHKeyResponseBody](../../models/postprojectsshkeyresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_project_ssh_key

List all SSH Keys in the project. These keys can be used to access servers after deploy and reinstall actions.


### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.ssh_keys.get_project_ssh_key(project_id="proj_LYV8DZW1O5QoE", ssh_key_id="ssh_j0L6WO1QOPlXy")

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

## put_project_ssh_key

Allow you update SSH Key in a project. These keys can be used to access servers after deploy and reinstall actions.


### Example Usage

```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.ssh_keys.put_project_ssh_key(project_id="proj_KXgRdRMKOv9k5", ssh_key_id="ssh_5AEmq71XOBkWX", data={
        "type": latitudesh_python_sdk.PutProjectSSHKeyType.SSH_KEYS,
        "id": "ssh_5AEmq71XOBkWX",
        "attributes": {
            "tags": [
                "tag_oe32gQbvrbszzPGaL7EEiJXvynQ",
                "tag_5rgE2mnBYpFzG9eGN7E8C67b2eMe",
            ],
            "name": "New SSH Key Name",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Project ID or Slug                                                  |
| `ssh_key_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `data`                                                              | [models.PutProjectSSHKeyData](../../models/putprojectsshkeydata.md) | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PutProjectSSHKeyResponseBody](../../models/putprojectsshkeyresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete_project_ssh_key

Allow you remove SSH Keys in a project. Remove a SSH Key from the project won't revoke the SSH Keys access for previously deploy and reinstall actions.


### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.ssh_keys.delete_project_ssh_key(project_id="proj_1R3zq28EOWxyn", ssh_key_id="ssh_kjQwdEGNDYNVP")

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