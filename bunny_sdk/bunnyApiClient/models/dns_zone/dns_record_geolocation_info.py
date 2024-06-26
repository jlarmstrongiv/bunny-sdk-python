from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class DnsRecord_GeolocationInfo(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The City property
    city: Optional[str] = None
    # The Country property
    country: Optional[str] = None
    # The Latitude property
    latitude: Optional[float] = None
    # The Longitude property
    longitude: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DnsRecord_GeolocationInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DnsRecord_GeolocationInfo
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DnsRecord_GeolocationInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "City": lambda n : setattr(self, 'city', n.get_str_value()),
            "Country": lambda n : setattr(self, 'country', n.get_str_value()),
            "Latitude": lambda n : setattr(self, 'latitude', n.get_float_value()),
            "Longitude": lambda n : setattr(self, 'longitude', n.get_float_value()),
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
        writer.write_str_value("City", self.city)
        writer.write_str_value("Country", self.country)
        writer.write_float_value("Latitude", self.latitude)
        writer.write_float_value("Longitude", self.longitude)
        writer.write_additional_data_value(self.additional_data)
    

