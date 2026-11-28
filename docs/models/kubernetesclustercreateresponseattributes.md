# KubernetesClusterCreateResponseAttributes


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `name`                                                 | *str*                                                  | :heavy_check_mark:                                     | The cluster name                                       |
| `status`                                               | *str*                                                  | :heavy_check_mark:                                     | The cluster status (always 'provisioning' on creation) |
| `control_plane_endpoint`                               | *OptionalNullable[str]*                                | :heavy_minus_sign:                                     | The URL endpoint for the Kubernetes API server         |