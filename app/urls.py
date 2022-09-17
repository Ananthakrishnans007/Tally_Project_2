from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index,name='Index'),


    # Statistics

    path('Statistics',views.Statistics,name='Statistics'),

    path('Statistics_voucher_monthly_register/<int:id>',views.Statistics_voucher_monthly_register,name='Statistics_voucher_monthly_register'),

    path('Statistics_voucher_register/<int:id>/<int:pk>',views.Statistics_voucher_register,name='Statistics_voucher_register'),

    
    path('Statistics_voucher_Delete/<int:id>/<int:pk>/<int:de>',views.Statistics_voucher_Delete,name='Statistics_voucher_Delete'),




   
    
]
