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
    from ......models.manage_videos.video import Video

class RepackageRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /library/{libraryId}/videos/{videoId}/repackage
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new RepackageRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/library/{libraryId}/videos/{videoId}/repackage?keepOriginalFiles={keepOriginalFiles}", path_parameters)
    
    async def post(self,request_configuration: Optional[RequestConfiguration[RepackageRequestBuilderPostQueryParameters]] = None) -> Optional[Video]:
        """
        [RepackageVideo API Docs](https://docs.bunny.net/reference/video_repackage)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Video]
        """
        request_info = self.to_post_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.manage_videos.video import Video

        return await self.request_adapter.send_async(request_info, Video, None)
    
    def to_post_request_information(self,request_configuration: Optional[RequestConfiguration[RepackageRequestBuilderPostQueryParameters]] = None) -> RequestInformation:
        """
        [RepackageVideo API Docs](https://docs.bunny.net/reference/video_repackage)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> RepackageRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: RepackageRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return RepackageRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class RepackageRequestBuilderPostQueryParameters():
        """
        [RepackageVideo API Docs](https://docs.bunny.net/reference/video_repackage)
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "keep_original_files":
                return "keepOriginalFiles"
            return original_name
        
        # Marks whether previous file versions should be kept in storage, allows for faster repackage later on. Default is true.
        keep_original_files: Optional[bool] = None

    
    @dataclass
    class RepackageRequestBuilderPostRequestConfiguration(RequestConfiguration[RepackageRequestBuilderPostQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

