from __future__ import annotations
from kiota_abstractions.api_client_builder import enable_backing_store_for_serialization_writer_factory, register_default_deserializer, register_default_serializer
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.serialization import ParseNodeFactoryRegistry, SerializationWriterFactoryRegistry
from kiota_serialization_form.form_parse_node_factory import FormParseNodeFactory
from kiota_serialization_form.form_serialization_writer_factory import FormSerializationWriterFactory
from kiota_serialization_json.json_parse_node_factory import JsonParseNodeFactory
from kiota_serialization_json.json_serialization_writer_factory import JsonSerializationWriterFactory
from kiota_serialization_multipart.multipart_serialization_writer_factory import MultipartSerializationWriterFactory
from kiota_serialization_text.text_parse_node_factory import TextParseNodeFactory
from kiota_serialization_text.text_serialization_writer_factory import TextSerializationWriterFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .abusecase.abusecase_request_builder import AbusecaseRequestBuilder
    from .apikey.apikey_request_builder import ApikeyRequestBuilder
    from .compute.compute_request_builder import ComputeRequestBuilder
    from .country.country_request_builder import CountryRequestBuilder
    from .dmca.dmca_request_builder import DmcaRequestBuilder
    from .dnszone.dnszone_request_builder import DnszoneRequestBuilder
    from .pullzone.pullzone_request_builder import PullzoneRequestBuilder
    from .purge.purge_request_builder import PurgeRequestBuilder
    from .region.region_request_builder import RegionRequestBuilder
    from .statistics.statistics_request_builder import StatisticsRequestBuilder
    from .storagezone.storagezone_request_builder import StoragezoneRequestBuilder
    from .user.user_request_builder import UserRequestBuilder
    from .videolibrary.videolibrary_request_builder import VideolibraryRequestBuilder

class BunnyApiClient(BaseRequestBuilder):
    """
    The main entry point of the SDK, exposes the configuration and the fluent API.
    """
    def __init__(self,request_adapter: RequestAdapter) -> None:
        """
        Instantiates a new BunnyApiClient and sets the default values.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        if not request_adapter:
            raise TypeError("request_adapter cannot be null.")
        super().__init__(request_adapter, "{+baseurl}", None)
        register_default_serializer(JsonSerializationWriterFactory)
        register_default_serializer(TextSerializationWriterFactory)
        register_default_serializer(FormSerializationWriterFactory)
        register_default_serializer(MultipartSerializationWriterFactory)
        register_default_deserializer(JsonParseNodeFactory)
        register_default_deserializer(TextParseNodeFactory)
        register_default_deserializer(FormParseNodeFactory)
        if not self.request_adapter.base_url:
            self.request_adapter.base_url = "https://api.bunny.net"
        self.path_parameters["base_url"] = self.request_adapter.base_url
    
    @property
    def abusecase(self) -> AbusecaseRequestBuilder:
        """
        The abusecase property
        """
        from .abusecase.abusecase_request_builder import AbusecaseRequestBuilder

        return AbusecaseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def apikey(self) -> ApikeyRequestBuilder:
        """
        The apikey property
        """
        from .apikey.apikey_request_builder import ApikeyRequestBuilder

        return ApikeyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def compute(self) -> ComputeRequestBuilder:
        """
        The compute property
        """
        from .compute.compute_request_builder import ComputeRequestBuilder

        return ComputeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def country(self) -> CountryRequestBuilder:
        """
        The country property
        """
        from .country.country_request_builder import CountryRequestBuilder

        return CountryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dmca(self) -> DmcaRequestBuilder:
        """
        The dmca property
        """
        from .dmca.dmca_request_builder import DmcaRequestBuilder

        return DmcaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dnszone(self) -> DnszoneRequestBuilder:
        """
        The dnszone property
        """
        from .dnszone.dnszone_request_builder import DnszoneRequestBuilder

        return DnszoneRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pullzone(self) -> PullzoneRequestBuilder:
        """
        The pullzone property
        """
        from .pullzone.pullzone_request_builder import PullzoneRequestBuilder

        return PullzoneRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def purge(self) -> PurgeRequestBuilder:
        """
        The purge property
        """
        from .purge.purge_request_builder import PurgeRequestBuilder

        return PurgeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def region(self) -> RegionRequestBuilder:
        """
        The region property
        """
        from .region.region_request_builder import RegionRequestBuilder

        return RegionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def statistics(self) -> StatisticsRequestBuilder:
        """
        The statistics property
        """
        from .statistics.statistics_request_builder import StatisticsRequestBuilder

        return StatisticsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def storagezone(self) -> StoragezoneRequestBuilder:
        """
        The storagezone property
        """
        from .storagezone.storagezone_request_builder import StoragezoneRequestBuilder

        return StoragezoneRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user(self) -> UserRequestBuilder:
        """
        The user property
        """
        from .user.user_request_builder import UserRequestBuilder

        return UserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def videolibrary(self) -> VideolibraryRequestBuilder:
        """
        The videolibrary property
        """
        from .videolibrary.videolibrary_request_builder import VideolibraryRequestBuilder

        return VideolibraryRequestBuilder(self.request_adapter, self.path_parameters)
    

