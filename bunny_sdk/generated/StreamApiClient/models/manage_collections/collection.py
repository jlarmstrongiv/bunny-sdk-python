from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class Collection(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The unique ID of the collection
    guid: Optional[str] = None
    # The name of the collection
    name: Optional[str] = None
    # The URLs of preview images of videos in the collection
    preview_image_urls: Optional[str] = None
    # The IDs of videos to be used as preview icons
    preview_video_ids: Optional[str] = None
    # The total storage size of the collection
    total_size: Optional[int] = None
    # The number of videos that the collection contains
    video_count: Optional[int] = None
    # The video library ID that contains the collection
    video_library_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Collection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Collection
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Collection()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "guid": lambda n : setattr(self, 'guid', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "previewImageUrls": lambda n : setattr(self, 'preview_image_urls', n.get_str_value()),
            "previewVideoIds": lambda n : setattr(self, 'preview_video_ids', n.get_str_value()),
            "totalSize": lambda n : setattr(self, 'total_size', n.get_int_value()),
            "videoCount": lambda n : setattr(self, 'video_count', n.get_int_value()),
            "videoLibraryId": lambda n : setattr(self, 'video_library_id', n.get_int_value()),
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
        writer.write_str_value("name", self.name)
        writer.write_additional_data_value(self.additional_data)
    

