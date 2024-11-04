from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_shield_zone_item_request_builder import WithShieldZoneItemRequestBuilder

class CustomRulesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /shield/waf/custom-rules
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new CustomRulesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/shield/waf/custom-rules", path_parameters)
    
    def by_shield_zone_id(self,shield_zone_id: int) -> WithShieldZoneItemRequestBuilder:
        """
        Gets an item from the BunnyApiClient.shield.waf.customRules.item collection
        param shield_zone_id: Unique identifier of the item
        Returns: WithShieldZoneItemRequestBuilder
        """
        if shield_zone_id is None:
            raise TypeError("shield_zone_id cannot be null.")
        from .item.with_shield_zone_item_request_builder import WithShieldZoneItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["shieldZoneId"] = shield_zone_id
        return WithShieldZoneItemRequestBuilder(self.request_adapter, url_tpl_params)
    

