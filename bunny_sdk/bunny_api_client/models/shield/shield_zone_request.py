from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .pull_zone_waf_config_variable_model import PullZoneWafConfigVariableModel

@dataclass
class ShieldZoneRequest(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The dDoSChallengeWindow property
    d_do_s_challenge_window: Optional[int] = None
    # The dDoSShieldSensitivity property
    d_do_s_shield_sensitivity: Optional[float] = None
    # The learningMode property
    learning_mode: Optional[bool] = None
    # The premiumPlan property
    premium_plan: Optional[bool] = None
    # The shieldZoneId property
    shield_zone_id: Optional[int] = None
    # The wafDisabledRuleGroups property
    waf_disabled_rule_groups: Optional[List[str]] = None
    # The wafDisabledRules property
    waf_disabled_rules: Optional[List[str]] = None
    # The wafEnabled property
    waf_enabled: Optional[bool] = None
    # The wafEngineConfig property
    waf_engine_config: Optional[List[PullZoneWafConfigVariableModel]] = None
    # The wafExecutionMode property
    waf_execution_mode: Optional[float] = None
    # The wafLogOnlyRules property
    waf_log_only_rules: Optional[List[str]] = None
    # The wafProfileId property
    waf_profile_id: Optional[int] = None
    # The wafRequestHeaderLoggingEnabled property
    waf_request_header_logging_enabled: Optional[bool] = None
    # The wafRequestIgnoredHeaders property
    waf_request_ignored_headers: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ShieldZoneRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ShieldZoneRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ShieldZoneRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .pull_zone_waf_config_variable_model import PullZoneWafConfigVariableModel

        from .pull_zone_waf_config_variable_model import PullZoneWafConfigVariableModel

        fields: Dict[str, Callable[[Any], None]] = {
            "dDoSChallengeWindow": lambda n : setattr(self, 'd_do_s_challenge_window', n.get_int_value()),
            "dDoSShieldSensitivity": lambda n : setattr(self, 'd_do_s_shield_sensitivity', n.get_float_value()),
            "learningMode": lambda n : setattr(self, 'learning_mode', n.get_bool_value()),
            "premiumPlan": lambda n : setattr(self, 'premium_plan', n.get_bool_value()),
            "shieldZoneId": lambda n : setattr(self, 'shield_zone_id', n.get_int_value()),
            "wafDisabledRuleGroups": lambda n : setattr(self, 'waf_disabled_rule_groups', n.get_collection_of_primitive_values(str)),
            "wafDisabledRules": lambda n : setattr(self, 'waf_disabled_rules', n.get_collection_of_primitive_values(str)),
            "wafEnabled": lambda n : setattr(self, 'waf_enabled', n.get_bool_value()),
            "wafEngineConfig": lambda n : setattr(self, 'waf_engine_config', n.get_collection_of_object_values(PullZoneWafConfigVariableModel)),
            "wafExecutionMode": lambda n : setattr(self, 'waf_execution_mode', n.get_float_value()),
            "wafLogOnlyRules": lambda n : setattr(self, 'waf_log_only_rules', n.get_collection_of_primitive_values(str)),
            "wafProfileId": lambda n : setattr(self, 'waf_profile_id', n.get_int_value()),
            "wafRequestHeaderLoggingEnabled": lambda n : setattr(self, 'waf_request_header_logging_enabled', n.get_bool_value()),
            "wafRequestIgnoredHeaders": lambda n : setattr(self, 'waf_request_ignored_headers', n.get_collection_of_primitive_values(str)),
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
        writer.write_int_value("dDoSChallengeWindow", self.d_do_s_challenge_window)
        writer.write_float_value("dDoSShieldSensitivity", self.d_do_s_shield_sensitivity)
        writer.write_bool_value("learningMode", self.learning_mode)
        writer.write_bool_value("premiumPlan", self.premium_plan)
        writer.write_int_value("shieldZoneId", self.shield_zone_id)
        writer.write_collection_of_primitive_values("wafDisabledRuleGroups", self.waf_disabled_rule_groups)
        writer.write_collection_of_primitive_values("wafDisabledRules", self.waf_disabled_rules)
        writer.write_bool_value("wafEnabled", self.waf_enabled)
        writer.write_collection_of_object_values("wafEngineConfig", self.waf_engine_config)
        writer.write_float_value("wafExecutionMode", self.waf_execution_mode)
        writer.write_collection_of_primitive_values("wafLogOnlyRules", self.waf_log_only_rules)
        writer.write_int_value("wafProfileId", self.waf_profile_id)
        writer.write_bool_value("wafRequestHeaderLoggingEnabled", self.waf_request_header_logging_enabled)
        writer.write_collection_of_primitive_values("wafRequestIgnoredHeaders", self.waf_request_ignored_headers)
        writer.write_additional_data_value(self.additional_data)
    

