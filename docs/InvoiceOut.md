# InvoiceOut

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**list[InvoiceItemOut]**](InvoiceItemOut.md) | The invoice items | [optional] 
**user_id** | **str** | The user id. | [optional] 
**invoice_id** | **str** | The invoice ID. | [optional] 
**is_striped** | **bool** | If user is striped. | [optional] 
**stripe_customer_id** | **str** | The Stripe customer ID. | [optional] 
**amount_due** | **int** | The total amount due. | [optional] 
**amount_paid** | **int** | The total amount paid. | [optional] 
**amount_remaining** | **int** | The total amount remaining. | [optional] 
**attempted** | **bool** | The payment was attempted. | [optional] 
**currency** | **str** | The currency. | [optional] 
**invoice_date** | **datetime** | The invoice date. | [optional] 
**due_date** | **datetime** | The invoice due date. | [optional] 
**description** | **str** | The invoice description. | [optional] 
**invoice_pdf** | **str** | The link to the invoice PDF. | [optional] 
**period_start** | **datetime** | The API plan period start date. | [optional] 
**period_end** | **datetime** | The API plan period end date. | [optional] 
**receipt_number** | **str** | The payment receipt number. | [optional] 
**invoice_status** | **str** | The invoice status. | [optional] 
**sub_total** | **int** | The invoice subtotal before tax. | [optional] 
**tax** | **int** | The invoice tax amount. | [optional] 
**tax_percent** | **int** | The invoice tax percentage. | [optional] 
**total** | **int** | The invoice total amount. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


