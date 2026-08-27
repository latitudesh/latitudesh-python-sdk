# DeploymentStrategy

How the app is delivered: cloud-init install on a stock OS image (user_data) or a pre-built disk image (image)

## Example Usage

```python
from latitudesh_python_sdk.models import DeploymentStrategy

value = DeploymentStrategy.USER_DATA
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `USER_DATA` | user_data   |
| `IMAGE`     | image       |