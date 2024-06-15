from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .collections.collections_request_builder import CollectionsRequestBuilder
    from .statistics.statistics_request_builder import StatisticsRequestBuilder
    from .videos.videos_request_builder import VideosRequestBuilder

class WithLibraryItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /library/{libraryId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new WithLibraryItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/library/{libraryId}", path_parameters)
    
    @property
    def collections(self) -> CollectionsRequestBuilder:
        """
        The collections property
        """
        from .collections.collections_request_builder import CollectionsRequestBuilder

        return CollectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def statistics(self) -> StatisticsRequestBuilder:
        """
        The statistics property
        """
        from .statistics.statistics_request_builder import StatisticsRequestBuilder

        return StatisticsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def videos(self) -> VideosRequestBuilder:
        """
        The videos property
        """
        from .videos.videos_request_builder import VideosRequestBuilder

        return VideosRequestBuilder(self.request_adapter, self.path_parameters)
    

