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
    from .....models.shield.custom_waf_rule import CustomWafRule
    from .....models.shield.generic_request_response import GenericRequestResponse
    from .....models.shield.unauthorized_result import UnauthorizedResult
    from .....models.shield.update_custom_waf_rule_request import UpdateCustomWafRuleRequest

class CustomRuleItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /shield/waf/custom-rule/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new CustomRuleItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/shield/waf/custom-rule/{id}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[GenericRequestResponse]:
        """
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[GenericRequestResponse]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.shield.unauthorized_result import UnauthorizedResult

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "401": UnauthorizedResult,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.shield.generic_request_response import GenericRequestResponse

        return await self.request_adapter.send_async(request_info, GenericRequestResponse, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CustomWafRule]:
        """
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CustomWafRule]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.shield.unauthorized_result import UnauthorizedResult

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "401": UnauthorizedResult,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.shield.custom_waf_rule import CustomWafRule

        return await self.request_adapter.send_async(request_info, CustomWafRule, error_mapping)
    
    async def patch(self,body: UpdateCustomWafRuleRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CustomWafRule]:
        """
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CustomWafRule]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.shield.unauthorized_result import UnauthorizedResult

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "401": UnauthorizedResult,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.shield.custom_waf_rule import CustomWafRule

        return await self.request_adapter.send_async(request_info, CustomWafRule, error_mapping)
    
    async def put(self,body: UpdateCustomWafRuleRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CustomWafRule]:
        """
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CustomWafRule]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from .....models.shield.unauthorized_result import UnauthorizedResult

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "401": UnauthorizedResult,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.shield.custom_waf_rule import CustomWafRule

        return await self.request_adapter.send_async(request_info, CustomWafRule, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        return request_info
    
    def to_patch_request_information(self,body: UpdateCustomWafRuleRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def to_put_request_information(self,body: UpdateCustomWafRuleRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PUT, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> CustomRuleItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CustomRuleItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CustomRuleItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class CustomRuleItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CustomRuleItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CustomRuleItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CustomRuleItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

