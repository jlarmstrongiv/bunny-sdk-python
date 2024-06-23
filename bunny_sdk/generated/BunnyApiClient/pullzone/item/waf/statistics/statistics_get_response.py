from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .statistics_get_response_threats_blocked_chart import StatisticsGetResponse_ThreatsBlockedChart
    from .statistics_get_response_threats_checked_chart import StatisticsGetResponse_ThreatsCheckedChart

@dataclass
class StatisticsGetResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The ThreatsBlockedChart property
    threats_blocked_chart: Optional[StatisticsGetResponse_ThreatsBlockedChart] = None
    # The ThreatsCheckedChart property
    threats_checked_chart: Optional[StatisticsGetResponse_ThreatsCheckedChart] = None
    # The TotalBlockedRequests property
    total_blocked_requests: Optional[int] = None
    # The TotalCheckedRequests property
    total_checked_requests: Optional[int] = None
    
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
        from .statistics_get_response_threats_blocked_chart import StatisticsGetResponse_ThreatsBlockedChart
        from .statistics_get_response_threats_checked_chart import StatisticsGetResponse_ThreatsCheckedChart

        from .statistics_get_response_threats_blocked_chart import StatisticsGetResponse_ThreatsBlockedChart
        from .statistics_get_response_threats_checked_chart import StatisticsGetResponse_ThreatsCheckedChart

        fields: Dict[str, Callable[[Any], None]] = {
            "ThreatsBlockedChart": lambda n : setattr(self, 'threats_blocked_chart', n.get_object_value(StatisticsGetResponse_ThreatsBlockedChart)),
            "ThreatsCheckedChart": lambda n : setattr(self, 'threats_checked_chart', n.get_object_value(StatisticsGetResponse_ThreatsCheckedChart)),
            "TotalBlockedRequests": lambda n : setattr(self, 'total_blocked_requests', n.get_int_value()),
            "TotalCheckedRequests": lambda n : setattr(self, 'total_checked_requests', n.get_int_value()),
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
        writer.write_object_value("ThreatsBlockedChart", self.threats_blocked_chart)
        writer.write_object_value("ThreatsCheckedChart", self.threats_checked_chart)
        writer.write_int_value("TotalBlockedRequests", self.total_blocked_requests)
        writer.write_int_value("TotalCheckedRequests", self.total_checked_requests)
        writer.write_additional_data_value(self.additional_data)
    

