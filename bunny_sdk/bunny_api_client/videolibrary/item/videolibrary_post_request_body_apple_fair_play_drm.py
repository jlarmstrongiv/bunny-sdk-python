from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class VideolibraryPostRequestBody_AppleFairPlayDrm(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The CertificateExpirationDate property
    certificate_expiration_date: Optional[datetime.datetime] = None
    # The CertificateId property
    certificate_id: Optional[int] = None
    # The Enabled property
    enabled: Optional[bool] = None
    # The Provider property
    provider: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VideolibraryPostRequestBody_AppleFairPlayDrm:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VideolibraryPostRequestBody_AppleFairPlayDrm
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return VideolibraryPostRequestBody_AppleFairPlayDrm()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "CertificateExpirationDate": lambda n : setattr(self, 'certificate_expiration_date', n.get_datetime_value()),
            "CertificateId": lambda n : setattr(self, 'certificate_id', n.get_int_value()),
            "Enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "Provider": lambda n : setattr(self, 'provider', n.get_str_value()),
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
        writer.write_datetime_value("CertificateExpirationDate", self.certificate_expiration_date)
        writer.write_int_value("CertificateId", self.certificate_id)
        writer.write_bool_value("Enabled", self.enabled)
        writer.write_str_value("Provider", self.provider)
        writer.write_additional_data_value(self.additional_data)
    

