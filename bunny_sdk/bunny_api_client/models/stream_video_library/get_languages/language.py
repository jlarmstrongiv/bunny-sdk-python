from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class Language(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The Name property
    name: Optional[str] = None
    # The ShortCode property
    short_code: Optional[str] = None
    # The SupportPlayerTranslation property
    support_player_translation: Optional[bool] = None
    # The SupportTranscribing property
    support_transcribing: Optional[bool] = None
    # The TranscribingAccuracy property
    transcribing_accuracy: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Language:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Language
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Language()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "Name": lambda n : setattr(self, 'name', n.get_str_value()),
            "ShortCode": lambda n : setattr(self, 'short_code', n.get_str_value()),
            "SupportPlayerTranslation": lambda n : setattr(self, 'support_player_translation', n.get_bool_value()),
            "SupportTranscribing": lambda n : setattr(self, 'support_transcribing', n.get_bool_value()),
            "TranscribingAccuracy": lambda n : setattr(self, 'transcribing_accuracy', n.get_int_value()),
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
        writer.write_str_value("ShortCode", self.short_code)
        writer.write_bool_value("SupportPlayerTranslation", self.support_player_translation)
        writer.write_bool_value("SupportTranscribing", self.support_transcribing)
        writer.write_int_value("TranscribingAccuracy", self.transcribing_accuracy)
        writer.write_additional_data_value(self.additional_data)
    

