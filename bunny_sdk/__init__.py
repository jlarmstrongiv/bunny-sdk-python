from kiota_abstractions.authentication.api_key_authentication_provider import (
    ApiKeyAuthenticationProvider,
    KeyLocation,
)
from kiota_http.httpx_request_adapter import HttpxRequestAdapter


from .generated.BunnyApiClient.bunny_api_client import BunnyApiClient
from .generated.EdgeStorageApiClient.edge_storage_api_client import EdgeStorageApiClient
from .generated.StreamApiClient.stream_api_client import StreamApiClient


def createBunnyApiClient(api_key: str) -> BunnyApiClient:
    authentication_provider = ApiKeyAuthenticationProvider(
        key_location=KeyLocation.Header, api_key=api_key, parameter_name="AccessKey"
    )

    request_adapter = HttpxRequestAdapter(authentication_provider)

    return BunnyApiClient(request_adapter)


def createEdgeStorageApiClient(api_key: str) -> EdgeStorageApiClient:
    authentication_provider = ApiKeyAuthenticationProvider(
        key_location=KeyLocation.Header, api_key=api_key, parameter_name="AccessKey"
    )

    request_adapter = HttpxRequestAdapter(authentication_provider)

    return EdgeStorageApiClient(request_adapter)


def createStreamApiClient(api_key: str) -> StreamApiClient:
    authentication_provider = ApiKeyAuthenticationProvider(
        key_location=KeyLocation.Header, api_key=api_key, parameter_name="AccessKey"
    )

    request_adapter = HttpxRequestAdapter(authentication_provider)

    return StreamApiClient(request_adapter)
