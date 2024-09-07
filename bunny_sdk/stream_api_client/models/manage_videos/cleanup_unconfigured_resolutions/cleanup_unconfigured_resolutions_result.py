from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cleanup_unconfigured_resolutions_result_data import CleanupUnconfiguredResolutionsResult_data

@dataclass
class CleanupUnconfiguredResolutionsResult(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The resolutions were successfully deleted
    data: Optional[CleanupUnconfiguredResolutionsResult_data] = None
    # Response message description
    message: Optional[str] = None
    # The response status code
    status_code: Optional[int] = None
    # Determines if the request was successful
    success: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CleanupUnconfiguredResolutionsResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CleanupUnconfiguredResolutionsResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CleanupUnconfiguredResolutionsResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .cleanup_unconfigured_resolutions_result_data import CleanupUnconfiguredResolutionsResult_data

        from .cleanup_unconfigured_resolutions_result_data import CleanupUnconfiguredResolutionsResult_data

        fields: Dict[str, Callable[[Any], None]] = {
            "data": lambda n : setattr(self, 'data', n.get_object_value(CleanupUnconfiguredResolutionsResult_data)),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "statusCode": lambda n : setattr(self, 'status_code', n.get_int_value()),
            "success": lambda n : setattr(self, 'success', n.get_bool_value()),
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
        writer.write_object_value("data", self.data)
        writer.write_str_value("message", self.message)
        writer.write_int_value("statusCode", self.status_code)
        writer.write_bool_value("success", self.success)
        writer.write_additional_data_value(self.additional_data)
    

