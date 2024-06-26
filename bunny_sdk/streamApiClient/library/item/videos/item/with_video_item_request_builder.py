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
    from .....models.manage_videos.video import Video
    from .....models.manage_videos.video_create import VideoCreate
    from .....models.structured_success_response import StructuredSuccessResponse
    from .captions.captions_request_builder import CaptionsRequestBuilder
    from .heatmap.heatmap_request_builder import HeatmapRequestBuilder
    from .play.play_request_builder import PlayRequestBuilder
    from .reencode.reencode_request_builder import ReencodeRequestBuilder
    from .repackage.repackage_request_builder import RepackageRequestBuilder
    from .thumbnail.thumbnail_request_builder import ThumbnailRequestBuilder
    from .transcribe.transcribe_request_builder import TranscribeRequestBuilder

class WithVideoItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /library/{libraryId}/videos/{videoId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new WithVideoItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/library/{libraryId}/videos/{videoId}{?enabledResolutions*}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[StructuredSuccessResponse]:
        """
        [DeleteVideo API Docs](https://docs.bunny.net/reference/video_deletevideo)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[StructuredSuccessResponse]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.structured_success_response import StructuredSuccessResponse

        return await self.request_adapter.send_async(request_info, StructuredSuccessResponse, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Video]:
        """
        [GetVideo API Docs](https://docs.bunny.net/reference/video_getvideo)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Video]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.manage_videos.video import Video

        return await self.request_adapter.send_async(request_info, Video, None)
    
    async def post(self,body: VideoCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[StructuredSuccessResponse]:
        """
        [UpdateVideo API Docs](https://docs.bunny.net/reference/video_updatevideo)
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
    
    async def put(self,body: bytes, request_configuration: Optional[RequestConfiguration[WithVideoItemRequestBuilderPutQueryParameters]] = None) -> Optional[StructuredSuccessResponse]:
        """
        [UploadVideo API Docs](https://docs.bunny.net/reference/video_uploadvideo)
        param body: Binary request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[StructuredSuccessResponse]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.structured_success_response import StructuredSuccessResponse

        return await self.request_adapter.send_async(request_info, StructuredSuccessResponse, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        [DeleteVideo API Docs](https://docs.bunny.net/reference/video_deletevideo)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        [GetVideo API Docs](https://docs.bunny.net/reference/video_getvideo)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: VideoCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        [UpdateVideo API Docs](https://docs.bunny.net/reference/video_updatevideo)
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
    
    def to_put_request_information(self,body: bytes, request_configuration: Optional[RequestConfiguration[WithVideoItemRequestBuilderPutQueryParameters]] = None) -> RequestInformation:
        """
        [UploadVideo API Docs](https://docs.bunny.net/reference/video_uploadvideo)
        param body: Binary request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PUT, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_stream_content(body, "application/octet-stream")
        return request_info
    
    def with_url(self,raw_url: str) -> WithVideoItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithVideoItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return WithVideoItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def captions(self) -> CaptionsRequestBuilder:
        """
        The captions property
        """
        from .captions.captions_request_builder import CaptionsRequestBuilder

        return CaptionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def heatmap(self) -> HeatmapRequestBuilder:
        """
        The heatmap property
        """
        from .heatmap.heatmap_request_builder import HeatmapRequestBuilder

        return HeatmapRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def play(self) -> PlayRequestBuilder:
        """
        The play property
        """
        from .play.play_request_builder import PlayRequestBuilder

        return PlayRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reencode(self) -> ReencodeRequestBuilder:
        """
        The reencode property
        """
        from .reencode.reencode_request_builder import ReencodeRequestBuilder

        return ReencodeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def repackage(self) -> RepackageRequestBuilder:
        """
        The repackage property
        """
        from .repackage.repackage_request_builder import RepackageRequestBuilder

        return RepackageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def thumbnail(self) -> ThumbnailRequestBuilder:
        """
        The thumbnail property
        """
        from .thumbnail.thumbnail_request_builder import ThumbnailRequestBuilder

        return ThumbnailRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def transcribe(self) -> TranscribeRequestBuilder:
        """
        The transcribe property
        """
        from .transcribe.transcribe_request_builder import TranscribeRequestBuilder

        return TranscribeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WithVideoItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithVideoItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithVideoItemRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithVideoItemRequestBuilderPutQueryParameters():
        """
        [UploadVideo API Docs](https://docs.bunny.net/reference/video_uploadvideo)
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "enabled_resolutions":
                return "enabledResolutions"
            return original_name
        
        enabled_resolutions: Optional[str] = None

    
    @dataclass
    class WithVideoItemRequestBuilderPutRequestConfiguration(RequestConfiguration[WithVideoItemRequestBuilderPutQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

