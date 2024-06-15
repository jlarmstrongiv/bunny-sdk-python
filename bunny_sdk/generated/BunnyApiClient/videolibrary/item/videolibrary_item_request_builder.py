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
    from ...models.stream_video_library.video_library import VideoLibrary
    from .add_allowed_referrer.add_allowed_referrer_request_builder import AddAllowedReferrerRequestBuilder
    from .add_blocked_referrer.add_blocked_referrer_request_builder import AddBlockedReferrerRequestBuilder
    from .remove_allowed_referrer.remove_allowed_referrer_request_builder import RemoveAllowedReferrerRequestBuilder
    from .remove_blocked_referrer.remove_blocked_referrer_request_builder import RemoveBlockedReferrerRequestBuilder
    from .reset_api_key.reset_api_key_request_builder import ResetApiKeyRequestBuilder
    from .videolibrary_post_request_body import VideolibraryPostRequestBody
    from .watermark.watermark_request_builder import WatermarkRequestBuilder

class VideolibraryItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /videolibrary/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new VideolibraryItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/videolibrary/{id}?includeAccessKey={includeAccessKey}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        [DeleteVideoLibrary API Docs](https://docs.bunny.net/reference/videolibrarypublic_delete)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[VideolibraryItemRequestBuilderGetQueryParameters]] = None) -> Optional[VideoLibrary]:
        """
        [GetVideoLibrary API Docs](https://docs.bunny.net/reference/videolibrarypublic_index2)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[VideoLibrary]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.stream_video_library.video_library import VideoLibrary

        return await self.request_adapter.send_async(request_info, VideoLibrary, None)
    
    async def post(self,body: VideolibraryPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[VideoLibrary]:
        """
        [UpdateVideoLibrary API Docs](https://docs.bunny.net/reference/videolibrarypublic_update)
        param body: The template for adding optional properties.
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
        from ...models.stream_video_library.video_library import VideoLibrary

        return await self.request_adapter.send_async(request_info, VideoLibrary, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        [DeleteVideoLibrary API Docs](https://docs.bunny.net/reference/videolibrarypublic_delete)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, '{+baseurl}/videolibrary/{id}', self.path_parameters)
        request_info.configure(request_configuration)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[VideolibraryItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        [GetVideoLibrary API Docs](https://docs.bunny.net/reference/videolibrarypublic_index2)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: VideolibraryPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        [UpdateVideoLibrary API Docs](https://docs.bunny.net/reference/videolibrarypublic_update)
        param body: The template for adding optional properties.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, '{+baseurl}/videolibrary/{id}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> VideolibraryItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: VideolibraryItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return VideolibraryItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def add_allowed_referrer(self) -> AddAllowedReferrerRequestBuilder:
        """
        The addAllowedReferrer property
        """
        from .add_allowed_referrer.add_allowed_referrer_request_builder import AddAllowedReferrerRequestBuilder

        return AddAllowedReferrerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def add_blocked_referrer(self) -> AddBlockedReferrerRequestBuilder:
        """
        The addBlockedReferrer property
        """
        from .add_blocked_referrer.add_blocked_referrer_request_builder import AddBlockedReferrerRequestBuilder

        return AddBlockedReferrerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remove_allowed_referrer(self) -> RemoveAllowedReferrerRequestBuilder:
        """
        The removeAllowedReferrer property
        """
        from .remove_allowed_referrer.remove_allowed_referrer_request_builder import RemoveAllowedReferrerRequestBuilder

        return RemoveAllowedReferrerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remove_blocked_referrer(self) -> RemoveBlockedReferrerRequestBuilder:
        """
        The removeBlockedReferrer property
        """
        from .remove_blocked_referrer.remove_blocked_referrer_request_builder import RemoveBlockedReferrerRequestBuilder

        return RemoveBlockedReferrerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reset_api_key(self) -> ResetApiKeyRequestBuilder:
        """
        The resetApiKey property
        """
        from .reset_api_key.reset_api_key_request_builder import ResetApiKeyRequestBuilder

        return ResetApiKeyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def watermark(self) -> WatermarkRequestBuilder:
        """
        The watermark property
        """
        from .watermark.watermark_request_builder import WatermarkRequestBuilder

        return WatermarkRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class VideolibraryItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class VideolibraryItemRequestBuilderGetQueryParameters():
        """
        [GetVideoLibrary API Docs](https://docs.bunny.net/reference/videolibrarypublic_index2)
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
            return original_name
        
        include_access_key: Optional[bool] = None

    
    @dataclass
    class VideolibraryItemRequestBuilderGetRequestConfiguration(RequestConfiguration[VideolibraryItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class VideolibraryItemRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

