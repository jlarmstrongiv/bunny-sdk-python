from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .add.add_request_builder import AddRequestBuilder
    from .item.with_variable_item_request_builder import WithVariableItemRequestBuilder

class VariablesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /compute/script/{id}/variables
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new VariablesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/compute/script/{id}/variables", path_parameters)
    
    def by_variable_id(self,variable_id: int) -> WithVariableItemRequestBuilder:
        """
        Gets an item from the BunnyApiClient.compute.script.item.variables.item collection
        param variable_id: The ID of the Environment Variable that will be updated
        Returns: WithVariableItemRequestBuilder
        """
        if not variable_id:
            raise TypeError("variable_id cannot be null.")
        from .item.with_variable_item_request_builder import WithVariableItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["variableId"] = variable_id
        return WithVariableItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def add(self) -> AddRequestBuilder:
        """
        The add property
        """
        from .add.add_request_builder import AddRequestBuilder

        return AddRequestBuilder(self.request_adapter, self.path_parameters)
    

