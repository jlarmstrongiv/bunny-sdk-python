from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class User(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The Id of the user
    account_id: Optional[str] = None
    # The remaining balance on the user's account
    balance: Optional[float] = None
    # The email where the invoices and billing messages will be sent
    billing_email: Optional[str] = None
    # The end date of the account's free trial. If this is in the past, the free trial has expired.
    billing_free_until_date: Optional[datetime.datetime] = None
    # The BillingType property
    billing_type: Optional[float] = None
    # The city of the user
    city: Optional[str] = None
    # The country name that the user is from
    company_name: Optional[str] = None
    # The Alpha2 country code that the user is from
    country: Optional[str] = None
    # The date when the user joined bunny.net
    date_joined: Optional[datetime.datetime] = None
    # Determines if the DPA was accepted by the user or not
    dpa_accepted: Optional[bool] = None
    # Determines the date on which the DPA was accepted
    dpa_date_accepted: Optional[datetime.datetime] = None
    # Determines which version of the DPA was accepted
    dpa_version_accepted: Optional[int] = None
    # The email of the user
    email: Optional[str] = None
    # Determines if the account's email has been successfully verified
    email_verified: Optional[bool] = None
    # Contains the list of available payment types for this account
    enabled_payment_types: Optional[List[str]] = None
    # The list of features that the user has enabled
    feature_flags: Optional[List[str]] = None
    # The first name of the user
    first_name: Optional[str] = None
    # The FreeTrialExtendedDate property
    free_trial_extended_date: Optional[datetime.datetime] = None
    # The HasCompleteBillingProfile property
    has_complete_billing_profile: Optional[bool] = None
    # The Id of the user
    id: Optional[str] = None
    # Determines whether the user used a Single Sign On account
    is_sso_account: Optional[bool] = None
    # The last name of the user
    last_name: Optional[str] = None
    # Determines if the payments are disabled on this account
    payments_disabled: Optional[bool] = None
    # Determines if the account should receive notification emails from bunny.net
    receive_notification_emails: Optional[bool] = None
    # Determines if the account should receive promotional emails from bunny.net
    receive_promotional_emails: Optional[bool] = None
    # Determines the roles that the user belongs to
    roles: Optional[List[str]] = None
    # The street address of the user
    street_address: Optional[str] = None
    # Determines if the user's account is suspended
    suspended: Optional[bool] = None
    # The total bandwidth used by the account.
    total_bandwidth_used: Optional[int] = None
    # The total free trial bandwidth limit for this account
    trial_bandwidth_limit: Optional[int] = None
    # Determines if the account has 2FA enabled
    two_factor_authentication_enabled: Optional[bool] = None
    # Returns the number of unread tickets on the user's account
    unread_support_ticket_count: Optional[int] = None
    # The billing VAT number of the account
    v_a_t_number: Optional[str] = None
    # The address zip code of the user
    zip_code: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> User:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: User
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return User()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "AccountId": lambda n : setattr(self, 'account_id', n.get_str_value()),
            "Balance": lambda n : setattr(self, 'balance', n.get_float_value()),
            "BillingEmail": lambda n : setattr(self, 'billing_email', n.get_str_value()),
            "BillingFreeUntilDate": lambda n : setattr(self, 'billing_free_until_date', n.get_datetime_value()),
            "BillingType": lambda n : setattr(self, 'billing_type', n.get_float_value()),
            "City": lambda n : setattr(self, 'city', n.get_str_value()),
            "CompanyName": lambda n : setattr(self, 'company_name', n.get_str_value()),
            "Country": lambda n : setattr(self, 'country', n.get_str_value()),
            "DateJoined": lambda n : setattr(self, 'date_joined', n.get_datetime_value()),
            "DpaAccepted": lambda n : setattr(self, 'dpa_accepted', n.get_bool_value()),
            "DpaDateAccepted": lambda n : setattr(self, 'dpa_date_accepted', n.get_datetime_value()),
            "DpaVersionAccepted": lambda n : setattr(self, 'dpa_version_accepted', n.get_int_value()),
            "Email": lambda n : setattr(self, 'email', n.get_str_value()),
            "EmailVerified": lambda n : setattr(self, 'email_verified', n.get_bool_value()),
            "EnabledPaymentTypes": lambda n : setattr(self, 'enabled_payment_types', n.get_collection_of_primitive_values(str)),
            "FeatureFlags": lambda n : setattr(self, 'feature_flags', n.get_collection_of_primitive_values(str)),
            "FirstName": lambda n : setattr(self, 'first_name', n.get_str_value()),
            "FreeTrialExtendedDate": lambda n : setattr(self, 'free_trial_extended_date', n.get_datetime_value()),
            "HasCompleteBillingProfile": lambda n : setattr(self, 'has_complete_billing_profile', n.get_bool_value()),
            "Id": lambda n : setattr(self, 'id', n.get_str_value()),
            "IsSsoAccount": lambda n : setattr(self, 'is_sso_account', n.get_bool_value()),
            "LastName": lambda n : setattr(self, 'last_name', n.get_str_value()),
            "PaymentsDisabled": lambda n : setattr(self, 'payments_disabled', n.get_bool_value()),
            "ReceiveNotificationEmails": lambda n : setattr(self, 'receive_notification_emails', n.get_bool_value()),
            "ReceivePromotionalEmails": lambda n : setattr(self, 'receive_promotional_emails', n.get_bool_value()),
            "Roles": lambda n : setattr(self, 'roles', n.get_collection_of_primitive_values(str)),
            "StreetAddress": lambda n : setattr(self, 'street_address', n.get_str_value()),
            "Suspended": lambda n : setattr(self, 'suspended', n.get_bool_value()),
            "TotalBandwidthUsed": lambda n : setattr(self, 'total_bandwidth_used', n.get_int_value()),
            "TrialBandwidthLimit": lambda n : setattr(self, 'trial_bandwidth_limit', n.get_int_value()),
            "TwoFactorAuthenticationEnabled": lambda n : setattr(self, 'two_factor_authentication_enabled', n.get_bool_value()),
            "UnreadSupportTicketCount": lambda n : setattr(self, 'unread_support_ticket_count', n.get_int_value()),
            "VATNumber": lambda n : setattr(self, 'v_a_t_number', n.get_str_value()),
            "ZipCode": lambda n : setattr(self, 'zip_code', n.get_str_value()),
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
        writer.write_str_value("AccountId", self.account_id)
        writer.write_float_value("Balance", self.balance)
        writer.write_str_value("BillingEmail", self.billing_email)
        writer.write_datetime_value("BillingFreeUntilDate", self.billing_free_until_date)
        writer.write_float_value("BillingType", self.billing_type)
        writer.write_str_value("City", self.city)
        writer.write_str_value("CompanyName", self.company_name)
        writer.write_str_value("Country", self.country)
        writer.write_datetime_value("DateJoined", self.date_joined)
        writer.write_bool_value("DpaAccepted", self.dpa_accepted)
        writer.write_datetime_value("DpaDateAccepted", self.dpa_date_accepted)
        writer.write_int_value("DpaVersionAccepted", self.dpa_version_accepted)
        writer.write_str_value("Email", self.email)
        writer.write_bool_value("EmailVerified", self.email_verified)
        writer.write_collection_of_primitive_values("EnabledPaymentTypes", self.enabled_payment_types)
        writer.write_collection_of_primitive_values("FeatureFlags", self.feature_flags)
        writer.write_str_value("FirstName", self.first_name)
        writer.write_datetime_value("FreeTrialExtendedDate", self.free_trial_extended_date)
        writer.write_bool_value("HasCompleteBillingProfile", self.has_complete_billing_profile)
        writer.write_str_value("Id", self.id)
        writer.write_bool_value("IsSsoAccount", self.is_sso_account)
        writer.write_str_value("LastName", self.last_name)
        writer.write_bool_value("PaymentsDisabled", self.payments_disabled)
        writer.write_bool_value("ReceiveNotificationEmails", self.receive_notification_emails)
        writer.write_bool_value("ReceivePromotionalEmails", self.receive_promotional_emails)
        writer.write_collection_of_primitive_values("Roles", self.roles)
        writer.write_str_value("StreetAddress", self.street_address)
        writer.write_bool_value("Suspended", self.suspended)
        writer.write_int_value("TotalBandwidthUsed", self.total_bandwidth_used)
        writer.write_int_value("TrialBandwidthLimit", self.trial_bandwidth_limit)
        writer.write_bool_value("TwoFactorAuthenticationEnabled", self.two_factor_authentication_enabled)
        writer.write_int_value("UnreadSupportTicketCount", self.unread_support_ticket_count)
        writer.write_str_value("VATNumber", self.v_a_t_number)
        writer.write_str_value("ZipCode", self.zip_code)
        writer.write_additional_data_value(self.additional_data)
    

