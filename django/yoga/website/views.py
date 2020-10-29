from django.shortcuts import render,HttpResponse
from square.client import Client
from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse


import uuid

# Create your views here.
def index(request):
    return render(request, 'website/index.html')


def payment(request):
    return render(request,'website/payment.html')




def charge(request):

    # Create an instance of the API Client
    # and initialize it with the credentials
    # for the Square account whose assets you want to manage

    client = Client(
        access_token='EAAAEL9Ne4RXFPJBh_SvhmkC80bW2n6F2izDRDSyMYeGJ3H4DCG_YPkfUPFIQQkT',
        environment='sandbox',
    )
    nonce = request.POST['nonce']
    print(nonce)

    idempotency_key = str(uuid.uuid1())

    amount = {'amount': 100, 'currency': 'CAD'}

    body = {'idempotency_key': idempotency_key, 'source_id': nonce, 'amount_money': amount}

    api_response = client.payments.create_payment(body)
    if api_response.is_success():
        res = api_response.body['payment']

        print(res)
    elif api_response.is_error():
        res = "Exception when calling PaymentsApi->create_payment: {}".format(api_response.errors)
        print(res)

    return HttpResponse("Ok")



def send_email(request):
    print(request.POST.get('name'))

    name = request.POST.get('name')
    email = request.POST.get('email')
    subject =request.POST.get('subject')
    user_message =request.POST.get('message')

    send_mail(
        "Message from Website: "+subject,
        "Message from "+name+" with email: "+ email + "\r\n"+ user_message,
        'shaluwebsite@gmail.com',
        ['shaluwellbeing@gmail.com'],
        fail_silently=False,
    )

    return JsonResponse({'result':'OK'}) #{'mail':'Mail sent'}
