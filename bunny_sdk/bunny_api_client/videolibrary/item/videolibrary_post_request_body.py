from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models.stream_video_library.replication_regions import ReplicationRegions
    from .videolibrary_post_request_body_apple_fair_play_drm import VideolibraryPostRequestBody_AppleFairPlayDrm
    from .videolibrary_post_request_body_google_widevine_drm import VideolibraryPostRequestBody_GoogleWidevineDrm

@dataclass
class VideolibraryPostRequestBody(AdditionalDataHolder, Parsable):
    """
    The template for adding optional properties.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Determines direct play URLs are enabled for the library
    allow_direct_play: Optional[bool] = None
    # Determines if the Early-Play feature is enabled
    allow_early_play: Optional[bool] = None
    # The list of allowed referrer domains allowed to access the library
    allowed_referrers: Optional[List[str]] = None
    # The API access key for the library. Only added when the includeAccessKey parameter is set.
    api_access_key: Optional[str] = None
    # The API key used for authenticating with the video library
    api_key: Optional[str] = None
    # The AppleFairPlayDrm property
    apple_fair_play_drm: Optional[VideolibraryPostRequestBody_AppleFairPlayDrm] = None
    # The bitrate used for encoding 1080p videos
    bitrate1080p: Optional[int] = None
    # The bitrate used for encoding 1440p videos
    bitrate1440p: Optional[int] = None
    # The bitrate used for encoding 2160p videos
    bitrate2160p: Optional[int] = None
    # The bitrate used for encoding 240p videos
    bitrate240p: Optional[int] = None
    # The bitrate used for encoding 360p videos
    bitrate360p: Optional[int] = None
    # The bitrate used for encoding 480p videos
    bitrate480p: Optional[int] = None
    # The bitrate used for encoding 720p videos
    bitrate720p: Optional[int] = None
    # Determines if the requests without a referrer are blocked
    block_none_referrer: Optional[bool] = None
    # The list of blocked referrer domains blocked from accessing the library
    blocked_referrers: Optional[List[str]] = None
    # The captions display background color
    captions_background: Optional[str] = None
    # The captions display font color
    captions_font_color: Optional[str] = None
    # The captions display font size
    captions_font_size: Optional[int] = None
    # The list of controls on the video player.
    controls: Optional[str] = None
    # The custom HTMl that is added into the head of the HTML player.
    custom_h_t_m_l: Optional[str] = None
    # The date when the video library was created
    date_created: Optional[datetime.datetime] = None
    # The DrmVersion property
    drm_version: Optional[int] = None
    # Determines if content tagging should be enabled for this library.
    enable_content_tagging: Optional[bool] = None
    # Determines if the MediaCage basic DRM is enabled
    enable_d_r_m: Optional[bool] = None
    # Determines if the MP4 fallback feature is enabled
    enable_m_p4_fallback: Optional[bool] = None
    # Determines if the automatic audio transcribing is currently enabled for this zone.
    enable_transcribing: Optional[bool] = None
    # Determines if automatic transcribing description generation is currently enabled.
    enable_transcribing_description_generation: Optional[bool] = None
    # Determines if automatic transcribing title generation is currently enabled.
    enable_transcribing_title_generation: Optional[bool] = None
    # The comma separated list of enabled resolutions
    enabled_resolutions: Optional[str] = None
    # The captions font family.
    font_family: Optional[str] = None
    # The GoogleWidevineDrm property
    google_widevine_drm: Optional[VideolibraryPostRequestBody_GoogleWidevineDrm] = None
    # Determines if the video library has a watermark configured
    has_watermark: Optional[bool] = None
    # The Id property
    id: Optional[int] = None
    # Determines if the original video files should be stored after encoding
    keep_original_files: Optional[bool] = None
    # The name of the Video Library.
    name: Optional[str] = None
    # The key color of the player.
    player_key_color: Optional[str] = None
    # Determines if the player token authentication is enabled
    player_token_authentication_enabled: Optional[bool] = None
    # The ID of the connected underlying pull zone
    pull_zone_id: Optional[int] = None
    # The PullZoneType property
    pull_zone_type: Optional[float] = None
    # The read-only API key used for authenticating with the video library
    read_only_api_key: Optional[str] = None
    # The list of languages that the captions will be automatically transcribed to.
    remember_player_position: Optional[bool] = None
    # The geo-replication regions of the underlying storage zone
    replication_regions: Optional[List[ReplicationRegions]] = None
    # Determines if the video watch heatmap should be displayed in the player.
    show_heatmap: Optional[bool] = None
    # The total amount of storage used by the library
    storage_usage: Optional[int] = None
    # The ID of the connected underlying storage zone
    storage_zone_id: Optional[int] = None
    # The amount of traffic usage this month
    traffic_usage: Optional[int] = None
    # The TranscribingCaptionLanguages property
    transcribing_caption_languages: Optional[List[str]] = None
    # The UI language of the player
    u_i_language: Optional[str] = None
    # The URL of the VAST tag endpoint for advertising configuration
    vast_tag_url: Optional[str] = None
    # The vi.ai publisher id for advertising configuration
    vi_ai_publisher_id: Optional[str] = None
    # The number of videos in the video library
    video_count: Optional[int] = None
    # The height of the watermark (in %)
    watermark_height: Optional[int] = None
    # The left offset of the watermark position (in %)
    watermark_position_left: Optional[int] = None
    # The top offset of the watermark position (in %)
    watermark_position_top: Optional[int] = None
    # The WatermarkVersion property
    watermark_version: Optional[int] = None
    # The width of the watermark (in %)
    watermark_width: Optional[int] = None
    # The webhook URL of the video library
    webhook_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VideolibraryPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VideolibraryPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return VideolibraryPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ...models.stream_video_library.replication_regions import ReplicationRegions
        from .videolibrary_post_request_body_apple_fair_play_drm import VideolibraryPostRequestBody_AppleFairPlayDrm
        from .videolibrary_post_request_body_google_widevine_drm import VideolibraryPostRequestBody_GoogleWidevineDrm

        from ...models.stream_video_library.replication_regions import ReplicationRegions
        from .videolibrary_post_request_body_apple_fair_play_drm import VideolibraryPostRequestBody_AppleFairPlayDrm
        from .videolibrary_post_request_body_google_widevine_drm import VideolibraryPostRequestBody_GoogleWidevineDrm

        fields: Dict[str, Callable[[Any], None]] = {
            "AllowDirectPlay": lambda n : setattr(self, 'allow_direct_play', n.get_bool_value()),
            "AllowEarlyPlay": lambda n : setattr(self, 'allow_early_play', n.get_bool_value()),
            "AllowedReferrers": lambda n : setattr(self, 'allowed_referrers', n.get_collection_of_primitive_values(str)),
            "ApiAccessKey": lambda n : setattr(self, 'api_access_key', n.get_str_value()),
            "ApiKey": lambda n : setattr(self, 'api_key', n.get_str_value()),
            "AppleFairPlayDrm": lambda n : setattr(self, 'apple_fair_play_drm', n.get_object_value(VideolibraryPostRequestBody_AppleFairPlayDrm)),
            "Bitrate1080p": lambda n : setattr(self, 'bitrate1080p', n.get_int_value()),
            "Bitrate1440p": lambda n : setattr(self, 'bitrate1440p', n.get_int_value()),
            "Bitrate2160p": lambda n : setattr(self, 'bitrate2160p', n.get_int_value()),
            "Bitrate240p": lambda n : setattr(self, 'bitrate240p', n.get_int_value()),
            "Bitrate360p": lambda n : setattr(self, 'bitrate360p', n.get_int_value()),
            "Bitrate480p": lambda n : setattr(self, 'bitrate480p', n.get_int_value()),
            "Bitrate720p": lambda n : setattr(self, 'bitrate720p', n.get_int_value()),
            "BlockNoneReferrer": lambda n : setattr(self, 'block_none_referrer', n.get_bool_value()),
            "BlockedReferrers": lambda n : setattr(self, 'blocked_referrers', n.get_collection_of_primitive_values(str)),
            "CaptionsBackground": lambda n : setattr(self, 'captions_background', n.get_str_value()),
            "CaptionsFontColor": lambda n : setattr(self, 'captions_font_color', n.get_str_value()),
            "CaptionsFontSize": lambda n : setattr(self, 'captions_font_size', n.get_int_value()),
            "Controls": lambda n : setattr(self, 'controls', n.get_str_value()),
            "CustomHTML": lambda n : setattr(self, 'custom_h_t_m_l', n.get_str_value()),
            "DateCreated": lambda n : setattr(self, 'date_created', n.get_datetime_value()),
            "DrmVersion": lambda n : setattr(self, 'drm_version', n.get_int_value()),
            "EnableContentTagging": lambda n : setattr(self, 'enable_content_tagging', n.get_bool_value()),
            "EnableDRM": lambda n : setattr(self, 'enable_d_r_m', n.get_bool_value()),
            "EnableMP4Fallback": lambda n : setattr(self, 'enable_m_p4_fallback', n.get_bool_value()),
            "EnableTranscribing": lambda n : setattr(self, 'enable_transcribing', n.get_bool_value()),
            "EnableTranscribingDescriptionGeneration": lambda n : setattr(self, 'enable_transcribing_description_generation', n.get_bool_value()),
            "EnableTranscribingTitleGeneration": lambda n : setattr(self, 'enable_transcribing_title_generation', n.get_bool_value()),
            "EnabledResolutions": lambda n : setattr(self, 'enabled_resolutions', n.get_str_value()),
            "FontFamily": lambda n : setattr(self, 'font_family', n.get_str_value()),
            "GoogleWidevineDrm": lambda n : setattr(self, 'google_widevine_drm', n.get_object_value(VideolibraryPostRequestBody_GoogleWidevineDrm)),
            "HasWatermark": lambda n : setattr(self, 'has_watermark', n.get_bool_value()),
            "Id": lambda n : setattr(self, 'id', n.get_int_value()),
            "KeepOriginalFiles": lambda n : setattr(self, 'keep_original_files', n.get_bool_value()),
            "Name": lambda n : setattr(self, 'name', n.get_str_value()),
            "PlayerKeyColor": lambda n : setattr(self, 'player_key_color', n.get_str_value()),
            "PlayerTokenAuthenticationEnabled": lambda n : setattr(self, 'player_token_authentication_enabled', n.get_bool_value()),
            "PullZoneId": lambda n : setattr(self, 'pull_zone_id', n.get_int_value()),
            "PullZoneType": lambda n : setattr(self, 'pull_zone_type', n.get_float_value()),
            "ReadOnlyApiKey": lambda n : setattr(self, 'read_only_api_key', n.get_str_value()),
            "RememberPlayerPosition": lambda n : setattr(self, 'remember_player_position', n.get_bool_value()),
            "ReplicationRegions": lambda n : setattr(self, 'replication_regions', n.get_collection_of_enum_values(ReplicationRegions)),
            "ShowHeatmap": lambda n : setattr(self, 'show_heatmap', n.get_bool_value()),
            "StorageUsage": lambda n : setattr(self, 'storage_usage', n.get_int_value()),
            "StorageZoneId": lambda n : setattr(self, 'storage_zone_id', n.get_int_value()),
            "TrafficUsage": lambda n : setattr(self, 'traffic_usage', n.get_int_value()),
            "TranscribingCaptionLanguages": lambda n : setattr(self, 'transcribing_caption_languages', n.get_collection_of_primitive_values(str)),
            "UILanguage": lambda n : setattr(self, 'u_i_language', n.get_str_value()),
            "VastTagUrl": lambda n : setattr(self, 'vast_tag_url', n.get_str_value()),
            "ViAiPublisherId": lambda n : setattr(self, 'vi_ai_publisher_id', n.get_str_value()),
            "VideoCount": lambda n : setattr(self, 'video_count', n.get_int_value()),
            "WatermarkHeight": lambda n : setattr(self, 'watermark_height', n.get_int_value()),
            "WatermarkPositionLeft": lambda n : setattr(self, 'watermark_position_left', n.get_int_value()),
            "WatermarkPositionTop": lambda n : setattr(self, 'watermark_position_top', n.get_int_value()),
            "WatermarkVersion": lambda n : setattr(self, 'watermark_version', n.get_int_value()),
            "WatermarkWidth": lambda n : setattr(self, 'watermark_width', n.get_int_value()),
            "WebhookUrl": lambda n : setattr(self, 'webhook_url', n.get_str_value()),
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
        writer.write_bool_value("AllowDirectPlay", self.allow_direct_play)
        writer.write_bool_value("AllowEarlyPlay", self.allow_early_play)
        writer.write_int_value("Bitrate1080p", self.bitrate1080p)
        writer.write_int_value("Bitrate1440p", self.bitrate1440p)
        writer.write_int_value("Bitrate2160p", self.bitrate2160p)
        writer.write_int_value("Bitrate240p", self.bitrate240p)
        writer.write_int_value("Bitrate360p", self.bitrate360p)
        writer.write_int_value("Bitrate480p", self.bitrate480p)
        writer.write_int_value("Bitrate720p", self.bitrate720p)
        writer.write_bool_value("BlockNoneReferrer", self.block_none_referrer)
        writer.write_str_value("CaptionsBackground", self.captions_background)
        writer.write_str_value("CaptionsFontColor", self.captions_font_color)
        writer.write_int_value("CaptionsFontSize", self.captions_font_size)
        writer.write_str_value("Controls", self.controls)
        writer.write_str_value("CustomHTML", self.custom_h_t_m_l)
        writer.write_bool_value("EnableContentTagging", self.enable_content_tagging)
        writer.write_bool_value("EnableDRM", self.enable_d_r_m)
        writer.write_bool_value("EnableMP4Fallback", self.enable_m_p4_fallback)
        writer.write_bool_value("EnableTranscribing", self.enable_transcribing)
        writer.write_bool_value("EnableTranscribingDescriptionGeneration", self.enable_transcribing_description_generation)
        writer.write_bool_value("EnableTranscribingTitleGeneration", self.enable_transcribing_title_generation)
        writer.write_str_value("EnabledResolutions", self.enabled_resolutions)
        writer.write_str_value("FontFamily", self.font_family)
        writer.write_bool_value("KeepOriginalFiles", self.keep_original_files)
        writer.write_str_value("Name", self.name)
        writer.write_str_value("PlayerKeyColor", self.player_key_color)
        writer.write_bool_value("PlayerTokenAuthenticationEnabled", self.player_token_authentication_enabled)
        writer.write_bool_value("ShowHeatmap", self.show_heatmap)
        writer.write_collection_of_primitive_values("TranscribingCaptionLanguages", self.transcribing_caption_languages)
        writer.write_str_value("UILanguage", self.u_i_language)
        writer.write_str_value("VastTagUrl", self.vast_tag_url)
        writer.write_str_value("ViAiPublisherId", self.vi_ai_publisher_id)
        writer.write_int_value("WatermarkHeight", self.watermark_height)
        writer.write_int_value("WatermarkPositionLeft", self.watermark_position_left)
        writer.write_int_value("WatermarkPositionTop", self.watermark_position_top)
        writer.write_int_value("WatermarkWidth", self.watermark_width)
        writer.write_str_value("WebhookUrl", self.webhook_url)
        writer.write_additional_data_value(self.additional_data)
    

