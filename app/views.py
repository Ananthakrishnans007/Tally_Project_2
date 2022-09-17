from contextlib import redirect_stderr
from multiprocessing import context
from django.shortcuts import render,redirect

from . models import*

# Create your views here.


def Index(request):
    return render(request,'index.html')


# statistics    

def Statistics(request):
    voucher =statistics_Vouchers.objects.all().order_by('Vouchers_name')
    accounts = statistics_Accounts.objects.all()
    sum=0
    total1= statistics_Total_Voucher.objects.all()
    for i in total1:
        if i.Total:
            sum+=i.Total


    context = {
        
        'voucher':voucher,
        'sum':sum,
        'accounts':accounts,
        
        

    }

    
    return render(request,'statistics.html',context)

def Statistics_voucher_monthly_register(request,id):
    mo = Months.objects.all()

    vch = statistics_Vouchers.objects.get(id=id)
    count = statistics_Voucher_count.objects.filter(Voucher=id)
    total=0
    for i in count:
        if i.Total_Voucher:
            total+=i.Total_Voucher

    if statistics_Total_Voucher.objects.filter(Voucher=id):
        to=statistics_Total_Voucher.objects.get(Voucher=id)
        to.Voucher=vch
        to.Total=total
        to.save()
    else:
        to=statistics_Total_Voucher()
        to.Voucher=vch
        to.Total=total
        to.save()
   


    context = {
        'mo':mo,
        'vch':vch,
        'count':count,
        'total':total,
        
        
        
        

    }

    
    return render(request,'statistics_voucher_monthly_register.html',context)

def Statistics_voucher_register(request,id,pk):
    voucher = statistics_Voucher_Register.objects.filter(Month=id,Voucher=pk)
    vch = statistics_Vouchers.objects.get(id=pk)
    

    total_debit=0
    total_credit=0

    for i in voucher:
        if i.Debit_Amount:
            total_debit +=i.Debit_Amount
        if i.Credit_Amount:
            total_credit +=i.Credit_Amount
    v=statistics_Vouchers.objects.get(id=pk)
    m=Months.objects.get(id=id)
    count = voucher.count()
    if statistics_Voucher_count.objects.filter(Month=id,Voucher=pk):
        total= statistics_Voucher_count.objects.get(Month=id,Voucher=pk)
        
        total.Voucher=v
        total.Month=m
        total.Total_Voucher=count
        


        total.save()
    else:
        total= statistics_Voucher_count()
        total.Voucher=v
        total.Month=m
        total.Total_Voucher=count
        


        total.save()


    context = {
        'voucher':voucher,
        'total_debit':total_debit,
        'total_credit':total_credit,
        'vch':vch,
        'm':m,

        
        
        

    }

    
    return render(request,'statistics_voucher_register.html',context)




def Statistics_voucher_Delete(request,id,pk,de):
    voucher = statistics_Voucher_Register.objects.get(id=de)
    voucher.delete()
    

    return redirect(Statistics_voucher_register,id,pk)



