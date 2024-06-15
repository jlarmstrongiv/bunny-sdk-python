from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_library_item_request_builder import WithLibraryItemRequestBuilder

class LibraryRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /library
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new LibraryRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/library", path_parameters)
    
    def by_library_id(self,library_id: int) -> WithLibraryItemRequestBuilder:
        """
        Gets an item from the StreamApiClient.library.item collection
        param library_id: Unique identifier of the item
        Returns: WithLibraryItemRequestBuilder
        """
        if not library_id:
            raise TypeError("library_id cannot be null.")
        from .item.with_library_item_request_builder import WithLibraryItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["libraryId"] = library_id
        return WithLibraryItemRequestBuilder(self.request_adapter, url_tpl_params)
    

