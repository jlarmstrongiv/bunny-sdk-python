from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .statistics_get_response_file_count_chart import StatisticsGetResponse_FileCountChart
    from .statistics_get_response_storage_used_chart import StatisticsGetResponse_StorageUsedChart

@dataclass
class StatisticsGetResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The FileCountChart property
    file_count_chart: Optional[StatisticsGetResponse_FileCountChart] = None
    # The StorageUsedChart property
    storage_used_chart: Optional[StatisticsGetResponse_StorageUsedChart] = None
    
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
        from .statistics_get_response_file_count_chart import StatisticsGetResponse_FileCountChart
        from .statistics_get_response_storage_used_chart import StatisticsGetResponse_StorageUsedChart

        from .statistics_get_response_file_count_chart import StatisticsGetResponse_FileCountChart
        from .statistics_get_response_storage_used_chart import StatisticsGetResponse_StorageUsedChart

        fields: Dict[str, Callable[[Any], None]] = {
            "FileCountChart": lambda n : setattr(self, 'file_count_chart', n.get_object_value(StatisticsGetResponse_FileCountChart)),
            "StorageUsedChart": lambda n : setattr(self, 'storage_used_chart', n.get_object_value(StatisticsGetResponse_StorageUsedChart)),
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
        writer.write_object_value("FileCountChart", self.file_count_chart)
        writer.write_object_value("StorageUsedChart", self.storage_used_chart)
        writer.write_additional_data_value(self.additional_data)
    

