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
    from ..models.statistics.get_statistics.statistics import Statistics

class StatisticsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /statistics
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new StatisticsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/statistics{?dateFrom*,dateTo*,hourly*,loadErrors*,pullZone*,serverZoneId*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[StatisticsRequestBuilderGetQueryParameters]] = None) -> Optional[Statistics]:
        """
        [GetStatistics API Docs](https://docs.bunny.net/reference/statisticspublic_index)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Statistics]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.statistics.get_statistics.statistics import Statistics

        return await self.request_adapter.send_async(request_info, Statistics, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[StatisticsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        [GetStatistics API Docs](https://docs.bunny.net/reference/statisticspublic_index)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> StatisticsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: StatisticsRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return StatisticsRequestBuilder(self.request_adapter, raw_url)
    
    import datetime

    @dataclass
    class StatisticsRequestBuilderGetQueryParameters():
        import datetime

        """
        [GetStatistics API Docs](https://docs.bunny.net/reference/statisticspublic_index)
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "date_from":
                return "dateFrom"
            if original_name == "date_to":
                return "dateTo"
            if original_name == "load_errors":
                return "loadErrors"
            if original_name == "pull_zone":
                return "pullZone"
            if original_name == "server_zone_id":
                return "serverZoneId"
            if original_name == "hourly":
                return "hourly"
            return original_name
        
        date_from: Optional[datetime.datetime] = None

        date_to: Optional[datetime.datetime] = None

        hourly: Optional[bool] = None

        load_errors: Optional[bool] = None

        pull_zone: Optional[int] = None

        server_zone_id: Optional[int] = None

    
    @dataclass
    class StatisticsRequestBuilderGetRequestConfiguration(RequestConfiguration[StatisticsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

