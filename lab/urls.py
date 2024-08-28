# myapp/urls.py
from django.urls import path
from .views import upload_image, success,tires,battery,brake,engine,exterior_ok,tyre_ok,battery_ok,brake_ok,qr,home,inspection

urlpatterns = [
    path('upload/', upload_image, name='upload_image'),
    path('success/', success, name='success'),
    path('tires/',tires,name='tires'),
    path('battery/',battery,name='battery'),
    path('brake/',brake,name='brake'),
    path('engine/',engine,name='engine'),
    path('tires_exok/',exterior_ok,name='exterior_ok'),
    path('brake_exok/',tyre_ok,name = 'tyre_ok'),
    path('battery_exok/',brake_ok,name='brake_ok'),
    path('engine_exok/',battery_ok,name = 'battery_ok'),
    path('qr/',qr,name='qr'),
    path('',home,name='home'),
    path('inspection/',inspection,name='inspection')
]
