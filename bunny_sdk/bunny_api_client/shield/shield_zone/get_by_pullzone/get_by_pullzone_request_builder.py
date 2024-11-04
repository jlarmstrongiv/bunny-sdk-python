from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_pull_zone_item_request_builder import WithPullZoneItemRequestBuilder

class GetByPullzoneRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /shield/shield-zone/get-by-pullzone
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new GetByPullzoneRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/shield/shield-zone/get-by-pullzone", path_parameters)
    
    def by_pull_zone_id(self,pull_zone_id: int) -> WithPullZoneItemRequestBuilder:
        """
        Gets an item from the BunnyApiClient.shield.shieldZone.getByPullzone.item collection
        param pull_zone_id: Unique identifier of the item
        Returns: WithPullZoneItemRequestBuilder
        """
        if pull_zone_id is None:
            raise TypeError("pull_zone_id cannot be null.")
        from .item.with_pull_zone_item_request_builder import WithPullZoneItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["pullZoneId"] = pull_zone_id
        return WithPullZoneItemRequestBuilder(self.request_adapter, url_tpl_params)
    

