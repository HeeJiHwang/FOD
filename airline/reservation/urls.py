from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.reservation),
    path('selectflight/', views.selectflight),
    path('selectflight2/', views.selectflight2),
    path('ow_selectflight/', views.ow_selectflight),
    path('transaction/', views.transaction),
    path('ow_transaction/', views.ow_transaction),
    path('paymentpage/', views.paymentpage),
    path('ow_paymentpage/', views.ow_paymentpage),
    path('inquiry/', views.inquiry),
]