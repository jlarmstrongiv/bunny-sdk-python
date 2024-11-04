from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .create_custom_waf_rule_model import CreateCustomWafRuleModel

@dataclass
class CustomWafRule(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The id property
    id: Optional[int] = None
    # The ruleConfiguration property
    rule_configuration: Optional[CreateCustomWafRuleModel] = None
    # The ruleDescription property
    rule_description: Optional[str] = None
    # The ruleJson property
    rule_json: Optional[str] = None
    # The ruleName property
    rule_name: Optional[str] = None
    # The shieldZoneId property
    shield_zone_id: Optional[int] = None
    # The userId property
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomWafRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomWafRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomWafRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .create_custom_waf_rule_model import CreateCustomWafRuleModel

        from .create_custom_waf_rule_model import CreateCustomWafRuleModel

        fields: Dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "ruleConfiguration": lambda n : setattr(self, 'rule_configuration', n.get_object_value(CreateCustomWafRuleModel)),
            "ruleDescription": lambda n : setattr(self, 'rule_description', n.get_str_value()),
            "ruleJson": lambda n : setattr(self, 'rule_json', n.get_str_value()),
            "ruleName": lambda n : setattr(self, 'rule_name', n.get_str_value()),
            "shieldZoneId": lambda n : setattr(self, 'shield_zone_id', n.get_int_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_int_value("id", self.id)
        writer.write_object_value("ruleConfiguration", self.rule_configuration)
        writer.write_str_value("ruleDescription", self.rule_description)
        writer.write_str_value("ruleJson", self.rule_json)
        writer.write_str_value("ruleName", self.rule_name)
        writer.write_int_value("shieldZoneId", self.shield_zone_id)
        writer.write_str_value("userId", self.user_id)
        writer.write_additional_data_value(self.additional_data)
    

