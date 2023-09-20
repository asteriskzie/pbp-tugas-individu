from django.shortcuts import render

from django.http import HttpResponseRedirect
from main.forms import ItemForm
from main.models import Item
from django.urls import reverse

from django.http import HttpResponse
from django.core import serializers

from django.db.models import Sum


# Create your views here.
def show_main(request):
    items = Item.objects.all()
    print(items)
    sum = Item.objects.aggregate(Sum('amount'))['amount__sum']
    print(sum)
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
