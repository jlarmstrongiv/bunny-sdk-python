from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .queuestatistics_get_response_concurrent_requests_chart import QueuestatisticsGetResponse_ConcurrentRequestsChart
    from .queuestatistics_get_response_queued_requests_chart import QueuestatisticsGetResponse_QueuedRequestsChart

@dataclass
class QueuestatisticsGetResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The constructed chart of origin shield concurrent requests
    concurrent_requests_chart: Optional[QueuestatisticsGetResponse_ConcurrentRequestsChart] = None
    # The constructed chart of origin shield requests chart
    queued_requests_chart: Optional[QueuestatisticsGetResponse_QueuedRequestsChart] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> QueuestatisticsGetResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: QueuestatisticsGetResponse
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return QueuestatisticsGetResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .queuestatistics_get_response_concurrent_requests_chart import QueuestatisticsGetResponse_ConcurrentRequestsChart
        from .queuestatistics_get_response_queued_requests_chart import QueuestatisticsGetResponse_QueuedRequestsChart

        from .queuestatistics_get_response_concurrent_requests_chart import QueuestatisticsGetResponse_ConcurrentRequestsChart
        from .queuestatistics_get_response_queued_requests_chart import QueuestatisticsGetResponse_QueuedRequestsChart

        fields: Dict[str, Callable[[Any], None]] = {
            "ConcurrentRequestsChart": lambda n : setattr(self, 'concurrent_requests_chart', n.get_object_value(QueuestatisticsGetResponse_ConcurrentRequestsChart)),
            "QueuedRequestsChart": lambda n : setattr(self, 'queued_requests_chart', n.get_object_value(QueuestatisticsGetResponse_QueuedRequestsChart)),
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
        writer.write_object_value("ConcurrentRequestsChart", self.concurrent_requests_chart)
        writer.write_object_value("QueuedRequestsChart", self.queued_requests_chart)
        writer.write_additional_data_value(self.additional_data)
    

