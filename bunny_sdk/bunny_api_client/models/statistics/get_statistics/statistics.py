from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .statistics_bandwidth_cached_chart import Statistics_BandwidthCachedChart
    from .statistics_bandwidth_used_chart import Statistics_BandwidthUsedChart
    from .statistics_cache_hit_rate_chart import Statistics_CacheHitRateChart
    from .statistics_error3xx_chart import Statistics_Error3xxChart
    from .statistics_error4xx_chart import Statistics_Error4xxChart
    from .statistics_error5xx_chart import Statistics_Error5xxChart
    from .statistics_geo_traffic_distribution import Statistics_GeoTrafficDistribution
    from .statistics_origin_response_time_chart import Statistics_OriginResponseTimeChart
    from .statistics_origin_shield_bandwidth_used_chart import Statistics_OriginShieldBandwidthUsedChart
    from .statistics_origin_shield_internal_bandwidth_used_chart import Statistics_OriginShieldInternalBandwidthUsedChart
    from .statistics_origin_traffic_chart import Statistics_OriginTrafficChart
    from .statistics_pull_requests_pulled_chart import Statistics_PullRequestsPulledChart
    from .statistics_requests_served_chart import Statistics_RequestsServedChart
    from .statistics_user_balance_history_chart import Statistics_UserBalanceHistoryChart

