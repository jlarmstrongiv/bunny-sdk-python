from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .with_pull_zone_id_log.with_pull_zone_id_log_request_builder import WithPullZoneIdLogRequestBuilder

class WithMmWithDdWithYyRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /{mm}-{dd}-{yy}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]], dd: Optional[int] = None, mm: Optional[int] = None, yy: Optional[int] = None) -> None:
        """
        Instantiates a new WithMmWithDdWithYyRequestBuilder and sets the default values.
        param dd: The path parameter: dd
        param mm: The path parameter: mm
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        param yy: The path parameter: yy
        Returns: None
        """
        if isinstance(path_parameters, dict):
            path_parameters['dd'] = str(dd)
            path_parameters['mm'] = str(mm)
            path_parameters['yy'] = str(yy)
        super().__init__(request_adapter, "{+baseurl}/{mm}-{dd}-{yy}", path_parameters)
    
    def with_pull_zone_id_log(self,pull_zone_id: int) -> WithPullZoneIdLogRequestBuilder:
        """
        Builds and executes requests for operations under /{mm}-{dd}-{yy}/{pullZoneId}.log
        param pull_zone_id: The path parameter: pullZoneId
        Returns: WithPullZoneIdLogRequestBuilder
        """
        if not pull_zone_id:
            raise TypeError("pull_zone_id cannot be null.")
        from .with_pull_zone_id_log.with_pull_zone_id_log_request_builder import WithPullZoneIdLogRequestBuilder

        return WithPullZoneIdLogRequestBuilder(self.request_adapter, self.path_parameters, pull_zone_id)
    

