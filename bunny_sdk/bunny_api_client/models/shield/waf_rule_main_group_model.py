from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .waf_rule_group_model import WafRuleGroupModel

@dataclass
class WafRuleMainGroupModel(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The name property
    name: Optional[str] = None
    # The ruleGroups property
    rule_groups: Optional[List[WafRuleGroupModel]] = None
    # The ruleset property
    ruleset: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WafRuleMainGroupModel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WafRuleMainGroupModel
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WafRuleMainGroupModel()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .waf_rule_group_model import WafRuleGroupModel

        from .waf_rule_group_model import WafRuleGroupModel

        fields: Dict[str, Callable[[Any], None]] = {
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "ruleGroups": lambda n : setattr(self, 'rule_groups', n.get_collection_of_object_values(WafRuleGroupModel)),
            "ruleset": lambda n : setattr(self, 'ruleset', n.get_str_value()),
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
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("ruleGroups", self.rule_groups)
        writer.write_str_value("ruleset", self.ruleset)
        writer.write_additional_data_value(self.additional_data)
    

