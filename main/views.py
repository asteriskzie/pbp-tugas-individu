from django.shortcuts import render

from django.http import HttpResponseRedirect
from main.forms import ItemForm
from main.models import Item
from django.urls import reverse

from django.http import HttpResponse
from django.core import serializers

from django.db.models import Sum

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.all()
    
    # get the sum of a column
    # from https://stackoverflow.com/questions/8616343/django-calculate-the-sum-of-the-column-values-through-query
    sum = Item.objects.aggregate(Sum('amount'))['amount__sum']
    if sum is None : 
        sum = 0
    
    context = {
        'nama': 'Ester Gracia',
        'kelas': 'PBP A',
        'items' : items,
        'sum': sum,
    }

    return render(request, "main.html", context)

def add_item(request) :
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "add_item.html", context)

def show_html(request): 
    items = Item.objects.all()
    context = {
        'items' : items,
    }
    return render(request, "show_html.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request) :
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('main:login')