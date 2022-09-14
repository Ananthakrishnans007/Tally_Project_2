from contextlib import redirect_stderr
from multiprocessing import context
from django.shortcuts import render,redirect

from . models import*

# Create your views here.


def Index(request):
    return render(request,'index.html')


# statistics    

def Statistics(request):
    voucher =Vouchers.objects.all().order_by('Vouchers_name')
    accounts = Accounts.objects.all()
    sum=0
    total1= Total.objects.all()
    for i in total1:
        if i.Total:
            sum+=i.Total


    context = {
        
        'voucher':voucher,
        'sum':sum,
        'accounts':accounts,
        
        

    }

    
    return render(request,'statistics.html',context)

def voucher_monthly_register(request,id):
    mo = Months.objects.all()

    vch = Vouchers.objects.get(id=id)
    count = Voucher_count.objects.filter(Voucher=id)
    total=0
    for i in count:
        if i.Total_Voucher:
            total+=i.Total_Voucher

    if Total.objects.filter(Voucher=id):
        to=Total.objects.get(Voucher=id)
        to.Voucher=vch
        to.Total=total
        to.save()
    else:
        to=Total()
        to.Voucher=vch
        to.Total=total
        to.save()
   


    context = {
        'mo':mo,
        'vch':vch,
        'count':count,
        'total':total,
        
        
        
        

    }

    
    return render(request,'voucher_monthly_register.html',context)

def voucher_register(request,id,pk):
    voucher = Voucher_Register.objects.filter(Month=id,Voucher=pk)
    vch = Vouchers.objects.get(id=pk)
    

    total_debit=0
    total_credit=0

    for i in voucher:
        if i.Debit_Amount:
            total_debit +=i.Debit_Amount
        if i.Credit_Amount:
            total_credit +=i.Credit_Amount
    v=Vouchers.objects.get(id=pk)
    m=Months.objects.get(id=id)
    count = voucher.count()
    if Voucher_count.objects.filter(Month=id,Voucher=pk):
        total= Voucher_count.objects.get(Month=id,Voucher=pk)
        
        total.Voucher=v
        total.Month=m
        total.Total_Voucher=count
        


        total.save()
    else:
        total= Voucher_count()
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

    
    return render(request,'voucher_register.html',context)




def Delete(request,id,pk,de):
    voucher = Voucher_Register.objects.get(id=de)
    voucher.delete()
    

    return redirect(voucher_register,id,pk)

def test(request):
    return render(request,'test.html')



