from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class Connection(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The ConnectionType property
    connection_type: Optional[float] = None
    # The main custom connected CDN domain
    main_custom_domain: Optional[str] = None
    # The total amount of bandwidth served by this zone this month
    monthly_bandwidth_used: Optional[float] = None
    # The total monthly charges incurred by this zone
    monthly_charges: Optional[float] = None
    # The ID of the connected pull zone
    pull_zone_id: Optional[int] = None
    # The name of the connected pull zone
    pull_zone_name: Optional[str] = None
    # The Tier property
    tier: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Connection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Connection
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Connection()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "ConnectionType": lambda n : setattr(self, 'connection_type', n.get_float_value()),
            "MainCustomDomain": lambda n : setattr(self, 'main_custom_domain', n.get_str_value()),
            "MonthlyBandwidthUsed": lambda n : setattr(self, 'monthly_bandwidth_used', n.get_float_value()),
            "MonthlyCharges": lambda n : setattr(self, 'monthly_charges', n.get_float_value()),
            "PullZoneId": lambda n : setattr(self, 'pull_zone_id', n.get_int_value()),
            "PullZoneName": lambda n : setattr(self, 'pull_zone_name', n.get_str_value()),
            "Tier": lambda n : setattr(self, 'tier', n.get_float_value()),
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
        writer.write_float_value("ConnectionType", self.connection_type)
        writer.write_str_value("MainCustomDomain", self.main_custom_domain)
        writer.write_float_value("MonthlyBandwidthUsed", self.monthly_bandwidth_used)
        writer.write_float_value("MonthlyCharges", self.monthly_charges)
        writer.write_int_value("PullZoneId", self.pull_zone_id)
        writer.write_str_value("PullZoneName", self.pull_zone_name)
        writer.write_float_value("Tier", self.tier)
        writer.write_additional_data_value(self.additional_data)
    

