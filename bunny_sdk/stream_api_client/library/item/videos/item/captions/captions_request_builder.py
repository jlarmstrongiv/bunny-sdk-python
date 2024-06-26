from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_srclang_path_parameter_item_request_builder import WithSrclangPathParameterItemRequestBuilder

class CaptionsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /library/{libraryId}/videos/{videoId}/captions
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new CaptionsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/library/{libraryId}/videos/{videoId}/captions", path_parameters)
    
    def by_srclang_path_parameter(self,srclang_path_parameter: str) -> WithSrclangPathParameterItemRequestBuilder:
        """
        Gets an item from the StreamApiClient.library.item.videos.item.captions.item collection
        param srclang_path_parameter: srclang specified as a path parameter
        Returns: WithSrclangPathParameterItemRequestBuilder
        """
        if not srclang_path_parameter:
            raise TypeError("srclang_path_parameter cannot be null.")
        from .item.with_srclang_path_parameter_item_request_builder import WithSrclangPathParameterItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["srclangPathParameter"] = srclang_path_parameter
        return WithSrclangPathParameterItemRequestBuilder(self.request_adapter, url_tpl_params)
    

