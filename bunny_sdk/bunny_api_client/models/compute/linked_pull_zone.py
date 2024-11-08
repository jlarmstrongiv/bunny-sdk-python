from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class LinkedPullZone(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The DefaultHostname property
    default_hostname: Optional[str] = None
    # The Id property
    id: Optional[int] = None
    # The PullZoneName property
    pull_zone_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LinkedPullZone:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LinkedPullZone
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LinkedPullZone()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "DefaultHostname": lambda n : setattr(self, 'default_hostname', n.get_str_value()),
            "Id": lambda n : setattr(self, 'id', n.get_int_value()),
            "PullZoneName": lambda n : setattr(self, 'pull_zone_name', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("DefaultHostname", self.default_hostname)
        writer.write_int_value("Id", self.id)
        writer.write_str_value("PullZoneName", self.pull_zone_name)
        writer.write_additional_data_value(self.additional_data)
    

