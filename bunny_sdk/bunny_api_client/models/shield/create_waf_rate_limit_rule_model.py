from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .create_waf_rate_limit_rule_model_variable_types import CreateWafRateLimitRuleModel_variableTypes

@dataclass
class CreateWafRateLimitRuleModel(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The blockTime property
    block_time: Optional[float] = None
    # The operatorType property
    operator_type: Optional[float] = None
    # The requestCount property
    request_count: Optional[int] = None
    # The severityType property
    severity_type: Optional[float] = None
    # The timeframe property
    timeframe: Optional[float] = None
    # The transformationTypes property
    transformation_types: Optional[List[float]] = None
    # The value property
    value: Optional[str] = None
    # The variableTypes property
    variable_types: Optional[CreateWafRateLimitRuleModel_variableTypes] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CreateWafRateLimitRuleModel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreateWafRateLimitRuleModel
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CreateWafRateLimitRuleModel()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .create_waf_rate_limit_rule_model_variable_types import CreateWafRateLimitRuleModel_variableTypes

        from .create_waf_rate_limit_rule_model_variable_types import CreateWafRateLimitRuleModel_variableTypes

        fields: Dict[str, Callable[[Any], None]] = {
            "blockTime": lambda n : setattr(self, 'block_time', n.get_float_value()),
            "operatorType": lambda n : setattr(self, 'operator_type', n.get_float_value()),
            "requestCount": lambda n : setattr(self, 'request_count', n.get_int_value()),
            "severityType": lambda n : setattr(self, 'severity_type', n.get_float_value()),
            "timeframe": lambda n : setattr(self, 'timeframe', n.get_float_value()),
            "transformationTypes": lambda n : setattr(self, 'transformation_types', n.get_collection_of_primitive_values(float)),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
            "variableTypes": lambda n : setattr(self, 'variable_types', n.get_object_value(CreateWafRateLimitRuleModel_variableTypes)),
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
        writer.write_float_value("blockTime", self.block_time)
        writer.write_float_value("operatorType", self.operator_type)
        writer.write_int_value("requestCount", self.request_count)
        writer.write_float_value("severityType", self.severity_type)
        writer.write_float_value("timeframe", self.timeframe)
        writer.write_collection_of_primitive_values("transformationTypes", self.transformation_types)
        writer.write_str_value("value", self.value)
        writer.write_object_value("variableTypes", self.variable_types)
        writer.write_additional_data_value(self.additional_data)
    

