from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.api_error import APIError
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class StructuredBadRequestResponse(APIError):
    """
    The server could not understand the request due to invalid syntax.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The ErrorKey property
    error_key: Optional[str] = None
    # The Field property
    field: Optional[str] = None
    # The Message property
    message: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StructuredBadRequestResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StructuredBadRequestResponse
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return StructuredBadRequestResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "ErrorKey": lambda n : setattr(self, 'error_key', n.get_str_value()),
            "Field": lambda n : setattr(self, 'field', n.get_str_value()),
            "Message": lambda n : setattr(self, 'message', n.get_str_value()),
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
        writer.write_str_value("ErrorKey", self.error_key)
        writer.write_str_value("Field", self.field)
        writer.write_str_value("Message", self.message)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def primary_message(self) -> str:
        """
        The primary error message.
        """
        return super().message

