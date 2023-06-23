# coding: utf-8

"""
    Gotyai API v3

    Gotyai API : the Spartan explainable AI   # noqa: E501

    OpenAPI spec version: 3.0.2
    Contact: contact@namsor.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import gotyai_client
from gotyai_client.api.admin_api import AdminApi  # noqa: E501
from gotyai_client.rest import ApiException


class TestAdminApi(unittest.TestCase):
    """AdminApi unit test stubs"""

    def setUp(self):
        self.api = gotyai_client.api.admin_api.AdminApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_abuse_name_patterns(self):
        """Test case for abuse_name_patterns

        List blacklist name pattern.  # noqa: E501
        """
        pass

    def test_add_credits(self):
        """Test case for add_credits

        Add usage credits to an API Key.  # noqa: E501
        """
        pass

    def test_api_key_info(self):
        """Test case for api_key_info

        Read API Key info.  # noqa: E501
        """
        pass

    def test_api_usage(self):
        """Test case for api_usage

        Print current API usage.  # noqa: E501
        """
        pass

    def test_api_usage_history(self):
        """Test case for api_usage_history

        Print historical API usage.  # noqa: E501
        """
        pass

    def test_api_usage_history_aggregate(self):
        """Test case for api_usage_history_aggregate

        Print historical API usage (in an aggregated view, by service, by day/hour/min).  # noqa: E501
        """
        pass

    def test_available_plans(self):
        """Test case for available_plans

        List all available plans in the default currency (usd).  # noqa: E501
        """
        pass

    def test_available_plans1(self):
        """Test case for available_plans1

        List all available plans in the user's preferred currency.  # noqa: E501
        """
        pass

    def test_billing_currencies(self):
        """Test case for billing_currencies

        List possible currency options for billing (USD, EUR, GBP, ...)  # noqa: E501
        """
        pass

    def test_billing_history(self):
        """Test case for billing_history

        Read the history billing information (invoices paid via Stripe or manually).  # noqa: E501
        """
        pass

    def test_billing_info(self):
        """Test case for billing_info

        Read the billing information (company name, address, phone, vat ID)  # noqa: E501
        """
        pass

    def test_charge_new(self):
        """Test case for charge_new

        Create a Stripe Customer V2, based on a payment card token (from secure StripeJS) and email.  # noqa: E501
        """
        pass

    def test_corporate_key(self):
        """Test case for corporate_key

        Setting an API Key to a corporate status.  # noqa: E501
        """
        pass

    def test_count_spam_non_spam(self):
        """Test case for count_spam_non_spam

        Get email spam statistics over custom duration.  # noqa: E501
        """
        pass

    def test_count_spam_non_spam1(self):
        """Test case for count_spam_non_spam1

        Email spam statistics.  # noqa: E501
        """
        pass

    def test_debug_level(self):
        """Test case for debug_level

        Update debug level for a classifier  # noqa: E501
        """
        pass

    def test_disable(self):
        """Test case for disable

        Activate/deactivate an API Key.  # noqa: E501
        """
        pass

    def test_email_blacklist_pattern_add(self):
        """Test case for email_blacklist_pattern_add

        Add blacklist email pattern.  # noqa: E501
        """
        pass

    def test_email_blacklist_pattern_remove(self):
        """Test case for email_blacklist_pattern_remove

        Remove blacklist email pattern.  # noqa: E501
        """
        pass

    def test_email_blacklist_patterns(self):
        """Test case for email_blacklist_patterns

        List all blacklist email patterns.  # noqa: E501
        """
        pass

    def test_explainability(self):
        """Test case for explainability

        Activate/deactivate explainability for a source.  # noqa: E501
        """
        pass

    def test_flush(self):
        """Test case for flush

        Flush counters.  # noqa: E501
        """
        pass

    def test_gotya_counter(self):
        """Test case for gotya_counter

        Get the overall API counter  # noqa: E501
        """
        pass

    def test_invalidate_cache(self):
        """Test case for invalidate_cache

        Invalidate system caches.  # noqa: E501
        """
        pass

    def test_ip_addresses_blacklist_candidates(self):
        """Test case for ip_addresses_blacklist_candidates

        List IP blacklist candidates.  # noqa: E501
        """
        pass

    def test_name_blacklist_pattern_add(self):
        """Test case for name_blacklist_pattern_add

        Add blacklist name pattern.  # noqa: E501
        """
        pass

    def test_name_blacklist_pattern_remove(self):
        """Test case for name_blacklist_pattern_remove

        Remove blacklist name pattern.  # noqa: E501
        """
        pass

    def test_payment_info(self):
        """Test case for payment_info

        Get the Stripe payment information associated with the current google auth session token.  # noqa: E501
        """
        pass

    def test_procure_key(self):
        """Test case for procure_key

        Procure an API Key (sent via Email), based on an auth token and a recaptcha. Keep your API Key secret.  # noqa: E501
        """
        pass

    def test_procure_key1(self):
        """Test case for procure_key1

        [compatibility] Retrieve the user's API Key, based on an auth token. Keep your API Key secret.  # noqa: E501
        """
        pass

    def test_remove_payment(self):
        """Test case for remove_payment

        Remove Stripe card associated with the current google auth session token.  # noqa: E501
        """
        pass

    def test_remove_user_account(self):
        """Test case for remove_user_account

        Remove the user account.  # noqa: E501
        """
        pass

    def test_remove_user_account_on_behalf(self):
        """Test case for remove_user_account_on_behalf

        Remove (on behalf) a user account.  # noqa: E501
        """
        pass

    def test_resend_key(self):
        """Test case for resend_key

        Resend an API Key (sent via Email), based on an auth token and a recaptcha as well as verification link. Keep your API Key secret.  # noqa: E501
        """
        pass

    def test_retrieve_key(self):
        """Test case for retrieve_key

        Retrieve the user's API Key, based on an auth token. Keep your API Key secret.  # noqa: E501
        """
        pass

    def test_shutdown(self):
        """Test case for shutdown

        Stop learning and shutdown system.  # noqa: E501
        """
        pass

    def test_signups(self):
        """Test case for signups

        List userID signups by IP address.  # noqa: E501
        """
        pass

    def test_software_version(self):
        """Test case for software_version

        Get the current software version  # noqa: E501
        """
        pass

    def test_spamsurge(self):
        """Test case for spamsurge

        Activate/deactivate blocking of disposable emails in case of spam surge.  # noqa: E501
        """
        pass

    def test_stats(self):
        """Test case for stats

        Print basic system statistics.  # noqa: E501
        """
        pass

    def test_subscribe_plan(self):
        """Test case for subscribe_plan

        Subscribe to a give API plan, using the user's preferred or default currency.  # noqa: E501
        """
        pass

    def test_subscribe_plan_on_behalf(self):
        """Test case for subscribe_plan_on_behalf

        Subscribe to a give API plan, using the user's preferred or default currency (admin only).  # noqa: E501
        """
        pass

    def test_switch_default_api_key_active(self):
        """Test case for switch_default_api_key_active

        Switch defaullt API Key as blocked (need email verif) or active.  # noqa: E501
        """
        pass

    def test_update_billing_info(self):
        """Test case for update_billing_info

        Sets or update the billing information (company name, address, phone, vat ID)  # noqa: E501
        """
        pass

    def test_update_limit(self):
        """Test case for update_limit

        Modifies the hard/soft limit on the API plan's overages (default is 0$ soft limit).  # noqa: E501
        """
        pass

    def test_update_payment_default(self):
        """Test case for update_payment_default

        Update the default Stripe card associated with the current google auth session token.  # noqa: E501
        """
        pass

    def test_update_user_info(self):
        """Test case for update_user_info

        Sets or update the user email and name information  # noqa: E501
        """
        pass

    def test_user_info(self):
        """Test case for user_info

        Get the user profile associated with the current google auth session token.  # noqa: E501
        """
        pass

    def test_verify_email(self):
        """Test case for verify_email

        Verifies an email, based on token sent to that email  # noqa: E501
        """
        pass

    def test_verify_remove_email(self):
        """Test case for verify_remove_email

        Verifies an email, based on token sent to that email  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()