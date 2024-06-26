from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class EdgeScriptVariable(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The DefaultValue property
    default_value: Optional[str] = None
    # The Id property
    id: Optional[int] = None
    # The Name property
    name: Optional[str] = None
    # The Required property
    required: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EdgeScriptVariable:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EdgeScriptVariable
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EdgeScriptVariable()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "DefaultValue": lambda n : setattr(self, 'default_value', n.get_str_value()),
            "Id": lambda n : setattr(self, 'id', n.get_int_value()),
            "Name": lambda n : setattr(self, 'name', n.get_str_value()),
            "Required": lambda n : setattr(self, 'required', n.get_bool_value()),
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
        writer.write_str_value("DefaultValue", self.default_value)
        writer.write_str_value("Name", self.name)
        writer.write_bool_value("Required", self.required)
        writer.write_additional_data_value(self.additional_data)
    

