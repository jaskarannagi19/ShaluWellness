from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('payment',views.payment,name='payment'),
    path('charge',views.charge,name='charge'),
    path('thank-you',views.thankyou,name='thankyou'),
    path('send_mail/',views.send_email,name='send_mail')
]

