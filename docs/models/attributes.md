# Attributes


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `name`                                                               | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Name of the API Key                                                  |
| `api_version`                                                        | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The API version associated with this API Key                         |
| `token_last_slice`                                                   | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The last 5 characters of the token created for this API Key          |
| `last_used_at`                                                       | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | The last time a request was made to the API using this API Key       |
| `user`                                                               | [Optional[models.APIKeyUser]](../models/apikeyuser.md)               | :heavy_minus_sign:                                                   | The owner of the API Key                                             |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | The time when the API Key was created                                |
| `updated_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | The time when the API Key was updated                                |