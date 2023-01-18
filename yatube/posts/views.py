from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Главная страница
def index(request):
    template = 'posts/index.html'
    return render(request, template) 


# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр slug из path()
def group_posts(request, slug):
    return HttpResponse(f'Группа с названием <b>{slug}</b>') 