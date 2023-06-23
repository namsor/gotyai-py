# gotyai_client.ClassifyApi

All URIs are relative to *http://ns3044521.ip-91-121-222.eu:8080/gotyai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**explain_many**](ClassifyApi.md#explain_many) | **POST** /api2/json/explainMany/{classifierUuid} | Predict a category given the subjet&#39;s features, with explainability.
[**explain_one**](ClassifyApi.md#explain_one) | **POST** /api2/json/explainOne/{classifierUuid} | Predict a category given the subjet&#39;s features, with explainability.
[**fit_many**](ClassifyApi.md#fit_many) | **POST** /api2/json/fitMany/{classifierUuid} | Fit multiple rows in the training sample (up to 100)
[**fit_one**](ClassifyApi.md#fit_one) | **POST** /api2/json/fitOne/{classifierUuid} | Fit one row in the training sample.
[**multinomial**](ClassifyApi.md#multinomial) | **GET** /api2/json/multinomial/{classifierName} | Get the multinomila classifier by its name.
[**multinomial1**](ClassifyApi.md#multinomial1) | **GET** /api2/json/multinomial | Get all the multinomila classifiers.
[**multinomial_create**](ClassifyApi.md#multinomial_create) | **POST** /api2/json/multinomialCreate | Create a multinomial classiifer
[**predict_many**](ClassifyApi.md#predict_many) | **POST** /api2/json/predictMany/{classifierUuid} | Predict a category given the subjecct&#39;s features, for up to 100 rows at a time.
[**predict_one**](ClassifyApi.md#predict_one) | **POST** /api2/json/predictOne/{classifierUuid} | Predict a category given the subjet&#39;s features


# **explain_many**
> BatchPredictOut explain_many(classifier_uuid, batch_predict_in=batch_predict_in)

Predict a category given the subjet's features, with explainability.

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
api_instance = gotyai_client.ClassifyApi(gotyai_client.ApiClient(configuration))
classifier_uuid = 'classifier_uuid_example' # str | 
batch_predict_in = gotyai_client.BatchPredictIn() # BatchPredictIn | The features. (optional)

try:
    # Predict a category given the subjet's features, with explainability.
    api_response = api_instance.explain_many(classifier_uuid, batch_predict_in=batch_predict_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassifyApi->explain_many: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classifier_uuid** | **str**|  | 
 **batch_predict_in** | [**BatchPredictIn**](BatchPredictIn.md)| The features. | [optional] 

### Return type

[**BatchPredictOut**](BatchPredictOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **explain_one**
> PredictOut explain_one(classifier_uuid, predict_in=predict_in)

Predict a category given the subjet's features, with explainability.

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
api_instance = gotyai_client.ClassifyApi(gotyai_client.ApiClient(configuration))
classifier_uuid = 'classifier_uuid_example' # str | 
predict_in = gotyai_client.PredictIn() # PredictIn | The features. (optional)

try:
    # Predict a category given the subjet's features, with explainability.
    api_response = api_instance.explain_one(classifier_uuid, predict_in=predict_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassifyApi->explain_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classifier_uuid** | **str**|  | 
 **predict_in** | [**PredictIn**](PredictIn.md)| The features. | [optional] 

### Return type

[**PredictOut**](PredictOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fit_many**
> fit_many(classifier_uuid, batch_fit_in=batch_fit_in)

Fit multiple rows in the training sample (up to 100)

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
api_instance = gotyai_client.ClassifyApi(gotyai_client.ApiClient(configuration))
classifier_uuid = 'classifier_uuid_example' # str | 
batch_fit_in = gotyai_client.BatchFitIn() # BatchFitIn | A list of feature/values and target class value. (optional)

try:
    # Fit multiple rows in the training sample (up to 100)
    api_instance.fit_many(classifier_uuid, batch_fit_in=batch_fit_in)
except ApiException as e:
    print("Exception when calling ClassifyApi->fit_many: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classifier_uuid** | **str**|  | 
 **batch_fit_in** | [**BatchFitIn**](BatchFitIn.md)| A list of feature/values and target class value. | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fit_one**
> fit_one(classifier_uuid, fit_in=fit_in)

Fit one row in the training sample.

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
api_instance = gotyai_client.ClassifyApi(gotyai_client.ApiClient(configuration))
classifier_uuid = 'classifier_uuid_example' # str | 
fit_in = gotyai_client.FitIn() # FitIn | A list of feature/values and target class value. (optional)

try:
    # Fit one row in the training sample.
    api_instance.fit_one(classifier_uuid, fit_in=fit_in)
except ApiException as e:
    print("Exception when calling ClassifyApi->fit_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classifier_uuid** | **str**|  | 
 **fit_in** | [**FitIn**](FitIn.md)| A list of feature/values and target class value. | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **multinomial**
> ClassifierOut multinomial(classifier_name)

Get the multinomila classifier by its name.

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
api_instance = gotyai_client.ClassifyApi(gotyai_client.ApiClient(configuration))
classifier_name = 'classifier_name_example' # str | 

try:
    # Get the multinomila classifier by its name.
    api_response = api_instance.multinomial(classifier_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassifyApi->multinomial: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classifier_name** | **str**|  | 

### Return type

[**ClassifierOut**](ClassifierOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **multinomial1**
> ClassifierOut multinomial1()

Get all the multinomila classifiers.

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
api_instance = gotyai_client.ClassifyApi(gotyai_client.ApiClient(configuration))

try:
    # Get all the multinomila classifiers.
    api_response = api_instance.multinomial1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassifyApi->multinomial1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClassifierOut**](ClassifierOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **multinomial_create**
> ClassifierOut multinomial_create(classifier_spec_in=classifier_spec_in)

Create a multinomial classiifer

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
api_instance = gotyai_client.ClassifyApi(gotyai_client.ApiClient(configuration))
classifier_spec_in = gotyai_client.ClassifierSpecIn() # ClassifierSpecIn | The classifier name and list of categories. (optional)

try:
    # Create a multinomial classiifer
    api_response = api_instance.multinomial_create(classifier_spec_in=classifier_spec_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassifyApi->multinomial_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classifier_spec_in** | [**ClassifierSpecIn**](ClassifierSpecIn.md)| The classifier name and list of categories. | [optional] 

### Return type

[**ClassifierOut**](ClassifierOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **predict_many**
> BatchPredictOut predict_many(classifier_uuid, batch_predict_in=batch_predict_in)

Predict a category given the subjecct's features, for up to 100 rows at a time.

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
api_instance = gotyai_client.ClassifyApi(gotyai_client.ApiClient(configuration))
classifier_uuid = 'classifier_uuid_example' # str | 
batch_predict_in = gotyai_client.BatchPredictIn() # BatchPredictIn | The features. (optional)

try:
    # Predict a category given the subjecct's features, for up to 100 rows at a time.
    api_response = api_instance.predict_many(classifier_uuid, batch_predict_in=batch_predict_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassifyApi->predict_many: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classifier_uuid** | **str**|  | 
 **batch_predict_in** | [**BatchPredictIn**](BatchPredictIn.md)| The features. | [optional] 

### Return type

[**BatchPredictOut**](BatchPredictOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **predict_one**
> PredictOut predict_one(classifier_uuid, predict_in=predict_in)

Predict a category given the subjet's features

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
api_instance = gotyai_client.ClassifyApi(gotyai_client.ApiClient(configuration))
classifier_uuid = 'classifier_uuid_example' # str | 
predict_in = gotyai_client.PredictIn() # PredictIn | The features. (optional)

try:
    # Predict a category given the subjet's features
    api_response = api_instance.predict_one(classifier_uuid, predict_in=predict_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassifyApi->predict_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classifier_uuid** | **str**|  | 
 **predict_in** | [**PredictIn**](PredictIn.md)| The features. | [optional] 

### Return type

[**PredictOut**](PredictOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

