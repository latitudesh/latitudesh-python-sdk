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
* [latitudesh-python-sdk](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/#latitudesh-python-sdk)
  * [SDK Installation](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/#sdk-installation)
  * [IDE Support](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/#ide-support)
  * [SDK Example Usage](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/#sdk-example-usage)
  * [Authentication](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/#authentication)
  * [Available Resources and Operations](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/#available-resources-and-operations)
  * [Retries](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/#retries)
  * [Error Handling](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/#error-handling)
  * [Server Selection](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/#server-selection)
  * [Custom HTTP Client](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/#custom-http-client)
  * [Resource Management](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/#resource-management)
  * [Debugging](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/#debugging)
* [Development](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/#development)
  * [Maturity](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/#maturity)
  * [Contributions](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/#contributions)

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

The SDK can be installed with either *pip* or *poetry* package managers.

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

The same SDK client can also be used to make asychronous requests by importing asyncio.
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

### [api_keys](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/apikeys/README.md)

* [list](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/apikeys/README.md#list) - List API Keys
* [create](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/apikeys/README.md#create) - Create API Key
* [regenerate](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/apikeys/README.md#regenerate) - Regenerate API Key
* [delete](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/apikeys/README.md#delete) - Delete API Key

### [billing](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/billing/README.md)

* [list_usage](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/billing/README.md#list_usage) - List Billing Usage

### [events](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/eventssdk/README.md)

* [list](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/eventssdk/README.md#list) - List all Events

### [firewalls](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/firewallssdk/README.md)

* [create](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/firewallssdk/README.md#create) - Create a firewall
* [list](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/firewallssdk/README.md#list) - List firewalls
* [get](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/firewallssdk/README.md#get) - Retrieve Firewall
* [update](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/firewallssdk/README.md#update) - Update Firewall
* [delete](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/firewallssdk/README.md#delete) - Delete Firewall
* [assign](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/firewallssdk/README.md#assign) - Firewall Assignment
* [list_assignments](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/firewallssdk/README.md#list_assignments) - Firewall Assignments
* [delete_assignment](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/firewallssdk/README.md#delete_assignment) - Delete Firewall Assignment

### [ip_addresses](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/ipaddressessdk/README.md)

* [list](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/ipaddressessdk/README.md#list) - List IPs
* [get](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/ipaddressessdk/README.md#get) - Retrieve an IP


### [operating_systems](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/operatingsystemssdk/README.md)

* [list](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/operatingsystemssdk/README.md#list) - List all operating systems available

### [plans](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/plans/README.md)

* [list](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/plans/README.md#list) - List all Plans
* [get](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/plans/README.md#get) - Retrieve a Plan
* [list_bandwidth](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/plans/README.md#list_bandwidth) - List all bandwidth plans
* [update_bandwidth](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/plans/README.md#update_bandwidth) - Buy or remove bandwidth packages
* [list_storage](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/plans/README.md#list_storage) - List all Storage Plans
* [list_vm_plans](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/plans/README.md#list_vm_plans) - List all Virtual Machines Plans

### [private_networks](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/privatenetworks/README.md)

* [list](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/privatenetworks/README.md#list) - List all Virtual Networks
* [create](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/privatenetworks/README.md#create) - Create a Virtual Network
* [update](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/privatenetworks/README.md#update) - Update a Virtual Network
* [delete_virtual_network](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/privatenetworks/README.md#delete_virtual_network) - Delete a Virtual Network
* [get](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/privatenetworks/README.md#get) - Retrieve a Virtual Network
* [list_assignments](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/privatenetworks/README.md#list_assignments) - List all servers assigned to virtual networks
* [assign](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/privatenetworks/README.md#assign) - Assign Virtual network
* [remove_assignment](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/privatenetworks/README.md#remove_assignment) - Delete Virtual Network Assignment

### [projects](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/projectssdk/README.md)

* [list](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/projectssdk/README.md#list) - List all Projects
* [create](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/projectssdk/README.md#create) - Create a Project
* [update](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/projectssdk/README.md#update) - Update a Project
* [delete](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/projectssdk/README.md#delete) - Delete a Project

### [regions](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/regionssdk/README.md)

* [list](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/regionssdk/README.md#list) - List all Regions
* [get](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/regionssdk/README.md#get) - Retrieve a Region

### [roles](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/roles/README.md)

* [list](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/roles/README.md#list) - List all Roles
* [get](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/roles/README.md#get) - Retrieve Role

### [servers](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/serverssdk/README.md)

* [list](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/serverssdk/README.md#list) - List all Servers
* [create](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/serverssdk/README.md#create) - Deploy Server
* [get](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/serverssdk/README.md#get) - Retrieve a Server
* [update](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/serverssdk/README.md#update) - Update Server
* [delete](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/serverssdk/README.md#delete) - Remove Server
* [get_deploy_config](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/serverssdk/README.md#get_deploy_config) - Retrieve Deploy Config
* [update_deploy_config](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/serverssdk/README.md#update_deploy_config) - Update Deploy Config
* [lock](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/serverssdk/README.md#lock) - Lock the server
* [unlock](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/serverssdk/README.md#unlock) - Unlock the server
* [create_out_of_band_connection](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/serverssdk/README.md#create_out_of_band_connection) - Start Out of Band Connection
* [list_out_of_band_connections](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/serverssdk/README.md#list_out_of_band_connections) - List Out of Band Connections
* [actions](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/serverssdk/README.md#actions) - Run Server Action
* [create_ipmi_session](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/serverssdk/README.md#create_ipmi_session) - Generate IPMI credentials
* [start_rescue_mode](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/serverssdk/README.md#start_rescue_mode) - Puts a Server in rescue mode
* [exit_rescue_mode](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/serverssdk/README.md#exit_rescue_mode) - Exits rescue mode for a Server
* [schedule_deletion](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/serverssdk/README.md#schedule_deletion) - Schedule the server deletion
* [unschedule_deletion](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/serverssdk/README.md#unschedule_deletion) - Unschedule the server deletion
* [reinstall](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/serverssdk/README.md#reinstall) - Run Server Reinstall

### [ssh_keys](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/sshkeys/README.md)

* [list_for_project](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/sshkeys/README.md#list_for_project) - List all Project SSH Keys
* [create](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/sshkeys/README.md#create) - Create a Project SSH Key
* [get](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/sshkeys/README.md#get) - Retrieve a Project SSH Key
* [update](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/sshkeys/README.md#update) - Update a Project SSH Key
* [delete](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/sshkeys/README.md#delete) - Delete a Project SSH Key

### [storage](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/storage/README.md)

* [create_filesystem](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/storage/README.md#create_filesystem) - Create a filesystem for a project
* [list_filesystems](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/storage/README.md#list_filesystems) - List filesystems
* [delete_filesystem](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/storage/README.md#delete_filesystem) - Delete a filesystem for a project
* [update_filesystem](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/storage/README.md#update_filesystem) - Update a filesystem for a project

### [tags](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/tags/README.md)

* [list](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/tags/README.md#list) - List all Tags
* [create](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/tags/README.md#create) - Create a Tag
* [update](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/tags/README.md#update) - Update Tag
* [delete](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/tags/README.md#delete) - Delete Tag

### [teams](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/teamssdk/README.md)

* [get](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/teamssdk/README.md#get) - Retrieve the team
* [create](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/teamssdk/README.md#create) - Create a team
* [update](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/teamssdk/README.md#update) - Update a team

### [teams_members](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/teamsmembers/README.md)

* [list](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/teamsmembers/README.md#list) - List all Team Members
* [add](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/teamsmembers/README.md#add) - Add a Team Member
* [remove_member](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/teamsmembers/README.md#remove_member) - Remove a Team Member

### [traffic](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/trafficsdk/README.md)

* [get](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/trafficsdk/README.md#get) - Retrieve Traffic consumption
* [get_quota](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/trafficsdk/README.md#get_quota) - Retrieve Traffic Quota

### [user_data](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/userdatasdk/README.md)

* [list_project_user_data](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/userdatasdk/README.md#list_project_user_data) - List all Project User Data
* [create](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/userdatasdk/README.md#create) - Create a Project User Data
* [get_project_user_data](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/userdatasdk/README.md#get_project_user_data) - Retrieve a Project User Data
* [update](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/userdatasdk/README.md#update) - Update a Project User Data
* [delete](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/userdatasdk/README.md#delete) - Delete a Project User Data

### [user_profile](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/userprofile/README.md)

* [get](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/userprofile/README.md#get) - Get user profile
* [update](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/userprofile/README.md#update) - Update User Profile
* [list_teams](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/userprofile/README.md#list_teams) - List User Teams

### [virtual_machines](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/virtualmachines/README.md)

* [create](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/virtualmachines/README.md#create) - Create a Virtual Machine
* [list](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/virtualmachines/README.md#list) - Get Teams Virtual Machines
* [get](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/virtualmachines/README.md#get) - Get a Virtual Machine
* [delete](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/virtualmachines/README.md#delete) - Destroy a Virtual Machine

### [vpn_sessions](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/vpnsessions/README.md)

* [list](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/vpnsessions/README.md#list) - List all Active VPN Sessions
* [create](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/vpnsessions/README.md#create) - Create a VPN Session
* [refresh_password](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/vpnsessions/README.md#refresh_password) - Refresh a VPN Session
* [delete](https://github.com/latitudesh/latitudesh-python-sdk/blob/master/docs/sdks/vpnsessions/README.md#delete) - Delete a VPN Session

</details>
<!-- End Available Resources and Operations [operations] -->

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

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a models.APIError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `create_async` method may raise the following exceptions:

| Error Type         | Status Code | Content Type             |
| ------------------ | ----------- | ------------------------ |
| models.ErrorObject | 400, 422    | application/vnd.api+json |
| models.APIError    | 4XX, 5XX    | \*/\*                    |

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

        res = latitudesh.api_keys.create(request={
            "data": {
                "type": latitudesh_python_sdk.CreateAPIKeyType.API_KEYS,
                "attributes": {},
            },
        })

        # Handle response
        print(res)

    except models.ErrorObject as e:
        # handle e.data: models.ErrorObjectData
        raise(e)
    except models.APIError as e:
        # handle exception
        raise(e)
```
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
    server_idx=1,
    latitude_api_key="<value>"
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
    server_url="https://api.latitude.sh",
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
