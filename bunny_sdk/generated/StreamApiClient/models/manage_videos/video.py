from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .caption import Caption
    from .chapter import Chapter
    from .meta_tag import MetaTag
    from .moment import Moment
    from .transcoding_message.transcoding_message import TranscodingMessage
    from .video_category import Video_category

@dataclass
class Video(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The available resolutions of the video
    available_resolutions: Optional[str] = None
    # The average watch time of the video in seconds
    average_watch_time: Optional[int] = None
    # The captions property
    captions: Optional[List[Caption]] = None
    # The automatically detected category of the video
    category: Optional[Video_category] = None
    # The list of chapters available for the video
    chapters: Optional[List[Chapter]] = None
    # The ID of the collection where the video belongs
    collection_id: Optional[str] = None
    # The date when the video was uploaded
    date_uploaded: Optional[datetime.datetime] = None
    # The current encode progress of the video
    encode_progress: Optional[int] = None
    # The framerate of the video
    framerate: Optional[float] = None
    # The unique ID of the video
    guid: Optional[str] = None
    # Determines if the video has MP4 fallback files generated
    has_m_p4_fallback: Optional[bool] = None
    # The height of the original video file
    height: Optional[int] = None
    # Determines if the video is publicly accessible
    is_public: Optional[bool] = None
    # The duration of the video in seconds
    length: Optional[int] = None
    # The list of meta tags that have been added to the video
    meta_tags: Optional[List[MetaTag]] = None
    # The list of moments available for the video
    moments: Optional[List[Moment]] = None
    # The rotation of the video
    rotation: Optional[int] = None
    # The status of the video.
    status: Optional[float] = None
    # The amount of storage used by this video
    storage_size: Optional[int] = None
    # The number of thumbnails generated for this video
    thumbnail_count: Optional[int] = None
    # The file name of the thumbnail inside of the storage
    thumbnail_file_name: Optional[str] = None
    # The title of the video
    title: Optional[str] = None
    # The total video watch time in seconds
    total_watch_time: Optional[int] = None
    # The list of transcoding messages that describe potential issues while the video was transcoding
    transcoding_messages: Optional[List[TranscodingMessage]] = None
    # The ID of the video library that the video belongs to
    video_library_id: Optional[int] = None
    # The number of views the video received
    views: Optional[int] = None
    # The width of the original video file
    width: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Video:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Video
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Video()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .caption import Caption
        from .chapter import Chapter
        from .meta_tag import MetaTag
        from .moment import Moment
        from .transcoding_message.transcoding_message import TranscodingMessage
        from .video_category import Video_category

        from .caption import Caption
        from .chapter import Chapter
        from .meta_tag import MetaTag
        from .moment import Moment
        from .transcoding_message.transcoding_message import TranscodingMessage
        from .video_category import Video_category

        fields: Dict[str, Callable[[Any], None]] = {
            "availableResolutions": lambda n : setattr(self, 'available_resolutions', n.get_str_value()),
            "averageWatchTime": lambda n : setattr(self, 'average_watch_time', n.get_int_value()),
            "captions": lambda n : setattr(self, 'captions', n.get_collection_of_object_values(Caption)),
            "category": lambda n : setattr(self, 'category', n.get_enum_value(Video_category)),
            "chapters": lambda n : setattr(self, 'chapters', n.get_collection_of_object_values(Chapter)),
            "collectionId": lambda n : setattr(self, 'collection_id', n.get_str_value()),
            "dateUploaded": lambda n : setattr(self, 'date_uploaded', n.get_datetime_value()),
            "encodeProgress": lambda n : setattr(self, 'encode_progress', n.get_int_value()),
            "framerate": lambda n : setattr(self, 'framerate', n.get_float_value()),
            "guid": lambda n : setattr(self, 'guid', n.get_str_value()),
            "hasMP4Fallback": lambda n : setattr(self, 'has_m_p4_fallback', n.get_bool_value()),
            "height": lambda n : setattr(self, 'height', n.get_int_value()),
            "isPublic": lambda n : setattr(self, 'is_public', n.get_bool_value()),
            "length": lambda n : setattr(self, 'length', n.get_int_value()),
            "metaTags": lambda n : setattr(self, 'meta_tags', n.get_collection_of_object_values(MetaTag)),
            "moments": lambda n : setattr(self, 'moments', n.get_collection_of_object_values(Moment)),
            "rotation": lambda n : setattr(self, 'rotation', n.get_int_value()),
            "status": lambda n : setattr(self, 'status', n.get_float_value()),
            "storageSize": lambda n : setattr(self, 'storage_size', n.get_int_value()),
            "thumbnailCount": lambda n : setattr(self, 'thumbnail_count', n.get_int_value()),
            "thumbnailFileName": lambda n : setattr(self, 'thumbnail_file_name', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "totalWatchTime": lambda n : setattr(self, 'total_watch_time', n.get_int_value()),
            "transcodingMessages": lambda n : setattr(self, 'transcoding_messages', n.get_collection_of_object_values(TranscodingMessage)),
            "videoLibraryId": lambda n : setattr(self, 'video_library_id', n.get_int_value()),
            "views": lambda n : setattr(self, 'views', n.get_int_value()),
            "width": lambda n : setattr(self, 'width', n.get_int_value()),
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
        writer.write_collection_of_object_values("captions", self.captions)
        writer.write_collection_of_object_values("chapters", self.chapters)
        writer.write_str_value("collectionId", self.collection_id)
        writer.write_collection_of_object_values("metaTags", self.meta_tags)
        writer.write_collection_of_object_values("moments", self.moments)
        writer.write_str_value("title", self.title)
        writer.write_additional_data_value(self.additional_data)
    

