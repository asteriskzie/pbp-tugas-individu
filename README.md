Hello! 

Visit the deployed website at https://jam-terbang.adaptable.app/main :D

--- 

### TUGAS 2

#### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

Awalnya, saya mengatur environment untuk memulai project Django baru. Saya membuat folder dengan virtual environment dan menginstall beberapa library yang diperlukan menggunakan `pip install`. 

Berikut ini library yang saya install:

```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
Setelah itu, saya membuat project Django baru. Saya ingin menamai inventory app pada tugas ini "Jam Terbang", jadi saya menggunakan perintah `django-admin createproject jam_terbang`. 


Kemudian saya membuat aplikasi "main" dengan menggunakan ``python manage.py createapp main``. Saya lalu mendaftarkannya pada ``settings.py`` di folder proyek pada bagian ``INSTALLED_APPS``. 

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main'
]
```
Saya lalu melakukan konfigurasi routing proyek, dengan mendaftarkan aplikasi 'main' pada `urls.py` di folder proyek. Selain itu saya juga menambahkan `urls.py` dalam folder aplikasi 'main' dan menambahkan routingnya. 

Untuk mengatur tampilan pada aplikasi main, saya membuat folder `templates` dalam folder aplikasi main dan membuat tampilan page main tersebut dengan nama file `main.html`. Untuk menampilkan halaman dengan template yang sudah saya buat, saya mengatur `views.py` aplikasi main. 

```
from django.shortcuts import render

def show_main(request):
    context = {
        'nama': 'Ester Gracia',
        'kelas': 'PBP A',
    }

    return render(request, "main.html", context)
```
Saya lalu membuat model untuk database. Saya melakukannya dengan mengedit `models.py` dalam aplikasi main. Saya menambahkan model `Item` dengan field `name`, `amount`, dan `description`. 

```
from django.db import models

# Create your models here.
class Item(models.Model) : 
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    
```
Terakhir, saya tinggal melakukan deploy ke adaptable. Saya melakukannya dengan memilih `Python App Template` sebagai template deployment, erta `PostgreSQL` sebagai tipe basis data. Saya memasukkan `python manage.py migrate && gunicorn shopping_list.wsgi` sebagai start command. Saya kemudian memasukkan nama aplikasi sekaligus domain dan juga mencentang `HTTP Listener on PORT` lalu memulai proses deployment. 

#### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html!

![](/img/bagan.png) 


#### Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Kita menggunakan virtual environment supaya tidak terjadi conflict antar 2 versi package yang berbeda di project yang berbeda. Sebenarnya tanpa virtual environment kita bisa-bisa saja membuat aplikasi web berbasis Django. Namun, tanpa virtual environment kita akan menginstall semua requirements secara global yang berpotensi menimbulkan konflik di project yang berbeda. Dengan virtual environment, kita hanya mengistall untuk scope satu project saja jadi kalau ada project lain di komputer yang sama tapi ingin pakai versi yang berbeda, masih akan aman-aman saja. 

#### Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya!

Pada MVC (Model, View, Controller), Model berurusan dengan database, Controller mengatur routing ke View (tampilan) yang sesuai dengan request. Pada MVT (Model, View, Template), mirip seperti MVC hanya saja View MVT berperan seperti Controller MCV dan Template MVT berperan seperti View MVC. Pada MVVM (Model, View, ViewModel), terdapat ViewModel yang menghubungkan View dan Model. 
