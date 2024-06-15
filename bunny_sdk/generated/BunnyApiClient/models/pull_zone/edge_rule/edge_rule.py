from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .action import Action
    from .trigger import Trigger

@dataclass
class EdgeRule(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The Action parameter 1. The value depends on other parameters of the edge rule.
    action_parameter1: Optional[str] = None
    # The Action parameter 2. The value depends on other parameters of the edge rule.
    action_parameter2: Optional[str] = None
    # The ActionType property
    action_type: Optional[float] = None
    # The description of the edge rule
    description: Optional[str] = None
    # Determines if the edge rule is currently enabled or not
    enabled: Optional[bool] = None
    # The ExtraActions property
    extra_actions: Optional[List[Action]] = None
    # The unique GUID of the edge rule
    guid: Optional[str] = None
    # The TriggerMatchingType property
    trigger_matching_type: Optional[float] = None
    # The Triggers property
    triggers: Optional[List[Trigger]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EdgeRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EdgeRule
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EdgeRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .action import Action
        from .trigger import Trigger

        from .action import Action
        from .trigger import Trigger

        fields: Dict[str, Callable[[Any], None]] = {
            "ActionParameter1": lambda n : setattr(self, 'action_parameter1', n.get_str_value()),
            "ActionParameter2": lambda n : setattr(self, 'action_parameter2', n.get_str_value()),
            "ActionType": lambda n : setattr(self, 'action_type', n.get_float_value()),
            "Description": lambda n : setattr(self, 'description', n.get_str_value()),
            "Enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "ExtraActions": lambda n : setattr(self, 'extra_actions', n.get_collection_of_object_values(Action)),
            "Guid": lambda n : setattr(self, 'guid', n.get_str_value()),
            "TriggerMatchingType": lambda n : setattr(self, 'trigger_matching_type', n.get_float_value()),
            "Triggers": lambda n : setattr(self, 'triggers', n.get_collection_of_object_values(Trigger)),
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
        writer.write_str_value("ActionParameter1", self.action_parameter1)
        writer.write_str_value("ActionParameter2", self.action_parameter2)
        writer.write_float_value("ActionType", self.action_type)
        writer.write_str_value("Description", self.description)
        writer.write_bool_value("Enabled", self.enabled)
        writer.write_collection_of_object_values("ExtraActions", self.extra_actions)
        writer.write_str_value("Guid", self.guid)
        writer.write_float_value("TriggerMatchingType", self.trigger_matching_type)
        writer.write_collection_of_object_values("Triggers", self.triggers)
        writer.write_additional_data_value(self.additional_data)
    

