from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class Hostname(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Contains the Base64Url encoded certificate for the hostname
    certificate: Optional[str] = None
    # Contains the Base64Url encoded certificate key for the hostname
    certificate_key: Optional[str] = None
    # Determines if the Force SSL feature is enabled
    force_s_s_l: Optional[bool] = None
    # Determines if the hostname has an SSL certificate configured
    has_certificate: Optional[bool] = None
    # The unique ID of the hostname
    id: Optional[int] = None
    # Determines if this is a system hostname controlled by bunny.net
    is_system_hostname: Optional[bool] = None
    # The hostname value for the domain name
    value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Hostname:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Hostname
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Hostname()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "Certificate": lambda n : setattr(self, 'certificate', n.get_str_value()),
            "CertificateKey": lambda n : setattr(self, 'certificate_key', n.get_str_value()),
            "ForceSSL": lambda n : setattr(self, 'force_s_s_l', n.get_bool_value()),
            "HasCertificate": lambda n : setattr(self, 'has_certificate', n.get_bool_value()),
            "Id": lambda n : setattr(self, 'id', n.get_int_value()),
            "IsSystemHostname": lambda n : setattr(self, 'is_system_hostname', n.get_bool_value()),
            "Value": lambda n : setattr(self, 'value', n.get_str_value()),
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
        writer.write_bool_value("ForceSSL", self.force_s_s_l)
        writer.write_bool_value("HasCertificate", self.has_certificate)
        writer.write_int_value("Id", self.id)
        writer.write_bool_value("IsSystemHostname", self.is_system_hostname)
        writer.write_str_value("Value", self.value)
        writer.write_additional_data_value(self.additional_data)
    

