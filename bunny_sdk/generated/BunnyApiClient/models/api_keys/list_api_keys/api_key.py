from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class ApiKey(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The Id property
    id: Optional[int] = None
    # The Key property
    key: Optional[str] = None
    # The Roles property
    roles: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ApiKey:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ApiKey
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ApiKey()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "Id": lambda n : setattr(self, 'id', n.get_int_value()),
            "Key": lambda n : setattr(self, 'key', n.get_str_value()),
            "Roles": lambda n : setattr(self, 'roles', n.get_collection_of_primitive_values(str)),
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
        writer.write_int_value("Id", self.id)
        writer.write_str_value("Key", self.key)
        writer.write_collection_of_primitive_values("Roles", self.roles)
        writer.write_additional_data_value(self.additional_data)
    

