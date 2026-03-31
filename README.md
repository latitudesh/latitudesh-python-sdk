# latitudesh-python-sdk

Developer-friendly & type-safe Python SDK specifically catered to leverage *latitudesh-python-sdk* API.

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=latitudesh-python-sdk&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


<!-- Start Summary [summary] -->
## Summary

Latitude.sh API: The Latitude.sh API is a RESTful API to manage your Latitude.sh account. It allows you to perform the same actions as the Latitude.sh dashboard.
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [latitudesh-python-sdk](#latitudesh-python-sdk)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Pagination](#pagination)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install git+https://github.com/latitudesh/latitudesh-python-sdk.git
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add git+https://github.com/latitudesh/latitudesh-python-sdk.git
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from latitudesh-python-sdk python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "latitudesh-python-sdk",
# ]
# ///

from latitudesh_python_sdk import Latitudesh

sdk = Latitudesh(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add latitudesh-python-sdk
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install latitudesh-python-sdk
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add latitudesh-python-sdk
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from latitudesh-python-sdk python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "latitudesh-python-sdk",
# ]
# ///

from latitudesh_python_sdk import Latitudesh

sdk = Latitudesh(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.api_keys.list()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from latitudesh_python_sdk import Latitudesh
import os

async def main():

    async with Latitudesh(
        bearer=os.getenv("LATITUDESH_BEARER", ""),
    ) as latitudesh:

        res = await latitudesh.api_keys.list_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name     | Type   | Scheme  | Environment Variable |
| -------- | ------ | ------- | -------------------- |
| `bearer` | apiKey | API key | `LATITUDESH_BEARER`  |

To authenticate with the API the `bearer` parameter must be set when initializing the SDK client instance. For example:
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.api_keys.list()

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [ApiKeys](docs/sdks/apikeyssdk/README.md)

* [list](docs/sdks/apikeyssdk/README.md#list) - List API keys
* [create](docs/sdks/apikeyssdk/README.md#create) - Create API key
* [regenerate](docs/sdks/apikeyssdk/README.md#regenerate) - Rotate API key
* [delete](docs/sdks/apikeyssdk/README.md#delete) - Delete API key
* [update_api_key](docs/sdks/apikeyssdk/README.md#update_api_key) - Update API key settings

### [Billing](docs/sdks/billing/README.md)

* [list_usage](docs/sdks/billing/README.md#list_usage) - Retrieve billing usage

### [ElasticIps](docs/sdks/elasticipssdk/README.md)

* [list_elastic_ips](docs/sdks/elasticipssdk/README.md#list_elastic_ips) - List Elastic IPs
* [create_elastic_ip](docs/sdks/elasticipssdk/README.md#create_elastic_ip) - Create an Elastic IP
* [get_elastic_ip](docs/sdks/elasticipssdk/README.md#get_elastic_ip) - Retrieve an Elastic IP
* [delete_elastic_ip](docs/sdks/elasticipssdk/README.md#delete_elastic_ip) - Release an Elastic IP
* [update_elastic_ip](docs/sdks/elasticipssdk/README.md#update_elastic_ip) - Move an Elastic IP

### [Events](docs/sdks/eventssdk/README.md)

* [list](docs/sdks/eventssdk/README.md#list) - List events

### [Firewalls](docs/sdks/firewallssdk/README.md)

* [get_all_firewall_assignments](docs/sdks/firewallssdk/README.md#get_all_firewall_assignments) - List firewall assignments
* [create](docs/sdks/firewallssdk/README.md#create) - Create firewall
* [list](docs/sdks/firewallssdk/README.md#list) - List firewalls
* [get](docs/sdks/firewallssdk/README.md#get) - Retrieve firewall
* [update](docs/sdks/firewallssdk/README.md#update) - Update firewall
* [delete](docs/sdks/firewallssdk/README.md#delete) - Delete firewall
* [assign](docs/sdks/firewallssdk/README.md#assign) - Assign server to firewall
* [list_assignments](docs/sdks/firewallssdk/README.md#list_assignments) - Firewall assignments
* [delete_assignment](docs/sdks/firewallssdk/README.md#delete_assignment) - Delete assignment

### [IpAddresses](docs/sdks/ipaddressessdk/README.md)

* [list](docs/sdks/ipaddressessdk/README.md#list) - List IPs
* [get](docs/sdks/ipaddressessdk/README.md#get) - Retrieve an IP

### [KubernetesClusters](docs/sdks/kubernetesclusterssdk/README.md)

* [list_kubernetes_clusters](docs/sdks/kubernetesclusterssdk/README.md#list_kubernetes_clusters) - List Kubernetes Clusters
* [create_kubernetes_cluster](docs/sdks/kubernetesclusterssdk/README.md#create_kubernetes_cluster) - Create a Kubernetes Cluster
* [get_kubernetes_cluster](docs/sdks/kubernetesclusterssdk/README.md#get_kubernetes_cluster) - Get a Kubernetes Cluster
* [delete_kubernetes_cluster](docs/sdks/kubernetesclusterssdk/README.md#delete_kubernetes_cluster) - Delete a Kubernetes Cluster
* [update_kubernetes_cluster](docs/sdks/kubernetesclusterssdk/README.md#update_kubernetes_cluster) - Scale Kubernetes Cluster
* [get_kubernetes_cluster_kubeconfig](docs/sdks/kubernetesclusterssdk/README.md#get_kubernetes_cluster_kubeconfig) - Get Kubernetes Cluster Kubeconfig

### [OperatingSystems](docs/sdks/operatingsystemssdk/README.md)

* [list](docs/sdks/operatingsystemssdk/README.md#list) - List operating systems

### [Plans](docs/sdks/plans/README.md)

* [list](docs/sdks/plans/README.md#list) - List plans
* [get](docs/sdks/plans/README.md#get) - Retrieve plan
* [list_bandwidth](docs/sdks/plans/README.md#list_bandwidth) - List bandwidth plans
* [update_bandwidth](docs/sdks/plans/README.md#update_bandwidth) - Update bandwidth packages
* [list_storage](docs/sdks/plans/README.md#list_storage) - List storage plans
* [list_vm_plans](docs/sdks/plans/README.md#list_vm_plans) - List VM plans

### [PrivateNetworks](docs/sdks/privatenetworks/README.md)

* [list](docs/sdks/privatenetworks/README.md#list) - List VLANs
* [create](docs/sdks/privatenetworks/README.md#create) - Create VLAN
* [update](docs/sdks/privatenetworks/README.md#update) - Update VLAN
* [delete_virtual_network](docs/sdks/privatenetworks/README.md#delete_virtual_network) - Delete VLAN
* [get](docs/sdks/privatenetworks/README.md#get) - Retrieve VLAN
* [list_assignments](docs/sdks/privatenetworks/README.md#list_assignments) - List VLAN assignments
* [assign](docs/sdks/privatenetworks/README.md#assign) - Assign VLAN
* [remove_assignment](docs/sdks/privatenetworks/README.md#remove_assignment) - Delete VLAN assignment

### [Projects](docs/sdks/projectssdk/README.md)

* [list](docs/sdks/projectssdk/README.md#list) - List projects
* [create](docs/sdks/projectssdk/README.md#create) - Create project
* [update](docs/sdks/projectssdk/README.md#update) - Update project
* [delete](docs/sdks/projectssdk/README.md#delete) - Delete project

### [Regions](docs/sdks/regionssdk/README.md)

* [list](docs/sdks/regionssdk/README.md#list) - List regions
* [get](docs/sdks/regionssdk/README.md#get) - Retrieve region

### [Roles](docs/sdks/roles/README.md)

* [list](docs/sdks/roles/README.md#list) - List roles
* [get](docs/sdks/roles/README.md#get) - Retrieve role

### [Servers](docs/sdks/serverssdk/README.md)

* [list](docs/sdks/serverssdk/README.md#list) - List servers
* [create](docs/sdks/serverssdk/README.md#create) - Create server
* [get](docs/sdks/serverssdk/README.md#get) - Retrieve server
* [update](docs/sdks/serverssdk/README.md#update) - Update server
* [delete](docs/sdks/serverssdk/README.md#delete) - Remove server
* [get_deploy_config](docs/sdks/serverssdk/README.md#get_deploy_config) - Retrieve deploy config
* [update_deploy_config](docs/sdks/serverssdk/README.md#update_deploy_config) - Update deploy config
* [lock](docs/sdks/serverssdk/README.md#lock) - Lock server
* [unlock](docs/sdks/serverssdk/README.md#unlock) - Unlock server
* [create_out_of_band_connection](docs/sdks/serverssdk/README.md#create_out_of_band_connection) - Create out-of-band connection
* [list_out_of_band_connections](docs/sdks/serverssdk/README.md#list_out_of_band_connections) - List out-of-band connections
* [actions](docs/sdks/serverssdk/README.md#actions) - Run power action
* [create_ipmi_session](docs/sdks/serverssdk/README.md#create_ipmi_session) - Create IPMI credentials
* [start_rescue_mode](docs/sdks/serverssdk/README.md#start_rescue_mode) - Put server in rescue mode
* [exit_rescue_mode](docs/sdks/serverssdk/README.md#exit_rescue_mode) - Exits rescue mode
* [schedule_deletion](docs/sdks/serverssdk/README.md#schedule_deletion) - Schedule server deletion
* [unschedule_deletion](docs/sdks/serverssdk/README.md#unschedule_deletion) - Unschedule server deletion
* [reinstall](docs/sdks/serverssdk/README.md#reinstall) - Run Server Reinstall

### [SshKeys](docs/sdks/sshkeyssdk/README.md)

* [~~list_for_project~~](docs/sdks/sshkeyssdk/README.md#list_for_project) - List SSH Keys :warning: **Deprecated**
* [~~create~~](docs/sdks/sshkeyssdk/README.md#create) - Create SSH Key :warning: **Deprecated**
* [~~get~~](docs/sdks/sshkeyssdk/README.md#get) - Retrieve Project SSH Key :warning: **Deprecated**
* [~~update~~](docs/sdks/sshkeyssdk/README.md#update) - Update Project SSH Key :warning: **Deprecated**
* [~~delete~~](docs/sdks/sshkeyssdk/README.md#delete) - Delete Project SSH Key :warning: **Deprecated**
* [get_ssh_keys](docs/sdks/sshkeyssdk/README.md#get_ssh_keys) - List SSH Keys
* [post_ssh_key](docs/sdks/sshkeyssdk/README.md#post_ssh_key) - Create SSH Key
* [get_ssh_key](docs/sdks/sshkeyssdk/README.md#get_ssh_key) - Retrieve SSH Key
* [delete_ssh_key](docs/sdks/sshkeyssdk/README.md#delete_ssh_key) - Delete SSH Key
* [put_ssh_key](docs/sdks/sshkeyssdk/README.md#put_ssh_key) - Update SSH Key

### [Storage](docs/sdks/storage/README.md)

* [create_filesystem](docs/sdks/storage/README.md#create_filesystem) - Create filesystem
* [list_filesystems](docs/sdks/storage/README.md#list_filesystems) - List filesystems
* [delete_filesystem](docs/sdks/storage/README.md#delete_filesystem) - Delete filesystem
* [update_filesystem](docs/sdks/storage/README.md#update_filesystem) - Update filesystem
* [get_storage_volumes](docs/sdks/storage/README.md#get_storage_volumes) - List volumes
* [post_storage_volumes](docs/sdks/storage/README.md#post_storage_volumes) - Create volume
* [get_storage_volume](docs/sdks/storage/README.md#get_storage_volume) - Retrieve volume
* [delete_storage_volumes](docs/sdks/storage/README.md#delete_storage_volumes) - Delete volume
* [post_storage_volumes_mount](docs/sdks/storage/README.md#post_storage_volumes_mount) - Mount volume
* [get_storage_objects](docs/sdks/storage/README.md#get_storage_objects) - List object storages
* [post_storage_objects](docs/sdks/storage/README.md#post_storage_objects) - Create object storage
* [get_storage_object](docs/sdks/storage/README.md#get_storage_object) - Retrieve object storage
* [delete_storage_objects](docs/sdks/storage/README.md#delete_storage_objects) - Delete object storage

### [Tags](docs/sdks/tags/README.md)

* [list](docs/sdks/tags/README.md#list) - List tags
* [create](docs/sdks/tags/README.md#create) - Create tag
* [update](docs/sdks/tags/README.md#update) - Update tag
* [delete](docs/sdks/tags/README.md#delete) - Delete tag

### [Teams](docs/sdks/teamssdk/README.md)

* [get](docs/sdks/teamssdk/README.md#get) - Retrieve team
* [create](docs/sdks/teamssdk/README.md#create) - Create team
* [update](docs/sdks/teamssdk/README.md#update) - Update team

### [TeamsMembers](docs/sdks/teamsmembers/README.md)

* [list](docs/sdks/teamsmembers/README.md#list) - List members
* [add](docs/sdks/teamsmembers/README.md#add) - Create member
* [remove_member](docs/sdks/teamsmembers/README.md#remove_member) - Remove a member

### [Traffic](docs/sdks/trafficsdk/README.md)

* [get](docs/sdks/trafficsdk/README.md#get) - Retrieve traffic
* [get_quota](docs/sdks/trafficsdk/README.md#get_quota) - Retrieve traffic quota

### [UserData](docs/sdks/userdatasdk/README.md)

* [~~list_project_user_data~~](docs/sdks/userdatasdk/README.md#list_project_user_data) - List Project user data :warning: **Deprecated**
* [~~create~~](docs/sdks/userdatasdk/README.md#create) - Create Project user data :warning: **Deprecated**
* [~~get_project_user_data~~](docs/sdks/userdatasdk/README.md#get_project_user_data) - Retrieve Project user data :warning: **Deprecated**
* [~~update~~](docs/sdks/userdatasdk/README.md#update) - Update Project user data :warning: **Deprecated**
* [~~delete~~](docs/sdks/userdatasdk/README.md#delete) - Delete Project user data :warning: **Deprecated**
* [get_users_data](docs/sdks/userdatasdk/README.md#get_users_data) - List user data
* [post_user_data](docs/sdks/userdatasdk/README.md#post_user_data) - Create user data
* [get_user_data](docs/sdks/userdatasdk/README.md#get_user_data) - Retrieve user data
* [delete_user_data](docs/sdks/userdatasdk/README.md#delete_user_data) - Delete user data
* [patch_user_data](docs/sdks/userdatasdk/README.md#patch_user_data) - Update user data

### [UserProfile](docs/sdks/userprofile/README.md)

* [get](docs/sdks/userprofile/README.md#get) - Retrieve profile
* [update](docs/sdks/userprofile/README.md#update) - Update profile
* [list_teams](docs/sdks/userprofile/README.md#list_teams) - List user teams

### [VirtualMachines](docs/sdks/virtualmachinessdk/README.md)

* [create](docs/sdks/virtualmachinessdk/README.md#create) - Create VM
* [list](docs/sdks/virtualmachinessdk/README.md#list) - List VMs
* [get](docs/sdks/virtualmachinessdk/README.md#get) - Retrieve VM
* [delete](docs/sdks/virtualmachinessdk/README.md#delete) - Destroy VM
* [update_virtual_machine](docs/sdks/virtualmachinessdk/README.md#update_virtual_machine) - Update VM
* [create_virtual_machine_action](docs/sdks/virtualmachinessdk/README.md#create_virtual_machine_action) - Run VM power action

### [VpnSessions](docs/sdks/vpnsessions/README.md)

* [list](docs/sdks/vpnsessions/README.md#list) - List VPN sessions
* [create](docs/sdks/vpnsessions/README.md#create) - Create VPN session
* [refresh_password](docs/sdks/vpnsessions/README.md#refresh_password) - Refresh VPN session
* [delete](docs/sdks/vpnsessions/README.md#delete) - Delete VPN session

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Pagination [pagination] -->
## Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:
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
<!-- End Pagination [pagination] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from latitudesh_python_sdk import Latitudesh
from latitudesh_python_sdk.utils import BackoffStrategy, RetryConfig
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.api_keys.list(,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from latitudesh_python_sdk import Latitudesh
from latitudesh_python_sdk.utils import BackoffStrategy, RetryConfig
import os


with Latitudesh(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.api_keys.list()

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`LatitudeshError`](./src/latitudesh_python_sdk/models/latitudesherror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](#error-classes). |

### Example
```python
import latitudesh_python_sdk
from latitudesh_python_sdk import Latitudesh, models
import os


with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:
    res = None
    try:

        res = latitudesh.elastic_ips.create_elastic_ip(data={
            "type": latitudesh_python_sdk.CreateElasticIPType.ELASTIC_IPS,
            "attributes": {
                "project_id": "proj_AoW6vRnwkvLn0",
                "server_id": "sv_2GmAlJ6BXlK1a",
            },
        })

        # Handle response
        print(res)


    except models.LatitudeshError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, models.ErrorObject):
            print(e.data.errors)  # Optional[List[latitudesh_python_sdk.Errors]]
```

### Error Classes
**Primary error:**
* [`LatitudeshError`](./src/latitudesh_python_sdk/models/latitudesherror.py): The base class for HTTP error responses.

<details><summary>Less common errors (6)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`LatitudeshError`](./src/latitudesh_python_sdk/models/latitudesherror.py)**:
* [`ErrorObject`](./src/latitudesh_python_sdk/models/errorobject.py): Applicable to 18 of 128 methods.*
* [`ResponseValidationError`](./src/latitudesh_python_sdk/models/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

\* Check [the method documentation](#available-resources-and-operations) to see if the error is applicable.
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| #   | Server                    | Variables          | Description |
| --- | ------------------------- | ------------------ | ----------- |
| 0   | `https://api.latitude.sh` | `latitude_api_key` |             |
| 1   | `http://api.latitude.sh`  | `latitude_api_key` |             |

If the selected server has variables, you may override its default values through the additional parameters made available in the SDK constructor:

| Variable           | Parameter               | Default                        | Description |
| ------------------ | ----------------------- | ------------------------------ | ----------- |
| `latitude_api_key` | `latitude_api_key: str` | `"<insert your api key here>"` |             |

#### Example

```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    server_idx=0,
    latitude_api_key="<insert your api key here>",
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.api_keys.list()

    # Handle response
    print(res)

```

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from latitudesh_python_sdk import Latitudesh
import os


with Latitudesh(
    server_url="http://api.latitude.sh",
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.api_keys.list()

    # Handle response
    print(res)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from latitudesh_python_sdk import Latitudesh
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Latitudesh(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from latitudesh_python_sdk import Latitudesh
from latitudesh_python_sdk.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Latitudesh(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Latitudesh` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from latitudesh_python_sdk import Latitudesh
import os
def main():

    with Latitudesh(
        bearer=os.getenv("LATITUDESH_BEARER", ""),
    ) as latitudesh:
        # Rest of application here...


# Or when using async:
async def amain():

    async with Latitudesh(
        bearer=os.getenv("LATITUDESH_BEARER", ""),
    ) as latitudesh:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from latitudesh_python_sdk import Latitudesh
import logging

logging.basicConfig(level=logging.DEBUG)
s = Latitudesh(debug_logger=logging.getLogger("latitudesh_python_sdk"))
```

You can also enable a default debug logger by setting an environment variable `LATITUDESH_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=latitudesh-python-sdk&utm_campaign=python)
