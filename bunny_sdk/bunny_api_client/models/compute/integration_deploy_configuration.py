from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class Integration_DeployConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The Branch property
    branch: Optional[str] = None
    # The BuildCommand property
    build_command: Optional[str] = None
    # The CreateWorkflow property
    create_workflow: Optional[bool] = None
    # The EntryFile property
    entry_file: Optional[str] = None
    # The InstallCommand property
    install_command: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Integration_DeployConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Integration_DeployConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Integration_DeployConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "Branch": lambda n : setattr(self, 'branch', n.get_str_value()),
            "BuildCommand": lambda n : setattr(self, 'build_command', n.get_str_value()),
            "CreateWorkflow": lambda n : setattr(self, 'create_workflow', n.get_bool_value()),
            "EntryFile": lambda n : setattr(self, 'entry_file', n.get_str_value()),
            "InstallCommand": lambda n : setattr(self, 'install_command', n.get_str_value()),
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
        writer.write_str_value("Branch", self.branch)
        writer.write_str_value("BuildCommand", self.build_command)
        writer.write_bool_value("CreateWorkflow", self.create_workflow)
        writer.write_str_value("EntryFile", self.entry_file)
        writer.write_str_value("InstallCommand", self.install_command)
        writer.write_additional_data_value(self.additional_data)
    

