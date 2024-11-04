from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .create_custom_waf_rule_model_variable_types import CreateCustomWafRuleModel_variableTypes

@dataclass
class CreateCustomWafRuleModel(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The actionType property
    action_type: Optional[float] = None
    # The operatorType property
    operator_type: Optional[float] = None
    # The severityType property
    severity_type: Optional[float] = None
    # The transformationTypes property
    transformation_types: Optional[List[float]] = None
    # The value property
    value: Optional[str] = None
    # The variableTypes property
    variable_types: Optional[CreateCustomWafRuleModel_variableTypes] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CreateCustomWafRuleModel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreateCustomWafRuleModel
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CreateCustomWafRuleModel()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .create_custom_waf_rule_model_variable_types import CreateCustomWafRuleModel_variableTypes

        from .create_custom_waf_rule_model_variable_types import CreateCustomWafRuleModel_variableTypes

        fields: Dict[str, Callable[[Any], None]] = {
            "actionType": lambda n : setattr(self, 'action_type', n.get_float_value()),
            "operatorType": lambda n : setattr(self, 'operator_type', n.get_float_value()),
            "severityType": lambda n : setattr(self, 'severity_type', n.get_float_value()),
            "transformationTypes": lambda n : setattr(self, 'transformation_types', n.get_collection_of_primitive_values(float)),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
            "variableTypes": lambda n : setattr(self, 'variable_types', n.get_object_value(CreateCustomWafRuleModel_variableTypes)),
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
        writer.write_float_value("actionType", self.action_type)
        writer.write_float_value("operatorType", self.operator_type)
        writer.write_float_value("severityType", self.severity_type)
        writer.write_collection_of_primitive_values("transformationTypes", self.transformation_types)
        writer.write_str_value("value", self.value)
        writer.write_object_value("variableTypes", self.variable_types)
        writer.write_additional_data_value(self.additional_data)
    

