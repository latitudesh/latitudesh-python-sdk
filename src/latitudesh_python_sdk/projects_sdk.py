"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from jsonpath import JSONPath
from latitudesh_python_sdk import models, utils
from latitudesh_python_sdk._hooks import HookContext
from latitudesh_python_sdk.types import OptionalNullable, UNSET
from latitudesh_python_sdk.utils import get_security_from_env
from latitudesh_python_sdk.utils.unmarshal_json_response import unmarshal_json_response
from typing import Any, Dict, List, Mapping, Optional, Union


class ProjectsSDK(BaseSDK):
    def list(
        self,
        *,
        filter_name: Optional[str] = None,
        filter_slug: Optional[str] = None,
        filter_description: Optional[str] = None,
        filter_billing_type: Optional[str] = None,
        filter_environment: Optional[str] = None,
        filter_tags: Optional[str] = None,
        extra_fields_projects: Optional[str] = None,
        page_size: Optional[int] = 20,
        page_number: Optional[int] = 1,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Optional[models.GetProjectsResponse]:
        r"""List all Projects

        Returns a list of all projects for the current team


        :param filter_name: The project name to filter by
        :param filter_slug: The project slug to filter by
        :param filter_description: The project description to filter by
        :param filter_billing_type: The billing type to filter by
        :param filter_environment: The environment to filter by
        :param filter_tags: The tags ids to filter by, separated by comma, e.g. `filter[tags]=tag_1,tag_2`will return projects with `tag_1` AND `tag_2`
        :param extra_fields_projects: The `last_renewal_date` and `next_renewal_date` are provided as extra attributes that show previous and future billing cycle dates. To request it, just set `extra_fields[projects]=last_renewal_date,next_renewal_date` in the query string.
        :param page_size: Number of items to return per page
        :param page_number: Page number to return (starts at 1)
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.GetProjectsRequest(
            filter_name=filter_name,
            filter_slug=filter_slug,
            filter_description=filter_description,
            filter_billing_type=filter_billing_type,
            filter_environment=filter_environment,
            filter_tags=filter_tags,
            extra_fields_projects=extra_fields_projects,
            page_size=page_size,
            page_number=page_number,
        )

        req = self._build_request(
            method="GET",
            path="/projects",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/vnd.api+json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                config=self.sdk_configuration,
                base_url=base_url or "",
                operation_id="get-projects",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            retry_config=retry_config,
        )

        def next_func() -> Optional[models.GetProjectsResponse]:
            body = utils.unmarshal_json(http_res.text, Union[Dict[Any, Any], List[Any]])
            page = request.page_number if not request.page_number is None else 1
            next_page = page + 1

            if not http_res.text:
                return None
            results = JSONPath("$.data").parse(body)
            if len(results) == 0 or len(results[0]) == 0:
                return None
            limit = request.page_size if not request.page_size is None else 20
            if len(results[0]) < limit:
                return None

            return self.list(
                filter_name=filter_name,
                filter_slug=filter_slug,
                filter_description=filter_description,
                filter_billing_type=filter_billing_type,
                filter_environment=filter_environment,
                filter_tags=filter_tags,
                extra_fields_projects=extra_fields_projects,
                page_size=page_size,
                page_number=next_page,
                retries=retries,
            )

        if utils.match_response(http_res, "200", "application/vnd.api+json"):
            return models.GetProjectsResponse(
                result=unmarshal_json_response(models.Projects, http_res),
                next=next_func,
            )
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError("API error occurred", http_res, http_res_text)
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError("API error occurred", http_res, http_res_text)

        raise models.APIError("Unexpected response received", http_res)

    async def list_async(
        self,
        *,
        filter_name: Optional[str] = None,
        filter_slug: Optional[str] = None,
        filter_description: Optional[str] = None,
        filter_billing_type: Optional[str] = None,
        filter_environment: Optional[str] = None,
        filter_tags: Optional[str] = None,
        extra_fields_projects: Optional[str] = None,
        page_size: Optional[int] = 20,
        page_number: Optional[int] = 1,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Optional[models.GetProjectsResponse]:
        r"""List all Projects

        Returns a list of all projects for the current team


        :param filter_name: The project name to filter by
        :param filter_slug: The project slug to filter by
        :param filter_description: The project description to filter by
        :param filter_billing_type: The billing type to filter by
        :param filter_environment: The environment to filter by
        :param filter_tags: The tags ids to filter by, separated by comma, e.g. `filter[tags]=tag_1,tag_2`will return projects with `tag_1` AND `tag_2`
        :param extra_fields_projects: The `last_renewal_date` and `next_renewal_date` are provided as extra attributes that show previous and future billing cycle dates. To request it, just set `extra_fields[projects]=last_renewal_date,next_renewal_date` in the query string.
        :param page_size: Number of items to return per page
        :param page_number: Page number to return (starts at 1)
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.GetProjectsRequest(
            filter_name=filter_name,
            filter_slug=filter_slug,
            filter_description=filter_description,
            filter_billing_type=filter_billing_type,
            filter_environment=filter_environment,
            filter_tags=filter_tags,
            extra_fields_projects=extra_fields_projects,
            page_size=page_size,
            page_number=page_number,
        )

        req = self._build_request_async(
            method="GET",
            path="/projects",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/vnd.api+json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                config=self.sdk_configuration,
                base_url=base_url or "",
                operation_id="get-projects",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            retry_config=retry_config,
        )

        def next_func() -> Optional[models.GetProjectsResponse]:
            body = utils.unmarshal_json(http_res.text, Union[Dict[Any, Any], List[Any]])
            page = request.page_number if not request.page_number is None else 1
            next_page = page + 1

            if not http_res.text:
                return None
            results = JSONPath("$.data").parse(body)
            if len(results) == 0 or len(results[0]) == 0:
                return None
            limit = request.page_size if not request.page_size is None else 20
            if len(results[0]) < limit:
                return None

            return self.list(
                filter_name=filter_name,
                filter_slug=filter_slug,
                filter_description=filter_description,
                filter_billing_type=filter_billing_type,
                filter_environment=filter_environment,
                filter_tags=filter_tags,
                extra_fields_projects=extra_fields_projects,
                page_size=page_size,
                page_number=next_page,
                retries=retries,
            )

        if utils.match_response(http_res, "200", "application/vnd.api+json"):
            return models.GetProjectsResponse(
                result=unmarshal_json_response(models.Projects, http_res),
                next=next_func,
            )
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError("API error occurred", http_res, http_res_text)
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError("API error occurred", http_res, http_res_text)

        raise models.APIError("Unexpected response received", http_res)

    def create(
        self,
        *,
        data: Optional[
            Union[
                models.CreateProjectProjectsData,
                models.CreateProjectProjectsDataTypedDict,
            ]
        ] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.CreateProjectResponseBody:
        r"""Create a Project

        :param data:
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.CreateProjectProjectsRequestBody(
            data=utils.get_pydantic_model(
                data, Optional[models.CreateProjectProjectsData]
            ),
        )

        req = self._build_request(
            method="POST",
            path="/projects",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/vnd.api+json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, False, "json", models.CreateProjectProjectsRequestBody
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                config=self.sdk_configuration,
                base_url=base_url or "",
                operation_id="create-project",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "403", "422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "201", "application/vnd.api+json"):
            return unmarshal_json_response(models.CreateProjectResponseBody, http_res)
        if utils.match_response(
            http_res, ["400", "403", "422"], "application/vnd.api+json"
        ):
            response_data = unmarshal_json_response(models.ErrorObjectData, http_res)
            raise models.ErrorObject(response_data, http_res)
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError("API error occurred", http_res, http_res_text)
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError("API error occurred", http_res, http_res_text)

        raise models.APIError("Unexpected response received", http_res)

    async def create_async(
        self,
        *,
        data: Optional[
            Union[
                models.CreateProjectProjectsData,
                models.CreateProjectProjectsDataTypedDict,
            ]
        ] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.CreateProjectResponseBody:
        r"""Create a Project

        :param data:
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.CreateProjectProjectsRequestBody(
            data=utils.get_pydantic_model(
                data, Optional[models.CreateProjectProjectsData]
            ),
        )

        req = self._build_request_async(
            method="POST",
            path="/projects",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/vnd.api+json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, False, "json", models.CreateProjectProjectsRequestBody
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                config=self.sdk_configuration,
                base_url=base_url or "",
                operation_id="create-project",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "403", "422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "201", "application/vnd.api+json"):
            return unmarshal_json_response(models.CreateProjectResponseBody, http_res)
        if utils.match_response(
            http_res, ["400", "403", "422"], "application/vnd.api+json"
        ):
            response_data = unmarshal_json_response(models.ErrorObjectData, http_res)
            raise models.ErrorObject(response_data, http_res)
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError("API error occurred", http_res, http_res_text)
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError("API error occurred", http_res, http_res_text)

        raise models.APIError("Unexpected response received", http_res)

    def update(
        self,
        *,
        project_id: str,
        data: Union[
            models.UpdateProjectProjectsData, models.UpdateProjectProjectsDataTypedDict
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.UpdateProjectResponseBody:
        r"""Update a Project

        :param project_id: The project ID or Slug
        :param data:
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.UpdateProjectRequest(
            project_id=project_id,
            request_body=models.UpdateProjectProjectsRequestBody(
                data=utils.get_pydantic_model(data, models.UpdateProjectProjectsData),
            ),
        )

        req = self._build_request(
            method="PATCH",
            path="/projects/{project_id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/vnd.api+json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request.request_body,
                False,
                True,
                "json",
                Optional[models.UpdateProjectProjectsRequestBody],
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                config=self.sdk_configuration,
                base_url=base_url or "",
                operation_id="update-project",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["403", "404", "422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "200", "application/vnd.api+json"):
            return unmarshal_json_response(models.UpdateProjectResponseBody, http_res)
        if utils.match_response(
            http_res, ["403", "404", "422"], "application/vnd.api+json"
        ):
            response_data = unmarshal_json_response(models.ErrorObjectData, http_res)
            raise models.ErrorObject(response_data, http_res)
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError("API error occurred", http_res, http_res_text)
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError("API error occurred", http_res, http_res_text)

        raise models.APIError("Unexpected response received", http_res)

    async def update_async(
        self,
        *,
        project_id: str,
        data: Union[
            models.UpdateProjectProjectsData, models.UpdateProjectProjectsDataTypedDict
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.UpdateProjectResponseBody:
        r"""Update a Project

        :param project_id: The project ID or Slug
        :param data:
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.UpdateProjectRequest(
            project_id=project_id,
            request_body=models.UpdateProjectProjectsRequestBody(
                data=utils.get_pydantic_model(data, models.UpdateProjectProjectsData),
            ),
        )

        req = self._build_request_async(
            method="PATCH",
            path="/projects/{project_id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/vnd.api+json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request.request_body,
                False,
                True,
                "json",
                Optional[models.UpdateProjectProjectsRequestBody],
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                config=self.sdk_configuration,
                base_url=base_url or "",
                operation_id="update-project",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["403", "404", "422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "200", "application/vnd.api+json"):
            return unmarshal_json_response(models.UpdateProjectResponseBody, http_res)
        if utils.match_response(
            http_res, ["403", "404", "422"], "application/vnd.api+json"
        ):
            response_data = unmarshal_json_response(models.ErrorObjectData, http_res)
            raise models.ErrorObject(response_data, http_res)
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError("API error occurred", http_res, http_res_text)
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError("API error occurred", http_res, http_res_text)

        raise models.APIError("Unexpected response received", http_res)

    def delete(
        self,
        *,
        project_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ):
        r"""Delete a Project

        :param project_id: The project ID or Slug
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.DeleteProjectRequest(
            project_id=project_id,
        )

        req = self._build_request(
            method="DELETE",
            path="/projects/{project_id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/vnd.api+json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                config=self.sdk_configuration,
                base_url=base_url or "",
                operation_id="delete-project",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["403", "404", "422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "204", "*"):
            return
        if utils.match_response(
            http_res, ["403", "404", "422"], "application/vnd.api+json"
        ):
            response_data = unmarshal_json_response(models.ErrorObjectData, http_res)
            raise models.ErrorObject(response_data, http_res)
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError("API error occurred", http_res, http_res_text)
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError("API error occurred", http_res, http_res_text)

        raise models.APIError("Unexpected response received", http_res)

    async def delete_async(
        self,
        *,
        project_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ):
        r"""Delete a Project

        :param project_id: The project ID or Slug
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.DeleteProjectRequest(
            project_id=project_id,
        )

        req = self._build_request_async(
            method="DELETE",
            path="/projects/{project_id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/vnd.api+json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                config=self.sdk_configuration,
                base_url=base_url or "",
                operation_id="delete-project",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["403", "404", "422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "204", "*"):
            return
        if utils.match_response(
            http_res, ["403", "404", "422"], "application/vnd.api+json"
        ):
            response_data = unmarshal_json_response(models.ErrorObjectData, http_res)
            raise models.ErrorObject(response_data, http_res)
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError("API error occurred", http_res, http_res_text)
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError("API error occurred", http_res, http_res_text)

        raise models.APIError("Unexpected response received", http_res)
