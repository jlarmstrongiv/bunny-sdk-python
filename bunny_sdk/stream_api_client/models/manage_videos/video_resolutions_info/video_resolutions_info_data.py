from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .resolutions import Resolutions

@dataclass
class VideoResolutionsInfoData(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The availableResolutions property
    available_resolutions: Optional[List[str]] = None
    # The configuredResolutions property
    configured_resolutions: Optional[List[str]] = None
    # The hasOriginal property
    has_original: Optional[bool] = None
    # The mp4Resolutions property
    mp4_resolutions: Optional[Resolutions] = None
    # The playlistResolutions property
    playlist_resolutions: Optional[Resolutions] = None
    # The storageResolutions property
    storage_resolutions: Optional[Resolutions] = None
    # The videoId property
    video_id: Optional[str] = None
    # The videoLibraryId property
    video_library_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VideoResolutionsInfoData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VideoResolutionsInfoData
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VideoResolutionsInfoData()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .resolutions import Resolutions

        from .resolutions import Resolutions

        fields: Dict[str, Callable[[Any], None]] = {
            "availableResolutions": lambda n : setattr(self, 'available_resolutions', n.get_collection_of_primitive_values(str)),
            "configuredResolutions": lambda n : setattr(self, 'configured_resolutions', n.get_collection_of_primitive_values(str)),
            "hasOriginal": lambda n : setattr(self, 'has_original', n.get_bool_value()),
            "mp4Resolutions": lambda n : setattr(self, 'mp4_resolutions', n.get_object_value(Resolutions)),
            "playlistResolutions": lambda n : setattr(self, 'playlist_resolutions', n.get_object_value(Resolutions)),
            "storageResolutions": lambda n : setattr(self, 'storage_resolutions', n.get_object_value(Resolutions)),
            "videoId": lambda n : setattr(self, 'video_id', n.get_str_value()),
            "videoLibraryId": lambda n : setattr(self, 'video_library_id', n.get_int_value()),
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
        writer.write_collection_of_primitive_values("availableResolutions", self.available_resolutions)
        writer.write_collection_of_primitive_values("configuredResolutions", self.configured_resolutions)
        writer.write_bool_value("hasOriginal", self.has_original)
        writer.write_object_value("mp4Resolutions", self.mp4_resolutions)
        writer.write_object_value("playlistResolutions", self.playlist_resolutions)
        writer.write_object_value("storageResolutions", self.storage_resolutions)
        writer.write_str_value("videoId", self.video_id)
        writer.write_int_value("videoLibraryId", self.video_library_id)
        writer.write_additional_data_value(self.additional_data)
    

