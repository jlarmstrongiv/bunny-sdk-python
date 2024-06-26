from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class WithSrclangPathParameterPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Base64 encoded captions file
    captions_file: Optional[str] = None
    # The text description label for the caption
    label: Optional[str] = None
    # The unique srclang shortcode for the caption
    srclang: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WithSrclangPathParameterPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WithSrclangPathParameterPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WithSrclangPathParameterPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "captionsFile": lambda n : setattr(self, 'captions_file', n.get_str_value()),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "srclang": lambda n : setattr(self, 'srclang', n.get_str_value()),
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
        writer.write_str_value("captionsFile", self.captions_file)
        writer.write_str_value("label", self.label)
        writer.write_str_value("srclang", self.srclang)
        writer.write_additional_data_value(self.additional_data)
    

