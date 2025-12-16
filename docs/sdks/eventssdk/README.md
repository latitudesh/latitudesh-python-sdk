# Events

## Overview

### Available Operations

* [list](#list) - List all Events

## list

Lists all events.


### Example Usage

<!-- UsageSnippet language="python" operationID="get-events" method="get" path="/events" -->
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.events.list(page_size=20, page_number=1)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `filter_author`                                                                                                    | *Optional[str]*                                                                                                    | :heavy_minus_sign:                                                                                                 | The author ID or email to filter by                                                                                |
| `filter_project`                                                                                                   | *Optional[str]*                                                                                                    | :heavy_minus_sign:                                                                                                 | The project ID to filter by                                                                                        |
| `filter_target_name`                                                                                               | List[*str*]                                                                                                        | :heavy_minus_sign:                                                                                                 | The target type(s) of the event to filter by                                                                       |
| `filter_target_id`                                                                                                 | *Optional[str]*                                                                                                    | :heavy_minus_sign:                                                                                                 | The target id of the event to filter by                                                                            |
| `filter_action`                                                                                                    | *Optional[str]*                                                                                                    | :heavy_minus_sign:                                                                                                 | The action performed in event to filter by                                                                         |
| `filter_created_at_gte`                                                                                            | *Optional[str]*                                                                                                    | :heavy_minus_sign:                                                                                                 | The created at greater than equal date to filter by, in ISO formatting (yyyy-MM-dd'T'HH:mm:ss)                     |
| `filter_created_at_lte`                                                                                            | *Optional[str]*                                                                                                    | :heavy_minus_sign:                                                                                                 | The created at less than equal date to filter by, in ISO formatting (yyyy-MM-dd'T'HH:mm:ss)                        |
| `filter_created_at`                                                                                                | List[*str*]                                                                                                        | :heavy_minus_sign:                                                                                                 | The created at between date range date1, date2 (inclusive) to filter by, in ISO formatting (yyyy-MM-dd'T'HH:mm:ss) |
| `page_size`                                                                                                        | *Optional[int]*                                                                                                    | :heavy_minus_sign:                                                                                                 | Number of items to return per page                                                                                 |
| `page_number`                                                                                                      | *Optional[int]*                                                                                                    | :heavy_minus_sign:                                                                                                 | Page number to return (starts at 1)                                                                                |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[models.GetEventsResponse](../../models/geteventsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |