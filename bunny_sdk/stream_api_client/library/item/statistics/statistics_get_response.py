from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .statistics_get_response_country_view_counts import StatisticsGetResponse_countryViewCounts
    from .statistics_get_response_country_watch_time import StatisticsGetResponse_countryWatchTime
    from .statistics_get_response_views_chart import StatisticsGetResponse_viewsChart
    from .statistics_get_response_watch_time_chart import StatisticsGetResponse_watchTimeChart

@dataclass
class StatisticsGetResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The countryViewCounts property
    country_view_counts: Optional[StatisticsGetResponse_countryViewCounts] = None
    # The countryWatchTime property
    country_watch_time: Optional[StatisticsGetResponse_countryWatchTime] = None
    # The engagementScore property
    engagement_score: Optional[int] = None
    # The viewsChart property
    views_chart: Optional[StatisticsGetResponse_viewsChart] = None
    # The watchTimeChart property
    watch_time_chart: Optional[StatisticsGetResponse_watchTimeChart] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StatisticsGetResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StatisticsGetResponse
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return StatisticsGetResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .statistics_get_response_country_view_counts import StatisticsGetResponse_countryViewCounts
        from .statistics_get_response_country_watch_time import StatisticsGetResponse_countryWatchTime
        from .statistics_get_response_views_chart import StatisticsGetResponse_viewsChart
        from .statistics_get_response_watch_time_chart import StatisticsGetResponse_watchTimeChart

        from .statistics_get_response_country_view_counts import StatisticsGetResponse_countryViewCounts
        from .statistics_get_response_country_watch_time import StatisticsGetResponse_countryWatchTime
        from .statistics_get_response_views_chart import StatisticsGetResponse_viewsChart
        from .statistics_get_response_watch_time_chart import StatisticsGetResponse_watchTimeChart

        fields: Dict[str, Callable[[Any], None]] = {
            "countryViewCounts": lambda n : setattr(self, 'country_view_counts', n.get_object_value(StatisticsGetResponse_countryViewCounts)),
            "countryWatchTime": lambda n : setattr(self, 'country_watch_time', n.get_object_value(StatisticsGetResponse_countryWatchTime)),
            "engagementScore": lambda n : setattr(self, 'engagement_score', n.get_int_value()),
            "viewsChart": lambda n : setattr(self, 'views_chart', n.get_object_value(StatisticsGetResponse_viewsChart)),
            "watchTimeChart": lambda n : setattr(self, 'watch_time_chart', n.get_object_value(StatisticsGetResponse_watchTimeChart)),
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
        writer.write_object_value("countryViewCounts", self.country_view_counts)
        writer.write_object_value("countryWatchTime", self.country_watch_time)
        writer.write_int_value("engagementScore", self.engagement_score)
        writer.write_object_value("viewsChart", self.views_chart)
        writer.write_object_value("watchTimeChart", self.watch_time_chart)
        writer.write_additional_data_value(self.additional_data)
    

