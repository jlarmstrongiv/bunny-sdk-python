from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .properties import Properties

@dataclass
class OptimizerClass(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The Name property
    name: Optional[str] = None
    # The Properties property
    properties: Optional[Properties] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OptimizerClass:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OptimizerClass
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return OptimizerClass()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .properties import Properties

        from .properties import Properties

        fields: Dict[str, Callable[[Any], None]] = {
            "Name": lambda n : setattr(self, 'name', n.get_str_value()),
            "Properties": lambda n : setattr(self, 'properties', n.get_object_value(Properties)),
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
        writer.write_str_value("Name", self.name)
        writer.write_object_value("Properties", self.properties)
        writer.write_additional_data_value(self.additional_data)
    

