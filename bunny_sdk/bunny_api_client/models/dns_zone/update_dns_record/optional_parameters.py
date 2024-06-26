from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .optional_parameters_enviromental_variables import OptionalParameters_EnviromentalVariables

@dataclass
class OptionalParameters(AdditionalDataHolder, Parsable):
    """
    The template for adding optional properties.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The Accelerated property
    accelerated: Optional[bool] = None
    # The Comment property
    comment: Optional[str] = None
    # The Disabled property
    disabled: Optional[bool] = None
    # The EnviromentalVariables property
    enviromental_variables: Optional[List[OptionalParameters_EnviromentalVariables]] = None
    # The Flags property
    flags: Optional[int] = None
    # The GeolocationLatitude property
    geolocation_latitude: Optional[float] = None
    # The GeolocationLongitude property
    geolocation_longitude: Optional[float] = None
    # The LatencyZone property
    latency_zone: Optional[str] = None
    # The MonitorType property
    monitor_type: Optional[float] = None
    # The Port property
    port: Optional[int] = None
    # The Priority property
    priority: Optional[int] = None
    # The PullZoneId property
    pull_zone_id: Optional[int] = None
    # The ScriptId property
    script_id: Optional[int] = None
    # The SmartRoutingType property
    smart_routing_type: Optional[float] = None
    # The Tag property
    tag: Optional[str] = None
    # The Ttl property
    ttl: Optional[float] = None
    # The Weight property
    weight: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OptionalParameters:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OptionalParameters
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return OptionalParameters()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .optional_parameters_enviromental_variables import OptionalParameters_EnviromentalVariables

        from .optional_parameters_enviromental_variables import OptionalParameters_EnviromentalVariables

        fields: Dict[str, Callable[[Any], None]] = {
            "Accelerated": lambda n : setattr(self, 'accelerated', n.get_bool_value()),
            "Comment": lambda n : setattr(self, 'comment', n.get_str_value()),
            "Disabled": lambda n : setattr(self, 'disabled', n.get_bool_value()),
            "EnviromentalVariables": lambda n : setattr(self, 'enviromental_variables', n.get_collection_of_object_values(OptionalParameters_EnviromentalVariables)),
            "Flags": lambda n : setattr(self, 'flags', n.get_int_value()),
            "GeolocationLatitude": lambda n : setattr(self, 'geolocation_latitude', n.get_float_value()),
            "GeolocationLongitude": lambda n : setattr(self, 'geolocation_longitude', n.get_float_value()),
            "LatencyZone": lambda n : setattr(self, 'latency_zone', n.get_str_value()),
            "MonitorType": lambda n : setattr(self, 'monitor_type', n.get_float_value()),
            "Port": lambda n : setattr(self, 'port', n.get_int_value()),
            "Priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "PullZoneId": lambda n : setattr(self, 'pull_zone_id', n.get_int_value()),
            "ScriptId": lambda n : setattr(self, 'script_id', n.get_int_value()),
            "SmartRoutingType": lambda n : setattr(self, 'smart_routing_type', n.get_float_value()),
            "Tag": lambda n : setattr(self, 'tag', n.get_str_value()),
            "Ttl": lambda n : setattr(self, 'ttl', n.get_float_value()),
            "Weight": lambda n : setattr(self, 'weight', n.get_int_value()),
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
        writer.write_bool_value("Accelerated", self.accelerated)
        writer.write_str_value("Comment", self.comment)
        writer.write_bool_value("Disabled", self.disabled)
        writer.write_collection_of_object_values("EnviromentalVariables", self.enviromental_variables)
        writer.write_int_value("Flags", self.flags)
        writer.write_float_value("GeolocationLatitude", self.geolocation_latitude)
        writer.write_float_value("GeolocationLongitude", self.geolocation_longitude)
        writer.write_str_value("LatencyZone", self.latency_zone)
        writer.write_float_value("MonitorType", self.monitor_type)
        writer.write_int_value("Port", self.port)
        writer.write_int_value("Priority", self.priority)
        writer.write_int_value("PullZoneId", self.pull_zone_id)
        writer.write_int_value("ScriptId", self.script_id)
        writer.write_float_value("SmartRoutingType", self.smart_routing_type)
        writer.write_str_value("Tag", self.tag)
        writer.write_float_value("Ttl", self.ttl)
        writer.write_int_value("Weight", self.weight)
        writer.write_additional_data_value(self.additional_data)
    

