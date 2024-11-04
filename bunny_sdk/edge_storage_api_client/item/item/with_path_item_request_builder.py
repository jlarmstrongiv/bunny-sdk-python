from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_file_name_item_request_builder import WithFileNameItemRequestBuilder

class WithPathItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /{storageZoneName}/{+path}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new WithPathItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/{storageZoneName}/{+path}", path_parameters)
    
    def by_file_name(self,file_name: str) -> WithFileNameItemRequestBuilder:
        """
        Gets an item from the EdgeStorageApiClient.item.item.item collection
        param file_name: The name of the file that you wish to download.
        Returns: WithFileNameItemRequestBuilder
        """
        if file_name is None:
            raise TypeError("file_name cannot be null.")
        from .item.with_file_name_item_request_builder import WithFileNameItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["fileName"] = file_name
        return WithFileNameItemRequestBuilder(self.request_adapter, url_tpl_params)
    

