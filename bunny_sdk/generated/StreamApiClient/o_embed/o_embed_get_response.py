from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class OEmbedGetResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The height property
    height: Optional[int] = None
    # The html property
    html: Optional[str] = None
    # The providerName property
    provider_name: Optional[str] = None
    # The providerUrl property
    provider_url: Optional[str] = None
    # The thumbnailUrl property
    thumbnail_url: Optional[str] = None
    # The title property
    title: Optional[str] = None
    # The type property
    type: Optional[str] = None
    # The version property
    version: Optional[str] = None
    # The width property
    width: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OEmbedGetResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OEmbedGetResponse
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return OEmbedGetResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "height": lambda n : setattr(self, 'height', n.get_int_value()),
            "html": lambda n : setattr(self, 'html', n.get_str_value()),
            "providerName": lambda n : setattr(self, 'provider_name', n.get_str_value()),
            "providerUrl": lambda n : setattr(self, 'provider_url', n.get_str_value()),
            "thumbnailUrl": lambda n : setattr(self, 'thumbnail_url', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
            "width": lambda n : setattr(self, 'width', n.get_int_value()),
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
        writer.write_int_value("height", self.height)
        writer.write_str_value("html", self.html)
        writer.write_str_value("providerName", self.provider_name)
        writer.write_str_value("providerUrl", self.provider_url)
        writer.write_str_value("thumbnailUrl", self.thumbnail_url)
        writer.write_str_value("title", self.title)
        writer.write_str_value("type", self.type)
        writer.write_str_value("version", self.version)
        writer.write_int_value("width", self.width)
        writer.write_additional_data_value(self.additional_data)
    

