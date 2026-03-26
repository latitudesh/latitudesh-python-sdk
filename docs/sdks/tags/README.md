# Tags

## Overview

### Available Operations

* [list](#list) - List tags
* [create](#create) - Create tag
* [update](#update) - Update tag
* [delete](#delete) - Delete tag

## list

List all Tags in the team.


### Example Usage

<!-- UsageSnippet language="python" operationID="get-tags" method="get" path="/tags" example="Success" -->
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


### Example Usage: Created

<!-- UsageSnippet language="python" operationID="create-tag" method="post" path="/tags" example="Created" -->
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
### Example Usage: NameAlreadyTaken

<!-- UsageSnippet language="python" operationID="create-tag" method="post" path="/tags" example="NameAlreadyTaken" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.tags.create()

    # Handle response
    print(res)

```
### Example Usage: NameTooSimilar

<!-- UsageSnippet language="python" operationID="create-tag" method="post" path="/tags" example="NameTooSimilar" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.tags.create()

    # Handle response
    print(res)

```
### Example Usage: when any attribute is missing or not filled

<!-- UsageSnippet language="python" operationID="create-tag" method="post" path="/tags" example="when any attribute is missing or not filled" -->
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
            "description": "",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: when color is in wrong format

<!-- UsageSnippet language="python" operationID="create-tag" method="post" path="/tags" example="when color is in wrong format" -->
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
            "color": "bebebe",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: when description is too long

<!-- UsageSnippet language="python" operationID="create-tag" method="post" path="/tags" example="when description is too long" -->
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
            "description": "lj553vy8r5j831s7dp78fscnq4z0iv9jjwtkeudrpsdsefghd2w3cd6b5qb3knpq6bin7uurf5qj1ya4xd2yhyzv6o4krqirha1aoubs0nvc04jd21hdp9etq6g3a4o7vb8ol0avqc2j4hlbw5o6yqxa2vsm9jhyf5kt9wy78gxr7jlaol3bxe18xau5fcff3b9qjmy14b2nw5tjynjefh1kjdmfmsn0wu1tg32mr563ndefj3y24j0cyyrlbl7b",
            "color": "#bebebe",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: when name is already taken

<!-- UsageSnippet language="python" operationID="create-tag" method="post" path="/tags" example="when name is already taken" -->
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
            "name": "Argon",
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

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 422                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## update

Update a Tag in the team.


### Example Usage: NameAlreadyTaken

<!-- UsageSnippet language="python" operationID="update-tag" method="patch" path="/tags/{tag_id}" example="NameAlreadyTaken" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.tags.update(tag_id="<id>")

    # Handle response
    print(res)

```
### Example Usage: NameTooSimilar

<!-- UsageSnippet language="python" operationID="update-tag" method="patch" path="/tags/{tag_id}" example="NameTooSimilar" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.tags.update(tag_id="<id>")

    # Handle response
    print(res)

```
### Example Usage: Not Found

<!-- UsageSnippet language="python" operationID="update-tag" method="patch" path="/tags/{tag_id}" example="Not Found" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.tags.update(tag_id="invalid", data={
        "id": "invalid",
        "type": latitudesh_python_sdk.UpdateTagTagsType.TAGS,
        "attributes": {
            "name": "Tag Name",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Success

<!-- UsageSnippet language="python" operationID="update-tag" method="patch" path="/tags/{tag_id}" example="Success" -->
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
### Example Usage: when any attribute is blank

<!-- UsageSnippet language="python" operationID="update-tag" method="patch" path="/tags/{tag_id}" example="when any attribute is blank" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.tags.update(tag_id="tag_X0oz3V4bB4Cy94Wm3G0MfWga24B", data={
        "id": "tag_X0oz3V4bB4Cy94Wm3G0MfWga24B",
        "type": latitudesh_python_sdk.UpdateTagTagsType.TAGS,
        "attributes": {
            "name": "",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: when color is invalid

<!-- UsageSnippet language="python" operationID="update-tag" method="patch" path="/tags/{tag_id}" example="when color is invalid" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.tags.update(tag_id="tag_pppwBaKxmacw7eJmMEJ2tj8o7Lb", data={
        "id": "tag_pppwBaKxmacw7eJmMEJ2tj8o7Lb",
        "type": latitudesh_python_sdk.UpdateTagTagsType.TAGS,
        "attributes": {
            "color": "bebebe",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: when description is too long

<!-- UsageSnippet language="python" operationID="update-tag" method="patch" path="/tags/{tag_id}" example="when description is too long" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.tags.update(tag_id="tag_K5G3oWwnPbfjVJ2v4V3xSbEMex0", data={
        "id": "tag_K5G3oWwnPbfjVJ2v4V3xSbEMex0",
        "type": latitudesh_python_sdk.UpdateTagTagsType.TAGS,
        "attributes": {
            "description": "sdfil1bdxt8hoe5tf0q54af15q2984xhaxmyqzkqr945acgllrmy1h7nrqy70lvz3lfiqla2on8ulx12949f6ffejxog1x5hzj5ec2eqkx1keeabd5k4b4jrfa0yzpii9a04xevll2r1530u2yzjexvqku7budmlmrp5y5o2ypxpds5wh2o69hjkpjw7fapf1lafjdibw6f5xd8n730qjh40eh9rqujovey0xovs7rn6b4w3qbjaxac48fcvr23e",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: when name is already taken

<!-- UsageSnippet language="python" operationID="update-tag" method="patch" path="/tags/{tag_id}" example="when name is already taken" -->
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.tags.update(tag_id="tag_lPZ90rpX3PcJ8EYlyjrWCE9AyEk", data={
        "id": "tag_lPZ90rpX3PcJ8EYlyjrWCE9AyEk",
        "type": latitudesh_python_sdk.UpdateTagTagsType.TAGS,
        "attributes": {
            "name": "Tag Name 2",
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

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorObject       | 422                      | application/vnd.api+json |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

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