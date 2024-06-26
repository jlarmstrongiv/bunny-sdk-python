from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class Region(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The AllowLatencyRouting property
    allow_latency_routing: Optional[bool] = None
    # The ContinentCode property
    continent_code: Optional[str] = None
    # The CountryCode property
    country_code: Optional[str] = None
    # The Id property
    id: Optional[int] = None
    # The Latitude property
    latitude: Optional[float] = None
    # The Longitude property
    longitude: Optional[float] = None
    # The Name property
    name: Optional[str] = None
    # The PricePerGigabyte property
    price_per_gigabyte: Optional[float] = None
    # The RegionCode property
    region_code: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Region:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Region
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Region()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "AllowLatencyRouting": lambda n : setattr(self, 'allow_latency_routing', n.get_bool_value()),
            "ContinentCode": lambda n : setattr(self, 'continent_code', n.get_str_value()),
            "CountryCode": lambda n : setattr(self, 'country_code', n.get_str_value()),
            "Id": lambda n : setattr(self, 'id', n.get_int_value()),
            "Latitude": lambda n : setattr(self, 'latitude', n.get_float_value()),
            "Longitude": lambda n : setattr(self, 'longitude', n.get_float_value()),
            "Name": lambda n : setattr(self, 'name', n.get_str_value()),
            "PricePerGigabyte": lambda n : setattr(self, 'price_per_gigabyte', n.get_float_value()),
            "RegionCode": lambda n : setattr(self, 'region_code', n.get_str_value()),
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
        writer.write_bool_value("AllowLatencyRouting", self.allow_latency_routing)
        writer.write_str_value("ContinentCode", self.continent_code)
        writer.write_str_value("CountryCode", self.country_code)
        writer.write_int_value("Id", self.id)
        writer.write_float_value("Latitude", self.latitude)
        writer.write_float_value("Longitude", self.longitude)
        writer.write_str_value("Name", self.name)
        writer.write_float_value("PricePerGigabyte", self.price_per_gigabyte)
        writer.write_str_value("RegionCode", self.region_code)
        writer.write_additional_data_value(self.additional_data)
    

