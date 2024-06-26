from kiota_abstractions.authentication.api_key_authentication_provider import (
    ApiKeyAuthenticationProvider,
    KeyLocation,
)
from kiota_http.httpx_request_adapter import HttpxRequestAdapter


from .bunny_api_client.bunny_api_client import BunnyApiClient
from .edge_storage_api_client.edge_storage_api_client import EdgeStorageApiClient
from .stream_api_client.stream_api_client import StreamApiClient
from .logging_api_client.logging_api_client import LoggingApiClient


def create_bunny_api_client(access_key: str) -> BunnyApiClient:
    authentication_provider = ApiKeyAuthenticationProvider(
        key_location=KeyLocation.Header, api_key=access_key, parameter_name="AccessKey"
    )

    request_adapter = HttpxRequestAdapter(authentication_provider)

    return BunnyApiClient(request_adapter)


def create_edge_storage_api_client(
    access_key: str, base_url: str
) -> EdgeStorageApiClient:
    authentication_provider = ApiKeyAuthenticationProvider(
        key_location=KeyLocation.Header, api_key=access_key, parameter_name="AccessKey"
    )

    request_adapter = HttpxRequestAdapter(authentication_provider)
    request_adapter.base_url = base_url

    return EdgeStorageApiClient(request_adapter)


def create_stream_api_client(access_key: str) -> StreamApiClient:
    authentication_provider = ApiKeyAuthenticationProvider(
        key_location=KeyLocation.Header, api_key=access_key, parameter_name="AccessKey"
    )

    request_adapter = HttpxRequestAdapter(authentication_provider)

    return StreamApiClient(request_adapter)


def create_logging_api_client(access_key: str) -> LoggingApiClient:
    authentication_provider = ApiKeyAuthenticationProvider(
        key_location=KeyLocation.Header, api_key=access_key, parameter_name="AccessKey"
    )

    request_adapter = HttpxRequestAdapter(authentication_provider)

    return LoggingApiClient(request_adapter)
