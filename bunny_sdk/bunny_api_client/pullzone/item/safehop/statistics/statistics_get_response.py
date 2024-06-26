from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .statistics_get_response_requests_retried_chart import StatisticsGetResponse_RequestsRetriedChart
    from .statistics_get_response_requests_saved_chart import StatisticsGetResponse_RequestsSavedChart

@dataclass
class StatisticsGetResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The constructed chart of requests retried
    requests_retried_chart: Optional[StatisticsGetResponse_RequestsRetriedChart] = None
    # The constructed chart of requests saved
    requests_saved_chart: Optional[StatisticsGetResponse_RequestsSavedChart] = None
    # The total number of retried requests
    total_requests_retried: Optional[int] = None
    # The total number of saved requests
    total_requests_saved: Optional[int] = None
    
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
        from .statistics_get_response_requests_retried_chart import StatisticsGetResponse_RequestsRetriedChart
        from .statistics_get_response_requests_saved_chart import StatisticsGetResponse_RequestsSavedChart

        from .statistics_get_response_requests_retried_chart import StatisticsGetResponse_RequestsRetriedChart
        from .statistics_get_response_requests_saved_chart import StatisticsGetResponse_RequestsSavedChart

        fields: Dict[str, Callable[[Any], None]] = {
            "RequestsRetriedChart": lambda n : setattr(self, 'requests_retried_chart', n.get_object_value(StatisticsGetResponse_RequestsRetriedChart)),
            "RequestsSavedChart": lambda n : setattr(self, 'requests_saved_chart', n.get_object_value(StatisticsGetResponse_RequestsSavedChart)),
            "TotalRequestsRetried": lambda n : setattr(self, 'total_requests_retried', n.get_int_value()),
            "TotalRequestsSaved": lambda n : setattr(self, 'total_requests_saved', n.get_int_value()),
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
        writer.write_object_value("RequestsRetriedChart", self.requests_retried_chart)
        writer.write_object_value("RequestsSavedChart", self.requests_saved_chart)
        writer.write_int_value("TotalRequestsRetried", self.total_requests_retried)
        writer.write_int_value("TotalRequestsSaved", self.total_requests_saved)
        writer.write_additional_data_value(self.additional_data)
    

