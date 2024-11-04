from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_rule.custom_rule_request_builder import CustomRuleRequestBuilder
    from .custom_rules.custom_rules_request_builder import CustomRulesRequestBuilder
    from .engine_config.engine_config_request_builder import EngineConfigRequestBuilder
    from .enums.enums_request_builder import EnumsRequestBuilder
    from .profiles.profiles_request_builder import ProfilesRequestBuilder
    from .rules.rules_request_builder import RulesRequestBuilder

class WafRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /shield/waf
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new WafRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/shield/waf", path_parameters)
    
    @property
    def custom_rule(self) -> CustomRuleRequestBuilder:
        """
        The customRule property
        """
        from .custom_rule.custom_rule_request_builder import CustomRuleRequestBuilder

        return CustomRuleRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def custom_rules(self) -> CustomRulesRequestBuilder:
        """
        The customRules property
        """
        from .custom_rules.custom_rules_request_builder import CustomRulesRequestBuilder

        return CustomRulesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def engine_config(self) -> EngineConfigRequestBuilder:
        """
        The engineConfig property
        """
        from .engine_config.engine_config_request_builder import EngineConfigRequestBuilder

        return EngineConfigRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def enums(self) -> EnumsRequestBuilder:
        """
        The enums property
        """
        from .enums.enums_request_builder import EnumsRequestBuilder

        return EnumsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def profiles(self) -> ProfilesRequestBuilder:
        """
        The profiles property
        """
        from .profiles.profiles_request_builder import ProfilesRequestBuilder

        return ProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rules(self) -> RulesRequestBuilder:
        """
        The rules property
        """
        from .rules.rules_request_builder import RulesRequestBuilder

        return RulesRequestBuilder(self.request_adapter, self.path_parameters)
    

