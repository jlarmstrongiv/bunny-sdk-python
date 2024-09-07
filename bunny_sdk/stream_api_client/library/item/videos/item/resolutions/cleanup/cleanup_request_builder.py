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
    from .......models.manage_videos.cleanup_unconfigured_resolutions.cleanup_unconfigured_resolutions_result import CleanupUnconfiguredResolutionsResult

class CleanupRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /library/{libraryId}/videos/{videoId}/resolutions/cleanup
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new CleanupRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/library/{libraryId}/videos/{videoId}/resolutions/cleanup{?deleteMp4Files,deleteNonConfiguredResolutions,deleteOriginal,resolutionsToDelete}", path_parameters)
    
    async def post(self,request_configuration: Optional[RequestConfiguration[CleanupRequestBuilderPostQueryParameters]] = None) -> Optional[CleanupUnconfiguredResolutionsResult]:
        """
        [CleanupUnconfiguredResolutions API Docs](https://docs.bunny.net/reference/video_deleteresolutions)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CleanupUnconfiguredResolutionsResult]
        """
        request_info = self.to_post_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.manage_videos.cleanup_unconfigured_resolutions.cleanup_unconfigured_resolutions_result import CleanupUnconfiguredResolutionsResult

        return await self.request_adapter.send_async(request_info, CleanupUnconfiguredResolutionsResult, None)
    
    def to_post_request_information(self,request_configuration: Optional[RequestConfiguration[CleanupRequestBuilderPostQueryParameters]] = None) -> RequestInformation:
        """
        [CleanupUnconfiguredResolutions API Docs](https://docs.bunny.net/reference/video_deleteresolutions)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> CleanupRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CleanupRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CleanupRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class CleanupRequestBuilderPostQueryParameters():
        """
        [CleanupUnconfiguredResolutions API Docs](https://docs.bunny.net/reference/video_deleteresolutions)
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "delete_mp4_files":
                return "deleteMp4Files"
            if original_name == "delete_non_configured_resolutions":
                return "deleteNonConfiguredResolutions"
            if original_name == "delete_original":
                return "deleteOriginal"
            if original_name == "resolutions_to_delete":
                return "resolutionsToDelete"
            return original_name
        
        delete_mp4_files: Optional[bool] = None

        delete_non_configured_resolutions: Optional[bool] = None

        delete_original: Optional[bool] = None

        resolutions_to_delete: Optional[str] = None

    
    @dataclass
    class CleanupRequestBuilderPostRequestConfiguration(RequestConfiguration[CleanupRequestBuilderPostQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

