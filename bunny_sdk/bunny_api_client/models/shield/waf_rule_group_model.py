from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .waf_rule_model import WafRuleModel

@dataclass
class WafRuleGroupModel(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The code property
    code: Optional[str] = None
    # The description property
    description: Optional[str] = None
    # The fileName property
    file_name: Optional[str] = None
    # The id property
    id: Optional[int] = None
    # The mainGroup property
    main_group: Optional[str] = None
    # The name property
    name: Optional[str] = None
    # The rules property
    rules: Optional[List[WafRuleModel]] = None
    # The ruleset property
    ruleset: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WafRuleGroupModel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WafRuleGroupModel
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WafRuleGroupModel()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .waf_rule_model import WafRuleModel

        from .waf_rule_model import WafRuleModel

        fields: Dict[str, Callable[[Any], None]] = {
            "code": lambda n : setattr(self, 'code', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "mainGroup": lambda n : setattr(self, 'main_group', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "rules": lambda n : setattr(self, 'rules', n.get_collection_of_object_values(WafRuleModel)),
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
        writer.write_str_value("code", self.code)
        writer.write_str_value("description", self.description)
        writer.write_str_value("fileName", self.file_name)
        writer.write_int_value("id", self.id)
        writer.write_str_value("mainGroup", self.main_group)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("rules", self.rules)
        writer.write_str_value("ruleset", self.ruleset)
        writer.write_additional_data_value(self.additional_data)
    

