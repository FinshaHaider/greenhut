from django.template import loader
from django.shortcuts import redirect, render
from .models import Menu,ItemImg

# Create your views here.
def index(request):
    # menu=Menu.objects.all()
    item=ItemImg.objects.all()
    return render(request,'index.html',{'item':item})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def menu(request):
    
    menu=Menu.objects.all()
    return render(request,'menu.html',{'menu':menu})

def addmenu(request):
    if request.method == 'POST':
        name = request.POST.get('itemname')
        price = request.POST.get('price')
        stockavailabliti = request.POST.get('stockavailabliti')
        menu = Menu(itemname=name, price=price, stockavailabliti=stockavailabliti)
        menu.save()
        # msg={'msg':'Item Added successfully'}
    return render(request,'addmenu.html')

def updatemenu(request,pkey):
    menu_update=Menu.objects.get(pk=pkey)# select object
    
    if request.method == 'POST':
        name = request.POST.get('itemname')
        price = request.POST.get('price')
        stockavailabliti = request.POST.get('stockavailabliti')
        menu_update.itemname=name
        menu_update.price=price
        menu_update.stockavailabliti=stockavailabliti
        menu_update.save()
        menu=Menu.objects.all()
        return redirect(request,'menu.html',{'menu':menu})
    return render(request,'updatemenu.html',{'menu_update':menu_update})


    
def deletemenu(request,pkey):
    menu_del=Menu.objects.get(pk=pkey)
    menu_del.delete()
    menu=Menu.objects.all()

    return render(request,'menu.html',{'menu':menu
    })