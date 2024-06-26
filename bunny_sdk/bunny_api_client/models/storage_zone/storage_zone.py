from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..pull_zone.pull_zone import PullZone
    from .edge_replication_regions import EdgeReplicationRegions
    from .standard_regions import StandardRegions

@dataclass
class StorageZone(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The Custom404FilePath property
    custom404_file_path: Optional[str] = None
    # The DateModified property
    date_modified: Optional[datetime.datetime] = None
    # The Deleted property
    deleted: Optional[bool] = None
    # The Discount property
    discount: Optional[int] = None
    # The FilesStored property
    files_stored: Optional[int] = None
    # The Id property
    id: Optional[int] = None
    # The Name property
    name: Optional[str] = None
    # The Password property
    password: Optional[str] = None
    # The PriceOverride property
    price_override: Optional[float] = None
    # The PullZones property
    pull_zones: Optional[List[PullZone]] = None
    # The ReadOnlyPassword property
    read_only_password: Optional[str] = None
    # The Region property
    region: Optional[StandardRegions] = None
    # The ReplicationChangeInProgress property
    replication_change_in_progress: Optional[bool] = None
    # The ReplicationRegions property
    replication_regions: Optional[List[EdgeReplicationRegions]] = None
    # The Rewrite404To200 property
    rewrite404_to200: Optional[bool] = None
    # The StorageHostname property
    storage_hostname: Optional[str] = None
    # The StorageUsed property
    storage_used: Optional[int] = None
    # The UserId property
    user_id: Optional[str] = None
    # The ZoneTier property
    zone_tier: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StorageZone:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StorageZone
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return StorageZone()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..pull_zone.pull_zone import PullZone
        from .edge_replication_regions import EdgeReplicationRegions
        from .standard_regions import StandardRegions

        from ..pull_zone.pull_zone import PullZone
        from .edge_replication_regions import EdgeReplicationRegions
        from .standard_regions import StandardRegions

        fields: Dict[str, Callable[[Any], None]] = {
            "Custom404FilePath": lambda n : setattr(self, 'custom404_file_path', n.get_str_value()),
            "DateModified": lambda n : setattr(self, 'date_modified', n.get_datetime_value()),
            "Deleted": lambda n : setattr(self, 'deleted', n.get_bool_value()),
            "Discount": lambda n : setattr(self, 'discount', n.get_int_value()),
            "FilesStored": lambda n : setattr(self, 'files_stored', n.get_int_value()),
            "Id": lambda n : setattr(self, 'id', n.get_int_value()),
            "Name": lambda n : setattr(self, 'name', n.get_str_value()),
            "Password": lambda n : setattr(self, 'password', n.get_str_value()),
            "PriceOverride": lambda n : setattr(self, 'price_override', n.get_float_value()),
            "PullZones": lambda n : setattr(self, 'pull_zones', n.get_collection_of_object_values(PullZone)),
            "ReadOnlyPassword": lambda n : setattr(self, 'read_only_password', n.get_str_value()),
            "Region": lambda n : setattr(self, 'region', n.get_enum_value(StandardRegions)),
            "ReplicationChangeInProgress": lambda n : setattr(self, 'replication_change_in_progress', n.get_bool_value()),
            "ReplicationRegions": lambda n : setattr(self, 'replication_regions', n.get_collection_of_enum_values(EdgeReplicationRegions)),
            "Rewrite404To200": lambda n : setattr(self, 'rewrite404_to200', n.get_bool_value()),
            "StorageHostname": lambda n : setattr(self, 'storage_hostname', n.get_str_value()),
            "StorageUsed": lambda n : setattr(self, 'storage_used', n.get_int_value()),
            "UserId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "ZoneTier": lambda n : setattr(self, 'zone_tier', n.get_float_value()),
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
        writer.write_str_value("Custom404FilePath", self.custom404_file_path)
        writer.write_str_value("Name", self.name)
        writer.write_enum_value("Region", self.region)
        writer.write_collection_of_enum_values("ReplicationRegions", self.replication_regions)
        writer.write_bool_value("Rewrite404To200", self.rewrite404_to200)
        writer.write_float_value("ZoneTier", self.zone_tier)
        writer.write_additional_data_value(self.additional_data)
    

