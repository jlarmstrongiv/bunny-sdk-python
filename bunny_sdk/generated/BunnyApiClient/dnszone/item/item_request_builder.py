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
    from ...models.dns_zone.dns_zone import DnsZone
    from ...models.structured_bad_request_response import StructuredBadRequestResponse
    from .dismissnameservercheck.dismissnameservercheck_request_builder import DismissnameservercheckRequestBuilder
    from .export.export_request_builder import ExportRequestBuilder
    from .import_.import_request_builder import ImportRequestBuilder
    from .post_request_body import PostRequestBody
    from .recheckdns.recheckdns_request_builder import RecheckdnsRequestBuilder
    from .records.records_request_builder import RecordsRequestBuilder
    from .statistics.statistics_request_builder import StatisticsRequestBuilder

class ItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /dnszone/{-id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new ItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/dnszone/{%2Did}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        [DeleteDnsZone API Docs](https://docs.bunny.net/reference/dnszonepublic_delete)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.structured_bad_request_response import StructuredBadRequestResponse

        error_mapping: Dict[str, ParsableFactory] = {
            "400": StructuredBadRequestResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[DnsZone]:
        """
        [GetDnsZone API Docs](https://docs.bunny.net/reference/dnszonepublic_index2)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DnsZone]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.dns_zone.dns_zone import DnsZone

        return await self.request_adapter.send_async(request_info, DnsZone, None)
    
    async def post(self,body: PostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[DnsZone]:
        """
        [UpdateDnsZone API Docs](https://docs.bunny.net/reference/dnszonepublic_update)
        param body: The template for adding optional properties.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DnsZone]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.dns_zone.dns_zone import DnsZone

        return await self.request_adapter.send_async(request_info, DnsZone, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        [DeleteDnsZone API Docs](https://docs.bunny.net/reference/dnszonepublic_delete)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        [GetDnsZone API Docs](https://docs.bunny.net/reference/dnszonepublic_index2)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: PostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        [UpdateDnsZone API Docs](https://docs.bunny.net/reference/dnszonepublic_update)
        param body: The template for adding optional properties.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> ItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return ItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def dismissnameservercheck(self) -> DismissnameservercheckRequestBuilder:
        """
        The dismissnameservercheck property
        """
        from .dismissnameservercheck.dismissnameservercheck_request_builder import DismissnameservercheckRequestBuilder

        return DismissnameservercheckRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def export(self) -> ExportRequestBuilder:
        """
        The export property
        """
        from .export.export_request_builder import ExportRequestBuilder

        return ExportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def import_(self) -> ImportRequestBuilder:
        """
        The import property
        """
        from .import_.import_request_builder import ImportRequestBuilder

        return ImportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def recheckdns(self) -> RecheckdnsRequestBuilder:
        """
        The recheckdns property
        """
        from .recheckdns.recheckdns_request_builder import RecheckdnsRequestBuilder

        return RecheckdnsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def records(self) -> RecordsRequestBuilder:
        """
        The records property
        """
        from .records.records_request_builder import RecordsRequestBuilder

        return RecordsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def statistics(self) -> StatisticsRequestBuilder:
        """
        The statistics property
        """
        from .statistics.statistics_request_builder import StatisticsRequestBuilder

        return StatisticsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ItemRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

