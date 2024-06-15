from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class DnsRecord_IPGeoLocationInfo(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The ASN property
    a_s_n: Optional[int] = None
    # The City property
    city: Optional[str] = None
    # The Country property
    country: Optional[str] = None
    # The CountryCode property
    country_code: Optional[str] = None
    # The OrganizationName property
    organization_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DnsRecord_IPGeoLocationInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DnsRecord_IPGeoLocationInfo
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DnsRecord_IPGeoLocationInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "ASN": lambda n : setattr(self, 'a_s_n', n.get_int_value()),
            "City": lambda n : setattr(self, 'city', n.get_str_value()),
            "Country": lambda n : setattr(self, 'country', n.get_str_value()),
            "CountryCode": lambda n : setattr(self, 'country_code', n.get_str_value()),
            "OrganizationName": lambda n : setattr(self, 'organization_name', n.get_str_value()),
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
        writer.write_int_value("ASN", self.a_s_n)
        writer.write_str_value("City", self.city)
        writer.write_str_value("Country", self.country)
        writer.write_str_value("CountryCode", self.country_code)
        writer.write_str_value("OrganizationName", self.organization_name)
        writer.write_additional_data_value(self.additional_data)
    

