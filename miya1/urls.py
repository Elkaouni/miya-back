from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('/', views.say_hello),
    path('response/', views.generate_response, name="generate_response" ),
    path('response/miya/', views.generate_wav_response, name="generate_wav_response" )
]