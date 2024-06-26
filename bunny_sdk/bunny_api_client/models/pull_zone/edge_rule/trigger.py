from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class Trigger(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The trigger parameter 1. The value depends on the type of trigger.
    parameter1: Optional[str] = None
    # The list of pattern matches that will trigger the edge rule
    pattern_matches: Optional[List[str]] = None
    # The PatternMatchingType property
    pattern_matching_type: Optional[float] = None
    # The Type property
    type: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Trigger:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Trigger
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Trigger()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "Parameter1": lambda n : setattr(self, 'parameter1', n.get_str_value()),
            "PatternMatches": lambda n : setattr(self, 'pattern_matches', n.get_collection_of_primitive_values(str)),
            "PatternMatchingType": lambda n : setattr(self, 'pattern_matching_type', n.get_float_value()),
            "Type": lambda n : setattr(self, 'type', n.get_float_value()),
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
        writer.write_str_value("Parameter1", self.parameter1)
        writer.write_collection_of_primitive_values("PatternMatches", self.pattern_matches)
        writer.write_float_value("PatternMatchingType", self.pattern_matching_type)
        writer.write_float_value("Type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

