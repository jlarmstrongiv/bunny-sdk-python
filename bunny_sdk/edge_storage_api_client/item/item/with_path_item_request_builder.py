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
    from ...models.file import File
    from .item.with_file_name_item_request_builder import WithFileNameItemRequestBuilder

class WithPathItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /{storageZoneName}/{path}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new WithPathItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/{storageZoneName}/{path}", path_parameters)
    
    def by_file_name(self,file_name: str) -> WithFileNameItemRequestBuilder:
        """
        Gets an item from the EdgeStorageApiClient.item.item.item collection
        param file_name: The name of the file that you wish to download.
        Returns: WithFileNameItemRequestBuilder
        """
        if file_name is None:
            raise TypeError("file_name cannot be null.")
        from .item.with_file_name_item_request_builder import WithFileNameItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["fileName"] = file_name
        return WithFileNameItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[List[File]]:
        """
        [ListFiles API Docs](https://docs.bunny.net/reference/get_-storagezonename-path-)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[List[File]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.file import File

        return await self.request_adapter.send_collection_async(request_info, File, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        [ListFiles API Docs](https://docs.bunny.net/reference/get_-storagezonename-path-)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> WithPathItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithPathItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithPathItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithPathItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

