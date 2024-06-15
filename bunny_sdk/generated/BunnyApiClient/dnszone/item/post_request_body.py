from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class PostRequestBody(AdditionalDataHolder, Parsable):
    """
    The template for adding optional properties.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The CustomNameserversEnabled property
    custom_nameservers_enabled: Optional[bool] = None
    # The LogAnonymizationType property
    log_anonymization_type: Optional[float] = None
    # The LoggingEnabled property
    logging_enabled: Optional[bool] = None
    # Determines if the log anonymization should be enabled
    logging_i_p_anonymization_enabled: Optional[bool] = None
    # The Nameserver1 property
    nameserver1: Optional[str] = None
    # The Nameserver2 property
    nameserver2: Optional[str] = None
    # The SoaEmail property
    soa_email: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "CustomNameserversEnabled": lambda n : setattr(self, 'custom_nameservers_enabled', n.get_bool_value()),
            "LogAnonymizationType": lambda n : setattr(self, 'log_anonymization_type', n.get_float_value()),
            "LoggingEnabled": lambda n : setattr(self, 'logging_enabled', n.get_bool_value()),
            "LoggingIPAnonymizationEnabled": lambda n : setattr(self, 'logging_i_p_anonymization_enabled', n.get_bool_value()),
            "Nameserver1": lambda n : setattr(self, 'nameserver1', n.get_str_value()),
            "Nameserver2": lambda n : setattr(self, 'nameserver2', n.get_str_value()),
            "SoaEmail": lambda n : setattr(self, 'soa_email', n.get_str_value()),
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
        writer.write_bool_value("CustomNameserversEnabled", self.custom_nameservers_enabled)
        writer.write_float_value("LogAnonymizationType", self.log_anonymization_type)
        writer.write_bool_value("LoggingEnabled", self.logging_enabled)
        writer.write_bool_value("LoggingIPAnonymizationEnabled", self.logging_i_p_anonymization_enabled)
        writer.write_str_value("Nameserver1", self.nameserver1)
        writer.write_str_value("Nameserver2", self.nameserver2)
        writer.write_str_value("SoaEmail", self.soa_email)
        writer.write_additional_data_value(self.additional_data)
    

