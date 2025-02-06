"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from latitudesh_python_sdk import models, utils
from latitudesh_python_sdk._hooks import HookContext
from latitudesh_python_sdk.types import OptionalNullable, UNSET
from latitudesh_python_sdk.utils import get_security_from_env
from typing import List, Mapping, Optional


class EventsSDK(BaseSDK):
    def get_events(
        self,
        *,
        filter_author: Optional[str] = None,
        filter_project: Optional[str] = None,
        filter_target_name: Optional[List[str]] = None,
        filter_target_id: Optional[str] = None,
        filter_action: Optional[str] = None,
        filter_created_at_gte: Optional[str] = None,
        filter_created_at_lte: Optional[str] = None,
        filter_created_at: Optional[List[str]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.GetEventsResponseBody:
        r"""List all Events

        Lists all events.


        :param filter_author: The author ID or email to filter by
        :param filter_project: The project ID to filter by
        :param filter_target_name: The target type(s) of the event to filter by
        :param filter_target_id: The target id of the event to filter by
        :param filter_action: The action performed in event to filter by
        :param filter_created_at_gte: The created at greater than equal date to filter by, in ISO formatting (yyyy-MM-dd'T'HH:mm:ss)
        :param filter_created_at_lte: The created at less than equal date to filter by, in ISO formatting (yyyy-MM-dd'T'HH:mm:ss)
        :param filter_created_at: The created at between date range date1, date2 (inclusive) to filter by, in ISO formatting (yyyy-MM-dd'T'HH:mm:ss)
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

        request = models.GetEventsRequest(
            filter_author=filter_author,
            filter_project=filter_project,
            filter_target_name=filter_target_name,
            filter_target_id=filter_target_id,
            filter_action=filter_action,
            filter_created_at_gte=filter_created_at_gte,
            filter_created_at_lte=filter_created_at_lte,
            filter_created_at=filter_created_at,
        )

        req = self._build_request(
            method="GET",
            path="/events",
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
                operation_id="get-events",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/vnd.api+json"):
            return utils.unmarshal_json(http_res.text, models.GetEventsResponseBody)
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def get_events_async(
        self,
        *,
        filter_author: Optional[str] = None,
        filter_project: Optional[str] = None,
        filter_target_name: Optional[List[str]] = None,
        filter_target_id: Optional[str] = None,
        filter_action: Optional[str] = None,
        filter_created_at_gte: Optional[str] = None,
        filter_created_at_lte: Optional[str] = None,
        filter_created_at: Optional[List[str]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.GetEventsResponseBody:
        r"""List all Events

        Lists all events.


        :param filter_author: The author ID or email to filter by
        :param filter_project: The project ID to filter by
        :param filter_target_name: The target type(s) of the event to filter by
        :param filter_target_id: The target id of the event to filter by
        :param filter_action: The action performed in event to filter by
        :param filter_created_at_gte: The created at greater than equal date to filter by, in ISO formatting (yyyy-MM-dd'T'HH:mm:ss)
        :param filter_created_at_lte: The created at less than equal date to filter by, in ISO formatting (yyyy-MM-dd'T'HH:mm:ss)
        :param filter_created_at: The created at between date range date1, date2 (inclusive) to filter by, in ISO formatting (yyyy-MM-dd'T'HH:mm:ss)
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

        request = models.GetEventsRequest(
            filter_author=filter_author,
            filter_project=filter_project,
            filter_target_name=filter_target_name,
            filter_target_id=filter_target_id,
            filter_action=filter_action,
            filter_created_at_gte=filter_created_at_gte,
            filter_created_at_lte=filter_created_at_lte,
            filter_created_at=filter_created_at,
        )

        req = self._build_request_async(
            method="GET",
            path="/events",
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
                operation_id="get-events",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/vnd.api+json"):
            return utils.unmarshal_json(http_res.text, models.GetEventsResponseBody)
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )
