from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class ImportPostResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The RecordsFailed property
    records_failed: Optional[int] = None
    # The RecordsSkipped property
    records_skipped: Optional[int] = None
    # The RecordsSuccessful property
    records_successful: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ImportPostResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ImportPostResponse
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ImportPostResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "RecordsFailed": lambda n : setattr(self, 'records_failed', n.get_int_value()),
            "RecordsSkipped": lambda n : setattr(self, 'records_skipped', n.get_int_value()),
            "RecordsSuccessful": lambda n : setattr(self, 'records_successful', n.get_int_value()),
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
        writer.write_int_value("RecordsFailed", self.records_failed)
        writer.write_int_value("RecordsSkipped", self.records_skipped)
        writer.write_int_value("RecordsSuccessful", self.records_successful)
        writer.write_additional_data_value(self.additional_data)
    

