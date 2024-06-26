from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_path_item_request_builder import WithPathItemRequestBuilder

class WithStorageZoneNameItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /{storageZoneName}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new WithStorageZoneNameItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/{storageZoneName}", path_parameters)
    
    def by_path(self,path: str) -> WithPathItemRequestBuilder:
        """
        Gets an item from the EdgeStorageApiClient.item.item collection
        param path: The directory path that you want to list.
        Returns: WithPathItemRequestBuilder
        """
        if not path:
            raise TypeError("path cannot be null.")
        from .item.with_path_item_request_builder import WithPathItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["path"] = path
        return WithPathItemRequestBuilder(self.request_adapter, url_tpl_params)
    

