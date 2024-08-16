from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from .....models.pull_zone.edge_rule.edge_rule import EdgeRule

class AddOrUpdateRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /pullzone/{-id}/edgerules/addOrUpdate
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new AddOrUpdateRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/pullzone/{%2Did}/edgerules/addOrUpdate", path_parameters)
    
    async def post(self,body: EdgeRule, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[EdgeRule]:
        """
        [AddUpdateEdgeRule API Docs](https://docs.bunny.net/reference/pullzonepublic_addedgerule)
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EdgeRule]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.pull_zone.edge_rule.edge_rule import EdgeRule

        return await self.request_adapter.send_async(request_info, EdgeRule, None)
    
    def to_post_request_information(self,body: EdgeRule, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        [AddUpdateEdgeRule API Docs](https://docs.bunny.net/reference/pullzonepublic_addedgerule)
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> AddOrUpdateRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AddOrUpdateRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return AddOrUpdateRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class AddOrUpdateRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

