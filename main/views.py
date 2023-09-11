from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama': 'Ester Gracia',
        'kelas': "PBP A", 
    }

    return render(request, "main.html", context)