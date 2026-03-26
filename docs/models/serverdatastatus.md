# ServerDataStatus

`on` - The server is powered ON
`off` - The server is powered OFF
`unknown` - The server power status is unknown
`disk_erasing` - The server is in reinstalling state `disk_erasing`
`deploying` - The server is deploying or reinstalling
`failed_deployment` - The server has failed deployment or reinstall
`rescue_mode` - The server is in rescue mode


## Example Usage

```python
from latitudesh_python_sdk.models import ServerDataStatus

value = ServerDataStatus.ON
```


## Values

| Name                | Value               |
| ------------------- | ------------------- |
| `ON`                | on                  |
| `OFF`               | off                 |
| `UNKNOWN`           | unknown             |
| `DISK_ERASING`      | disk_erasing        |
| `DEPLOYING`         | deploying           |
| `FAILED_DEPLOYMENT` | failed_deployment   |
| `RESCUE_MODE`       | rescue_mode         |