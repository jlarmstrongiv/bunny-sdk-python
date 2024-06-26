from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .statistics_get_response_average_compression_chart import StatisticsGetResponse_AverageCompressionChart
    from .statistics_get_response_average_processing_time_chart import StatisticsGetResponse_AverageProcessingTimeChart
    from .statistics_get_response_requests_optimized_chart import StatisticsGetResponse_RequestsOptimizedChart
    from .statistics_get_response_traffic_saved_chart import StatisticsGetResponse_TrafficSavedChart

@dataclass
class StatisticsGetResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Average compression chart of the responses
    average_compression_chart: Optional[StatisticsGetResponse_AverageCompressionChart] = None
    # The average compression ratio of CDN responses
    average_compression_ratio: Optional[float] = None
    # The average processing time of each request
    average_processing_time: Optional[float] = None
    # The AverageProcessingTimeChart property
    average_processing_time_chart: Optional[StatisticsGetResponse_AverageProcessingTimeChart] = None
    # The constructed chart of optimized requests
    requests_optimized_chart: Optional[StatisticsGetResponse_RequestsOptimizedChart] = None
    # The total number of optimized requests
    total_requests_optimized: Optional[float] = None
    # The total requests saved
    total_traffic_saved: Optional[float] = None
    # The constructed chart of saved traffic
    traffic_saved_chart: Optional[StatisticsGetResponse_TrafficSavedChart] = None
    
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
        from .statistics_get_response_average_compression_chart import StatisticsGetResponse_AverageCompressionChart
        from .statistics_get_response_average_processing_time_chart import StatisticsGetResponse_AverageProcessingTimeChart
        from .statistics_get_response_requests_optimized_chart import StatisticsGetResponse_RequestsOptimizedChart
        from .statistics_get_response_traffic_saved_chart import StatisticsGetResponse_TrafficSavedChart

        from .statistics_get_response_average_compression_chart import StatisticsGetResponse_AverageCompressionChart
        from .statistics_get_response_average_processing_time_chart import StatisticsGetResponse_AverageProcessingTimeChart
        from .statistics_get_response_requests_optimized_chart import StatisticsGetResponse_RequestsOptimizedChart
        from .statistics_get_response_traffic_saved_chart import StatisticsGetResponse_TrafficSavedChart

        fields: Dict[str, Callable[[Any], None]] = {
            "AverageCompressionChart": lambda n : setattr(self, 'average_compression_chart', n.get_object_value(StatisticsGetResponse_AverageCompressionChart)),
            "AverageCompressionRatio": lambda n : setattr(self, 'average_compression_ratio', n.get_float_value()),
            "AverageProcessingTime": lambda n : setattr(self, 'average_processing_time', n.get_float_value()),
            "AverageProcessingTimeChart": lambda n : setattr(self, 'average_processing_time_chart', n.get_object_value(StatisticsGetResponse_AverageProcessingTimeChart)),
            "RequestsOptimizedChart": lambda n : setattr(self, 'requests_optimized_chart', n.get_object_value(StatisticsGetResponse_RequestsOptimizedChart)),
            "TotalRequestsOptimized": lambda n : setattr(self, 'total_requests_optimized', n.get_float_value()),
            "TotalTrafficSaved": lambda n : setattr(self, 'total_traffic_saved', n.get_float_value()),
            "TrafficSavedChart": lambda n : setattr(self, 'traffic_saved_chart', n.get_object_value(StatisticsGetResponse_TrafficSavedChart)),
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
        writer.write_object_value("AverageCompressionChart", self.average_compression_chart)
        writer.write_float_value("AverageCompressionRatio", self.average_compression_ratio)
        writer.write_float_value("AverageProcessingTime", self.average_processing_time)
        writer.write_object_value("AverageProcessingTimeChart", self.average_processing_time_chart)
        writer.write_object_value("RequestsOptimizedChart", self.requests_optimized_chart)
        writer.write_float_value("TotalRequestsOptimized", self.total_requests_optimized)
        writer.write_float_value("TotalTrafficSaved", self.total_traffic_saved)
        writer.write_object_value("TrafficSavedChart", self.traffic_saved_chart)
        writer.write_additional_data_value(self.additional_data)
    

