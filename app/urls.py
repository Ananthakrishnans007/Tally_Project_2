from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index,name='Index'),


    # Statistics

    path('Statistics',views.Statistics,name='Statistics'),

    path('voucher_monthly_register',views.voucher_monthly_register,name='voucher_monthly_register'),



    path('test',views.test,name='test'),



   
    
]
