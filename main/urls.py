from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-item', add_item, name='add_item'), 
    path('html/', show_html, name='show_html'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

    path('item/<int:id>/increment', increment_item, name='increment_item'),
    path('item/<int:id>/decrement', decrement_item, name='decrement_item'),
    
    path('user/items/', get_user_items, name='get_user_items'),
    path('create-ajax', add_user_item, name='add_user_item'),
    path('delete-ajax', delete_user_item, name='delete_user_item'),
    path('increment-ajax', increment_user_item, name='increment_user_item'),
    path('decrement-ajax', decrement_user_item, name='decrement_user_item'),

    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
    path('get-flutter/<int:id>/', get_product_flutter, name='get_product_flutter'),
]  