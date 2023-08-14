from django.http import HttpResponse, HttpResponseRedirect
import requests
from django.shortcuts import redirect, render
from datetime import date
from .models import *
from django.utils import timezone
# Create your views here.

def index (request):
    return redirect("view/WTq8zYcZfaWVvMncigHqwQTEUE1WTq8zYcZfa2023-08-15WVvMncigHqwQ")

def view(request, code='TE002',expiredt='2023-08-10'):
    url = code  # Replace with the actual URL
    expiredt = expiredt  # Replace with the actual URL
    
    today = timezone.now().date() # GET CURRENT DATE
    messagedate = today.strftime("%Y-%m-%d")

    if messagedate > expiredt: # EXPIRE DATE CODE
     message = "This coupon is expired."
     return render(request, 'error_page.html', {'msg': message})

    return render(request, 'view.html', {'fetched_data': url,'expire_date': expiredt})

def handleRedeemCode(request):

    if request.method == "POST":
        uname=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        coupon_code=request.POST.get('Ccode')
        upi_address=request.POST.get('upid')
        review=request.POST.get('review')

        print(uname, phone, email, coupon_code, upi_address, review)
        if couponCodes.objects.filter(Ccode=coupon_code).exists():
            if redeemTbl.objects.filter(Ccode=coupon_code).exists():
             message = "This coupon is already used."
             return render(request, 'error_page.html', {'msg': message})
            else:
                RedeemCoupon = redeemTbl(name=uname, mobile=phone, email=email, Ccode=coupon_code, upi_address=upi_address, review=review)     
                RedeemCoupon.save()
                return redirect('/thankyou')
        else:
             message = "Invalide Coupon Code ."
             return render(request, 'error_page.html', {'msg': message})

    message = "This link is not working."
    return render(request, 'error_page.html', {'msg': message})

def thanks(request):
   
    return render(request, 'thankyou.html')

def error(request):
   
     return render(request, 'error_page.html')
