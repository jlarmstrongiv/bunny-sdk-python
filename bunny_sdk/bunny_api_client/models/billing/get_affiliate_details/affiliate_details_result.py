from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .affiliate_details_result_affiliate_clicks_chart import AffiliateDetailsResult_AffiliateClicksChart
    from .affiliate_details_result_affiliate_signups_chart import AffiliateDetailsResult_AffiliateSignupsChart

@dataclass
class AffiliateDetailsResult(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The amount of affiliate credits on the account
    affiliate_balance: Optional[float] = None
    # The constructed affiliate click history chart data
    affiliate_clicks_chart: Optional[AffiliateDetailsResult_AffiliateClicksChart] = None
    # The constructed affiliate signup history chart data
    affiliate_signups_chart: Optional[AffiliateDetailsResult_AffiliateSignupsChart] = None
    # The affiliate URL for the currently authenticated user
    affiliate_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AffiliateDetailsResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AffiliateDetailsResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AffiliateDetailsResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .affiliate_details_result_affiliate_clicks_chart import AffiliateDetailsResult_AffiliateClicksChart
        from .affiliate_details_result_affiliate_signups_chart import AffiliateDetailsResult_AffiliateSignupsChart

        from .affiliate_details_result_affiliate_clicks_chart import AffiliateDetailsResult_AffiliateClicksChart
        from .affiliate_details_result_affiliate_signups_chart import AffiliateDetailsResult_AffiliateSignupsChart

        fields: Dict[str, Callable[[Any], None]] = {
            "AffiliateBalance": lambda n : setattr(self, 'affiliate_balance', n.get_float_value()),
            "AffiliateClicksChart": lambda n : setattr(self, 'affiliate_clicks_chart', n.get_object_value(AffiliateDetailsResult_AffiliateClicksChart)),
            "AffiliateSignupsChart": lambda n : setattr(self, 'affiliate_signups_chart', n.get_object_value(AffiliateDetailsResult_AffiliateSignupsChart)),
            "AffiliateUrl": lambda n : setattr(self, 'affiliate_url', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_float_value("AffiliateBalance", self.affiliate_balance)
        writer.write_object_value("AffiliateClicksChart", self.affiliate_clicks_chart)
        writer.write_object_value("AffiliateSignupsChart", self.affiliate_signups_chart)
        writer.write_str_value("AffiliateUrl", self.affiliate_url)
        writer.write_additional_data_value(self.additional_data)
    

