# Create your views here.
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Status login sukses.
            return JsonResponse({
                "user": user.id,
                "username": user.username,
                "status": True,
                "message": "Login sukses!"
                # Tambahkan data lainnya jika ingin mengirim data ke Flutter.
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun dinonaktifkan."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali email atau kata sandi."
        }, status=401)

@csrf_exempt
def logout(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        print("logouttttnya gagal")
        return JsonResponse({
        "status": False,
        "message": "Logout gagal."
        }, status=401)
    
@csrf_exempt
def register(request): 
    # receive a POST request with data
    username = request.POST['username']
    password1 = request.POST['password']
    password2 = request.POST['password_confirmation']
    # print(username, password1, password2)
    # return JsonResponse({"status": False, "message": "testing"}, status=401)

    if (User.objects.filter(username=username).exists()) : 
        return JsonResponse({
            "status": False,
            "message": "Register gagal, username sudah terdaftar."
        }, status=401)
    

    if (password1 != password2) :
        return JsonResponse({
            "status": False,
            "message": "Register gagal, password tidak sama."
        }, status=401)
     
    user = User.objects.create_user(username=username, password=password1)
    user.save()
    return JsonResponse({
        "status": True,
        "message": "Register berhasil!"
    }, status=200)