from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from .bunny_ai_image_blueprint import BunnyAiImageBlueprint
    from .edge_rule.edge_rule import EdgeRule
    from .optimizer.optimizer_class import OptimizerClass
    from .pull_zone_create_routing_filters import PullZoneCreate_RoutingFilters

@dataclass
class PullZoneCreate(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Determines if the AWS Signing is enabled
    a_w_s_signing_enabled: Optional[bool] = None
    # The AWS Signing region key
    a_w_s_signing_key: Optional[str] = None
    # The AWS Signing region name
    a_w_s_signing_region_name: Optional[str] = None
    # The AWS Signing region secret
    a_w_s_signing_secret: Optional[str] = None
    # The list of extensions that will return the CORS headers
    access_control_origin_header_extensions: Optional[List[str]] = None
    # Determines if the Add Canonical Header is enabled for this Pull Zone
    add_canonical_header: Optional[bool] = None
    # Determines if the Pull Zone should forward the current hostname to the origin
    add_host_header: Optional[bool] = None
    # The list of referrer hostnames that are allowed to access the pull zone.Requests containing the header Referer: hostname that is not on the list will be rejected.If empty, all the referrers are allowed
    allowed_referrers: Optional[List[str]] = None
    # The BlockNoneReferrer property
    block_none_referrer: Optional[bool] = None
    # If true, POST requests to the zone will be blocked
    block_post_requests: Optional[bool] = None
    # If true, access to root path will return a 403 error
    block_root_path_access: Optional[bool] = None
    # The list of blocked countries with the two-letter Alpha2 ISO codes
    blocked_countries: Optional[List[str]] = None
    # The list of IPs that are blocked from accessing the pull zone. Requests coming from the following IPs will be rejected. If empty, all the IPs will be allowed
    blocked_ips: Optional[List[str]] = None
    # The list of referrer hostnames that are not allowed to access the pull zone. Requests containing the header Referer: hostname that is on the list will be rejected. If empty, all the referrers are allowed
    blocked_referrers: Optional[List[str]] = None
    # The list of budget redirected countries with the two-letter Alpha2 ISO codes
    budget_redirected_countries: Optional[List[str]] = None
    # The BunnyAiImageBlueprints property
    bunny_ai_image_blueprints: Optional[List[BunnyAiImageBlueprint]] = None
    # Excessive requests are delayed until their number exceeds the maximum burst size.
    burst_size: Optional[int] = None
    # Sets the browser cache control override setting for this zone
    cache_control_browser_max_age_override: Optional[int] = None
    # The override cache time for the pull zone
    cache_control_max_age_override: Optional[int] = None
    # The override cache time for the pull zone for the end client
    cache_control_public_max_age_override: Optional[int] = None
    # Determines if bunny.net should be caching error responses
    cache_error_responses: Optional[bool] = None
    # The number of connections limited per IP for this zone
    connection_limit_per_i_p_count: Optional[int] = None
    # Contains the list of vary parameters that will be used for vary cache by cookie string. If empty, cookie vary will not be used.
    cookie_vary_parameters: Optional[List[str]] = None
    # Determines if the cookies are disabled for the pull zone
    disable_cookies: Optional[bool] = None
    # If true, the built-in let's encrypt is disabled and requests are passed to the origin.
    disable_lets_encrypt: Optional[bool] = None
    # Determines the origin port of the pull zone.
    dns_origin_port: Optional[int] = None
    # Determines the origin scheme of the pull zone.
    dns_origin_scheme: Optional[str] = None
    # The list of edge rules on this Pull Zone
    edge_rules: Optional[List[EdgeRule]] = None
    # The EdgeScriptExecutionPhase property
    edge_script_execution_phase: Optional[float] = None
    # The ID of the edge script that the pull zone is linked to
    edge_script_id: Optional[int] = None
    # Determines if the CORS headers should be enabled
    enable_access_control_origin_header: Optional[bool] = None
    # If set to true, any hostnames added to this Pull Zone will automatically enable SSL.
    enable_auto_s_s_l: Optional[bool] = None
    # Determines if the AVIF Vary feature is enabled.
    enable_avif_vary: Optional[bool] = None
    # The EnableBunnyImageAi property
    enable_bunny_image_ai: Optional[bool] = None
    # Determines if the cache slice (Optimize for video) feature is enabled for the Pull Zone
    enable_cache_slice: Optional[bool] = None
    # Determines if the Cookie Vary feature is enabled.
    enable_cookie_vary: Optional[bool] = None
    # Determines if the Country Code Vary feature is enabled.
    enable_country_code_vary: Optional[bool] = None
    # Determines if the delivery from the Africa region is enabled for this pull zone
    enable_geo_zone_a_f: Optional[bool] = None
    # Determines if the delivery from the Asian / Oceanian region is enabled for this pull zone
    enable_geo_zone_a_s_i_a: Optional[bool] = None
    # Determines if the delivery from the European region is enabled for this pull zone
    enable_geo_zone_e_u: Optional[bool] = None
    # Determines if the delivery from the South American region is enabled for this pull zone
    enable_geo_zone_s_a: Optional[bool] = None
    # Determines if the delivery from the North American region is enabled for this pull zone
    enable_geo_zone_u_s: Optional[bool] = None
    # Determines if the Hostname Vary feature is enabled.
    enable_hostname_vary: Optional[bool] = None
    # Determines if the logging is enabled for this Pull Zone
    enable_logging: Optional[bool] = None
    # Determines if the Mobile Vary feature is enabled.
    enable_mobile_vary: Optional[bool] = None
    # If true the server will use the origin shield feature
    enable_origin_shield: Optional[bool] = None
    # If set to true the query string ordering property is enabled.
    enable_query_string_ordering: Optional[bool] = None
    # Determines if request coalescing is currently enabled.
    enable_request_coalescing: Optional[bool] = None
    # The EnableSafeHop property
    enable_safe_hop: Optional[bool] = None
    # Determines if smart caching is enabled for this zone
    enable_smart_cache: Optional[bool] = None
    # Determines if the TLS 1 is enabled on the Pull Zone
    enable_t_l_s1: Optional[bool] = None
    # Determines if the TLS 1.1 is enabled on the Pull Zone
    enable_t_l_s1_1: Optional[bool] = None
    # Determines if the WebP Vary feature is enabled.
    enable_web_p_vary: Optional[bool] = None
    # Contains the custom error page code that will be returned
    error_page_custom_code: Optional[str] = None
    # Determines if custom error page code should be enabled.
    error_page_enable_custom_code: Optional[bool] = None
    # Determines if the statuspage widget should be displayed on the error pages
    error_page_enable_statuspage_widget: Optional[bool] = None
    # The statuspage code that will be used to build the status widget
    error_page_statuspage_code: Optional[str] = None
    # Determines if the error pages should be whitelabel or not
    error_page_whitelabel: Optional[bool] = None
    # Determines if the zone will follow origin redirects
    follow_redirects: Optional[bool] = None
    # True if the Pull Zone is ignoring query strings when serving cached objects
    ignore_query_strings: Optional[bool] = None
    # The amount of data after the rate limit will be activated
    limit_rate_after: Optional[float] = None
    # The maximum rate at which the zone will transfer data in kb/s. 0 for unlimited
    limit_rate_per_second: Optional[float] = None
    # The LogAnonymizationType property
    log_anonymization_type: Optional[float] = None
    # The LogFormat property
    log_format: Optional[float] = None
    # Determines if the log forwarding is enabled
    log_forwarding_enabled: Optional[bool] = None
    # The LogForwardingFormat property
    log_forwarding_format: Optional[float] = None
    # The log forwarding hostname
    log_forwarding_hostname: Optional[str] = None
    # The log forwarding port
    log_forwarding_port: Optional[int] = None
    # The LogForwardingProtocol property
    log_forwarding_protocol: Optional[float] = None
    # The log forwarding token value
    log_forwarding_token: Optional[str] = None
    # Determines if the log anonymization should be enabled
    logging_i_p_anonymization_enabled: Optional[bool] = None
    # Determines if the permanent logging feature is enabled
    logging_save_to_storage: Optional[bool] = None
    # The ID of the logging storage zone that is configured for this Pull Zone
    logging_storage_zone_id: Optional[int] = None
    # The MagicContainersAppId property
    magic_containers_app_id: Optional[str] = None
    # The MagicContainersEndpointId property
    magic_containers_endpoint_id: Optional[int] = None
    # The MiddlewareScriptId property
    middleware_script_id: Optional[int] = None
    # The monthly limit of bandwidth in bytes that the pullzone is allowed to use
    monthly_bandwidth_limit: Optional[int] = None
    # The total monthly charges for this so zone so far
    monthly_charges: Optional[float] = None
    # The name of the pull zone.
    name: Optional[str] = None
    # Determines if the automatic image optimization should be enabled
    optimizer_automatic_optimization_enabled: Optional[bool] = None
    # Contains the list of optimizer classes
    optimizer_classes: Optional[List[OptimizerClass]] = None
    # Determines the maximum automatic image size for desktop clients
    optimizer_desktop_max_width: Optional[int] = None
    # Determines the image manipulation should be enabled
    optimizer_enable_manipulation_engine: Optional[bool] = None
    # Determines if the WebP optimization should be enabled
    optimizer_enable_web_p: Optional[bool] = None
    # Determines if the optimizer should be enabled for this zone
    optimizer_enabled: Optional[bool] = None
    # Determines if the optimizer class list should be enforced
    optimizer_force_classes: Optional[bool] = None
    # Determines the image quality for desktop clients
    optimizer_image_quality: Optional[int] = None
    # Determines if the CSS minification should be enabled
    optimizer_minify_c_s_s: Optional[bool] = None
    # Determines if the JavaScript minification should be enabled
    optimizer_minify_java_script: Optional[bool] = None
    # Determines the image quality for mobile clients
    optimizer_mobile_image_quality: Optional[int] = None
    # Determines the maximum automatic image size for mobile clients
    optimizer_mobile_max_width: Optional[int] = None
    # The OptimizerStaticHtmlEnabled property
    optimizer_static_html_enabled: Optional[bool] = None
    # The OptimizerStaticHtmlWordPressBypassCookie property
    optimizer_static_html_word_press_bypass_cookie: Optional[str] = None
    # The OptimizerStaticHtmlWordPressPath property
    optimizer_static_html_word_press_path: Optional[str] = None
    # Determines if image watermarking should be enabled
    optimizer_watermark_enabled: Optional[bool] = None
    # Sets the minimum image size to which the watermark will be added
    optimizer_watermark_min_image_size: Optional[int] = None
    # Sets the offset of the watermark image
    optimizer_watermark_offset: Optional[float] = None
    # The OptimizerWatermarkPosition property
    optimizer_watermark_position: Optional[float] = None
    # Sets the URL of the watermark image
    optimizer_watermark_url: Optional[str] = None
    # The amount of seconds to wait when connecting to the origin. Otherwise the request will fail or retry.
    origin_connect_timeout: Optional[int] = None
    # Determines the host header that will be sent to the origin
    origin_host_header: Optional[str] = None
    # The amount of seconds to wait when waiting for the origin reply. Otherwise the request will fail or retry.
    origin_response_timeout: Optional[int] = None
    # The number of retries to the origin server
    origin_retries: Optional[int] = None
    # Determines if we should retry the request in case of a connection timeout.
    origin_retry_connection_timeout: Optional[bool] = None
    # Determines the amount of time that the CDN should wait before retrying an origin request.
    origin_retry_delay: Optional[int] = None
    # Determines if we should retry the request in case of a response timeout.
    origin_retry_response_timeout: Optional[bool] = None
    # Determines if we should retry the request in case of a 5XX response.
    origin_retry5_x_x_responses: Optional[bool] = None
    # Determines if the origin shield concurrency limit is enabled.
    origin_shield_enable_concurrency_limit: Optional[bool] = None
    # Determines the number of maximum concurrent requests allowed to the origin.
    origin_shield_max_concurrent_requests: Optional[int] = None
    # Determines the max number of origin requests that will remain in the queue
    origin_shield_max_queued_requests: Optional[int] = None
    # Determines the max queue wait time
    origin_shield_queue_max_wait_time: Optional[int] = None
    # The zone code of the origin shield
    origin_shield_zone_code: Optional[str] = None
    # The OriginType property
    origin_type: Optional[float] = None
    # The origin URL of the pull zone where the files are fetched from.
    origin_url: Optional[str] = None
    # The IP of the storage zone used for Perma-Cache
    perma_cache_storage_zone_id: Optional[int] = None
    # The PermaCacheType property
    perma_cache_type: Optional[int] = None
    # The custom preloading screen code
    preloading_screen_code: Optional[str] = None
    # Determines if the custom preloader screen is enabled
    preloading_screen_code_enabled: Optional[bool] = None
    # The delay in milliseconds after which the preloading screen will be displayed
    preloading_screen_delay: Optional[int] = None
    # Determines if the preloading screen is currently enabled
    preloading_screen_enabled: Optional[bool] = None
    # The preloading screen logo URL
    preloading_screen_logo_url: Optional[str] = None
    # The PreloadingScreenShowOnFirstVisit property
    preloading_screen_show_on_first_visit: Optional[bool] = None
    # The PreloadingScreenTheme property
    preloading_screen_theme: Optional[float] = None
    # Contains the list of vary parameters that will be used for vary cache by query string. If empty, all parameters will be used to construct the key
    query_string_vary_parameters: Optional[List[str]] = None
    # Determines the lock time for coalesced requests.
    request_coalescing_timeout: Optional[int] = None
    # Max number of requests per IP per second
    request_limit: Optional[int] = None
    # The list of routing filters enabled for this zone
    routing_filters: Optional[List[PullZoneCreate_RoutingFilters]] = None
    # The ShieldDDosProtectionEnabled property
    shield_d_dos_protection_enabled: Optional[bool] = None
    # The ShieldDDosProtectionType property
    shield_d_dos_protection_type: Optional[float] = None
    # The ID of the storage zone that the pull zone is linked to
    storage_zone_id: Optional[int] = None
    # The Type property
    type: Optional[float] = None
    # Determines if cache update is performed in the background.
    use_background_update: Optional[bool] = None
    # Determines if we should use stale cache while the origin is offline
    use_stale_while_offline: Optional[bool] = None
    # Determines if we should use stale cache while cache is updating
    use_stale_while_updating: Optional[bool] = None
    # Determines if the Pull Zone should verify the origin SSL certificate
    verify_origin_s_s_l: Optional[bool] = None
    # Determines the enabled WAF rule groups
    w_a_f_disabled_rule_groups: Optional[List[str]] = None
    # Determines the disabled WAF rules
    w_a_f_disabled_rules: Optional[List[str]] = None
    # Determines if WAF should enable request headers logging
    w_a_f_enable_request_header_logging: Optional[bool] = None
    # Determines if WAF should be enabled on the zone
    w_a_f_enabled: Optional[bool] = None
    # Determines the list of headers that will be ignored in the WAF logs
    w_a_f_request_header_ignores: Optional[bool] = None
    # True if the URL secure token authentication security is enabled
    zone_security_enabled: Optional[bool] = None
    # True if the zone security hash should include the remote IP
    zone_security_include_hash_remote_i_p: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PullZoneCreate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PullZoneCreate
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PullZoneCreate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .bunny_ai_image_blueprint import BunnyAiImageBlueprint
        from .edge_rule.edge_rule import EdgeRule
        from .optimizer.optimizer_class import OptimizerClass
        from .pull_zone_create_routing_filters import PullZoneCreate_RoutingFilters

        from .bunny_ai_image_blueprint import BunnyAiImageBlueprint
        from .edge_rule.edge_rule import EdgeRule
        from .optimizer.optimizer_class import OptimizerClass
        from .pull_zone_create_routing_filters import PullZoneCreate_RoutingFilters

        fields: Dict[str, Callable[[Any], None]] = {
            "AWSSigningEnabled": lambda n : setattr(self, 'a_w_s_signing_enabled', n.get_bool_value()),
            "AWSSigningKey": lambda n : setattr(self, 'a_w_s_signing_key', n.get_str_value()),
            "AWSSigningRegionName": lambda n : setattr(self, 'a_w_s_signing_region_name', n.get_str_value()),
            "AWSSigningSecret": lambda n : setattr(self, 'a_w_s_signing_secret', n.get_str_value()),
            "AccessControlOriginHeaderExtensions": lambda n : setattr(self, 'access_control_origin_header_extensions', n.get_collection_of_primitive_values(str)),
            "AddCanonicalHeader": lambda n : setattr(self, 'add_canonical_header', n.get_bool_value()),
            "AddHostHeader": lambda n : setattr(self, 'add_host_header', n.get_bool_value()),
            "AllowedReferrers": lambda n : setattr(self, 'allowed_referrers', n.get_collection_of_primitive_values(str)),
            "BlockNoneReferrer": lambda n : setattr(self, 'block_none_referrer', n.get_bool_value()),
            "BlockPostRequests": lambda n : setattr(self, 'block_post_requests', n.get_bool_value()),
            "BlockRootPathAccess": lambda n : setattr(self, 'block_root_path_access', n.get_bool_value()),
            "BlockedCountries": lambda n : setattr(self, 'blocked_countries', n.get_collection_of_primitive_values(str)),
            "BlockedIps": lambda n : setattr(self, 'blocked_ips', n.get_collection_of_primitive_values(str)),
            "BlockedReferrers": lambda n : setattr(self, 'blocked_referrers', n.get_collection_of_primitive_values(str)),
            "BudgetRedirectedCountries": lambda n : setattr(self, 'budget_redirected_countries', n.get_collection_of_primitive_values(str)),
            "BunnyAiImageBlueprints": lambda n : setattr(self, 'bunny_ai_image_blueprints', n.get_collection_of_object_values(BunnyAiImageBlueprint)),
            "BurstSize": lambda n : setattr(self, 'burst_size', n.get_int_value()),
            "CacheControlBrowserMaxAgeOverride": lambda n : setattr(self, 'cache_control_browser_max_age_override', n.get_int_value()),
            "CacheControlMaxAgeOverride": lambda n : setattr(self, 'cache_control_max_age_override', n.get_int_value()),
            "CacheControlPublicMaxAgeOverride": lambda n : setattr(self, 'cache_control_public_max_age_override', n.get_int_value()),
            "CacheErrorResponses": lambda n : setattr(self, 'cache_error_responses', n.get_bool_value()),
            "ConnectionLimitPerIPCount": lambda n : setattr(self, 'connection_limit_per_i_p_count', n.get_int_value()),
            "CookieVaryParameters": lambda n : setattr(self, 'cookie_vary_parameters', n.get_collection_of_primitive_values(str)),
            "DisableCookies": lambda n : setattr(self, 'disable_cookies', n.get_bool_value()),
            "DisableLetsEncrypt": lambda n : setattr(self, 'disable_lets_encrypt', n.get_bool_value()),
            "DnsOriginPort": lambda n : setattr(self, 'dns_origin_port', n.get_int_value()),
            "DnsOriginScheme": lambda n : setattr(self, 'dns_origin_scheme', n.get_str_value()),
            "EdgeRules": lambda n : setattr(self, 'edge_rules', n.get_collection_of_object_values(EdgeRule)),
            "EdgeScriptExecutionPhase": lambda n : setattr(self, 'edge_script_execution_phase', n.get_float_value()),
            "EdgeScriptId": lambda n : setattr(self, 'edge_script_id', n.get_int_value()),
            "EnableAccessControlOriginHeader": lambda n : setattr(self, 'enable_access_control_origin_header', n.get_bool_value()),
            "EnableAutoSSL": lambda n : setattr(self, 'enable_auto_s_s_l', n.get_bool_value()),
            "EnableAvifVary": lambda n : setattr(self, 'enable_avif_vary', n.get_bool_value()),
            "EnableBunnyImageAi": lambda n : setattr(self, 'enable_bunny_image_ai', n.get_bool_value()),
            "EnableCacheSlice": lambda n : setattr(self, 'enable_cache_slice', n.get_bool_value()),
            "EnableCookieVary": lambda n : setattr(self, 'enable_cookie_vary', n.get_bool_value()),
            "EnableCountryCodeVary": lambda n : setattr(self, 'enable_country_code_vary', n.get_bool_value()),
            "EnableGeoZoneAF": lambda n : setattr(self, 'enable_geo_zone_a_f', n.get_bool_value()),
            "EnableGeoZoneASIA": lambda n : setattr(self, 'enable_geo_zone_a_s_i_a', n.get_bool_value()),
            "EnableGeoZoneEU": lambda n : setattr(self, 'enable_geo_zone_e_u', n.get_bool_value()),
            "EnableGeoZoneSA": lambda n : setattr(self, 'enable_geo_zone_s_a', n.get_bool_value()),
            "EnableGeoZoneUS": lambda n : setattr(self, 'enable_geo_zone_u_s', n.get_bool_value()),
            "EnableHostnameVary": lambda n : setattr(self, 'enable_hostname_vary', n.get_bool_value()),
            "EnableLogging": lambda n : setattr(self, 'enable_logging', n.get_bool_value()),
            "EnableMobileVary": lambda n : setattr(self, 'enable_mobile_vary', n.get_bool_value()),
            "EnableOriginShield": lambda n : setattr(self, 'enable_origin_shield', n.get_bool_value()),
            "EnableQueryStringOrdering": lambda n : setattr(self, 'enable_query_string_ordering', n.get_bool_value()),
            "EnableRequestCoalescing": lambda n : setattr(self, 'enable_request_coalescing', n.get_bool_value()),
            "EnableSafeHop": lambda n : setattr(self, 'enable_safe_hop', n.get_bool_value()),
            "EnableSmartCache": lambda n : setattr(self, 'enable_smart_cache', n.get_bool_value()),
            "EnableTLS1": lambda n : setattr(self, 'enable_t_l_s1', n.get_bool_value()),
            "EnableTLS1_1": lambda n : setattr(self, 'enable_t_l_s1_1', n.get_bool_value()),
            "EnableWebPVary": lambda n : setattr(self, 'enable_web_p_vary', n.get_bool_value()),
            "ErrorPageCustomCode": lambda n : setattr(self, 'error_page_custom_code', n.get_str_value()),
            "ErrorPageEnableCustomCode": lambda n : setattr(self, 'error_page_enable_custom_code', n.get_bool_value()),
            "ErrorPageEnableStatuspageWidget": lambda n : setattr(self, 'error_page_enable_statuspage_widget', n.get_bool_value()),
            "ErrorPageStatuspageCode": lambda n : setattr(self, 'error_page_statuspage_code', n.get_str_value()),
            "ErrorPageWhitelabel": lambda n : setattr(self, 'error_page_whitelabel', n.get_bool_value()),
            "FollowRedirects": lambda n : setattr(self, 'follow_redirects', n.get_bool_value()),
            "IgnoreQueryStrings": lambda n : setattr(self, 'ignore_query_strings', n.get_bool_value()),
            "LimitRateAfter": lambda n : setattr(self, 'limit_rate_after', n.get_float_value()),
            "LimitRatePerSecond": lambda n : setattr(self, 'limit_rate_per_second', n.get_float_value()),
            "LogAnonymizationType": lambda n : setattr(self, 'log_anonymization_type', n.get_float_value()),
            "LogFormat": lambda n : setattr(self, 'log_format', n.get_float_value()),
            "LogForwardingEnabled": lambda n : setattr(self, 'log_forwarding_enabled', n.get_bool_value()),
            "LogForwardingFormat": lambda n : setattr(self, 'log_forwarding_format', n.get_float_value()),
            "LogForwardingHostname": lambda n : setattr(self, 'log_forwarding_hostname', n.get_str_value()),
            "LogForwardingPort": lambda n : setattr(self, 'log_forwarding_port', n.get_int_value()),
            "LogForwardingProtocol": lambda n : setattr(self, 'log_forwarding_protocol', n.get_float_value()),
            "LogForwardingToken": lambda n : setattr(self, 'log_forwarding_token', n.get_str_value()),
            "LoggingIPAnonymizationEnabled": lambda n : setattr(self, 'logging_i_p_anonymization_enabled', n.get_bool_value()),
            "LoggingSaveToStorage": lambda n : setattr(self, 'logging_save_to_storage', n.get_bool_value()),
            "LoggingStorageZoneId": lambda n : setattr(self, 'logging_storage_zone_id', n.get_int_value()),
            "MagicContainersAppId": lambda n : setattr(self, 'magic_containers_app_id', n.get_str_value()),
            "MagicContainersEndpointId": lambda n : setattr(self, 'magic_containers_endpoint_id', n.get_int_value()),
            "MiddlewareScriptId": lambda n : setattr(self, 'middleware_script_id', n.get_int_value()),
            "MonthlyBandwidthLimit": lambda n : setattr(self, 'monthly_bandwidth_limit', n.get_int_value()),
            "MonthlyCharges": lambda n : setattr(self, 'monthly_charges', n.get_float_value()),
            "Name": lambda n : setattr(self, 'name', n.get_str_value()),
            "OptimizerAutomaticOptimizationEnabled": lambda n : setattr(self, 'optimizer_automatic_optimization_enabled', n.get_bool_value()),
            "OptimizerClasses": lambda n : setattr(self, 'optimizer_classes', n.get_collection_of_object_values(OptimizerClass)),
            "OptimizerDesktopMaxWidth": lambda n : setattr(self, 'optimizer_desktop_max_width', n.get_int_value()),
            "OptimizerEnableManipulationEngine": lambda n : setattr(self, 'optimizer_enable_manipulation_engine', n.get_bool_value()),
            "OptimizerEnableWebP": lambda n : setattr(self, 'optimizer_enable_web_p', n.get_bool_value()),
            "OptimizerEnabled": lambda n : setattr(self, 'optimizer_enabled', n.get_bool_value()),
            "OptimizerForceClasses": lambda n : setattr(self, 'optimizer_force_classes', n.get_bool_value()),
            "OptimizerImageQuality": lambda n : setattr(self, 'optimizer_image_quality', n.get_int_value()),
            "OptimizerMinifyCSS": lambda n : setattr(self, 'optimizer_minify_c_s_s', n.get_bool_value()),
            "OptimizerMinifyJavaScript": lambda n : setattr(self, 'optimizer_minify_java_script', n.get_bool_value()),
            "OptimizerMobileImageQuality": lambda n : setattr(self, 'optimizer_mobile_image_quality', n.get_int_value()),
            "OptimizerMobileMaxWidth": lambda n : setattr(self, 'optimizer_mobile_max_width', n.get_int_value()),
            "OptimizerStaticHtmlEnabled": lambda n : setattr(self, 'optimizer_static_html_enabled', n.get_bool_value()),
            "OptimizerStaticHtmlWordPressBypassCookie": lambda n : setattr(self, 'optimizer_static_html_word_press_bypass_cookie', n.get_str_value()),
            "OptimizerStaticHtmlWordPressPath": lambda n : setattr(self, 'optimizer_static_html_word_press_path', n.get_str_value()),
            "OptimizerWatermarkEnabled": lambda n : setattr(self, 'optimizer_watermark_enabled', n.get_bool_value()),
            "OptimizerWatermarkMinImageSize": lambda n : setattr(self, 'optimizer_watermark_min_image_size', n.get_int_value()),
            "OptimizerWatermarkOffset": lambda n : setattr(self, 'optimizer_watermark_offset', n.get_float_value()),
            "OptimizerWatermarkPosition": lambda n : setattr(self, 'optimizer_watermark_position', n.get_float_value()),
            "OptimizerWatermarkUrl": lambda n : setattr(self, 'optimizer_watermark_url', n.get_str_value()),
            "OriginConnectTimeout": lambda n : setattr(self, 'origin_connect_timeout', n.get_int_value()),
            "OriginHostHeader": lambda n : setattr(self, 'origin_host_header', n.get_str_value()),
            "OriginResponseTimeout": lambda n : setattr(self, 'origin_response_timeout', n.get_int_value()),
            "OriginRetries": lambda n : setattr(self, 'origin_retries', n.get_int_value()),
            "OriginRetryConnectionTimeout": lambda n : setattr(self, 'origin_retry_connection_timeout', n.get_bool_value()),
            "OriginRetryDelay": lambda n : setattr(self, 'origin_retry_delay', n.get_int_value()),
            "OriginRetryResponseTimeout": lambda n : setattr(self, 'origin_retry_response_timeout', n.get_bool_value()),
            "OriginRetry5XXResponses": lambda n : setattr(self, 'origin_retry5_x_x_responses', n.get_bool_value()),
            "OriginShieldEnableConcurrencyLimit": lambda n : setattr(self, 'origin_shield_enable_concurrency_limit', n.get_bool_value()),
            "OriginShieldMaxConcurrentRequests": lambda n : setattr(self, 'origin_shield_max_concurrent_requests', n.get_int_value()),
            "OriginShieldMaxQueuedRequests": lambda n : setattr(self, 'origin_shield_max_queued_requests', n.get_int_value()),
            "OriginShieldQueueMaxWaitTime": lambda n : setattr(self, 'origin_shield_queue_max_wait_time', n.get_int_value()),
            "OriginShieldZoneCode": lambda n : setattr(self, 'origin_shield_zone_code', n.get_str_value()),
            "OriginType": lambda n : setattr(self, 'origin_type', n.get_float_value()),
            "OriginUrl": lambda n : setattr(self, 'origin_url', n.get_str_value()),
            "PermaCacheStorageZoneId": lambda n : setattr(self, 'perma_cache_storage_zone_id', n.get_int_value()),
            "PermaCacheType": lambda n : setattr(self, 'perma_cache_type', n.get_int_value()),
            "PreloadingScreenCode": lambda n : setattr(self, 'preloading_screen_code', n.get_str_value()),
            "PreloadingScreenCodeEnabled": lambda n : setattr(self, 'preloading_screen_code_enabled', n.get_bool_value()),
            "PreloadingScreenDelay": lambda n : setattr(self, 'preloading_screen_delay', n.get_int_value()),
            "PreloadingScreenEnabled": lambda n : setattr(self, 'preloading_screen_enabled', n.get_bool_value()),
            "PreloadingScreenLogoUrl": lambda n : setattr(self, 'preloading_screen_logo_url', n.get_str_value()),
            "PreloadingScreenShowOnFirstVisit": lambda n : setattr(self, 'preloading_screen_show_on_first_visit', n.get_bool_value()),
            "PreloadingScreenTheme": lambda n : setattr(self, 'preloading_screen_theme', n.get_float_value()),
            "QueryStringVaryParameters": lambda n : setattr(self, 'query_string_vary_parameters', n.get_collection_of_primitive_values(str)),
            "RequestCoalescingTimeout": lambda n : setattr(self, 'request_coalescing_timeout', n.get_int_value()),
            "RequestLimit": lambda n : setattr(self, 'request_limit', n.get_int_value()),
            "RoutingFilters": lambda n : setattr(self, 'routing_filters', n.get_collection_of_enum_values(PullZoneCreate_RoutingFilters)),
            "ShieldDDosProtectionEnabled": lambda n : setattr(self, 'shield_d_dos_protection_enabled', n.get_bool_value()),
            "ShieldDDosProtectionType": lambda n : setattr(self, 'shield_d_dos_protection_type', n.get_float_value()),
            "StorageZoneId": lambda n : setattr(self, 'storage_zone_id', n.get_int_value()),
            "Type": lambda n : setattr(self, 'type', n.get_float_value()),
            "UseBackgroundUpdate": lambda n : setattr(self, 'use_background_update', n.get_bool_value()),
            "UseStaleWhileOffline": lambda n : setattr(self, 'use_stale_while_offline', n.get_bool_value()),
            "UseStaleWhileUpdating": lambda n : setattr(self, 'use_stale_while_updating', n.get_bool_value()),
            "VerifyOriginSSL": lambda n : setattr(self, 'verify_origin_s_s_l', n.get_bool_value()),
            "WAFDisabledRuleGroups": lambda n : setattr(self, 'w_a_f_disabled_rule_groups', n.get_collection_of_primitive_values(str)),
            "WAFDisabledRules": lambda n : setattr(self, 'w_a_f_disabled_rules', n.get_collection_of_primitive_values(str)),
            "WAFEnableRequestHeaderLogging": lambda n : setattr(self, 'w_a_f_enable_request_header_logging', n.get_bool_value()),
            "WAFEnabled": lambda n : setattr(self, 'w_a_f_enabled', n.get_bool_value()),
            "WAFRequestHeaderIgnores": lambda n : setattr(self, 'w_a_f_request_header_ignores', n.get_bool_value()),
            "ZoneSecurityEnabled": lambda n : setattr(self, 'zone_security_enabled', n.get_bool_value()),
            "ZoneSecurityIncludeHashRemoteIP": lambda n : setattr(self, 'zone_security_include_hash_remote_i_p', n.get_bool_value()),
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
        writer.write_bool_value("AWSSigningEnabled", self.a_w_s_signing_enabled)
        writer.write_str_value("AWSSigningKey", self.a_w_s_signing_key)
        writer.write_str_value("AWSSigningRegionName", self.a_w_s_signing_region_name)
        writer.write_str_value("AWSSigningSecret", self.a_w_s_signing_secret)
        writer.write_collection_of_primitive_values("AccessControlOriginHeaderExtensions", self.access_control_origin_header_extensions)
        writer.write_bool_value("AddCanonicalHeader", self.add_canonical_header)
        writer.write_bool_value("AddHostHeader", self.add_host_header)
        writer.write_collection_of_primitive_values("AllowedReferrers", self.allowed_referrers)
        writer.write_bool_value("BlockNoneReferrer", self.block_none_referrer)
        writer.write_bool_value("BlockPostRequests", self.block_post_requests)
        writer.write_bool_value("BlockRootPathAccess", self.block_root_path_access)
        writer.write_collection_of_primitive_values("BlockedCountries", self.blocked_countries)
        writer.write_collection_of_primitive_values("BlockedIps", self.blocked_ips)
        writer.write_collection_of_primitive_values("BlockedReferrers", self.blocked_referrers)
        writer.write_collection_of_primitive_values("BudgetRedirectedCountries", self.budget_redirected_countries)
        writer.write_collection_of_object_values("BunnyAiImageBlueprints", self.bunny_ai_image_blueprints)
        writer.write_int_value("BurstSize", self.burst_size)
        writer.write_int_value("CacheControlBrowserMaxAgeOverride", self.cache_control_browser_max_age_override)
        writer.write_int_value("CacheControlMaxAgeOverride", self.cache_control_max_age_override)
        writer.write_int_value("CacheControlPublicMaxAgeOverride", self.cache_control_public_max_age_override)
        writer.write_bool_value("CacheErrorResponses", self.cache_error_responses)
        writer.write_int_value("ConnectionLimitPerIPCount", self.connection_limit_per_i_p_count)
        writer.write_collection_of_primitive_values("CookieVaryParameters", self.cookie_vary_parameters)
        writer.write_bool_value("DisableCookies", self.disable_cookies)
        writer.write_bool_value("DisableLetsEncrypt", self.disable_lets_encrypt)
        writer.write_int_value("DnsOriginPort", self.dns_origin_port)
        writer.write_str_value("DnsOriginScheme", self.dns_origin_scheme)
        writer.write_collection_of_object_values("EdgeRules", self.edge_rules)
        writer.write_float_value("EdgeScriptExecutionPhase", self.edge_script_execution_phase)
        writer.write_int_value("EdgeScriptId", self.edge_script_id)
        writer.write_bool_value("EnableAccessControlOriginHeader", self.enable_access_control_origin_header)
        writer.write_bool_value("EnableAutoSSL", self.enable_auto_s_s_l)
        writer.write_bool_value("EnableAvifVary", self.enable_avif_vary)
        writer.write_bool_value("EnableBunnyImageAi", self.enable_bunny_image_ai)
        writer.write_bool_value("EnableCacheSlice", self.enable_cache_slice)
        writer.write_bool_value("EnableCookieVary", self.enable_cookie_vary)
        writer.write_bool_value("EnableCountryCodeVary", self.enable_country_code_vary)
        writer.write_bool_value("EnableGeoZoneAF", self.enable_geo_zone_a_f)
        writer.write_bool_value("EnableGeoZoneASIA", self.enable_geo_zone_a_s_i_a)
        writer.write_bool_value("EnableGeoZoneEU", self.enable_geo_zone_e_u)
        writer.write_bool_value("EnableGeoZoneSA", self.enable_geo_zone_s_a)
        writer.write_bool_value("EnableGeoZoneUS", self.enable_geo_zone_u_s)
        writer.write_bool_value("EnableHostnameVary", self.enable_hostname_vary)
        writer.write_bool_value("EnableLogging", self.enable_logging)
        writer.write_bool_value("EnableMobileVary", self.enable_mobile_vary)
        writer.write_bool_value("EnableOriginShield", self.enable_origin_shield)
        writer.write_bool_value("EnableQueryStringOrdering", self.enable_query_string_ordering)
        writer.write_bool_value("EnableRequestCoalescing", self.enable_request_coalescing)
        writer.write_bool_value("EnableSafeHop", self.enable_safe_hop)
        writer.write_bool_value("EnableSmartCache", self.enable_smart_cache)
        writer.write_bool_value("EnableTLS1", self.enable_t_l_s1)
        writer.write_bool_value("EnableTLS1_1", self.enable_t_l_s1_1)
        writer.write_bool_value("EnableWebPVary", self.enable_web_p_vary)
        writer.write_str_value("ErrorPageCustomCode", self.error_page_custom_code)
        writer.write_bool_value("ErrorPageEnableCustomCode", self.error_page_enable_custom_code)
        writer.write_bool_value("ErrorPageEnableStatuspageWidget", self.error_page_enable_statuspage_widget)
        writer.write_str_value("ErrorPageStatuspageCode", self.error_page_statuspage_code)
        writer.write_bool_value("ErrorPageWhitelabel", self.error_page_whitelabel)
        writer.write_bool_value("FollowRedirects", self.follow_redirects)
        writer.write_bool_value("IgnoreQueryStrings", self.ignore_query_strings)
        writer.write_float_value("LimitRateAfter", self.limit_rate_after)
        writer.write_float_value("LimitRatePerSecond", self.limit_rate_per_second)
        writer.write_float_value("LogAnonymizationType", self.log_anonymization_type)
        writer.write_float_value("LogFormat", self.log_format)
        writer.write_bool_value("LogForwardingEnabled", self.log_forwarding_enabled)
        writer.write_float_value("LogForwardingFormat", self.log_forwarding_format)
        writer.write_str_value("LogForwardingHostname", self.log_forwarding_hostname)
        writer.write_int_value("LogForwardingPort", self.log_forwarding_port)
        writer.write_float_value("LogForwardingProtocol", self.log_forwarding_protocol)
        writer.write_str_value("LogForwardingToken", self.log_forwarding_token)
        writer.write_bool_value("LoggingIPAnonymizationEnabled", self.logging_i_p_anonymization_enabled)
        writer.write_bool_value("LoggingSaveToStorage", self.logging_save_to_storage)
        writer.write_int_value("LoggingStorageZoneId", self.logging_storage_zone_id)
        writer.write_str_value("MagicContainersAppId", self.magic_containers_app_id)
        writer.write_int_value("MagicContainersEndpointId", self.magic_containers_endpoint_id)
        writer.write_int_value("MiddlewareScriptId", self.middleware_script_id)
        writer.write_int_value("MonthlyBandwidthLimit", self.monthly_bandwidth_limit)
        writer.write_float_value("MonthlyCharges", self.monthly_charges)
        writer.write_str_value("Name", self.name)
        writer.write_bool_value("OptimizerAutomaticOptimizationEnabled", self.optimizer_automatic_optimization_enabled)
        writer.write_collection_of_object_values("OptimizerClasses", self.optimizer_classes)
        writer.write_int_value("OptimizerDesktopMaxWidth", self.optimizer_desktop_max_width)
        writer.write_bool_value("OptimizerEnableManipulationEngine", self.optimizer_enable_manipulation_engine)
        writer.write_bool_value("OptimizerEnableWebP", self.optimizer_enable_web_p)
        writer.write_bool_value("OptimizerEnabled", self.optimizer_enabled)
        writer.write_bool_value("OptimizerForceClasses", self.optimizer_force_classes)
        writer.write_int_value("OptimizerImageQuality", self.optimizer_image_quality)
        writer.write_bool_value("OptimizerMinifyCSS", self.optimizer_minify_c_s_s)
        writer.write_bool_value("OptimizerMinifyJavaScript", self.optimizer_minify_java_script)
        writer.write_int_value("OptimizerMobileImageQuality", self.optimizer_mobile_image_quality)
        writer.write_int_value("OptimizerMobileMaxWidth", self.optimizer_mobile_max_width)
        writer.write_bool_value("OptimizerStaticHtmlEnabled", self.optimizer_static_html_enabled)
        writer.write_str_value("OptimizerStaticHtmlWordPressBypassCookie", self.optimizer_static_html_word_press_bypass_cookie)
        writer.write_str_value("OptimizerStaticHtmlWordPressPath", self.optimizer_static_html_word_press_path)
        writer.write_bool_value("OptimizerWatermarkEnabled", self.optimizer_watermark_enabled)
        writer.write_int_value("OptimizerWatermarkMinImageSize", self.optimizer_watermark_min_image_size)
        writer.write_float_value("OptimizerWatermarkOffset", self.optimizer_watermark_offset)
        writer.write_float_value("OptimizerWatermarkPosition", self.optimizer_watermark_position)
        writer.write_str_value("OptimizerWatermarkUrl", self.optimizer_watermark_url)
        writer.write_int_value("OriginConnectTimeout", self.origin_connect_timeout)
        writer.write_str_value("OriginHostHeader", self.origin_host_header)
        writer.write_int_value("OriginResponseTimeout", self.origin_response_timeout)
        writer.write_int_value("OriginRetries", self.origin_retries)
        writer.write_bool_value("OriginRetryConnectionTimeout", self.origin_retry_connection_timeout)
        writer.write_int_value("OriginRetryDelay", self.origin_retry_delay)
        writer.write_bool_value("OriginRetryResponseTimeout", self.origin_retry_response_timeout)
        writer.write_bool_value("OriginRetry5XXResponses", self.origin_retry5_x_x_responses)
        writer.write_bool_value("OriginShieldEnableConcurrencyLimit", self.origin_shield_enable_concurrency_limit)
        writer.write_int_value("OriginShieldMaxConcurrentRequests", self.origin_shield_max_concurrent_requests)
        writer.write_int_value("OriginShieldMaxQueuedRequests", self.origin_shield_max_queued_requests)
        writer.write_int_value("OriginShieldQueueMaxWaitTime", self.origin_shield_queue_max_wait_time)
        writer.write_str_value("OriginShieldZoneCode", self.origin_shield_zone_code)
        writer.write_float_value("OriginType", self.origin_type)
        writer.write_str_value("OriginUrl", self.origin_url)
        writer.write_int_value("PermaCacheStorageZoneId", self.perma_cache_storage_zone_id)
        writer.write_int_value("PermaCacheType", self.perma_cache_type)
        writer.write_str_value("PreloadingScreenCode", self.preloading_screen_code)
        writer.write_bool_value("PreloadingScreenCodeEnabled", self.preloading_screen_code_enabled)
        writer.write_int_value("PreloadingScreenDelay", self.preloading_screen_delay)
        writer.write_bool_value("PreloadingScreenEnabled", self.preloading_screen_enabled)
        writer.write_str_value("PreloadingScreenLogoUrl", self.preloading_screen_logo_url)
        writer.write_bool_value("PreloadingScreenShowOnFirstVisit", self.preloading_screen_show_on_first_visit)
        writer.write_float_value("PreloadingScreenTheme", self.preloading_screen_theme)
        writer.write_collection_of_primitive_values("QueryStringVaryParameters", self.query_string_vary_parameters)
        writer.write_int_value("RequestCoalescingTimeout", self.request_coalescing_timeout)
        writer.write_int_value("RequestLimit", self.request_limit)
        writer.write_collection_of_enum_values("RoutingFilters", self.routing_filters)
        writer.write_bool_value("ShieldDDosProtectionEnabled", self.shield_d_dos_protection_enabled)
        writer.write_float_value("ShieldDDosProtectionType", self.shield_d_dos_protection_type)
        writer.write_int_value("StorageZoneId", self.storage_zone_id)
        writer.write_float_value("Type", self.type)
        writer.write_bool_value("UseBackgroundUpdate", self.use_background_update)
        writer.write_bool_value("UseStaleWhileOffline", self.use_stale_while_offline)
        writer.write_bool_value("UseStaleWhileUpdating", self.use_stale_while_updating)
        writer.write_bool_value("VerifyOriginSSL", self.verify_origin_s_s_l)
        writer.write_collection_of_primitive_values("WAFDisabledRuleGroups", self.w_a_f_disabled_rule_groups)
        writer.write_collection_of_primitive_values("WAFDisabledRules", self.w_a_f_disabled_rules)
        writer.write_bool_value("WAFEnableRequestHeaderLogging", self.w_a_f_enable_request_header_logging)
        writer.write_bool_value("WAFEnabled", self.w_a_f_enabled)
        writer.write_bool_value("WAFRequestHeaderIgnores", self.w_a_f_request_header_ignores)
        writer.write_bool_value("ZoneSecurityEnabled", self.zone_security_enabled)
        writer.write_bool_value("ZoneSecurityIncludeHashRemoteIP", self.zone_security_include_hash_remote_i_p)
        writer.write_additional_data_value(self.additional_data)
    

