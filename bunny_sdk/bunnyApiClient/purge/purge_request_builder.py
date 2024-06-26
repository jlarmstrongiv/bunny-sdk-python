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

class PurgeRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /purge
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new PurgeRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/purge?async={async}&headerName={headerName}&headerValue={headerValue}&url={url}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[PurgeRequestBuilderGetQueryParameters]] = None) -> bytes:
        """
        [PurgeUrlGet API Docs](https://docs.bunny.net/reference/purgepublic_index)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", None)
    
    async def post(self,request_configuration: Optional[RequestConfiguration[PurgeRequestBuilderPostQueryParameters]] = None) -> bytes:
        """
        [PurgeUrlPost API Docs](https://docs.bunny.net/reference/purgepublic_indexpost)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        request_info = self.to_post_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[PurgeRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        [PurgeUrlGet API Docs](https://docs.bunny.net/reference/purgepublic_index)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        return request_info
    
    def to_post_request_information(self,request_configuration: Optional[RequestConfiguration[PurgeRequestBuilderPostQueryParameters]] = None) -> RequestInformation:
        """
        [PurgeUrlPost API Docs](https://docs.bunny.net/reference/purgepublic_indexpost)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.POST, '{+baseurl}/purge?async={async}&url={url}', self.path_parameters)
        request_info.configure(request_configuration)
        return request_info
    
    def with_url(self,raw_url: str) -> PurgeRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PurgeRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return PurgeRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class PurgeRequestBuilderGetQueryParameters():
        """
        [PurgeUrlGet API Docs](https://docs.bunny.net/reference/purgepublic_index)
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "header_name":
                return "headerName"
            if original_name == "header_value":
                return "headerValue"
            if original_name == "async_":
                return "async_"
            if original_name == "url":
                return "url"
            return original_name
        
        async_: Optional[bool] = None

        header_name: Optional[str] = None

        header_value: Optional[str] = None

        url: Optional[str] = None

    
    @dataclass
    class PurgeRequestBuilderGetRequestConfiguration(RequestConfiguration[PurgeRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class PurgeRequestBuilderPostQueryParameters():
        """
        [PurgeUrlPost API Docs](https://docs.bunny.net/reference/purgepublic_indexpost)
        """
        async_: Optional[bool] = None

        url: Optional[str] = None

    
    @dataclass
    class PurgeRequestBuilderPostRequestConfiguration(RequestConfiguration[PurgeRequestBuilderPostQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

