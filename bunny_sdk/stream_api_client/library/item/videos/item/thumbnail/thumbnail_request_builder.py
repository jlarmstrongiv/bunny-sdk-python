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
    from ......models.structured_success_response import StructuredSuccessResponse

class ThumbnailRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /library/{libraryId}/videos/{videoId}/thumbnail
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new ThumbnailRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/library/{libraryId}/videos/{videoId}/thumbnail{?thumbnailUrl*}", path_parameters)
    
    async def post(self,body: bytes, request_configuration: Optional[RequestConfiguration[ThumbnailRequestBuilderPostQueryParameters]] = None) -> Optional[StructuredSuccessResponse]:
        """
        [SetThumbnail API Docs](https://docs.bunny.net/reference/video_setthumbnail)
        param body: Binary request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[StructuredSuccessResponse]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.structured_success_response import StructuredSuccessResponse

        return await self.request_adapter.send_async(request_info, StructuredSuccessResponse, None)
    
    def to_post_request_information(self,body: bytes, request_configuration: Optional[RequestConfiguration[ThumbnailRequestBuilderPostQueryParameters]] = None) -> RequestInformation:
        """
        [SetThumbnail API Docs](https://docs.bunny.net/reference/video_setthumbnail)
        param body: Binary request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_stream_content(body, "image/*")
        return request_info
    
    def with_url(self,raw_url: str) -> ThumbnailRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ThumbnailRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return ThumbnailRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ThumbnailRequestBuilderPostQueryParameters():
        """
        [SetThumbnail API Docs](https://docs.bunny.net/reference/video_setthumbnail)
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "thumbnail_url":
                return "thumbnailUrl"
            return original_name
        
        thumbnail_url: Optional[str] = None

    
    @dataclass
    class ThumbnailRequestBuilderPostRequestConfiguration(RequestConfiguration[ThumbnailRequestBuilderPostQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

