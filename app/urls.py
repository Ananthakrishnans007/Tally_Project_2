from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index,name='Index'),


    # Statistics

    path('Statistics',views.Statistics,name='Statistics'),

    path('voucher_monthly_register/<int:id>',views.voucher_monthly_register,name='voucher_monthly_register'),

    path('voucher_register/<int:id>/<int:pk>',views.voucher_register,name='voucher_register'),

    



    path('test',views.test,name='test'),



   
    
]
