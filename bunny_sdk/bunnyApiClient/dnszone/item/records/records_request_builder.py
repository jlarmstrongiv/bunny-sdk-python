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
    from ....models.dns_zone.update_dns_record.dns_record import DnsRecord
    from ....models.structured_bad_request_response import StructuredBadRequestResponse
    from .item.records_item_request_builder import RecordsItemRequestBuilder
    from .records_put_request_body import RecordsPutRequestBody

class RecordsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /dnszone/{-id}/records
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new RecordsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/dnszone/{%2Did}/records", path_parameters)
    
    def by_id(self,id: int) -> RecordsItemRequestBuilder:
        """
        Gets an item from the BunnyApiClient.dnszone.item.records.item collection
        param id: The ID of the DNS record that will be updated.
        Returns: RecordsItemRequestBuilder
        """
        if not id:
            raise TypeError("id cannot be null.")
        from .item.records_item_request_builder import RecordsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return RecordsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def put(self,body: RecordsPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[DnsRecord]:
        """
        [AddDnsRecord API Docs](https://docs.bunny.net/reference/dnszonepublic_addrecord)
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DnsRecord]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ....models.structured_bad_request_response import StructuredBadRequestResponse

        error_mapping: Dict[str, ParsableFactory] = {
            "400": StructuredBadRequestResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.dns_zone.update_dns_record.dns_record import DnsRecord

        return await self.request_adapter.send_async(request_info, DnsRecord, error_mapping)
    
    def to_put_request_information(self,body: RecordsPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        [AddDnsRecord API Docs](https://docs.bunny.net/reference/dnszonepublic_addrecord)
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PUT, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> RecordsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: RecordsRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return RecordsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class RecordsRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

