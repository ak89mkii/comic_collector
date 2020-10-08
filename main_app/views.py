from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Comic
from .forms import ReadingForm

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
  # instantiate FeedingForm to be rendered in the template
  reading_form = ReadingForm()
  return render(request, 'comics/detail.html', {
    # include the cat and feeding_form in the context
    'comic': comic, 'reading_form': reading_form
  })

def add_reading(request, comic_id):
  # create a ModelForm instance using the data in request.POST
  form = ReadingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_reading = form.save(commit=False)
    new_reading.comic_id = comic_id
    new_reading.save()
  return redirect('detail', comic_id=comic_id)



class ComicCreate(CreateView):
  model = Comic
  fields = '__all__'

class ComicUpdate(UpdateView):
  model = Comic
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['publisher', 'info', 'decade']

class ComicDelete(DeleteView):
  model = Comic
  success_url = '/comics/'