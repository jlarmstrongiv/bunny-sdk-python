from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .update_dns_record.dns_record import DnsRecord

@dataclass
class DnsZone(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The CustomNameserversEnabled property
    custom_nameservers_enabled: Optional[bool] = None
    # The DateCreated property
    date_created: Optional[datetime.datetime] = None
    # The DateModified property
    date_modified: Optional[datetime.datetime] = None
    # The Domain property
    domain: Optional[str] = None
    # The Id property
    id: Optional[int] = None
    # The LogAnonymizationType property
    log_anonymization_type: Optional[float] = None
    # The LoggingEnabled property
    logging_enabled: Optional[bool] = None
    # Determines if the log anonymization should be enabled
    logging_i_p_anonymization_enabled: Optional[bool] = None
    # The Nameserver1 property
    nameserver1: Optional[str] = None
    # The Nameserver2 property
    nameserver2: Optional[str] = None
    # The NameserversDetected property
    nameservers_detected: Optional[bool] = None
    # The NameserversNextCheck property
    nameservers_next_check: Optional[datetime.datetime] = None
    # The Records property
    records: Optional[List[DnsRecord]] = None
    # The SoaEmail property
    soa_email: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DnsZone:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DnsZone
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DnsZone()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .update_dns_record.dns_record import DnsRecord

        from .update_dns_record.dns_record import DnsRecord

        fields: Dict[str, Callable[[Any], None]] = {
            "CustomNameserversEnabled": lambda n : setattr(self, 'custom_nameservers_enabled', n.get_bool_value()),
            "DateCreated": lambda n : setattr(self, 'date_created', n.get_datetime_value()),
            "DateModified": lambda n : setattr(self, 'date_modified', n.get_datetime_value()),
            "Domain": lambda n : setattr(self, 'domain', n.get_str_value()),
            "Id": lambda n : setattr(self, 'id', n.get_int_value()),
            "LogAnonymizationType": lambda n : setattr(self, 'log_anonymization_type', n.get_float_value()),
            "LoggingEnabled": lambda n : setattr(self, 'logging_enabled', n.get_bool_value()),
            "LoggingIPAnonymizationEnabled": lambda n : setattr(self, 'logging_i_p_anonymization_enabled', n.get_bool_value()),
            "Nameserver1": lambda n : setattr(self, 'nameserver1', n.get_str_value()),
            "Nameserver2": lambda n : setattr(self, 'nameserver2', n.get_str_value()),
            "NameserversDetected": lambda n : setattr(self, 'nameservers_detected', n.get_bool_value()),
            "NameserversNextCheck": lambda n : setattr(self, 'nameservers_next_check', n.get_datetime_value()),
            "Records": lambda n : setattr(self, 'records', n.get_collection_of_object_values(DnsRecord)),
            "SoaEmail": lambda n : setattr(self, 'soa_email', n.get_str_value()),
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
        writer.write_bool_value("CustomNameserversEnabled", self.custom_nameservers_enabled)
        writer.write_float_value("LogAnonymizationType", self.log_anonymization_type)
        writer.write_bool_value("LoggingEnabled", self.logging_enabled)
        writer.write_bool_value("LoggingIPAnonymizationEnabled", self.logging_i_p_anonymization_enabled)
        writer.write_str_value("Nameserver1", self.nameserver1)
        writer.write_str_value("Nameserver2", self.nameserver2)
        writer.write_str_value("SoaEmail", self.soa_email)
        writer.write_additional_data_value(self.additional_data)
    