@dataclass
class Statistics(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The AverageOriginResponseTime property
    average_origin_response_time: Optional[int] = None
    # The BandwidthCachedChart property
    bandwidth_cached_chart: Optional[Statistics_BandwidthCachedChart] = None
    # The BandwidthUsedChart property
    bandwidth_used_chart: Optional[Statistics_BandwidthUsedChart] = None
    # The CacheHitRate property
    cache_hit_rate: Optional[float] = None
    # The CacheHitRateChart property
    cache_hit_rate_chart: Optional[Statistics_CacheHitRateChart] = None
    # The Error3xxChart property
    error3xx_chart: Optional[Statistics_Error3xxChart] = None
    # The Error4xxChart property
    error4xx_chart: Optional[Statistics_Error4xxChart] = None
    # The Error5xxChart property
    error5xx_chart: Optional[Statistics_Error5xxChart] = None
    # The GeoTrafficDistribution property
    geo_traffic_distribution: Optional[Statistics_GeoTrafficDistribution] = None
    # The OriginResponseTimeChart property
    origin_response_time_chart: Optional[Statistics_OriginResponseTimeChart] = None
    # The OriginShieldBandwidthUsedChart property
    origin_shield_bandwidth_used_chart: Optional[Statistics_OriginShieldBandwidthUsedChart] = None
    # The OriginShieldInternalBandwidthUsedChart property
    origin_shield_internal_bandwidth_used_chart: Optional[Statistics_OriginShieldInternalBandwidthUsedChart] = None
    # The OriginTrafficChart property
    origin_traffic_chart: Optional[Statistics_OriginTrafficChart] = None
    # The PullRequestsPulledChart property
    pull_requests_pulled_chart: Optional[Statistics_PullRequestsPulledChart] = None
    # The RequestsServedChart property
    requests_served_chart: Optional[Statistics_RequestsServedChart] = None
    # The TotalBandwidthUsed property
    total_bandwidth_used: Optional[int] = None
    # The TotalOriginTraffic property
    total_origin_traffic: Optional[int] = None
    # The TotalRequestsServed property
    total_requests_served: Optional[int] = None
    # The UserBalanceHistoryChart property
    user_balance_history_chart: Optional[Statistics_UserBalanceHistoryChart] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Statistics:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Statistics
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Statistics()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .statistics_bandwidth_cached_chart import Statistics_BandwidthCachedChart
        from .statistics_bandwidth_used_chart import Statistics_BandwidthUsedChart
        from .statistics_cache_hit_rate_chart import Statistics_CacheHitRateChart
        from .statistics_error3xx_chart import Statistics_Error3xxChart
        from .statistics_error4xx_chart import Statistics_Error4xxChart
        from .statistics_error5xx_chart import Statistics_Error5xxChart
        from .statistics_geo_traffic_distribution import Statistics_GeoTrafficDistribution
        from .statistics_origin_response_time_chart import Statistics_OriginResponseTimeChart
        from .statistics_origin_shield_bandwidth_used_chart import Statistics_OriginShieldBandwidthUsedChart
        from .statistics_origin_shield_internal_bandwidth_used_chart import Statistics_OriginShieldInternalBandwidthUsedChart
        from .statistics_origin_traffic_chart import Statistics_OriginTrafficChart
        from .statistics_pull_requests_pulled_chart import Statistics_PullRequestsPulledChart
        from .statistics_requests_served_chart import Statistics_RequestsServedChart
        from .statistics_user_balance_history_chart import Statistics_UserBalanceHistoryChart

        from .statistics_bandwidth_cached_chart import Statistics_BandwidthCachedChart
        from .statistics_bandwidth_used_chart import Statistics_BandwidthUsedChart
        from .statistics_cache_hit_rate_chart import Statistics_CacheHitRateChart
        from .statistics_error3xx_chart import Statistics_Error3xxChart
        from .statistics_error4xx_chart import Statistics_Error4xxChart
        from .statistics_error5xx_chart import Statistics_Error5xxChart
        from .statistics_geo_traffic_distribution import Statistics_GeoTrafficDistribution
        from .statistics_origin_response_time_chart import Statistics_OriginResponseTimeChart
        from .statistics_origin_shield_bandwidth_used_chart import Statistics_OriginShieldBandwidthUsedChart
        from .statistics_origin_shield_internal_bandwidth_used_chart import Statistics_OriginShieldInternalBandwidthUsedChart
        from .statistics_origin_traffic_chart import Statistics_OriginTrafficChart
        from .statistics_pull_requests_pulled_chart import Statistics_PullRequestsPulledChart
        from .statistics_requests_served_chart import Statistics_RequestsServedChart
        from .statistics_user_balance_history_chart import Statistics_UserBalanceHistoryChart

        fields: Dict[str, Callable[[Any], None]] = {
            "AverageOriginResponseTime": lambda n : setattr(self, 'average_origin_response_time', n.get_int_value()),
            "BandwidthCachedChart": lambda n : setattr(self, 'bandwidth_cached_chart', n.get_object_value(Statistics_BandwidthCachedChart)),
            "BandwidthUsedChart": lambda n : setattr(self, 'bandwidth_used_chart', n.get_object_value(Statistics_BandwidthUsedChart)),
            "CacheHitRate": lambda n : setattr(self, 'cache_hit_rate', n.get_float_value()),
            "CacheHitRateChart": lambda n : setattr(self, 'cache_hit_rate_chart', n.get_object_value(Statistics_CacheHitRateChart)),
            "Error3xxChart": lambda n : setattr(self, 'error3xx_chart', n.get_object_value(Statistics_Error3xxChart)),
            "Error4xxChart": lambda n : setattr(self, 'error4xx_chart', n.get_object_value(Statistics_Error4xxChart)),
            "Error5xxChart": lambda n : setattr(self, 'error5xx_chart', n.get_object_value(Statistics_Error5xxChart)),
            "GeoTrafficDistribution": lambda n : setattr(self, 'geo_traffic_distribution', n.get_object_value(Statistics_GeoTrafficDistribution)),
            "OriginResponseTimeChart": lambda n : setattr(self, 'origin_response_time_chart', n.get_object_value(Statistics_OriginResponseTimeChart)),
            "OriginShieldBandwidthUsedChart": lambda n : setattr(self, 'origin_shield_bandwidth_used_chart', n.get_object_value(Statistics_OriginShieldBandwidthUsedChart)),
            "OriginShieldInternalBandwidthUsedChart": lambda n : setattr(self, 'origin_shield_internal_bandwidth_used_chart', n.get_object_value(Statistics_OriginShieldInternalBandwidthUsedChart)),
            "OriginTrafficChart": lambda n : setattr(self, 'origin_traffic_chart', n.get_object_value(Statistics_OriginTrafficChart)),
            "PullRequestsPulledChart": lambda n : setattr(self, 'pull_requests_pulled_chart', n.get_object_value(Statistics_PullRequestsPulledChart)),
            "RequestsServedChart": lambda n : setattr(self, 'requests_served_chart', n.get_object_value(Statistics_RequestsServedChart)),
            "TotalBandwidthUsed": lambda n : setattr(self, 'total_bandwidth_used', n.get_int_value()),
            "TotalOriginTraffic": lambda n : setattr(self, 'total_origin_traffic', n.get_int_value()),
            "TotalRequestsServed": lambda n : setattr(self, 'total_requests_served', n.get_int_value()),
            "UserBalanceHistoryChart": lambda n : setattr(self, 'user_balance_history_chart', n.get_object_value(Statistics_UserBalanceHistoryChart)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_int_value("AverageOriginResponseTime", self.average_origin_response_time)
        writer.write_object_value("BandwidthCachedChart", self.bandwidth_cached_chart)
        writer.write_object_value("BandwidthUsedChart", self.bandwidth_used_chart)
        writer.write_float_value("CacheHitRate", self.cache_hit_rate)
        writer.write_object_value("CacheHitRateChart", self.cache_hit_rate_chart)
        writer.write_object_value("Error3xxChart", self.error3xx_chart)
        writer.write_object_value("Error4xxChart", self.error4xx_chart)
        writer.write_object_value("Error5xxChart", self.error5xx_chart)
        writer.write_object_value("GeoTrafficDistribution", self.geo_traffic_distribution)
        writer.write_object_value("OriginResponseTimeChart", self.origin_response_time_chart)
        writer.write_object_value("OriginShieldBandwidthUsedChart", self.origin_shield_bandwidth_used_chart)
        writer.write_object_value("OriginShieldInternalBandwidthUsedChart", self.origin_shield_internal_bandwidth_used_chart)
        writer.write_object_value("OriginTrafficChart", self.origin_traffic_chart)
        writer.write_object_value("PullRequestsPulledChart", self.pull_requests_pulled_chart)
        writer.write_object_value("RequestsServedChart", self.requests_served_chart)
        writer.write_int_value("TotalBandwidthUsed", self.total_bandwidth_used)
        writer.write_int_value("TotalOriginTraffic", self.total_origin_traffic)
        writer.write_int_value("TotalRequestsServed", self.total_requests_served)
        writer.write_object_value("UserBalanceHistoryChart", self.user_balance_history_chart)
        writer.write_additional_data_value(self.additional_data)
    

