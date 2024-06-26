from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .fetch_post_request_body_headers import FetchPostRequestBody_headers

@dataclass
class FetchPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The headers that will be sent along with the fetch request.
    headers: Optional[FetchPostRequestBody_headers] = None
    # The title that will be set to video.
    title: Optional[str] = None
    # The URL from which the video will be fetched from.
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FetchPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FetchPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return FetchPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .fetch_post_request_body_headers import FetchPostRequestBody_headers

        from .fetch_post_request_body_headers import FetchPostRequestBody_headers

        fields: Dict[str, Callable[[Any], None]] = {
            "headers": lambda n : setattr(self, 'headers', n.get_object_value(FetchPostRequestBody_headers)),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
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
        writer.write_object_value("headers", self.headers)
        writer.write_str_value("title", self.title)
        writer.write_str_value("url", self.url)
        writer.write_additional_data_value(self.additional_data)
    

