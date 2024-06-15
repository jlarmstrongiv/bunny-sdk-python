from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .properties_auto_optimize import Properties_auto_optimize
    from .properties_crop_gravity import Properties_crop_gravity
    from .properties_optimizer import Properties_optimizer

@dataclass
class Properties(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The aspect_ratio property
    aspect_ratio: Optional[str] = None
    # The auto_optimize property
    auto_optimize: Optional[Properties_auto_optimize] = None
    # The blur property
    blur: Optional[str] = None
    # The brightness property
    brightness: Optional[str] = None
    # The contrast property
    contrast: Optional[str] = None
    # The crop property
    crop: Optional[str] = None
    # The crop_gravity property
    crop_gravity: Optional[Properties_crop_gravity] = None
    # The flip property
    flip: Optional[str] = None
    # The flop property
    flop: Optional[str] = None
    # The gamma property
    gamma: Optional[str] = None
    # The height property
    height: Optional[str] = None
    # The hue property
    hue: Optional[str] = None
    # The optimizer property
    optimizer: Optional[Properties_optimizer] = None
    # The quality property
    quality: Optional[str] = None
    # The saturation property
    saturation: Optional[str] = None
    # The sharpen property
    sharpen: Optional[str] = None
    # The width property
    width: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Properties:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Properties
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Properties()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .properties_auto_optimize import Properties_auto_optimize
        from .properties_crop_gravity import Properties_crop_gravity
        from .properties_optimizer import Properties_optimizer

        from .properties_auto_optimize import Properties_auto_optimize
        from .properties_crop_gravity import Properties_crop_gravity
        from .properties_optimizer import Properties_optimizer

        fields: Dict[str, Callable[[Any], None]] = {
            "aspect_ratio": lambda n : setattr(self, 'aspect_ratio', n.get_str_value()),
            "auto_optimize": lambda n : setattr(self, 'auto_optimize', n.get_enum_value(Properties_auto_optimize)),
            "blur": lambda n : setattr(self, 'blur', n.get_str_value()),
            "brightness": lambda n : setattr(self, 'brightness', n.get_str_value()),
            "contrast": lambda n : setattr(self, 'contrast', n.get_str_value()),
            "crop": lambda n : setattr(self, 'crop', n.get_str_value()),
            "crop_gravity": lambda n : setattr(self, 'crop_gravity', n.get_enum_value(Properties_crop_gravity)),
            "flip": lambda n : setattr(self, 'flip', n.get_str_value()),
            "flop": lambda n : setattr(self, 'flop', n.get_str_value()),
            "gamma": lambda n : setattr(self, 'gamma', n.get_str_value()),
            "height": lambda n : setattr(self, 'height', n.get_str_value()),
            "hue": lambda n : setattr(self, 'hue', n.get_str_value()),
            "optimizer": lambda n : setattr(self, 'optimizer', n.get_enum_value(Properties_optimizer)),
            "quality": lambda n : setattr(self, 'quality', n.get_str_value()),
            "saturation": lambda n : setattr(self, 'saturation', n.get_str_value()),
            "sharpen": lambda n : setattr(self, 'sharpen', n.get_str_value()),
            "width": lambda n : setattr(self, 'width', n.get_str_value()),
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
        writer.write_str_value("aspect_ratio", self.aspect_ratio)
        writer.write_enum_value("auto_optimize", self.auto_optimize)
        writer.write_str_value("blur", self.blur)
        writer.write_str_value("brightness", self.brightness)
        writer.write_str_value("contrast", self.contrast)
        writer.write_str_value("crop", self.crop)
        writer.write_enum_value("crop_gravity", self.crop_gravity)
        writer.write_str_value("flip", self.flip)
        writer.write_str_value("flop", self.flop)
        writer.write_str_value("gamma", self.gamma)
        writer.write_str_value("height", self.height)
        writer.write_str_value("hue", self.hue)
        writer.write_enum_value("optimizer", self.optimizer)
        writer.write_str_value("quality", self.quality)
        writer.write_str_value("saturation", self.saturation)
        writer.write_str_value("sharpen", self.sharpen)
        writer.write_str_value("width", self.width)
        writer.write_additional_data_value(self.additional_data)
    

