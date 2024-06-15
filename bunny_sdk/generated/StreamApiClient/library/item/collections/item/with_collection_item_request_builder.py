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
    from .....models.manage_collections.collection import Collection
    from .....models.structured_success_response import StructuredSuccessResponse

class WithCollectionItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /library/{libraryId}/collections/{collectionId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new WithCollectionItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/library/{libraryId}/collections/{collectionId}?includeThumbnails={includeThumbnails}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[StructuredSuccessResponse]:
        """
        [DeleteCollection API Docs](https://docs.bunny.net/reference/collection_deletecollection)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[StructuredSuccessResponse]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.structured_success_response import StructuredSuccessResponse

        return await self.request_adapter.send_async(request_info, StructuredSuccessResponse, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[WithCollectionItemRequestBuilderGetQueryParameters]] = None) -> Optional[Collection]:
        """
        [GetCollection API Docs](https://docs.bunny.net/reference/collection_getcollection)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Collection]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.manage_collections.collection import Collection

        return await self.request_adapter.send_async(request_info, Collection, None)
    
    async def post(self,body: Collection, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[StructuredSuccessResponse]:
        """
        [UpdateCollection API Docs](https://docs.bunny.net/reference/collection_updatecollection)
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[StructuredSuccessResponse]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.structured_success_response import StructuredSuccessResponse

        return await self.request_adapter.send_async(request_info, StructuredSuccessResponse, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        [DeleteCollection API Docs](https://docs.bunny.net/reference/collection_deletecollection)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, '{+baseurl}/library/{libraryId}/collections/{collectionId}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[WithCollectionItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        [GetCollection API Docs](https://docs.bunny.net/reference/collection_getcollection)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: Collection, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        [UpdateCollection API Docs](https://docs.bunny.net/reference/collection_updatecollection)
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, '{+baseurl}/library/{libraryId}/collections/{collectionId}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> WithCollectionItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithCollectionItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return WithCollectionItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithCollectionItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithCollectionItemRequestBuilderGetQueryParameters():
        """
        [GetCollection API Docs](https://docs.bunny.net/reference/collection_getcollection)
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "include_thumbnails":
                return "includeThumbnails"
            return original_name
        
        include_thumbnails: Optional[bool] = None

    
    @dataclass
    class WithCollectionItemRequestBuilderGetRequestConfiguration(RequestConfiguration[WithCollectionItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithCollectionItemRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

