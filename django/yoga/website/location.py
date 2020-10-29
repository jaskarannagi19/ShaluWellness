from square.client import Client

# Create an instance of the API Client
# and initialize it with the credentials
# for the Square account whose assets you want to manage

client = Client(
    access_token='EAAAEL9Ne4RXFPJBh_SvhmkC80bW2n6F2izDRDSyMYeGJ3H4DCG_YPkfUPFIQQkT',
    environment='sandbox',
)


body = {}
body['source_id'] = 'ccof:uIbfJXhXETSP197M3GB'
body['idempotency_key'] = '4935a656-a929-4792-b97c-8848be85c27c'
body['amount_money'] = {}
body['amount_money']['amount'] = 200
body['amount_money']['currency'] = 'USD'
body['tip_money'] = {}
body['tip_money']['amount'] = 198
body['tip_money']['currency'] = 'USD'
body['app_fee_money'] = {}
body['app_fee_money']['amount'] = 10
body['app_fee_money']['currency'] = 'USD'
#body['delay_duration'] = 'delay_duration6'
body['autocomplete'] = False
body['order_id'] = '123'
body['customer_id'] = 'VDKXEEKPJN48QDG3BGGFAK05P8'
body['location_id'] = 'L966W4YHYGNWP'
body['reference_id'] = '123456'
body['note'] = 'Brief description'

payments_api = client.payments

result = payments_api.create_payment(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)