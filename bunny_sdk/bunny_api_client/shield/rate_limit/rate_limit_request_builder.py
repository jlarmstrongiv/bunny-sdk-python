from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ...models.shield.create_waf_rate_limit_request import CreateWafRateLimitRequest
    from ...models.shield.custom_waf_rule import CustomWafRule
    from ...models.shield.unauthorized_result import UnauthorizedResult
    from .item.rate_limit_item_request_builder import RateLimitItemRequestBuilder

class RateLimitRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /shield/rate-limit
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new RateLimitRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/shield/rate-limit", path_parameters)
    
    def by_id(self,id: int) -> RateLimitItemRequestBuilder:
        """
        Gets an item from the BunnyApiClient.shield.rateLimit.item collection
        param id: Unique identifier of the item
        Returns: RateLimitItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.rate_limit_item_request_builder import RateLimitItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return RateLimitItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: CreateWafRateLimitRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CustomWafRule]:
        """
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CustomWafRule]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ...models.shield.unauthorized_result import UnauthorizedResult

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "401": UnauthorizedResult,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.shield.custom_waf_rule import CustomWafRule

        return await self.request_adapter.send_async(request_info, CustomWafRule, error_mapping)
    
    def to_post_request_information(self,body: CreateWafRateLimitRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> RateLimitRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: RateLimitRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return RateLimitRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class RateLimitRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

