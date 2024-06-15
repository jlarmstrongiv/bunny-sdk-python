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
    from .....models.structured_success_response import StructuredSuccessResponse
    from .fetch_post_request_body import FetchPostRequestBody

class FetchRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /library/{libraryId}/videos/fetch
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new FetchRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/library/{libraryId}/videos/fetch{?collectionId*,thumbnailTime*}", path_parameters)
    
    async def post(self,body: FetchPostRequestBody, request_configuration: Optional[RequestConfiguration[FetchRequestBuilderPostQueryParameters]] = None) -> Optional[StructuredSuccessResponse]:
        """
        [FetchVideo API Docs](https://docs.bunny.net/reference/video_fetchnewvideo)
        param body: The request body
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
        from .....models.structured_success_response import StructuredSuccessResponse

        return await self.request_adapter.send_async(request_info, StructuredSuccessResponse, None)
    
    def to_post_request_information(self,body: FetchPostRequestBody, request_configuration: Optional[RequestConfiguration[FetchRequestBuilderPostQueryParameters]] = None) -> RequestInformation:
        """
        [FetchVideo API Docs](https://docs.bunny.net/reference/video_fetchnewvideo)
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> FetchRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: FetchRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return FetchRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class FetchRequestBuilderPostQueryParameters():
        """
        [FetchVideo API Docs](https://docs.bunny.net/reference/video_fetchnewvideo)
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "collection_id":
                return "collectionId"
            if original_name == "thumbnail_time":
                return "thumbnailTime"
            return original_name
        
        collection_id: Optional[str] = None

        # Video time in ms to extract the main video thumbnail.
        thumbnail_time: Optional[int] = None

    
    @dataclass
    class FetchRequestBuilderPostRequestConfiguration(RequestConfiguration[FetchRequestBuilderPostQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

