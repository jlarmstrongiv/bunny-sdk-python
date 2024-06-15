from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class AddCertificatePostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The Base64Url encoded binary data of the certificate file
    certificate: Optional[str] = None
    # The Base64Url encoded binary data of the certificate key file
    certificate_key: Optional[str] = None
    # The hostname to which the certificate will be added
    hostname: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AddCertificatePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AddCertificatePostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AddCertificatePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "Certificate": lambda n : setattr(self, 'certificate', n.get_str_value()),
            "CertificateKey": lambda n : setattr(self, 'certificate_key', n.get_str_value()),
            "Hostname": lambda n : setattr(self, 'hostname', n.get_str_value()),
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
        writer.write_str_value("Certificate", self.certificate)
        writer.write_str_value("CertificateKey", self.certificate_key)
        writer.write_str_value("Hostname", self.hostname)
        writer.write_additional_data_value(self.additional_data)
    

