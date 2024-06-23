from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .url import Url

@dataclass
class AbuseCase(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The ActualUrl property
    actual_url: Optional[str] = None
    # The DateCreated property
    date_created: Optional[datetime.datetime] = None
    # The DateUpdated property
    date_updated: Optional[datetime.datetime] = None
    # The Deadline property
    deadline: Optional[datetime.datetime] = None
    # The Id property
    id: Optional[int] = None
    # The Message property
    message: Optional[str] = None
    # The Path property
    path: Optional[str] = None
    # The PullZoneId property
    pull_zone_id: Optional[int] = None
    # The PullZoneName property
    pull_zone_name: Optional[str] = None
    # The Status property
    status: Optional[float] = None
    # The Urls property
    urls: Optional[List[Url]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AbuseCase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AbuseCase
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AbuseCase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .url import Url

        from .url import Url

        fields: Dict[str, Callable[[Any], None]] = {
            "ActualUrl": lambda n : setattr(self, 'actual_url', n.get_str_value()),
            "DateCreated": lambda n : setattr(self, 'date_created', n.get_datetime_value()),
            "DateUpdated": lambda n : setattr(self, 'date_updated', n.get_datetime_value()),
            "Deadline": lambda n : setattr(self, 'deadline', n.get_datetime_value()),
            "Id": lambda n : setattr(self, 'id', n.get_int_value()),
            "Message": lambda n : setattr(self, 'message', n.get_str_value()),
            "Path": lambda n : setattr(self, 'path', n.get_str_value()),
            "PullZoneId": lambda n : setattr(self, 'pull_zone_id', n.get_int_value()),
            "PullZoneName": lambda n : setattr(self, 'pull_zone_name', n.get_str_value()),
            "Status": lambda n : setattr(self, 'status', n.get_float_value()),
            "Urls": lambda n : setattr(self, 'urls', n.get_collection_of_object_values(Url)),
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
        writer.write_str_value("ActualUrl", self.actual_url)
        writer.write_datetime_value("DateCreated", self.date_created)
        writer.write_datetime_value("DateUpdated", self.date_updated)
        writer.write_datetime_value("Deadline", self.deadline)
        writer.write_int_value("Id", self.id)
        writer.write_str_value("Message", self.message)
        writer.write_str_value("Path", self.path)
        writer.write_int_value("PullZoneId", self.pull_zone_id)
        writer.write_str_value("PullZoneName", self.pull_zone_name)
        writer.write_float_value("Status", self.status)
        writer.write_collection_of_object_values("Urls", self.urls)
        writer.write_additional_data_value(self.additional_data)
    

