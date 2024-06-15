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
    from ....models.manage_videos.video import Video
    from ....models.manage_videos.video_create import VideoCreate
    from .fetch.fetch_request_builder import FetchRequestBuilder
    from .get_order_by_query_parameter_type import GetOrderByQueryParameterType
    from .item.with_video_item_request_builder import WithVideoItemRequestBuilder
    from .videos_get_response import VideosGetResponse

class VideosRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /library/{libraryId}/videos
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new VideosRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/library/{libraryId}/videos?itemsPerPage={itemsPerPage}&orderBy={orderBy}&page={page}{&collection*,search*}", path_parameters)
    
    def by_video_id(self,video_id: str) -> WithVideoItemRequestBuilder:
        """
        Gets an item from the StreamApiClient.library.item.videos.item collection
        param video_id: Unique identifier of the item
        Returns: WithVideoItemRequestBuilder
        """
        if not video_id:
            raise TypeError("video_id cannot be null.")
        from .item.with_video_item_request_builder import WithVideoItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["videoId"] = video_id
        return WithVideoItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[VideosRequestBuilderGetQueryParameters]] = None) -> Optional[VideosGetResponse]:
        """
        [ListVideos API Docs](https://docs.bunny.net/reference/video_list)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[VideosGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .videos_get_response import VideosGetResponse

        return await self.request_adapter.send_async(request_info, VideosGetResponse, None)
    
    async def post(self,body: VideoCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Video]:
        """
        [CreateVideo API Docs](https://docs.bunny.net/reference/video_createvideo)
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Video]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.manage_videos.video import Video

        return await self.request_adapter.send_async(request_info, Video, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[VideosRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        [ListVideos API Docs](https://docs.bunny.net/reference/video_list)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: VideoCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        [CreateVideo API Docs](https://docs.bunny.net/reference/video_createvideo)
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, '{+baseurl}/library/{libraryId}/videos', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> VideosRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: VideosRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return VideosRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def fetch(self) -> FetchRequestBuilder:
        """
        The fetch property
        """
        from .fetch.fetch_request_builder import FetchRequestBuilder

        return FetchRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class VideosRequestBuilderGetQueryParameters():
        """
        [ListVideos API Docs](https://docs.bunny.net/reference/video_list)
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "items_per_page":
                return "itemsPerPage"
            if original_name == "order_by":
                return "orderBy"
            if original_name == "collection":
                return "collection"
            if original_name == "page":
                return "page"
            if original_name == "search":
                return "search"
            return original_name
        
        collection: Optional[str] = None

        items_per_page: Optional[int] = None

        order_by: Optional[GetOrderByQueryParameterType] = None

        page: Optional[int] = None

        search: Optional[str] = None

    
    @dataclass
    class VideosRequestBuilderGetRequestConfiguration(RequestConfiguration[VideosRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class VideosRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

