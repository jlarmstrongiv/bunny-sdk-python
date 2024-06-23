from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ...models.pull_zone.pull_zone import PullZone
    from ...models.pull_zone.pull_zone_create import PullZoneCreate
    from .add_allowed_referrer.add_allowed_referrer_request_builder import AddAllowedReferrerRequestBuilder
    from .add_blocked_ip.add_blocked_ip_request_builder import AddBlockedIpRequestBuilder
    from .add_blocked_referrer.add_blocked_referrer_request_builder import AddBlockedReferrerRequestBuilder
    from .add_certificate.add_certificate_request_builder import AddCertificateRequestBuilder
    from .add_hostname.add_hostname_request_builder import AddHostnameRequestBuilder
    from .edgerules.edgerules_request_builder import EdgerulesRequestBuilder
    from .optimizer.optimizer_request_builder import OptimizerRequestBuilder
    from .originshield.originshield_request_builder import OriginshieldRequestBuilder
    from .purge_cache.purge_cache_request_builder import PurgeCacheRequestBuilder
    from .remove_allowed_referrer.remove_allowed_referrer_request_builder import RemoveAllowedReferrerRequestBuilder
    from .remove_blocked_ip.remove_blocked_ip_request_builder import RemoveBlockedIpRequestBuilder
    from .remove_blocked_referrer.remove_blocked_referrer_request_builder import RemoveBlockedReferrerRequestBuilder
    from .remove_certificate.remove_certificate_request_builder import RemoveCertificateRequestBuilder
    from .remove_hostname.remove_hostname_request_builder import RemoveHostnameRequestBuilder
    from .reset_security_key.reset_security_key_request_builder import ResetSecurityKeyRequestBuilder
    from .safehop.safehop_request_builder import SafehopRequestBuilder
    from .set_force_s_s_l.set_force_s_s_l_request_builder import SetForceSSLRequestBuilder
    from .waf.waf_request_builder import WafRequestBuilder

class ItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /pullzone/{-id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new ItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/pullzone/{%2Did}?includeCertificate={includeCertificate}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        [DeletePullZone API Docs](https://docs.bunny.net/reference/pullzonepublic_delete)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ItemRequestBuilderGetQueryParameters]] = None) -> Optional[PullZone]:
        """
        [GetPullZone API Docs](https://docs.bunny.net/reference/pullzonepublic_index2)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PullZone]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.pull_zone.pull_zone import PullZone

        return await self.request_adapter.send_async(request_info, PullZone, None)
    
    async def post(self,body: PullZoneCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PullZone]:
        """
        [UpdatePullZone API Docs](https://docs.bunny.net/reference/pullzonepublic_updatepullzone)
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PullZone]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.pull_zone.pull_zone import PullZone

        return await self.request_adapter.send_async(request_info, PullZone, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        [DeletePullZone API Docs](https://docs.bunny.net/reference/pullzonepublic_delete)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, '{+baseurl}/pullzone/{%2Did}', self.path_parameters)
        request_info.configure(request_configuration)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        [GetPullZone API Docs](https://docs.bunny.net/reference/pullzonepublic_index2)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: PullZoneCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        [UpdatePullZone API Docs](https://docs.bunny.net/reference/pullzonepublic_updatepullzone)
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, '{+baseurl}/pullzone/{%2Did}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> ItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return ItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def add_allowed_referrer(self) -> AddAllowedReferrerRequestBuilder:
        """
        The addAllowedReferrer property
        """
        from .add_allowed_referrer.add_allowed_referrer_request_builder import AddAllowedReferrerRequestBuilder

        return AddAllowedReferrerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def add_blocked_ip(self) -> AddBlockedIpRequestBuilder:
        """
        The addBlockedIp property
        """
        from .add_blocked_ip.add_blocked_ip_request_builder import AddBlockedIpRequestBuilder

        return AddBlockedIpRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def add_blocked_referrer(self) -> AddBlockedReferrerRequestBuilder:
        """
        The addBlockedReferrer property
        """
        from .add_blocked_referrer.add_blocked_referrer_request_builder import AddBlockedReferrerRequestBuilder

        return AddBlockedReferrerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def add_certificate(self) -> AddCertificateRequestBuilder:
        """
        The addCertificate property
        """
        from .add_certificate.add_certificate_request_builder import AddCertificateRequestBuilder

        return AddCertificateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def add_hostname(self) -> AddHostnameRequestBuilder:
        """
        The addHostname property
        """
        from .add_hostname.add_hostname_request_builder import AddHostnameRequestBuilder

        return AddHostnameRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def edgerules(self) -> EdgerulesRequestBuilder:
        """
        The edgerules property
        """
        from .edgerules.edgerules_request_builder import EdgerulesRequestBuilder

        return EdgerulesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def optimizer(self) -> OptimizerRequestBuilder:
        """
        The optimizer property
        """
        from .optimizer.optimizer_request_builder import OptimizerRequestBuilder

        return OptimizerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def originshield(self) -> OriginshieldRequestBuilder:
        """
        The originshield property
        """
        from .originshield.originshield_request_builder import OriginshieldRequestBuilder

        return OriginshieldRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def purge_cache(self) -> PurgeCacheRequestBuilder:
        """
        The purgeCache property
        """
        from .purge_cache.purge_cache_request_builder import PurgeCacheRequestBuilder

        return PurgeCacheRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remove_allowed_referrer(self) -> RemoveAllowedReferrerRequestBuilder:
        """
        The removeAllowedReferrer property
        """
        from .remove_allowed_referrer.remove_allowed_referrer_request_builder import RemoveAllowedReferrerRequestBuilder

        return RemoveAllowedReferrerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remove_blocked_ip(self) -> RemoveBlockedIpRequestBuilder:
        """
        The removeBlockedIp property
        """
        from .remove_blocked_ip.remove_blocked_ip_request_builder import RemoveBlockedIpRequestBuilder

        return RemoveBlockedIpRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remove_blocked_referrer(self) -> RemoveBlockedReferrerRequestBuilder:
        """
        The removeBlockedReferrer property
        """
        from .remove_blocked_referrer.remove_blocked_referrer_request_builder import RemoveBlockedReferrerRequestBuilder

        return RemoveBlockedReferrerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remove_certificate(self) -> RemoveCertificateRequestBuilder:
        """
        The removeCertificate property
        """
        from .remove_certificate.remove_certificate_request_builder import RemoveCertificateRequestBuilder

        return RemoveCertificateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remove_hostname(self) -> RemoveHostnameRequestBuilder:
        """
        The removeHostname property
        """
        from .remove_hostname.remove_hostname_request_builder import RemoveHostnameRequestBuilder

        return RemoveHostnameRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reset_security_key(self) -> ResetSecurityKeyRequestBuilder:
        """
        The resetSecurityKey property
        """
        from .reset_security_key.reset_security_key_request_builder import ResetSecurityKeyRequestBuilder

        return ResetSecurityKeyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def safehop(self) -> SafehopRequestBuilder:
        """
        The safehop property
        """
        from .safehop.safehop_request_builder import SafehopRequestBuilder

        return SafehopRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def set_force_s_s_l(self) -> SetForceSSLRequestBuilder:
        """
        The setForceSSL property
        """
        from .set_force_s_s_l.set_force_s_s_l_request_builder import SetForceSSLRequestBuilder

        return SetForceSSLRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def waf(self) -> WafRequestBuilder:
        """
        The waf property
        """
        from .waf.waf_request_builder import WafRequestBuilder

        return WafRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ItemRequestBuilderGetQueryParameters():
        """
        [GetPullZone API Docs](https://docs.bunny.net/reference/pullzonepublic_index2)
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "include_certificate":
                return "includeCertificate"
            return original_name
        
        # Determines if the result hostnames should contain the SSL certificate
        include_certificate: Optional[bool] = None

    
    @dataclass
    class ItemRequestBuilderGetRequestConfiguration(RequestConfiguration[ItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ItemRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

