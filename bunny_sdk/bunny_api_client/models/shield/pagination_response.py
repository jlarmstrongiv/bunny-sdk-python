from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class PaginationResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The currentPage property
    current_page: Optional[int] = None
    # The nextPage property
    next_page: Optional[int] = None
    # The pageSize property
    page_size: Optional[int] = None
    # The totalCount property
    total_count: Optional[int] = None
    # The totalPages property
    total_pages: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PaginationResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PaginationResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PaginationResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "currentPage": lambda n : setattr(self, 'current_page', n.get_int_value()),
            "nextPage": lambda n : setattr(self, 'next_page', n.get_int_value()),
            "pageSize": lambda n : setattr(self, 'page_size', n.get_int_value()),
            "totalCount": lambda n : setattr(self, 'total_count', n.get_int_value()),
            "totalPages": lambda n : setattr(self, 'total_pages', n.get_int_value()),
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
        writer.write_int_value("currentPage", self.current_page)
        writer.write_int_value("nextPage", self.next_page)
        writer.write_int_value("pageSize", self.page_size)
        writer.write_int_value("totalCount", self.total_count)
        writer.write_int_value("totalPages", self.total_pages)
        writer.write_additional_data_value(self.additional_data)
    

