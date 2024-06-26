from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class Action(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The ActionParameter1 property
    action_parameter1: Optional[str] = None
    # The ActionParameter2 property
    action_parameter2: Optional[str] = None
    # The ActionType property
    action_type: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Action:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Action
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Action()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "ActionParameter1": lambda n : setattr(self, 'action_parameter1', n.get_str_value()),
            "ActionParameter2": lambda n : setattr(self, 'action_parameter2', n.get_str_value()),
            "ActionType": lambda n : setattr(self, 'action_type', n.get_float_value()),
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
        writer.write_str_value("ActionParameter1", self.action_parameter1)
        writer.write_str_value("ActionParameter2", self.action_parameter2)
        writer.write_float_value("ActionType", self.action_type)
        writer.write_additional_data_value(self.additional_data)
    

