from django.shortcuts import render
from .models import Comic

# Create your views here.
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')
  
def comics_index(request):
  comics = Comic.objects.all()
  return render(request, 'comics/index.html', { 'comics': comics })

def comics_detail(request, comic_id):
  comic = Comic.objects.get(id=comic_id)
  return render(request, 'comics/detail.html', { 'comic': comic })