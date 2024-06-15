from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .statistics_get_response_queries_by_type_chart import StatisticsGetResponse_QueriesByTypeChart
    from .statistics_get_response_queries_served_chart import StatisticsGetResponse_QueriesServedChart

@dataclass
class StatisticsGetResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The QueriesByTypeChart property
    queries_by_type_chart: Optional[StatisticsGetResponse_QueriesByTypeChart] = None
    # The QueriesServedChart property
    queries_served_chart: Optional[StatisticsGetResponse_QueriesServedChart] = None
    # The TotalQueriesServed property
    total_queries_served: Optional[int] = None
    
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
        from .statistics_get_response_queries_by_type_chart import StatisticsGetResponse_QueriesByTypeChart
        from .statistics_get_response_queries_served_chart import StatisticsGetResponse_QueriesServedChart

        from .statistics_get_response_queries_by_type_chart import StatisticsGetResponse_QueriesByTypeChart
        from .statistics_get_response_queries_served_chart import StatisticsGetResponse_QueriesServedChart

        fields: Dict[str, Callable[[Any], None]] = {
            "QueriesByTypeChart": lambda n : setattr(self, 'queries_by_type_chart', n.get_object_value(StatisticsGetResponse_QueriesByTypeChart)),
            "QueriesServedChart": lambda n : setattr(self, 'queries_served_chart', n.get_object_value(StatisticsGetResponse_QueriesServedChart)),
            "TotalQueriesServed": lambda n : setattr(self, 'total_queries_served', n.get_int_value()),
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
        writer.write_object_value("QueriesByTypeChart", self.queries_by_type_chart)
        writer.write_object_value("QueriesServedChart", self.queries_served_chart)
        writer.write_int_value("TotalQueriesServed", self.total_queries_served)
        writer.write_additional_data_value(self.additional_data)
    

