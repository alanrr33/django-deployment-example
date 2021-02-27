from basic_app import views
from django.urls import path

#Template tagging

app_name='basic_app'

#aca especifico adonde redirigir cuando es llamado desde la pagina de la 
# forma 127.0.0.1:8000/other o lo q sea 
urlpatterns=[
    path('',views.index,name='index'),
    path('other/',views.other,name='other'),
    path('relative/',views.relative,name='relative'),
]