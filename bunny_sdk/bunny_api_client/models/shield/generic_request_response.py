from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class GenericRequestResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The errorKey property
    error_key: Optional[str] = None
    # The message property
    message: Optional[str] = None
    # The statusCode property
    status_code: Optional[float] = None
    # The success property
    success: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GenericRequestResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GenericRequestResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GenericRequestResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "errorKey": lambda n : setattr(self, 'error_key', n.get_str_value()),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "statusCode": lambda n : setattr(self, 'status_code', n.get_float_value()),
            "success": lambda n : setattr(self, 'success', n.get_bool_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("errorKey", self.error_key)
        writer.write_str_value("message", self.message)
        writer.write_float_value("statusCode", self.status_code)
        writer.write_bool_value("success", self.success)
        writer.write_additional_data_value(self.additional_data)
    

