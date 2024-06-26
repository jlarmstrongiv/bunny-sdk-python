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
    from ..models.dns_zone.dns_zone import DnsZone
    from ..models.structured_bad_request_response import StructuredBadRequestResponse
    from .checkavailability.checkavailability_request_builder import CheckavailabilityRequestBuilder
    from .dnszone_get_response import DnszoneGetResponse
    from .dnszone_post_request_body import DnszonePostRequestBody
    from .item.item_request_builder import ItemRequestBuilder

class DnszoneRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /dnszone
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new DnszoneRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/dnszone?page={page}&perPage={perPage}&search={search}", path_parameters)
    
    def by_id(self,id: int) -> ItemRequestBuilder:
        """
        Gets an item from the BunnyApiClient.dnszone.item collection
        param id: The ID of the DNS Zone that will be returned
        Returns: ItemRequestBuilder
        """
        if not id:
            raise TypeError("id cannot be null.")
        from .item.item_request_builder import ItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["%2Did"] = id
        return ItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[DnszoneRequestBuilderGetQueryParameters]] = None) -> Optional[DnszoneGetResponse]:
        """
        [ListDnsZones API Docs](https://docs.bunny.net/reference/dnszonepublic_index)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DnszoneGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .dnszone_get_response import DnszoneGetResponse

        return await self.request_adapter.send_async(request_info, DnszoneGetResponse, None)
    
    async def post(self,body: DnszonePostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[DnsZone]:
        """
        [AddDnsZone API Docs](https://docs.bunny.net/reference/dnszonepublic_add)
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DnsZone]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ..models.structured_bad_request_response import StructuredBadRequestResponse

        error_mapping: Dict[str, ParsableFactory] = {
            "400": StructuredBadRequestResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.dns_zone.dns_zone import DnsZone

        return await self.request_adapter.send_async(request_info, DnsZone, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[DnszoneRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        [ListDnsZones API Docs](https://docs.bunny.net/reference/dnszonepublic_index)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: DnszonePostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        [AddDnsZone API Docs](https://docs.bunny.net/reference/dnszonepublic_add)
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, '{+baseurl}/dnszone', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> DnszoneRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DnszoneRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return DnszoneRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def checkavailability(self) -> CheckavailabilityRequestBuilder:
        """
        The checkavailability property
        """
        from .checkavailability.checkavailability_request_builder import CheckavailabilityRequestBuilder

        return CheckavailabilityRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class DnszoneRequestBuilderGetQueryParameters():
        """
        [ListDnsZones API Docs](https://docs.bunny.net/reference/dnszonepublic_index)
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "per_page":
                return "perPage"
            if original_name == "page":
                return "page"
            if original_name == "search":
                return "search"
            return original_name
        
        page: Optional[int] = None

        per_page: Optional[int] = None

        # The search term that will be used to filter the results
        search: Optional[str] = None

    
    @dataclass
    class DnszoneRequestBuilderGetRequestConfiguration(RequestConfiguration[DnszoneRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class DnszoneRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

