from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .add_or_update.add_or_update_request_builder import AddOrUpdateRequestBuilder
    from .item.with_edge_rule_item_request_builder import WithEdgeRuleItemRequestBuilder

class EdgerulesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /pullzone/{-id}/edgerules
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new EdgerulesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/pullzone/{%2Did}/edgerules", path_parameters)
    
    def by_edge_rule_id(self,edge_rule_id: str) -> WithEdgeRuleItemRequestBuilder:
        """
        Gets an item from the BunnyApiClient.pullzone.item.edgerules.item collection
        param edge_rule_id: The ID of the Edge Rule that should be deleted
        Returns: WithEdgeRuleItemRequestBuilder
        """
        if not edge_rule_id:
            raise TypeError("edge_rule_id cannot be null.")
        from .item.with_edge_rule_item_request_builder import WithEdgeRuleItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["edgeRuleId"] = edge_rule_id
        return WithEdgeRuleItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def add_or_update(self) -> AddOrUpdateRequestBuilder:
        """
        The addOrUpdate property
        """
        from .add_or_update.add_or_update_request_builder import AddOrUpdateRequestBuilder

        return AddOrUpdateRequestBuilder(self.request_adapter, self.path_parameters)
    

