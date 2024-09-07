from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .search_result import SearchResult

@dataclass
class SearchResults(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The number of results skipped in the search query
    from_: Optional[int] = None
    # The input query for the search request
    query: Optional[str] = None
    # The list of search results found for the query
    search_results: Optional[List[SearchResult]] = None
    # The size of the result set
    size: Optional[int] = None
    # The total number of search results found matching the query
    total: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SearchResults:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SearchResults
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SearchResults()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .search_result import SearchResult

        from .search_result import SearchResult

        fields: Dict[str, Callable[[Any], None]] = {
            "From": lambda n : setattr(self, 'from_', n.get_int_value()),
            "Query": lambda n : setattr(self, 'query', n.get_str_value()),
            "SearchResults": lambda n : setattr(self, 'search_results', n.get_collection_of_object_values(SearchResult)),
            "Size": lambda n : setattr(self, 'size', n.get_int_value()),
            "Total": lambda n : setattr(self, 'total', n.get_int_value()),
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
        writer.write_int_value("From", self.from_)
        writer.write_str_value("Query", self.query)
        writer.write_collection_of_object_values("SearchResults", self.search_results)
        writer.write_int_value("Size", self.size)
        writer.write_int_value("Total", self.total)
        writer.write_additional_data_value(self.additional_data)
    

