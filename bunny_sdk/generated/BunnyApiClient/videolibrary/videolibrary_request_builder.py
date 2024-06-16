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
    from ..models.stream_video_library.video_library import VideoLibrary
    from .item.videolibrary_item_request_builder import VideolibraryItemRequestBuilder
    from .languages.languages_request_builder import LanguagesRequestBuilder
    from .reset_api_key.reset_api_key_request_builder import ResetApiKeyRequestBuilder
    from .videolibrary_get_response import VideolibraryGetResponse
    from .videolibrary_post_request_body import VideolibraryPostRequestBody

class VideolibraryRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /videolibrary
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new VideolibraryRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/videolibrary?includeAccessKey={includeAccessKey}&page={page}&perPage={perPage}&search={search}", path_parameters)
    
    def by_id(self,id: int) -> VideolibraryItemRequestBuilder:
        """
        Gets an item from the BunnyApiClient.videolibrary.item collection
        param id: The ID of the Video Library that will be returned
        Returns: VideolibraryItemRequestBuilder
        """
        if not id:
            raise TypeError("id cannot be null.")
        from .item.videolibrary_item_request_builder import VideolibraryItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return VideolibraryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[VideolibraryRequestBuilderGetQueryParameters]] = None) -> Optional[VideolibraryGetResponse]:
        """
        [ListVideoLibraries API Docs](https://docs.bunny.net/reference/videolibrarypublic_index)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[VideolibraryGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .videolibrary_get_response import VideolibraryGetResponse

        return await self.request_adapter.send_async(request_info, VideolibraryGetResponse, None)
    
    async def post(self,body: VideolibraryPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[VideoLibrary]:
        """
        [AddVideoLibrary API Docs](https://docs.bunny.net/reference/videolibrarypublic_add)
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[VideoLibrary]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.stream_video_library.video_library import VideoLibrary

        return await self.request_adapter.send_async(request_info, VideoLibrary, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[VideolibraryRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        [ListVideoLibraries API Docs](https://docs.bunny.net/reference/videolibrarypublic_index)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: VideolibraryPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        [AddVideoLibrary API Docs](https://docs.bunny.net/reference/videolibrarypublic_add)
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, '{+baseurl}/videolibrary', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> VideolibraryRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: VideolibraryRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return VideolibraryRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def languages(self) -> LanguagesRequestBuilder:
        """
        The languages property
        """
        from .languages.languages_request_builder import LanguagesRequestBuilder

        return LanguagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reset_api_key(self) -> ResetApiKeyRequestBuilder:
        """
        The resetApiKey property
        """
        from .reset_api_key.reset_api_key_request_builder import ResetApiKeyRequestBuilder

        return ResetApiKeyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class VideolibraryRequestBuilderGetQueryParameters():
        """
        [ListVideoLibraries API Docs](https://docs.bunny.net/reference/videolibrarypublic_index)
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "include_access_key":
                return "includeAccessKey"
            if original_name == "per_page":
                return "perPage"
            if original_name == "page":
                return "page"
            if original_name == "search":
                return "search"
            return original_name
        
        include_access_key: Optional[bool] = None

        page: Optional[int] = None

        per_page: Optional[int] = None

        # The search term that will be used to filter the results
        search: Optional[str] = None

    
    @dataclass
    class VideolibraryRequestBuilderGetRequestConfiguration(RequestConfiguration[VideolibraryRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class VideolibraryRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

