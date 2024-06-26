from kiota_abstractions.authentication.api_key_authentication_provider import (
    ApiKeyAuthenticationProvider,
    KeyLocation,
)
from kiota_http.httpx_request_adapter import HttpxRequestAdapter


from .bunnyApiClient.bunny_api_client import BunnyApiClient
from .edgeStorageApiClient.edge_storage_api_client import EdgeStorageApiClient
from .streamApiClient.stream_api_client import StreamApiClient
from .loggingApiClient.logging_api_client import LoggingApiClient


def createBunnyApiClient(access_key: str) -> BunnyApiClient:
    authentication_provider = ApiKeyAuthenticationProvider(
        key_location=KeyLocation.Header, api_key=access_key, parameter_name="AccessKey"
    )

    request_adapter = HttpxRequestAdapter(authentication_provider)

    return BunnyApiClient(request_adapter)


def createEdgeStorageApiClient(access_key: str) -> EdgeStorageApiClient:
    authentication_provider = ApiKeyAuthenticationProvider(
        key_location=KeyLocation.Header, api_key=access_key, parameter_name="AccessKey"
    )

    request_adapter = HttpxRequestAdapter(authentication_provider)

    return EdgeStorageApiClient(request_adapter)


def createStreamApiClient(access_key: str) -> StreamApiClient:
    authentication_provider = ApiKeyAuthenticationProvider(
        key_location=KeyLocation.Header, api_key=access_key, parameter_name="AccessKey"
    )

    request_adapter = HttpxRequestAdapter(authentication_provider)

    return StreamApiClient(request_adapter)


def createLoggingApiClient(access_key: str) -> LoggingApiClient:
    authentication_provider = ApiKeyAuthenticationProvider(
        key_location=KeyLocation.Header, api_key=access_key, parameter_name="AccessKey"
    )

    request_adapter = HttpxRequestAdapter(authentication_provider)

    return LoggingApiClient(request_adapter)
