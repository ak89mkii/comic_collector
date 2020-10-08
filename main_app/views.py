from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# NEW
from django.views.generic import ListView, DetailView
from .models import Comic, Collectable
from .forms import ReadingForm

from django.http import HttpResponse

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')
  
def comics_index(request):
  comics = Comic.objects.all()
  return render(request, 'comics/index.html', { 'comics': comics })

def comics_detail(request, comic_id):
  comic = Comic.objects.get(id=comic_id)

  # NEW
  collectables_comic_doesnt_have = Collectable.objects.exclude(id__in = comic.collectables.all().values_list('id'))

  reading_form = ReadingForm()
  return render(request, 'comics/detail.html', {
    'comic': comic, 'reading_form': reading_form, 'collectables':       collectables_comic_doesnt_have
  })

def add_reading(request, comic_id):
  form = ReadingForm(request.POST)
  if form.is_valid():
    new_reading = form.save(commit=False)
    new_reading.comic_id = comic_id
    new_reading.save()
  return redirect('detail', comic_id=comic_id)


class ComicCreate(CreateView):
  model = Comic
  fields = '__all__'

class ComicUpdate(UpdateView):
  model = Comic
  fields = ['publisher', 'info', 'decade']

class ComicDelete(DeleteView):
  model = Comic
  success_url = '/comics/'

# NEW
class CollectableList(ListView):
  model = Collectable

class CollectableDetail(DetailView):
  model = Collectable

class CollectableCreate(CreateView):
  model = Collectable
  fields = '__all__'

class CollectableUpdate(UpdateView):
  model = Collectable
  fields = ['name', 'color']

class CollectableDelete(DeleteView):
  model = Collectable
  success_url = '/collectables/'

def assoc_collectable(request, comic_id, collectable_id):
  Comic.objects.get(id=comic_id).collectables.add(collectable_id)
  return redirect('detail', comic_id=comic_id)

 