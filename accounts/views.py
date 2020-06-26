from django.shortcuts import render #render will render an html page
from django.http import HttpResponse

#This is where the views should be created

# Create your views here.
def home(request):
    return render(request,'accounts/dashboard.html')

def products(request):
    return render(request,'accounts/products.html')

def customer(request):
    return render(request,'accounts/customer.html')
    # return HttpResponse('customer')




 