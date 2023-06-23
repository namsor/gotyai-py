# gotyai_client.AdminApi

All URIs are relative to *http://ns3044521.ip-91-121-222.eu:8080/gotyai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abuse_name_patterns**](AdminApi.md#abuse_name_patterns) | **GET** /api2/json/nameBlacklistPatterns | List blacklist name pattern.
[**add_credits**](AdminApi.md#add_credits) | **GET** /api2/json/addCredits/{apiKey}/{usageCredits}/{userMessage} | Add usage credits to an API Key.
[**api_key_info**](AdminApi.md#api_key_info) | **GET** /api2/json/apiKeyInfo | Read API Key info.
[**api_usage**](AdminApi.md#api_usage) | **GET** /api2/json/apiUsage | Print current API usage.
[**api_usage_history**](AdminApi.md#api_usage_history) | **GET** /api2/json/apiUsageHistory | Print historical API usage.
[**api_usage_history_aggregate**](AdminApi.md#api_usage_history_aggregate) | **GET** /api2/json/apiUsageHistoryAggregate | Print historical API usage (in an aggregated view, by service, by day/hour/min).
[**available_plans**](AdminApi.md#available_plans) | **GET** /api2/json/availablePlans | List all available plans in the default currency (usd).
[**available_plans1**](AdminApi.md#available_plans1) | **GET** /api2/json/availablePlans/{token} | List all available plans in the user&#39;s preferred currency.
[**billing_currencies**](AdminApi.md#billing_currencies) | **GET** /api2/json/billingCurrencies | List possible currency options for billing (USD, EUR, GBP, ...)
[**billing_history**](AdminApi.md#billing_history) | **GET** /api2/json/billingHistory/{token} | Read the history billing information (invoices paid via Stripe or manually).
[**billing_info**](AdminApi.md#billing_info) | **GET** /api2/json/billingInfo/{token} | Read the billing information (company name, address, phone, vat ID)
[**charge_new**](AdminApi.md#charge_new) | **GET** /api2/json/chargeNew/{stripeToken}/{stripeEmail} | Create a Stripe Customer V2, based on a payment card token (from secure StripeJS) and email.
[**corporate_key**](AdminApi.md#corporate_key) | **GET** /api2/json/corporateKey/{apiKey}/{corporate} | Setting an API Key to a corporate status.
[**count_spam_non_spam**](AdminApi.md#count_spam_non_spam) | **GET** /api2/json/countSpamNonSpam/{durationMillis} | Get email spam statistics over custom duration.
[**count_spam_non_spam1**](AdminApi.md#count_spam_non_spam1) | **GET** /api2/json/countSpamNonSpam | Email spam statistics.
[**debug_level**](AdminApi.md#debug_level) | **GET** /api2/json/debugLevel/{logger}/{level} | Update debug level for a classifier
[**disable**](AdminApi.md#disable) | **GET** /api2/json/disable/{source}/{disabled} | Activate/deactivate an API Key.
[**email_blacklist_pattern_add**](AdminApi.md#email_blacklist_pattern_add) | **GET** /api2/json/emailBlacklistPatternAdd/{pattern} | Add blacklist email pattern.
[**email_blacklist_pattern_remove**](AdminApi.md#email_blacklist_pattern_remove) | **GET** /api2/json/emailBlacklistPatternRemove/{pattern} | Remove blacklist email pattern.
[**email_blacklist_patterns**](AdminApi.md#email_blacklist_patterns) | **GET** /api2/json/emailBlacklistPatterns | List all blacklist email patterns.
[**explainability**](AdminApi.md#explainability) | **GET** /api2/json/explainability/{source}/{explainable} | Activate/deactivate explainability for a source.
[**flush**](AdminApi.md#flush) | **GET** /api2/json/flush | Flush counters.
[**gotya_counter**](AdminApi.md#gotya_counter) | **GET** /api2/json/namsorCounter | Get the overall API counter
[**invalidate_cache**](AdminApi.md#invalidate_cache) | **GET** /api2/json/invalidateCache | Invalidate system caches.
[**ip_addresses_blacklist_candidates**](AdminApi.md#ip_addresses_blacklist_candidates) | **GET** /api2/json/ipAddressesBlacklistCandidates | List IP blacklist candidates.
[**name_blacklist_pattern_add**](AdminApi.md#name_blacklist_pattern_add) | **GET** /api2/json/nameBlacklistPatternAdd/{pattern} | Add blacklist name pattern.
[**name_blacklist_pattern_remove**](AdminApi.md#name_blacklist_pattern_remove) | **GET** /api2/json/nameBlacklistPatternRemove/{pattern} | Remove blacklist name pattern.
[**payment_info**](AdminApi.md#payment_info) | **GET** /api2/json/paymentInfo/{token} | Get the Stripe payment information associated with the current google auth session token.
[**procure_key**](AdminApi.md#procure_key) | **GET** /api2/json/procureKey/{token}/{recaptchav2} | Procure an API Key (sent via Email), based on an auth token and a recaptcha. Keep your API Key secret.
[**procure_key1**](AdminApi.md#procure_key1) | **GET** /api2/json/procureKey/{token} | [compatibility] Retrieve the user&#39;s API Key, based on an auth token. Keep your API Key secret.
[**remove_payment**](AdminApi.md#remove_payment) | **GET** /api2/json/removePayment/{sourceId}/{token} | Remove Stripe card associated with the current google auth session token.
[**remove_user_account**](AdminApi.md#remove_user_account) | **GET** /api2/json/removeUserAccount/{token} | Remove the user account.
[**remove_user_account_on_behalf**](AdminApi.md#remove_user_account_on_behalf) | **GET** /api2/json/removeUserAccountOnBehalf/{apiKey} | Remove (on behalf) a user account.
[**resend_key**](AdminApi.md#resend_key) | **GET** /api2/json/resendKey/{token}/{recaptchav2} | Resend an API Key (sent via Email), based on an auth token and a recaptcha as well as verification link. Keep your API Key secret.
[**retrieve_key**](AdminApi.md#retrieve_key) | **GET** /api2/json/retrieveKey/{token} | Retrieve the user&#39;s API Key, based on an auth token. Keep your API Key secret.
[**shutdown**](AdminApi.md#shutdown) | **GET** /api2/json/shutdown | Stop learning and shutdown system.
[**signups**](AdminApi.md#signups) | **GET** /api2/json/signups/{ipAddress} | List userID signups by IP address.
[**software_version**](AdminApi.md#software_version) | **GET** /api2/json/softwareVersion | Get the current software version
[**spamsurge**](AdminApi.md#spamsurge) | **GET** /api2/json/spamsurge/{blockDisposableEmails} | Activate/deactivate blocking of disposable emails in case of spam surge.
[**stats**](AdminApi.md#stats) | **GET** /api2/json/stats | Print basic system statistics.
[**subscribe_plan**](AdminApi.md#subscribe_plan) | **GET** /api2/json/subscribePlan/{planName}/{token} | Subscribe to a give API plan, using the user&#39;s preferred or default currency.
[**subscribe_plan_on_behalf**](AdminApi.md#subscribe_plan_on_behalf) | **GET** /api2/json/subscribePlanOnBehalf/{planName}/{apiKey} | Subscribe to a give API plan, using the user&#39;s preferred or default currency (admin only).
[**switch_default_api_key_active**](AdminApi.md#switch_default_api_key_active) | **GET** /api2/json/switchDefaultAPIKeyActive/{defaultBlocked} | Switch defaullt API Key as blocked (need email verif) or active.
[**update_billing_info**](AdminApi.md#update_billing_info) | **POST** /api2/json/updateBillingInfo/{token} | Sets or update the billing information (company name, address, phone, vat ID)
[**update_limit**](AdminApi.md#update_limit) | **GET** /api2/json/updateLimit/{usageLimit}/{hardOrSoft}/{token} | Modifies the hard/soft limit on the API plan&#39;s overages (default is 0$ soft limit).
[**update_payment_default**](AdminApi.md#update_payment_default) | **GET** /api2/json/updatePaymentDefault/{defautSourceId}/{token} | Update the default Stripe card associated with the current google auth session token.
[**update_user_info**](AdminApi.md#update_user_info) | **GET** /api2/json/updateUserInfo/{email}/{displayName}/{token} | Sets or update the user email and name information
[**user_info**](AdminApi.md#user_info) | **GET** /api2/json/userInfo/{token} | Get the user profile associated with the current google auth session token.
[**verify_email**](AdminApi.md#verify_email) | **GET** /api2/json/verifyEmail/{emailToken} | Verifies an email, based on token sent to that email
[**verify_remove_email**](AdminApi.md#verify_remove_email) | **GET** /api2/json/verifyRemoveEmail/{emailToken} | Verifies an email, based on token sent to that email


# **abuse_name_patterns**
> abuse_name_patterns()

List blacklist name pattern.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))

try:
    # List blacklist name pattern.
    api_instance.abuse_name_patterns()
except ApiException as e:
    print("Exception when calling AdminApi->abuse_name_patterns: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_credits**
> APIPeriodUsageOut add_credits(api_key, usage_credits, user_message)

Add usage credits to an API Key.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))
api_key = 'api_key_example' # str | 
usage_credits = 56 # int | 
user_message = 'user_message_example' # str | 

try:
    # Add usage credits to an API Key.
    api_response = api_instance.add_credits(api_key, usage_credits, user_message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->add_credits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **usage_credits** | **int**|  | 
 **user_message** | **str**|  | 

### Return type

[**APIPeriodUsageOut**](APIPeriodUsageOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_key_info**
> APIKeyOut api_key_info()

Read API Key info.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))

try:
    # Read API Key info.
    api_response = api_instance.api_key_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->api_key_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**APIKeyOut**](APIKeyOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_usage**
> APIPeriodUsageOut api_usage()

Print current API usage.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))

try:
    # Print current API usage.
    api_response = api_instance.api_usage()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->api_usage: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**APIPeriodUsageOut**](APIPeriodUsageOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_usage_history**
> APIUsageHistoryOut api_usage_history()

Print historical API usage.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))

try:
    # Print historical API usage.
    api_response = api_instance.api_usage_history()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->api_usage_history: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**APIUsageHistoryOut**](APIUsageHistoryOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_usage_history_aggregate**
> APIUsageAggregatedOut api_usage_history_aggregate()

Print historical API usage (in an aggregated view, by service, by day/hour/min).

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))

try:
    # Print historical API usage (in an aggregated view, by service, by day/hour/min).
    api_response = api_instance.api_usage_history_aggregate()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->api_usage_history_aggregate: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**APIUsageAggregatedOut**](APIUsageAggregatedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **available_plans**
> APIPlansOut available_plans()

List all available plans in the default currency (usd).

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))

try:
    # List all available plans in the default currency (usd).
    api_response = api_instance.available_plans()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->available_plans: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**APIPlansOut**](APIPlansOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **available_plans1**
> APIPlansOut available_plans1(token)

List all available plans in the user's preferred currency.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))
token = 'token_example' # str | 

try:
    # List all available plans in the user's preferred currency.
    api_response = api_instance.available_plans1(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->available_plans1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

[**APIPlansOut**](APIPlansOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **billing_currencies**
> CurrenciesOut billing_currencies()

List possible currency options for billing (USD, EUR, GBP, ...)

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))

try:
    # List possible currency options for billing (USD, EUR, GBP, ...)
    api_response = api_instance.billing_currencies()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->billing_currencies: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CurrenciesOut**](CurrenciesOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **billing_history**
> BillingHistoryOut billing_history(token)

Read the history billing information (invoices paid via Stripe or manually).

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))
token = 'token_example' # str | 

try:
    # Read the history billing information (invoices paid via Stripe or manually).
    api_response = api_instance.billing_history(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->billing_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

[**BillingHistoryOut**](BillingHistoryOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **billing_info**
> BillingInfoInOut billing_info(token)

Read the billing information (company name, address, phone, vat ID)

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))
token = 'token_example' # str | 

try:
    # Read the billing information (company name, address, phone, vat ID)
    api_response = api_instance.billing_info(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->billing_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

[**BillingInfoInOut**](BillingInfoInOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **charge_new**
> charge_new(stripe_token, stripe_email)

Create a Stripe Customer V2, based on a payment card token (from secure StripeJS) and email.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))
stripe_token = 'stripe_token_example' # str | 
stripe_email = 'stripe_email_example' # str | 

try:
    # Create a Stripe Customer V2, based on a payment card token (from secure StripeJS) and email.
    api_instance.charge_new(stripe_token, stripe_email)
except ApiException as e:
    print("Exception when calling AdminApi->charge_new: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stripe_token** | **str**|  | 
 **stripe_email** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **corporate_key**
> corporate_key(api_key, corporate)

Setting an API Key to a corporate status.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))
api_key = 'api_key_example' # str | 
corporate = True # bool | 

try:
    # Setting an API Key to a corporate status.
    api_instance.corporate_key(api_key, corporate)
except ApiException as e:
    print("Exception when calling AdminApi->corporate_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **corporate** | **bool**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **count_spam_non_spam**
> SpamStatsOut count_spam_non_spam(duration_millis)

Get email spam statistics over custom duration.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))
duration_millis = 56 # int | 

try:
    # Get email spam statistics over custom duration.
    api_response = api_instance.count_spam_non_spam(duration_millis)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->count_spam_non_spam: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **duration_millis** | **int**|  | 

### Return type

[**SpamStatsOut**](SpamStatsOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **count_spam_non_spam1**
> SpamStatsOut count_spam_non_spam1()

Email spam statistics.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))

try:
    # Email spam statistics.
    api_response = api_instance.count_spam_non_spam1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->count_spam_non_spam1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SpamStatsOut**](SpamStatsOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug_level**
> debug_level(logger, level)

Update debug level for a classifier

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))
logger = 'logger_example' # str | 
level = 'level_example' # str | 

try:
    # Update debug level for a classifier
    api_instance.debug_level(logger, level)
except ApiException as e:
    print("Exception when calling AdminApi->debug_level: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logger** | **str**|  | 
 **level** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable**
> disable(source, disabled)

Activate/deactivate an API Key.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))
source = 'source_example' # str | The API Key to set as enabled/disabled.
disabled = True # bool | 

try:
    # Activate/deactivate an API Key.
    api_instance.disable(source, disabled)
except ApiException as e:
    print("Exception when calling AdminApi->disable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| The API Key to set as enabled/disabled. | 
 **disabled** | **bool**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_blacklist_pattern_add**
> email_blacklist_pattern_add(pattern)

Add blacklist email pattern.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))
pattern = 'pattern_example' # str | 

try:
    # Add blacklist email pattern.
    api_instance.email_blacklist_pattern_add(pattern)
except ApiException as e:
    print("Exception when calling AdminApi->email_blacklist_pattern_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pattern** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_blacklist_pattern_remove**
> email_blacklist_pattern_remove(pattern)

Remove blacklist email pattern.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))
pattern = 'pattern_example' # str | 

try:
    # Remove blacklist email pattern.
    api_instance.email_blacklist_pattern_remove(pattern)
except ApiException as e:
    print("Exception when calling AdminApi->email_blacklist_pattern_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pattern** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_blacklist_patterns**
> email_blacklist_patterns()

List all blacklist email patterns.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))

try:
    # List all blacklist email patterns.
    api_instance.email_blacklist_patterns()
except ApiException as e:
    print("Exception when calling AdminApi->email_blacklist_patterns: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **explainability**
> explainability(source, explainable)

Activate/deactivate explainability for a source.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))
source = 'source_example' # str | 
explainable = True # bool | 

try:
    # Activate/deactivate explainability for a source.
    api_instance.explainability(source, explainable)
except ApiException as e:
    print("Exception when calling AdminApi->explainability: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**|  | 
 **explainable** | **bool**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flush**
> flush()

Flush counters.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))

try:
    # Flush counters.
    api_instance.flush()
except ApiException as e:
    print("Exception when calling AdminApi->flush: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gotya_counter**
> GotyaCounterOut gotya_counter()

Get the overall API counter

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))

try:
    # Get the overall API counter
    api_response = api_instance.gotya_counter()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->gotya_counter: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GotyaCounterOut**](GotyaCounterOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invalidate_cache**
> invalidate_cache()

Invalidate system caches.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))

try:
    # Invalidate system caches.
    api_instance.invalidate_cache()
except ApiException as e:
    print("Exception when calling AdminApi->invalidate_cache: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_addresses_blacklist_candidates**
> ip_addresses_blacklist_candidates()

List IP blacklist candidates.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))

try:
    # List IP blacklist candidates.
    api_instance.ip_addresses_blacklist_candidates()
except ApiException as e:
    print("Exception when calling AdminApi->ip_addresses_blacklist_candidates: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **name_blacklist_pattern_add**
> name_blacklist_pattern_add(pattern)

Add blacklist name pattern.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))
pattern = 'pattern_example' # str | 

try:
    # Add blacklist name pattern.
    api_instance.name_blacklist_pattern_add(pattern)
except ApiException as e:
    print("Exception when calling AdminApi->name_blacklist_pattern_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pattern** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **name_blacklist_pattern_remove**
> name_blacklist_pattern_remove(pattern)

Remove blacklist name pattern.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))
pattern = 'pattern_example' # str | 

try:
    # Remove blacklist name pattern.
    api_instance.name_blacklist_pattern_remove(pattern)
except ApiException as e:
    print("Exception when calling AdminApi->name_blacklist_pattern_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pattern** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_info**
> StripeCustomerOut payment_info(token)

Get the Stripe payment information associated with the current google auth session token.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))
token = 'token_example' # str | 

try:
    # Get the Stripe payment information associated with the current google auth session token.
    api_response = api_instance.payment_info(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->payment_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

[**StripeCustomerOut**](StripeCustomerOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **procure_key**
> APIKeyOut procure_key(token, recaptchav2)

Procure an API Key (sent via Email), based on an auth token and a recaptcha. Keep your API Key secret.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))
token = 'token_example' # str | 
recaptchav2 = 'recaptchav2_example' # str | 

try:
    # Procure an API Key (sent via Email), based on an auth token and a recaptcha. Keep your API Key secret.
    api_response = api_instance.procure_key(token, recaptchav2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->procure_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **recaptchav2** | **str**|  | 

### Return type

[**APIKeyOut**](APIKeyOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **procure_key1**
> APIKeyOut procure_key1(token)

[compatibility] Retrieve the user's API Key, based on an auth token. Keep your API Key secret.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))
token = 'token_example' # str | 

try:
    # [compatibility] Retrieve the user's API Key, based on an auth token. Keep your API Key secret.
    api_response = api_instance.procure_key1(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->procure_key1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

[**APIKeyOut**](APIKeyOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_payment**
> StripeCustomerOut remove_payment(source_id, token)

Remove Stripe card associated with the current google auth session token.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))
source_id = 'source_id_example' # str | 
token = 'token_example' # str | 

try:
    # Remove Stripe card associated with the current google auth session token.
    api_response = api_instance.remove_payment(source_id, token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->remove_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**|  | 
 **token** | **str**|  | 

### Return type

[**StripeCustomerOut**](StripeCustomerOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_account**
> APIPlanSubscriptionOut remove_user_account(token)

Remove the user account.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))
token = 'token_example' # str | 

try:
    # Remove the user account.
    api_response = api_instance.remove_user_account(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->remove_user_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

[**APIPlanSubscriptionOut**](APIPlanSubscriptionOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_account_on_behalf**
> APIPlanSubscriptionOut remove_user_account_on_behalf(api_key)

Remove (on behalf) a user account.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))
api_key = 'api_key_example' # str | 

try:
    # Remove (on behalf) a user account.
    api_response = api_instance.remove_user_account_on_behalf(api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->remove_user_account_on_behalf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 

### Return type

[**APIPlanSubscriptionOut**](APIPlanSubscriptionOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_key**
> APIKeyOut resend_key(token, recaptchav2)

Resend an API Key (sent via Email), based on an auth token and a recaptcha as well as verification link. Keep your API Key secret.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))
token = 'token_example' # str | 
recaptchav2 = 'recaptchav2_example' # str | 

try:
    # Resend an API Key (sent via Email), based on an auth token and a recaptcha as well as verification link. Keep your API Key secret.
    api_response = api_instance.resend_key(token, recaptchav2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->resend_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **recaptchav2** | **str**|  | 

### Return type

[**APIKeyOut**](APIKeyOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_key**
> APIKeyOut retrieve_key(token)

Retrieve the user's API Key, based on an auth token. Keep your API Key secret.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))
token = 'token_example' # str | 

try:
    # Retrieve the user's API Key, based on an auth token. Keep your API Key secret.
    api_response = api_instance.retrieve_key(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->retrieve_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

[**APIKeyOut**](APIKeyOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shutdown**
> shutdown()

Stop learning and shutdown system.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))

try:
    # Stop learning and shutdown system.
    api_instance.shutdown()
except ApiException as e:
    print("Exception when calling AdminApi->shutdown: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signups**
> signups(ip_address)

List userID signups by IP address.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))
ip_address = 'ip_address_example' # str | 

try:
    # List userID signups by IP address.
    api_instance.signups(ip_address)
except ApiException as e:
    print("Exception when calling AdminApi->signups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_address** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_version**
> SoftwareVersionOut software_version()

Get the current software version

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))

try:
    # Get the current software version
    api_response = api_instance.software_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->software_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SoftwareVersionOut**](SoftwareVersionOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spamsurge**
> spamsurge(block_disposable_emails)

Activate/deactivate blocking of disposable emails in case of spam surge.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))
block_disposable_emails = True # bool | 

try:
    # Activate/deactivate blocking of disposable emails in case of spam surge.
    api_instance.spamsurge(block_disposable_emails)
except ApiException as e:
    print("Exception when calling AdminApi->spamsurge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_disposable_emails** | **bool**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stats**
> SystemMetricsOut stats()

Print basic system statistics.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))

try:
    # Print basic system statistics.
    api_response = api_instance.stats()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->stats: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemMetricsOut**](SystemMetricsOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe_plan**
> APIPlanSubscriptionOut subscribe_plan(plan_name, token)

Subscribe to a give API plan, using the user's preferred or default currency.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))
plan_name = 'plan_name_example' # str | 
token = 'token_example' # str | 

try:
    # Subscribe to a give API plan, using the user's preferred or default currency.
    api_response = api_instance.subscribe_plan(plan_name, token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->subscribe_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_name** | **str**|  | 
 **token** | **str**|  | 

### Return type

[**APIPlanSubscriptionOut**](APIPlanSubscriptionOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe_plan_on_behalf**
> APIPlanSubscriptionOut subscribe_plan_on_behalf(plan_name, api_key)

Subscribe to a give API plan, using the user's preferred or default currency (admin only).

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))
plan_name = 'plan_name_example' # str | 
api_key = 'api_key_example' # str | 

try:
    # Subscribe to a give API plan, using the user's preferred or default currency (admin only).
    api_response = api_instance.subscribe_plan_on_behalf(plan_name, api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->subscribe_plan_on_behalf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_name** | **str**|  | 
 **api_key** | **str**|  | 

### Return type

[**APIPlanSubscriptionOut**](APIPlanSubscriptionOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **switch_default_api_key_active**
> switch_default_api_key_active(default_blocked)

Switch defaullt API Key as blocked (need email verif) or active.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))
default_blocked = True # bool | 

try:
    # Switch defaullt API Key as blocked (need email verif) or active.
    api_instance.switch_default_api_key_active(default_blocked)
except ApiException as e:
    print("Exception when calling AdminApi->switch_default_api_key_active: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **default_blocked** | **bool**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_billing_info**
> BillingInfoInOut update_billing_info(token, billing_info_in_out=billing_info_in_out)

Sets or update the billing information (company name, address, phone, vat ID)

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))
token = 'token_example' # str | 
billing_info_in_out = gotyai_client.BillingInfoInOut() # BillingInfoInOut |  (optional)

try:
    # Sets or update the billing information (company name, address, phone, vat ID)
    api_response = api_instance.update_billing_info(token, billing_info_in_out=billing_info_in_out)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->update_billing_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **billing_info_in_out** | [**BillingInfoInOut**](BillingInfoInOut.md)|  | [optional] 

### Return type

[**BillingInfoInOut**](BillingInfoInOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_limit**
> APIPeriodUsageOut update_limit(usage_limit, hard_or_soft, token)

Modifies the hard/soft limit on the API plan's overages (default is 0$ soft limit).

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))
usage_limit = 56 # int | 
hard_or_soft = True # bool | 
token = 'token_example' # str | 

try:
    # Modifies the hard/soft limit on the API plan's overages (default is 0$ soft limit).
    api_response = api_instance.update_limit(usage_limit, hard_or_soft, token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->update_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usage_limit** | **int**|  | 
 **hard_or_soft** | **bool**|  | 
 **token** | **str**|  | 

### Return type

[**APIPeriodUsageOut**](APIPeriodUsageOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payment_default**
> StripeCustomerOut update_payment_default(defaut_source_id, token)

Update the default Stripe card associated with the current google auth session token.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))
defaut_source_id = 'defaut_source_id_example' # str | 
token = 'token_example' # str | 

try:
    # Update the default Stripe card associated with the current google auth session token.
    api_response = api_instance.update_payment_default(defaut_source_id, token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->update_payment_default: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **defaut_source_id** | **str**|  | 
 **token** | **str**|  | 

### Return type

[**StripeCustomerOut**](StripeCustomerOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_info**
> UserInfoOut update_user_info(email, display_name, token)

Sets or update the user email and name information

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))
email = 'email_example' # str | 
display_name = 'display_name_example' # str | 
token = 'token_example' # str | 

try:
    # Sets or update the user email and name information
    api_response = api_instance.update_user_info(email, display_name, token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->update_user_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **display_name** | **str**|  | 
 **token** | **str**|  | 

### Return type

[**UserInfoOut**](UserInfoOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_info**
> UserInfoOut user_info(token)

Get the user profile associated with the current google auth session token.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))
token = 'token_example' # str | 

try:
    # Get the user profile associated with the current google auth session token.
    api_response = api_instance.user_info(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->user_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

[**UserInfoOut**](UserInfoOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_email**
> verify_email(email_token)

Verifies an email, based on token sent to that email

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))
email_token = 'email_token_example' # str | 

try:
    # Verifies an email, based on token sent to that email
    api_instance.verify_email(email_token)
except ApiException as e:
    print("Exception when calling AdminApi->verify_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_token** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_remove_email**
> verify_remove_email(email_token)

Verifies an email, based on token sent to that email

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gotyai_client
from gotyai_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gotyai_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gotyai_client.AdminApi(gotyai_client.ApiClient(configuration))
email_token = 'email_token_example' # str | 

try:
    # Verifies an email, based on token sent to that email
    api_instance.verify_remove_email(email_token)
except ApiException as e:
    print("Exception when calling AdminApi->verify_remove_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_token** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

