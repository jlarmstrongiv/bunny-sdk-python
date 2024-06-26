from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class TranscodingMessage(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The issueCode property
    issue_code: Optional[float] = None
    # The level property
    level: Optional[float] = None
    # The message property
    message: Optional[str] = None
    # The timeStamp property
    time_stamp: Optional[datetime.datetime] = None
    # The value property
    value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TranscodingMessage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TranscodingMessage
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TranscodingMessage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "issueCode": lambda n : setattr(self, 'issue_code', n.get_float_value()),
            "level": lambda n : setattr(self, 'level', n.get_float_value()),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "timeStamp": lambda n : setattr(self, 'time_stamp', n.get_datetime_value()),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
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
        writer.write_float_value("issueCode", self.issue_code)
        writer.write_float_value("level", self.level)
        writer.write_str_value("message", self.message)
        writer.write_datetime_value("timeStamp", self.time_stamp)
        writer.write_str_value("value", self.value)
        writer.write_additional_data_value(self.additional_data)
    

