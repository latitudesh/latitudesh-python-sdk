# KubernetesClusterCreateResponseAttributes


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `name`                                                 | *Optional[str]*                                        | :heavy_minus_sign:                                     | The cluster name                                       |
| `status`                                               | *Optional[str]*                                        | :heavy_minus_sign:                                     | The cluster status (always 'provisioning' on creation) |
| `control_plane_endpoint`                               | *OptionalNullable[str]*                                | :heavy_minus_sign:                                     | The URL endpoint for the Kubernetes API server         |