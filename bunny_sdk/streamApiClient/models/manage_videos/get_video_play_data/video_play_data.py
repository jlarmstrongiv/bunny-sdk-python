from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..video import Video

@dataclass
class VideoPlayData(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The allowEarlyPlay property
    allow_early_play: Optional[bool] = None
    # The captionsBackground property
    captions_background: Optional[str] = None
    # The captionsFontColor property
    captions_font_color: Optional[str] = None
    # The captionsFontSize property
    captions_font_size: Optional[int] = None
    # The captionsPath property
    captions_path: Optional[str] = None
    # The controls property
    controls: Optional[str] = None
    # The drmVersion property
    drm_version: Optional[int] = None
    # The enableDRM property
    enable_d_r_m: Optional[bool] = None
    # The enableMP4Fallback property
    enable_m_p4_fallback: Optional[bool] = None
    # The fallbackUrl property
    fallback_url: Optional[str] = None
    # The fontFamily property
    font_family: Optional[str] = None
    # The originalUrl property
    original_url: Optional[str] = None
    # The playbackSpeeds property
    playback_speeds: Optional[str] = None
    # The playerKeyColor property
    player_key_color: Optional[str] = None
    # The previewUrl property
    preview_url: Optional[str] = None
    # The seekPath property
    seek_path: Optional[str] = None
    # The showHeatmap property
    show_heatmap: Optional[bool] = None
    # The thumbnailUrl property
    thumbnail_url: Optional[str] = None
    # The tokenAuthEnabled property
    token_auth_enabled: Optional[bool] = None
    # The uiLanguage property
    ui_language: Optional[str] = None
    # The vastTagUrl property
    vast_tag_url: Optional[str] = None
    # The video property
    video: Optional[Video] = None
    # The videoPlaylistUrl property
    video_playlist_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VideoPlayData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VideoPlayData
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return VideoPlayData()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..video import Video

        from ..video import Video

        fields: Dict[str, Callable[[Any], None]] = {
            "allowEarlyPlay": lambda n : setattr(self, 'allow_early_play', n.get_bool_value()),
            "captionsBackground": lambda n : setattr(self, 'captions_background', n.get_str_value()),
            "captionsFontColor": lambda n : setattr(self, 'captions_font_color', n.get_str_value()),
            "captionsFontSize": lambda n : setattr(self, 'captions_font_size', n.get_int_value()),
            "captionsPath": lambda n : setattr(self, 'captions_path', n.get_str_value()),
            "controls": lambda n : setattr(self, 'controls', n.get_str_value()),
            "drmVersion": lambda n : setattr(self, 'drm_version', n.get_int_value()),
            "enableDRM": lambda n : setattr(self, 'enable_d_r_m', n.get_bool_value()),
            "enableMP4Fallback": lambda n : setattr(self, 'enable_m_p4_fallback', n.get_bool_value()),
            "fallbackUrl": lambda n : setattr(self, 'fallback_url', n.get_str_value()),
            "fontFamily": lambda n : setattr(self, 'font_family', n.get_str_value()),
            "originalUrl": lambda n : setattr(self, 'original_url', n.get_str_value()),
            "playbackSpeeds": lambda n : setattr(self, 'playback_speeds', n.get_str_value()),
            "playerKeyColor": lambda n : setattr(self, 'player_key_color', n.get_str_value()),
            "previewUrl": lambda n : setattr(self, 'preview_url', n.get_str_value()),
            "seekPath": lambda n : setattr(self, 'seek_path', n.get_str_value()),
            "showHeatmap": lambda n : setattr(self, 'show_heatmap', n.get_bool_value()),
            "thumbnailUrl": lambda n : setattr(self, 'thumbnail_url', n.get_str_value()),
            "tokenAuthEnabled": lambda n : setattr(self, 'token_auth_enabled', n.get_bool_value()),
            "uiLanguage": lambda n : setattr(self, 'ui_language', n.get_str_value()),
            "vastTagUrl": lambda n : setattr(self, 'vast_tag_url', n.get_str_value()),
            "video": lambda n : setattr(self, 'video', n.get_object_value(Video)),
            "videoPlaylistUrl": lambda n : setattr(self, 'video_playlist_url', n.get_str_value()),
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
        writer.write_bool_value("allowEarlyPlay", self.allow_early_play)
        writer.write_str_value("captionsBackground", self.captions_background)
        writer.write_str_value("captionsFontColor", self.captions_font_color)
        writer.write_int_value("captionsFontSize", self.captions_font_size)
        writer.write_str_value("captionsPath", self.captions_path)
        writer.write_str_value("controls", self.controls)
        writer.write_int_value("drmVersion", self.drm_version)
        writer.write_bool_value("enableDRM", self.enable_d_r_m)
        writer.write_bool_value("enableMP4Fallback", self.enable_m_p4_fallback)
        writer.write_str_value("fallbackUrl", self.fallback_url)
        writer.write_str_value("fontFamily", self.font_family)
        writer.write_str_value("originalUrl", self.original_url)
        writer.write_str_value("playbackSpeeds", self.playback_speeds)
        writer.write_str_value("playerKeyColor", self.player_key_color)
        writer.write_str_value("previewUrl", self.preview_url)
        writer.write_str_value("seekPath", self.seek_path)
        writer.write_bool_value("showHeatmap", self.show_heatmap)
        writer.write_str_value("thumbnailUrl", self.thumbnail_url)
        writer.write_bool_value("tokenAuthEnabled", self.token_auth_enabled)
        writer.write_str_value("uiLanguage", self.ui_language)
        writer.write_str_value("vastTagUrl", self.vast_tag_url)
        writer.write_object_value("video", self.video)
        writer.write_str_value("videoPlaylistUrl", self.video_playlist_url)
        writer.write_additional_data_value(self.additional_data)
    

