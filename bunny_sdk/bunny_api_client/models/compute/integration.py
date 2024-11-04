from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .integration_deploy_configuration import Integration_DeployConfiguration
    from .integration_repository_settings import Integration_RepositorySettings

@dataclass
class Integration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The DeployConfiguration property
    deploy_configuration: Optional[Integration_DeployConfiguration] = None
    # The IntegrationId property
    integration_id: Optional[int] = None
    # The RepositorySettings property
    repository_settings: Optional[Integration_RepositorySettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Integration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Integration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Integration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .integration_deploy_configuration import Integration_DeployConfiguration
        from .integration_repository_settings import Integration_RepositorySettings

        from .integration_deploy_configuration import Integration_DeployConfiguration
        from .integration_repository_settings import Integration_RepositorySettings

        fields: Dict[str, Callable[[Any], None]] = {
            "DeployConfiguration": lambda n : setattr(self, 'deploy_configuration', n.get_object_value(Integration_DeployConfiguration)),
            "IntegrationId": lambda n : setattr(self, 'integration_id', n.get_int_value()),
            "RepositorySettings": lambda n : setattr(self, 'repository_settings', n.get_object_value(Integration_RepositorySettings)),
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
        writer.write_int_value("IntegrationId", self.integration_id)
        writer.write_object_value("RepositorySettings", self.repository_settings)
        writer.write_additional_data_value(self.additional_data)
    

