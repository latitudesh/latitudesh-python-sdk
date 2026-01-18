# Tags

## Overview

### Available Operations

* [list](#list) - List all Tags
* [create](#create) - Create a Tag
* [update](#update) - Update Tag
* [delete](#delete) - Delete Tag

## list

List all Tags in the team.


### Example Usage

<!-- UsageSnippet language="python" operationID="get-tags" method="get" path="/tags" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.tags.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CustomTags](../../models/customtags.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create

Create a Tag in the team.


### Example Usage

<!-- UsageSnippet language="python" operationID="create-tag" method="post" path="/tags" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.tags.create(data={
        "type": latitudesh_python_sdk.CreateTagTagsType.TAGS,
        "attributes": {
            "name": "Tag Name",
            "description": "Tag Description",
            "color": "#bebebe",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `data`                                                                  | [Optional[models.CreateTagTagsData]](../../models/createtagtagsdata.md) | :heavy_minus_sign:                                                      | N/A                                                                     |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.CustomTag](../../models/customtag.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update

Update a Tag in the team.


### Example Usage

<!-- UsageSnippet language="python" operationID="update-tag" method="patch" path="/tags/{tag_id}" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.tags.update(tag_id="tag_XBlke2r5RyiyVpG9LPK8tWjalLL", data={
        "id": "tag_XBlke2r5RyiyVpG9LPK8tWjalLL",
        "type": latitudesh_python_sdk.UpdateTagTagsType.TAGS,
        "attributes": {
            "name": "Tag Name",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `tag_id`                                                                | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `data`                                                                  | [Optional[models.UpdateTagTagsData]](../../models/updatetagtagsdata.md) | :heavy_minus_sign:                                                      | N/A                                                                     |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.CustomTag](../../models/customtag.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete

Update a Tag in the team.


### Example Usage

<!-- UsageSnippet language="python" operationID="destroy-tag" method="delete" path="/tags/{tag_id}" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    latitudesh.tags.delete(tag_id="invalid-id")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `tag_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |