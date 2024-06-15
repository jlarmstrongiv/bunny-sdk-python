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

class TranscribeRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /library/{libraryId}/videos/{videoId}/transcribe
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new TranscribeRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/library/{libraryId}/videos/{videoId}/transcribe?force={force}&language={language}", path_parameters)
    
    async def post(self,request_configuration: Optional[RequestConfiguration[TranscribeRequestBuilderPostQueryParameters]] = None) -> Optional[StructuredSuccessResponse]:
        """
        [TranscribeVideo API Docs](https://docs.bunny.net/reference/video_transcribevideo)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[StructuredSuccessResponse]
        """
        request_info = self.to_post_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.structured_success_response import StructuredSuccessResponse

        return await self.request_adapter.send_async(request_info, StructuredSuccessResponse, None)
    
    def to_post_request_information(self,request_configuration: Optional[RequestConfiguration[TranscribeRequestBuilderPostQueryParameters]] = None) -> RequestInformation:
        """
        [TranscribeVideo API Docs](https://docs.bunny.net/reference/video_transcribevideo)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> TranscribeRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TranscribeRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return TranscribeRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class TranscribeRequestBuilderPostQueryParameters():
        """
        [TranscribeVideo API Docs](https://docs.bunny.net/reference/video_transcribevideo)
        """
        force: Optional[bool] = None

        language: Optional[str] = None

    
    @dataclass
    class TranscribeRequestBuilderPostRequestConfiguration(RequestConfiguration[TranscribeRequestBuilderPostQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

