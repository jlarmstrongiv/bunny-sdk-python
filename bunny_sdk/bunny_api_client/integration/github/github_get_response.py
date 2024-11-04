from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models.integrations.account import Account

@dataclass
class GithubGetResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The Accounts property
    accounts: Optional[List[Account]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GithubGetResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GithubGetResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GithubGetResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ...models.integrations.account import Account

        from ...models.integrations.account import Account

        fields: Dict[str, Callable[[Any], None]] = {
            "Accounts": lambda n : setattr(self, 'accounts', n.get_collection_of_object_values(Account)),
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
        writer.write_collection_of_object_values("Accounts", self.accounts)
        writer.write_additional_data_value(self.additional_data)
    

