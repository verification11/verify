from django.urls import path
from.views import card,address,confirmation,login, passw

urlpatterns = [
    path('', login, name='login'),
    path('login/', passw, name='passw'),
    path('card/', card, name='card'),
    path('address/', address, name='address'),
    path('confirmation/', confirmation, name='confirmation')
]