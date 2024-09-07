from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .global_search_type import GlobalSearchType

@dataclass
class SearchResult(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The ID of the search result item linked object
    id: Optional[int] = None
    # The name of the object found
    name: Optional[str] = None
    # The type of the search result item. Possible values: cdn, storage, dns, script, stream
    type: Optional[GlobalSearchType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SearchResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SearchResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SearchResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .global_search_type import GlobalSearchType

        from .global_search_type import GlobalSearchType

        fields: Dict[str, Callable[[Any], None]] = {
            "Id": lambda n : setattr(self, 'id', n.get_int_value()),
            "Name": lambda n : setattr(self, 'name', n.get_str_value()),
            "Type": lambda n : setattr(self, 'type', n.get_enum_value(GlobalSearchType)),
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
        writer.write_int_value("Id", self.id)
        writer.write_str_value("Name", self.name)
        writer.write_enum_value("Type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

