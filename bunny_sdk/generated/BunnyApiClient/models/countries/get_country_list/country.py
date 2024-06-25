from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class Country(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The FlagUrl property
    flag_url: Optional[str] = None
    # The IsEU property
    is_e_u: Optional[bool] = None
    # The IsoCode property
    iso_code: Optional[str] = None
    # The Name property
    name: Optional[str] = None
    # The PopList property
    pop_list: Optional[List[str]] = None
    # The TaxPrefix property
    tax_prefix: Optional[str] = None
    # The TaxRate property
    tax_rate: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Country:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Country
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Country()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "FlagUrl": lambda n : setattr(self, 'flag_url', n.get_str_value()),
            "IsEU": lambda n : setattr(self, 'is_e_u', n.get_bool_value()),
            "IsoCode": lambda n : setattr(self, 'iso_code', n.get_str_value()),
            "Name": lambda n : setattr(self, 'name', n.get_str_value()),
            "PopList": lambda n : setattr(self, 'pop_list', n.get_collection_of_primitive_values(str)),
            "TaxPrefix": lambda n : setattr(self, 'tax_prefix', n.get_str_value()),
            "TaxRate": lambda n : setattr(self, 'tax_rate', n.get_float_value()),
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
        writer.write_str_value("FlagUrl", self.flag_url)
        writer.write_bool_value("IsEU", self.is_e_u)
        writer.write_str_value("IsoCode", self.iso_code)
        writer.write_str_value("Name", self.name)
        writer.write_collection_of_primitive_values("PopList", self.pop_list)
        writer.write_str_value("TaxPrefix", self.tax_prefix)
        writer.write_float_value("TaxRate", self.tax_rate)
        writer.write_additional_data_value(self.additional_data)
    

