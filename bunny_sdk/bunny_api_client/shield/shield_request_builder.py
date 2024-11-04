from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .metrics.metrics_request_builder import MetricsRequestBuilder
    from .rate_limit.rate_limit_request_builder import RateLimitRequestBuilder
    from .rate_limits.rate_limits_request_builder import RateLimitsRequestBuilder
    from .shield_zone.shield_zone_request_builder import ShieldZoneRequestBuilder
    from .shield_zones.shield_zones_request_builder import ShieldZonesRequestBuilder
    from .waf.waf_request_builder import WafRequestBuilder

class ShieldRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /shield
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new ShieldRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/shield", path_parameters)
    
    @property
    def metrics(self) -> MetricsRequestBuilder:
        """
        The metrics property
        """
        from .metrics.metrics_request_builder import MetricsRequestBuilder

        return MetricsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rate_limit(self) -> RateLimitRequestBuilder:
        """
        The rateLimit property
        """
        from .rate_limit.rate_limit_request_builder import RateLimitRequestBuilder

        return RateLimitRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rate_limits(self) -> RateLimitsRequestBuilder:
        """
        The rateLimits property
        """
        from .rate_limits.rate_limits_request_builder import RateLimitsRequestBuilder

        return RateLimitsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def shield_zone(self) -> ShieldZoneRequestBuilder:
        """
        The shieldZone property
        """
        from .shield_zone.shield_zone_request_builder import ShieldZoneRequestBuilder

        return ShieldZoneRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def shield_zones(self) -> ShieldZonesRequestBuilder:
        """
        The shieldZones property
        """
        from .shield_zones.shield_zones_request_builder import ShieldZonesRequestBuilder

        return ShieldZonesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def waf(self) -> WafRequestBuilder:
        """
        The waf property
        """
        from .waf.waf_request_builder import WafRequestBuilder

        return WafRequestBuilder(self.request_adapter, self.path_parameters)
    

