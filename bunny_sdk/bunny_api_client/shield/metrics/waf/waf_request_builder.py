from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .blocked.blocked_request_builder import BlockedRequestBuilder
    from .logged.logged_request_builder import LoggedRequestBuilder
    from .processed.processed_request_builder import ProcessedRequestBuilder
    from .triggered.triggered_request_builder import TriggeredRequestBuilder

class WafRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /shield/metrics/waf
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new WafRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/shield/metrics/waf", path_parameters)
    
    @property
    def blocked(self) -> BlockedRequestBuilder:
        """
        The blocked property
        """
        from .blocked.blocked_request_builder import BlockedRequestBuilder

        return BlockedRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def logged(self) -> LoggedRequestBuilder:
        """
        The logged property
        """
        from .logged.logged_request_builder import LoggedRequestBuilder

        return LoggedRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def processed(self) -> ProcessedRequestBuilder:
        """
        The processed property
        """
        from .processed.processed_request_builder import ProcessedRequestBuilder

        return ProcessedRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def triggered(self) -> TriggeredRequestBuilder:
        """
        The triggered property
        """
        from .triggered.triggered_request_builder import TriggeredRequestBuilder

        return TriggeredRequestBuilder(self.request_adapter, self.path_parameters)
    

