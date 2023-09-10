from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Alarm Clock',
        'amount': 10, 
        'description': 'Ready to wake u up to reality.'
    }

    return render(request, "main.html", context)