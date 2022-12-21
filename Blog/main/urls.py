from django.urls import path
from . import views
from main.views import *

urlpatterns = [
    path('', views.index, name='index.html'),
    path('users/', KorisnikList.as_view()),
    path('reputations/', ReputacijaList.as_view()),
    path('blogs/', BlogList.as_view()),
    path('comments/', KomentarList.as_view()),
]
