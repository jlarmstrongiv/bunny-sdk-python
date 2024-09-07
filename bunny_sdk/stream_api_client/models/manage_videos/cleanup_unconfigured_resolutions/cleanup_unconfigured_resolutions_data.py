from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class CleanupUnconfiguredResolutionsData(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The availableResolutionsAfter property
    available_resolutions_after: Optional[List[str]] = None
    # The deletedOriginal property
    deleted_original: Optional[bool] = None
    # The deletedStorageObjects property
    deleted_storage_objects: Optional[bool] = None
    # The modifiedPlaylist property
    modified_playlist: Optional[bool] = None
    # The resolutionsToDelete property
    resolutions_to_delete: Optional[List[str]] = None
    # The resolutionsToDeleteFromMp4 property
    resolutions_to_delete_from_mp4: Optional[List[str]] = None
    # The resolutionsToDeleteFromPlaylist property
    resolutions_to_delete_from_playlist: Optional[List[str]] = None
    # The resolutionsToDeleteFromStorage property
    resolutions_to_delete_from_storage: Optional[List[str]] = None
    # The storageObjectsToDelete property
    storage_objects_to_delete: Optional[List[str]] = None
    # The updatedAvailableResolutions property
    updated_available_resolutions: Optional[bool] = None
    # The videoId property
    video_id: Optional[str] = None
    # The videoLibraryId property
    video_library_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CleanupUnconfiguredResolutionsData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CleanupUnconfiguredResolutionsData
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CleanupUnconfiguredResolutionsData()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "availableResolutionsAfter": lambda n : setattr(self, 'available_resolutions_after', n.get_collection_of_primitive_values(str)),
            "deletedOriginal": lambda n : setattr(self, 'deleted_original', n.get_bool_value()),
            "deletedStorageObjects": lambda n : setattr(self, 'deleted_storage_objects', n.get_bool_value()),
            "modifiedPlaylist": lambda n : setattr(self, 'modified_playlist', n.get_bool_value()),
            "resolutionsToDelete": lambda n : setattr(self, 'resolutions_to_delete', n.get_collection_of_primitive_values(str)),
            "resolutionsToDeleteFromMp4": lambda n : setattr(self, 'resolutions_to_delete_from_mp4', n.get_collection_of_primitive_values(str)),
            "resolutionsToDeleteFromPlaylist": lambda n : setattr(self, 'resolutions_to_delete_from_playlist', n.get_collection_of_primitive_values(str)),
            "resolutionsToDeleteFromStorage": lambda n : setattr(self, 'resolutions_to_delete_from_storage', n.get_collection_of_primitive_values(str)),
            "storageObjectsToDelete": lambda n : setattr(self, 'storage_objects_to_delete', n.get_collection_of_primitive_values(str)),
            "updatedAvailableResolutions": lambda n : setattr(self, 'updated_available_resolutions', n.get_bool_value()),
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
        writer.write_collection_of_primitive_values("availableResolutionsAfter", self.available_resolutions_after)
        writer.write_bool_value("deletedOriginal", self.deleted_original)
        writer.write_bool_value("deletedStorageObjects", self.deleted_storage_objects)
        writer.write_bool_value("modifiedPlaylist", self.modified_playlist)
        writer.write_collection_of_primitive_values("resolutionsToDelete", self.resolutions_to_delete)
        writer.write_collection_of_primitive_values("resolutionsToDeleteFromMp4", self.resolutions_to_delete_from_mp4)
        writer.write_collection_of_primitive_values("resolutionsToDeleteFromPlaylist", self.resolutions_to_delete_from_playlist)
        writer.write_collection_of_primitive_values("resolutionsToDeleteFromStorage", self.resolutions_to_delete_from_storage)
        writer.write_collection_of_primitive_values("storageObjectsToDelete", self.storage_objects_to_delete)
        writer.write_bool_value("updatedAvailableResolutions", self.updated_available_resolutions)
        writer.write_str_value("videoId", self.video_id)
        writer.write_int_value("videoLibraryId", self.video_library_id)
        writer.write_additional_data_value(self.additional_data)
    

