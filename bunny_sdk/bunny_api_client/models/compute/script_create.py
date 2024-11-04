from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .integration import Integration

@dataclass
class ScriptCreate(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The Code property
    code: Optional[str] = None
    # The CreateLinkedPullZone property
    create_linked_pull_zone: Optional[bool] = None
    # The Integration property
    integration: Optional[Integration] = None
    # The Name property
    name: Optional[str] = None
    # The ScriptType property
    script_type: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ScriptCreate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ScriptCreate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ScriptCreate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .integration import Integration

        from .integration import Integration

        fields: Dict[str, Callable[[Any], None]] = {
            "Code": lambda n : setattr(self, 'code', n.get_str_value()),
            "CreateLinkedPullZone": lambda n : setattr(self, 'create_linked_pull_zone', n.get_bool_value()),
            "Integration": lambda n : setattr(self, 'integration', n.get_object_value(Integration)),
            "Name": lambda n : setattr(self, 'name', n.get_str_value()),
            "ScriptType": lambda n : setattr(self, 'script_type', n.get_float_value()),
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
        writer.write_str_value("Code", self.code)
        writer.write_bool_value("CreateLinkedPullZone", self.create_linked_pull_zone)
        writer.write_object_value("Integration", self.integration)
        writer.write_str_value("Name", self.name)
        writer.write_float_value("ScriptType", self.script_type)
        writer.write_additional_data_value(self.additional_data)
    

