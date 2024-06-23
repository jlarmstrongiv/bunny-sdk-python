from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class ScriptRelease(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The Author property
    author: Optional[str] = None
    # The AuthorEmail property
    author_email: Optional[str] = None
    # The Code property
    code: Optional[str] = None
    # The DatePublished property
    date_published: Optional[datetime.datetime] = None
    # The DateReleased property
    date_released: Optional[datetime.datetime] = None
    # The Deleted property
    deleted: Optional[bool] = None
    # The Id property
    id: Optional[int] = None
    # The Note property
    note: Optional[str] = None
    # The Status property
    status: Optional[float] = None
    # The Uuid property
    uuid: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ScriptRelease:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ScriptRelease
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ScriptRelease()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "Author": lambda n : setattr(self, 'author', n.get_str_value()),
            "AuthorEmail": lambda n : setattr(self, 'author_email', n.get_str_value()),
            "Code": lambda n : setattr(self, 'code', n.get_str_value()),
            "DatePublished": lambda n : setattr(self, 'date_published', n.get_datetime_value()),
            "DateReleased": lambda n : setattr(self, 'date_released', n.get_datetime_value()),
            "Deleted": lambda n : setattr(self, 'deleted', n.get_bool_value()),
            "Id": lambda n : setattr(self, 'id', n.get_int_value()),
            "Note": lambda n : setattr(self, 'note', n.get_str_value()),
            "Status": lambda n : setattr(self, 'status', n.get_float_value()),
            "Uuid": lambda n : setattr(self, 'uuid', n.get_str_value()),
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
        writer.write_str_value("Author", self.author)
        writer.write_str_value("AuthorEmail", self.author_email)
        writer.write_str_value("Code", self.code)
        writer.write_datetime_value("DatePublished", self.date_published)
        writer.write_datetime_value("DateReleased", self.date_released)
        writer.write_bool_value("Deleted", self.deleted)
        writer.write_int_value("Id", self.id)
        writer.write_str_value("Note", self.note)
        writer.write_float_value("Status", self.status)
        writer.write_str_value("Uuid", self.uuid)
        writer.write_additional_data_value(self.additional_data)
    

