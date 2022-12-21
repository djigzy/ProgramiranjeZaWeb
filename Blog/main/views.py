from django.shortcuts import render
from django.views.generic import ListView
from main.models import *

def index(request):
    return render(request, 'index.html')

class KorisnikList(ListView):
    model = Korisnik
    
class ReputacijaList(ListView):
    model = Reputacija
    
class BlogList(ListView):
    model = Blog
    
class KomentarList(ListView):
    model = Komentar