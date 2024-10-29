from django.shortcuts import render,redirect
from .models import product
from pathlib import os
# Create your views here.
def home(request):
    return render(request,'products.html')

def add_product(request):
    if request.method =='POST':
        pname=request.POST['pname']
        price=request.POST['price']
        quantity=request.POST['quantity']
        image=request.FILES.get('image')
        p= product(product_name=pname,price=price,quantity=quantity,image=image)
        print('save data')
        p.save()
        return redirect ('show_products')

def show_products(request):
    pr=product.objects.all()
    return render(request,'show_products.html',{'pr':pr})

def editpage(request,pk):
    pr=product.objects.get(id=pk)
    return render(request,'edit.html',{'pr':pr})

def edit_products(request,pk):
   
    if request.method=='POST':
        pr=product.objects.get(id=pk)
        pr.product_name=request.POST.get('product_name')
        pr.price=request.POST.get('price')
        pr.quantity=request.POST.get('quantity')
        
        if len(request.FILES)!=0:
         if len(pr.image)>0:
             os.remove(pr.image.path)
         pr.image=request.FILES.get('image')
        pr.save()
        return redirect('show_products')

    return render(request,'edit.html',{'pr':pr})
                

def deletepage(request,pk):
    pr=product.objects.get(id=pk)
    if pr.image and os.path.isfile(pr.image.path):
        os.remove(pr.image.path)
        
        pr.delete()
        return redirect('show_products')