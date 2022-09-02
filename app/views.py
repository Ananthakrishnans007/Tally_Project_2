from multiprocessing import context
from django.shortcuts import render

from . models import*

# Create your views here.


def Index(request):
    return render(request,'index.html')


# statistics    

def Statistics(request):
    voucher =Vouchers.objects.all().order_by('Vouchers_name')
    context = {
        
        'voucher':voucher,
        
        

    }

    
    return render(request,'statistics.html',context)

def voucher_monthly_register(request):
    mo = Months.objects.all()
    context = {
        'mo':mo,
        
        
        

    }

    
    return render(request,'voucher_monthly_register.html',context)



def test(request):
    return render(request,'test.html')



