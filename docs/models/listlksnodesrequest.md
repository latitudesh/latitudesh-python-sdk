# ListLksNodesRequest


## Fields

| Field                                                                             | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `cluster_id`                                                                      | *str*                                                                             | :heavy_check_mark:                                                                | The cluster ID (format: `lksc_<hash>`).                                           |
| `node_pool_id`                                                                    | *str*                                                                             | :heavy_check_mark:                                                                | The node pool ID (format: `lksnp_<hash>`).                                        |
| `filter_status`                                                                   | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | Only return nodes in this status: `pending`, `ready`, `not_ready`, or `deleting`. |