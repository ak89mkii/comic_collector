from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# NEW
from django.views.generic import ListView, DetailView
from .models import Comic, Collectable
from .forms import ReadingForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponse

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required  
def comics_index(request):
  comics = Comic.objects.filter(user=request.user)
  return render(request, 'comics/index.html', { 'comics': comics })

@login_required
def comics_detail(request, comic_id):
  comic = Comic.objects.get(id=comic_id)

  # NEW
  collectables_comic_doesnt_have = Collectable.objects.exclude(id__in = comic.collectables.all().values_list('id'))

  reading_form = ReadingForm()
  return render(request, 'comics/detail.html', {
    'comic': comic, 'reading_form': reading_form, 'collectables':       collectables_comic_doesnt_have
  })

@login_required
def add_reading(request, comic_id):
  form = ReadingForm(request.POST)
  if form.is_valid():
    new_reading = form.save(commit=False)
    new_reading.comic_id = comic_id
    new_reading.save()
  return redirect('detail', comic_id=comic_id)


class ComicCreate(LoginRequiredMixin, CreateView):
  model = Comic
  fields = ['title', 'publisher', 'description', 'info', 'decade']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class ComicUpdate(LoginRequiredMixin, UpdateView):
  model = Comic
  fields = ['publisher', 'info', 'decade']

class ComicDelete(LoginRequiredMixin, DeleteView):
  model = Comic
  success_url = '/comics/'

# NEW
class CollectableList(LoginRequiredMixin, ListView):
  model = Collectable

class CollectableDetail(LoginRequiredMixin, DetailView):
  model = Collectable

class CollectableCreate(LoginRequiredMixin, CreateView):
  model = Collectable
  fields = '__all__'

class CollectableUpdate(LoginRequiredMixin, UpdateView):
  model = Collectable
  fields = ['name', 'color']

class CollectableDelete(LoginRequiredMixin, DeleteView):
  model = Collectable
  success_url = '/collectables/'

@login_required
def assoc_collectable(request, comic_id, collectable_id):
  Comic.objects.get(id=comic_id).collectables.add(collectable_id)
  return redirect('detail', comic_id=comic_id)

@login_required
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

 