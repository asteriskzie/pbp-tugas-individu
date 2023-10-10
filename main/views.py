from django.shortcuts import render

from django.http import HttpResponseRedirect, HttpResponseNotFound
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
from django.contrib.auth.decorators import login_required, user_passes_test

import datetime
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse

from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)
    last_item_id = -1
    if (items.last()) : 
        items.last().id
    # get the sum of a column
    # from https://stackoverflow.com/questions/8616343/django-calculate-the-sum-of-the-column-values-through-query
    sum = items.aggregate(Sum('amount'))['amount__sum']
    if sum is None : 
        sum = 0

    context = {
        'nama': request.user.username,
        'kelas': 'PBP A',
        'items' : items,
        'most-items': items.order_by('amount').values(),
        'sum': sum,
        'last_login': request.COOKIES.get('last_login'),
        'last_item_id': last_item_id
    }

    return render(request, "main.html", context)

def add_item(request) :
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user 
        item.save()
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
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required
def increment_item(request, id) : 
    data = Item.objects.get(pk=id)
    data.amount+=1
    data.save()
    return HttpResponseRedirect(reverse('main:show_main'))

@login_required
def decrement_item(request, id) : 
    data = Item.objects.get(pk=id)
    data.amount-=1
    data.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def id_check(user, requested_id) : 
    requested_user = User.objects.get(pk=requested_id)
    return user.username == requested_user.username

@login_required
def get_user_items (request) : 
    items = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', items))

@csrf_exempt
@login_required 
def add_user_item(request) : 
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        new_item = Item(name=name, amount=amount, description=description, user=user)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()