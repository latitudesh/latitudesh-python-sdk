# EventsSDK
(*events*)

## Overview

### Available Operations

* [get_events](#get_events) - List all Events

## get_events

Lists all events.


### Example Usage

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.events.get_events()

    # Handle response
    print(res)

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
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[models.GetEventsResponseBody](../../models/geteventsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |