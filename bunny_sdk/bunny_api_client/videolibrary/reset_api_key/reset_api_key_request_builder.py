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

class ResetApiKeyRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /videolibrary/resetApiKey
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new ResetApiKeyRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/videolibrary/resetApiKey?id={id}", path_parameters)
    
    async def post(self,request_configuration: Optional[RequestConfiguration[ResetApiKeyRequestBuilderPostQueryParameters]] = None) -> None:
        """
        [ResetPasswordQuery API Docs](https://docs.bunny.net/reference/videolibrarypublic_resetpassword)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_post_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, None)
    
    def to_post_request_information(self,request_configuration: Optional[RequestConfiguration[ResetApiKeyRequestBuilderPostQueryParameters]] = None) -> RequestInformation:
        """
        [ResetPasswordQuery API Docs](https://docs.bunny.net/reference/videolibrarypublic_resetpassword)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        return request_info
    
    def with_url(self,raw_url: str) -> ResetApiKeyRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ResetApiKeyRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ResetApiKeyRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ResetApiKeyRequestBuilderPostQueryParameters():
        """
        [ResetPasswordQuery API Docs](https://docs.bunny.net/reference/videolibrarypublic_resetpassword)
        """
        # The ID of the Video Library that should have the password reset
        id: Optional[int] = None

    
    @dataclass
    class ResetApiKeyRequestBuilderPostRequestConfiguration(RequestConfiguration[ResetApiKeyRequestBuilderPostQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

