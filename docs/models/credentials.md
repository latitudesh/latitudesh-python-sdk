# Credentials

Latest provisioning credentials, lazy loaded. Request it with `extra_fields[servers]=credentials`. Empty when the latest provisioning has no valid credentials.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `username`                                                           | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | N/A                                                                  |
| `password`                                                           | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | N/A                                                                  |
| `ssh_keys`                                                           | List[[models.ServerDataSSHKeys](../models/serverdatasshkeys.md)]     | :heavy_minus_sign:                                                   | N/A                                                                  |
| `expires_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |