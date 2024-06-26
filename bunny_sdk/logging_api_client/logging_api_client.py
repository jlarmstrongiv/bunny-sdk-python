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
    from .with_mm_with_dd_with_yy.with_mm_with_dd_with_yy_request_builder import WithMmWithDdWithYyRequestBuilder

class LoggingApiClient(BaseRequestBuilder):
    """
    The main entry point of the SDK, exposes the configuration and the fluent API.
    """
    def __init__(self,request_adapter: RequestAdapter) -> None:
        """
        Instantiates a new LoggingApiClient and sets the default values.
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
            self.request_adapter.base_url = "https://logging.bunnycdn.com"
        self.path_parameters["base_url"] = self.request_adapter.base_url
    
    def with_mm_with_dd_with_yy(self,dd: int, mm: int, yy: int) -> WithMmWithDdWithYyRequestBuilder:
        """
        Builds and executes requests for operations under /{mm}-{dd}-{yy}
        param dd: The path parameter: dd
        param mm: The path parameter: mm
        param yy: The path parameter: yy
        Returns: WithMmWithDdWithYyRequestBuilder
        """
        if not dd:
            raise TypeError("dd cannot be null.")
        if not mm:
            raise TypeError("mm cannot be null.")
        if not yy:
            raise TypeError("yy cannot be null.")
        from .with_mm_with_dd_with_yy.with_mm_with_dd_with_yy_request_builder import WithMmWithDdWithYyRequestBuilder

        return WithMmWithDdWithYyRequestBuilder(self.request_adapter, self.path_parameters, dd, mm, yy)
    
