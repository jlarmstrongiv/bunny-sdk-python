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
    from ....models.compute.script import Script
    from ....models.compute.script_create import ScriptCreate
    from .code.code_request_builder import CodeRequestBuilder
    from .publish.publish_request_builder import PublishRequestBuilder
    from .releases.releases_request_builder import ReleasesRequestBuilder
    from .variables.variables_request_builder import VariablesRequestBuilder

class ScriptItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /compute/script/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new ScriptItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/compute/script/{id}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        [DeleteComputeScript API Docs](https://docs.bunny.net/reference/computeedgescriptpublic_delete)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Script]:
        """
        [GetComputeScript API Docs](https://docs.bunny.net/reference/computeedgescriptpublic_index2)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Script]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.compute.script import Script

        return await self.request_adapter.send_async(request_info, Script, None)
    
    async def post(self,body: ScriptCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Script]:
        """
        [UpdateComputeScript API Docs](https://docs.bunny.net/reference/computeedgescriptpublic_update)
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Script]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.compute.script import Script

        return await self.request_adapter.send_async(request_info, Script, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        [DeleteComputeScript API Docs](https://docs.bunny.net/reference/computeedgescriptpublic_delete)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        [GetComputeScript API Docs](https://docs.bunny.net/reference/computeedgescriptpublic_index2)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: ScriptCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        [UpdateComputeScript API Docs](https://docs.bunny.net/reference/computeedgescriptpublic_update)
        param body: The request body
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
    
    def with_url(self,raw_url: str) -> ScriptItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ScriptItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return ScriptItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def code(self) -> CodeRequestBuilder:
        """
        The code property
        """
        from .code.code_request_builder import CodeRequestBuilder

        return CodeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def publish(self) -> PublishRequestBuilder:
        """
        The publish property
        """
        from .publish.publish_request_builder import PublishRequestBuilder

        return PublishRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def releases(self) -> ReleasesRequestBuilder:
        """
        The releases property
        """
        from .releases.releases_request_builder import ReleasesRequestBuilder

        return ReleasesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def variables(self) -> VariablesRequestBuilder:
        """
        The variables property
        """
        from .variables.variables_request_builder import VariablesRequestBuilder

        return VariablesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ScriptItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ScriptItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ScriptItemRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

