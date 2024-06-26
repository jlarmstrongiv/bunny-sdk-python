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
    from ..models.storage_zone.storage_zone import StorageZone
    from ..models.storage_zone.storage_zone_create import StorageZoneCreate
    from .checkavailability.checkavailability_request_builder import CheckavailabilityRequestBuilder
    from .item.storagezone_item_request_builder import StoragezoneItemRequestBuilder
    from .reset_read_only_password.reset_read_only_password_request_builder import ResetReadOnlyPasswordRequestBuilder
    from .storagezone_get_response import StoragezoneGetResponse

class StoragezoneRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /storagezone
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new StoragezoneRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/storagezone?includeDeleted={includeDeleted}&page={page}&perPage={perPage}{&search*}", path_parameters)
    
    def by_id(self,id: int) -> StoragezoneItemRequestBuilder:
        """
        Gets an item from the BunnyApiClient.storagezone.item collection
        param id: The ID of the Storage Zone that should be returned
        Returns: StoragezoneItemRequestBuilder
        """
        if not id:
            raise TypeError("id cannot be null.")
        from .item.storagezone_item_request_builder import StoragezoneItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return StoragezoneItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[StoragezoneRequestBuilderGetQueryParameters]] = None) -> Optional[StoragezoneGetResponse]:
        """
        [ListStorageZones API Docs](https://docs.bunny.net/reference/storagezonepublic_index)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[StoragezoneGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .storagezone_get_response import StoragezoneGetResponse

        return await self.request_adapter.send_async(request_info, StoragezoneGetResponse, None)
    
    async def post(self,body: StorageZoneCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[StorageZone]:
        """
        [AddStorageZone API Docs](https://docs.bunny.net/reference/storagezonepublic_add)
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[StorageZone]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.storage_zone.storage_zone import StorageZone

        return await self.request_adapter.send_async(request_info, StorageZone, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[StoragezoneRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        [ListStorageZones API Docs](https://docs.bunny.net/reference/storagezonepublic_index)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: StorageZoneCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        [AddStorageZone API Docs](https://docs.bunny.net/reference/storagezonepublic_add)
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, '{+baseurl}/storagezone', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> StoragezoneRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: StoragezoneRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return StoragezoneRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def checkavailability(self) -> CheckavailabilityRequestBuilder:
        """
        The checkavailability property
        """
        from .checkavailability.checkavailability_request_builder import CheckavailabilityRequestBuilder

        return CheckavailabilityRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reset_read_only_password(self) -> ResetReadOnlyPasswordRequestBuilder:
        """
        The resetReadOnlyPassword property
        """
        from .reset_read_only_password.reset_read_only_password_request_builder import ResetReadOnlyPasswordRequestBuilder

        return ResetReadOnlyPasswordRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class StoragezoneRequestBuilderGetQueryParameters():
        """
        [ListStorageZones API Docs](https://docs.bunny.net/reference/storagezonepublic_index)
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "include_deleted":
                return "includeDeleted"
            if original_name == "per_page":
                return "perPage"
            if original_name == "page":
                return "page"
            if original_name == "search":
                return "search"
            return original_name
        
        include_deleted: Optional[bool] = None

        page: Optional[int] = None

        per_page: Optional[int] = None

        search: Optional[str] = None

    
    @dataclass
    class StoragezoneRequestBuilderGetRequestConfiguration(RequestConfiguration[StoragezoneRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class StoragezoneRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

