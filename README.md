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

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!TIP]
> To finish publishing your SDK to PyPI you must [run your first generation action](https://www.speakeasy.com/docs/github-setup#step-by-step-guide).


> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install git+<UNSET>.git
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add git+<UNSET>.git
```
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

    res = latitudesh.api_keys.get_api_keys()

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

        res = await latitudesh.api_keys.get_api_keys_async()

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

    res = latitudesh.api_keys.get_api_keys()

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [api_keys](docs/sdks/apikeys/README.md)

* [get_api_keys](docs/sdks/apikeys/README.md#get_api_keys) - List API Keys
* [post_api_key](docs/sdks/apikeys/README.md#post_api_key) - Create API Key
* [update_api_key](docs/sdks/apikeys/README.md#update_api_key) - Regenerate API Key
* [delete_api_key](docs/sdks/apikeys/README.md#delete_api_key) - Delete API Key

### [billing](docs/sdks/billing/README.md)

* [get_billing_usage](docs/sdks/billing/README.md#get_billing_usage) - List Billing Usage

### [events](docs/sdks/eventssdk/README.md)

* [get_events](docs/sdks/eventssdk/README.md#get_events) - List all Events

### [firewalls](docs/sdks/firewallssdk/README.md)

* [create_firewall](docs/sdks/firewallssdk/README.md#create_firewall) - Create a firewall
* [list_firewalls](docs/sdks/firewallssdk/README.md#list_firewalls) - List firewalls
* [get_firewall](docs/sdks/firewallssdk/README.md#get_firewall) - Retrieve Firewall
* [update_firewall](docs/sdks/firewallssdk/README.md#update_firewall) - Update Firewall
* [delete_firewall](docs/sdks/firewallssdk/README.md#delete_firewall) - Delete Firewall
* [create_firewall_assignment](docs/sdks/firewallssdk/README.md#create_firewall_assignment) - Firewall Assignment
* [get_firewall_assignments](docs/sdks/firewallssdk/README.md#get_firewall_assignments) - Firewall Assignments
* [delete_firewall_assignment](docs/sdks/firewallssdk/README.md#delete_firewall_assignment) - Delete Firewall Assignment

### [ip_addresses](docs/sdks/ipaddressessdk/README.md)

* [get_ips](docs/sdks/ipaddressessdk/README.md#get_ips) - List IPs
* [get_ip](docs/sdks/ipaddressessdk/README.md#get_ip) - Retrieve an IP


### [operating_systems](docs/sdks/operatingsystemssdk/README.md)

* [get_plans_operating_system](docs/sdks/operatingsystemssdk/README.md#get_plans_operating_system) - List all operating systems available

### [plans](docs/sdks/plans/README.md)

* [get_plans](docs/sdks/plans/README.md#get_plans) - List all Plans
* [get_plan](docs/sdks/plans/README.md#get_plan) - Retrieve a Plan
* [get_bandwidth_plans](docs/sdks/plans/README.md#get_bandwidth_plans) - List all bandwidth plans
* [update_plans_bandwidth](docs/sdks/plans/README.md#update_plans_bandwidth) - Buy or remove bandwidth packages
* [get_storage_plans](docs/sdks/plans/README.md#get_storage_plans) - List all Storage Plans

### [private_networks](docs/sdks/privatenetworks/README.md)

* [get_virtual_networks](docs/sdks/privatenetworks/README.md#get_virtual_networks) - List all Virtual Networks
* [create_virtual_network](docs/sdks/privatenetworks/README.md#create_virtual_network) - Create a Virtual Network
* [update_virtual_network](docs/sdks/privatenetworks/README.md#update_virtual_network) - Update a Virtual Network
* [destroy_virtual_network](docs/sdks/privatenetworks/README.md#destroy_virtual_network) - Delete a Virtual Network
* [get_virtual_network](docs/sdks/privatenetworks/README.md#get_virtual_network) - Retrieve a Virtual Network
* [get_virtual_networks_assignments](docs/sdks/privatenetworks/README.md#get_virtual_networks_assignments) - List all servers assigned to virtual networks
* [assign_server_virtual_network](docs/sdks/privatenetworks/README.md#assign_server_virtual_network) - Assign Virtual network
* [delete_virtual_networks_assignments](docs/sdks/privatenetworks/README.md#delete_virtual_networks_assignments) - Delete Virtual Network Assignment

### [projects](docs/sdks/projectssdk/README.md)

* [get_projects](docs/sdks/projectssdk/README.md#get_projects) - List all Projects
* [create_project](docs/sdks/projectssdk/README.md#create_project) - Create a Project
* [update_project](docs/sdks/projectssdk/README.md#update_project) - Update a Project
* [delete_project](docs/sdks/projectssdk/README.md#delete_project) - Delete a Project

### [regions](docs/sdks/regionssdk/README.md)

* [get_regions](docs/sdks/regionssdk/README.md#get_regions) - List all Regions
* [get_region](docs/sdks/regionssdk/README.md#get_region) - Retrieve a Region

### [roles](docs/sdks/roles/README.md)

* [get_roles](docs/sdks/roles/README.md#get_roles) - List all Roles
* [get_role_id](docs/sdks/roles/README.md#get_role_id) - Retrieve Role

### [servers](docs/sdks/serverssdk/README.md)

* [get_servers](docs/sdks/serverssdk/README.md#get_servers) - List all Servers
* [create_server](docs/sdks/serverssdk/README.md#create_server) - Deploy Server
* [get_server](docs/sdks/serverssdk/README.md#get_server) - Retrieve a Server
* [update_server](docs/sdks/serverssdk/README.md#update_server) - Update Server
* [destroy_server](docs/sdks/serverssdk/README.md#destroy_server) - Remove Server
* [get_server_deploy_config](docs/sdks/serverssdk/README.md#get_server_deploy_config) - Retrieve Deploy Config
* [update_server_deploy_config](docs/sdks/serverssdk/README.md#update_server_deploy_config) - Update Deploy Config
* [server_lock](docs/sdks/serverssdk/README.md#server_lock) - Lock the server
* [server_unlock](docs/sdks/serverssdk/README.md#server_unlock) - Unlock the server
* [create_server_out_of_band](docs/sdks/serverssdk/README.md#create_server_out_of_band) - Start Out of Band Connection
* [get_server_out_of_band](docs/sdks/serverssdk/README.md#get_server_out_of_band) - List Out of Band Connections
* [create_server_action](docs/sdks/serverssdk/README.md#create_server_action) - Run Server Action
* [create_ipmi_session](docs/sdks/serverssdk/README.md#create_ipmi_session) - Generate IPMI credentials
* [server_start_rescue_mode](docs/sdks/serverssdk/README.md#server_start_rescue_mode) - Puts a Server in rescue mode
* [server_exit_rescue_mode](docs/sdks/serverssdk/README.md#server_exit_rescue_mode) - Exits rescue mode for a Server
* [server_schedule_deletion](docs/sdks/serverssdk/README.md#server_schedule_deletion) - Schedule the server deletion
* [server_unschedule_deletion](docs/sdks/serverssdk/README.md#server_unschedule_deletion) - Unschedule the server deletion
* [create_server_reinstall](docs/sdks/serverssdk/README.md#create_server_reinstall) - Run Server Reinstall

### [ssh_keys](docs/sdks/sshkeys/README.md)

* [get_project_ssh_keys](docs/sdks/sshkeys/README.md#get_project_ssh_keys) - List all Project SSH Keys
* [post_project_ssh_key](docs/sdks/sshkeys/README.md#post_project_ssh_key) - Create a Project SSH Key
* [get_project_ssh_key](docs/sdks/sshkeys/README.md#get_project_ssh_key) - Retrieve a Project SSH Key
* [put_project_ssh_key](docs/sdks/sshkeys/README.md#put_project_ssh_key) - Update a Project SSH Key
* [delete_project_ssh_key](docs/sdks/sshkeys/README.md#delete_project_ssh_key) - Delete a Project SSH Key

### [storage](docs/sdks/storage/README.md)

* [post_storage_filesystems](docs/sdks/storage/README.md#post_storage_filesystems) - Create a filesystem for a project
* [get_storage_filesystems](docs/sdks/storage/README.md#get_storage_filesystems) - List filesystems
* [delete_storage_filesystems](docs/sdks/storage/README.md#delete_storage_filesystems) - Delete a filesystem for a project
* [patch_storage_filesystems](docs/sdks/storage/README.md#patch_storage_filesystems) - Update a filesystem for a project

### [tags](docs/sdks/tags/README.md)

* [get_tags](docs/sdks/tags/README.md#get_tags) - List all Tags
* [create_tag](docs/sdks/tags/README.md#create_tag) - Create a Tag
* [update_tag](docs/sdks/tags/README.md#update_tag) - Update Tag
* [destroy_tag](docs/sdks/tags/README.md#destroy_tag) - Delete Tag

### [teams](docs/sdks/teamssdk/README.md)

* [get_team](docs/sdks/teamssdk/README.md#get_team) - Retrieve the team
* [post_team](docs/sdks/teamssdk/README.md#post_team) - Create a team
* [patch_current_team](docs/sdks/teamssdk/README.md#patch_current_team) - Update a team

### [teams_members](docs/sdks/teamsmembers/README.md)

* [get_team_members](docs/sdks/teamsmembers/README.md#get_team_members) - List all Team Members
* [post_team_members](docs/sdks/teamsmembers/README.md#post_team_members) - Add a Team Member
* [destroy_team_member](docs/sdks/teamsmembers/README.md#destroy_team_member) - Remove a Team Member

### [traffic](docs/sdks/trafficsdk/README.md)

* [get_traffic_consumption](docs/sdks/trafficsdk/README.md#get_traffic_consumption) - Retrieve Traffic consumption
* [get_traffic_quota](docs/sdks/trafficsdk/README.md#get_traffic_quota) - Retrieve Traffic Quota

### [user_data](docs/sdks/userdatasdk/README.md)

* [get_project_users_data](docs/sdks/userdatasdk/README.md#get_project_users_data) - List all Project User Data
* [post_project_user_data](docs/sdks/userdatasdk/README.md#post_project_user_data) - Create a Project User Data
* [get_project_user_data](docs/sdks/userdatasdk/README.md#get_project_user_data) - Retrieve a Project User Data
* [put_project_user_data](docs/sdks/userdatasdk/README.md#put_project_user_data) - Update a Project User Data
* [delete_project_user_data](docs/sdks/userdatasdk/README.md#delete_project_user_data) - Delete a Project User Data

### [user_profile](docs/sdks/userprofile/README.md)

* [get_user_profile](docs/sdks/userprofile/README.md#get_user_profile) - Get user profile
* [patch_user_profile](docs/sdks/userprofile/README.md#patch_user_profile) - Update User Profile
* [get_user_teams](docs/sdks/userprofile/README.md#get_user_teams) - List User Teams

### [vpn_sessions](docs/sdks/vpnsessions/README.md)

* [get_vpn_sessions](docs/sdks/vpnsessions/README.md#get_vpn_sessions) - List all Active VPN Sessions
* [post_vpn_session](docs/sdks/vpnsessions/README.md#post_vpn_session) - Create a VPN Session
* [put_vpn_session](docs/sdks/vpnsessions/README.md#put_vpn_session) - Refresh a VPN Session
* [delete_vpn_session](docs/sdks/vpnsessions/README.md#delete_vpn_session) - Delete a VPN Session

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

    res = latitudesh.api_keys.get_api_keys(,
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

    res = latitudesh.api_keys.get_api_keys()

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

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `post_api_key_async` method may raise the following exceptions:

| Error Type         | Status Code | Content Type     |
| ------------------ | ----------- | ---------------- |
| models.ErrorObject | 400, 422    | application/json |
| models.APIError    | 4XX, 5XX    | \*/\*            |

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

        res = latitudesh.api_keys.post_api_key(request={
            "data": {
                "type": latitudesh_python_sdk.CreateAPIKeyType.API_KEYS,
                "attributes": {
                    "name": "App Token",
                },
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

| #   | Server                    | Variables               | Default values                 |
| --- | ------------------------- | ----------------------- | ------------------------------ |
| 0   | `https://api.latitude.sh` | `latitude_api_key: str` | `"<insert your api key here>"` |
| 1   | `http://api.latitude.sh`  | `latitude_api_key: str` | `"<insert your api key here>"` |

If the selected server has variables, you may override their default values through the additional parameters made available in the SDK constructor.

#### Example

```python
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    server_idx=1,
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.api_keys.get_api_keys()

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

    res = latitudesh.api_keys.get_api_keys()

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
