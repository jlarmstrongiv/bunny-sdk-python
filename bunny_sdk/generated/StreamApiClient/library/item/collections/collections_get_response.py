from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.manage_collections.collection import Collection

@dataclass
class CollectionsGetResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The currentPage property
    current_page: Optional[int] = None
    # The items property
    items: Optional[List[Collection]] = None
    # The itemsPerPage property
    items_per_page: Optional[int] = None
    # The totalItems property
    total_items: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CollectionsGetResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CollectionsGetResponse
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CollectionsGetResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ....models.manage_collections.collection import Collection

        from ....models.manage_collections.collection import Collection

        fields: Dict[str, Callable[[Any], None]] = {
            "currentPage": lambda n : setattr(self, 'current_page', n.get_int_value()),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(Collection)),
            "itemsPerPage": lambda n : setattr(self, 'items_per_page', n.get_int_value()),
            "totalItems": lambda n : setattr(self, 'total_items', n.get_int_value()),
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
        writer.write_int_value("currentPage", self.current_page)
        writer.write_collection_of_object_values("items", self.items)
        writer.write_int_value("itemsPerPage", self.items_per_page)
        writer.write_int_value("totalItems", self.total_items)
        writer.write_additional_data_value(self.additional_data)
    

