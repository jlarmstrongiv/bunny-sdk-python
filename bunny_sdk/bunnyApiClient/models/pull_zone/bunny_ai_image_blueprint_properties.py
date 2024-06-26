from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class BunnyAiImageBlueprint_Properties(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The Cfg property
    cfg: Optional[str] = None
    # The NegativePrompt property
    negative_prompt: Optional[str] = None
    # The PostPrompt property
    post_prompt: Optional[str] = None
    # The PrePrompt property
    pre_prompt: Optional[str] = None
    # The Steps property
    steps: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BunnyAiImageBlueprint_Properties:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BunnyAiImageBlueprint_Properties
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return BunnyAiImageBlueprint_Properties()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "Cfg": lambda n : setattr(self, 'cfg', n.get_str_value()),
            "NegativePrompt": lambda n : setattr(self, 'negative_prompt', n.get_str_value()),
            "PostPrompt": lambda n : setattr(self, 'post_prompt', n.get_str_value()),
            "PrePrompt": lambda n : setattr(self, 'pre_prompt', n.get_str_value()),
            "Steps": lambda n : setattr(self, 'steps', n.get_str_value()),
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
        writer.write_str_value("Cfg", self.cfg)
        writer.write_str_value("NegativePrompt", self.negative_prompt)
        writer.write_str_value("PostPrompt", self.post_prompt)
        writer.write_str_value("PrePrompt", self.pre_prompt)
        writer.write_str_value("Steps", self.steps)
        writer.write_additional_data_value(self.additional_data)
    

