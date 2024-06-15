from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class File(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The ArrayNumber property
    array_number: Optional[int] = None
    # The Checksum property
    checksum: Optional[str] = None
    # The ContentType property
    content_type: Optional[str] = None
    # The DateCreated property
    date_created: Optional[datetime.datetime] = None
    # The Guid property
    guid: Optional[str] = None
    # The IsDirectory property
    is_directory: Optional[bool] = None
    # The LastChanged property
    last_changed: Optional[datetime.datetime] = None
    # The Length property
    length: Optional[int] = None
    # The ObjectName property
    object_name: Optional[str] = None
    # The Path property
    path: Optional[str] = None
    # The ReplicatedZones property
    replicated_zones: Optional[str] = None
    # The ServerId property
    server_id: Optional[int] = None
    # The StorageZoneId property
    storage_zone_id: Optional[int] = None
    # The StorageZoneName property
    storage_zone_name: Optional[str] = None
    # The UserId property
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> File:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: File
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return File()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "ArrayNumber": lambda n : setattr(self, 'array_number', n.get_int_value()),
            "Checksum": lambda n : setattr(self, 'checksum', n.get_str_value()),
            "ContentType": lambda n : setattr(self, 'content_type', n.get_str_value()),
            "DateCreated": lambda n : setattr(self, 'date_created', n.get_datetime_value()),
            "Guid": lambda n : setattr(self, 'guid', n.get_str_value()),
            "IsDirectory": lambda n : setattr(self, 'is_directory', n.get_bool_value()),
            "LastChanged": lambda n : setattr(self, 'last_changed', n.get_datetime_value()),
            "Length": lambda n : setattr(self, 'length', n.get_int_value()),
            "ObjectName": lambda n : setattr(self, 'object_name', n.get_str_value()),
            "Path": lambda n : setattr(self, 'path', n.get_str_value()),
            "ReplicatedZones": lambda n : setattr(self, 'replicated_zones', n.get_str_value()),
            "ServerId": lambda n : setattr(self, 'server_id', n.get_int_value()),
            "StorageZoneId": lambda n : setattr(self, 'storage_zone_id', n.get_int_value()),
            "StorageZoneName": lambda n : setattr(self, 'storage_zone_name', n.get_str_value()),
            "UserId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_int_value("ArrayNumber", self.array_number)
        writer.write_str_value("Checksum", self.checksum)
        writer.write_str_value("ContentType", self.content_type)
        writer.write_datetime_value("DateCreated", self.date_created)
        writer.write_str_value("Guid", self.guid)
        writer.write_bool_value("IsDirectory", self.is_directory)
        writer.write_datetime_value("LastChanged", self.last_changed)
        writer.write_int_value("Length", self.length)
        writer.write_str_value("ObjectName", self.object_name)
        writer.write_str_value("Path", self.path)
        writer.write_str_value("ReplicatedZones", self.replicated_zones)
        writer.write_int_value("ServerId", self.server_id)
        writer.write_int_value("StorageZoneId", self.storage_zone_id)
        writer.write_str_value("StorageZoneName", self.storage_zone_name)
        writer.write_str_value("UserId", self.user_id)
        writer.write_additional_data_value(self.additional_data)
    

