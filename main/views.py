from django.shortcuts import render
from django.http import HttpResponse

# python manage.py runserver
def index(request):
    context = {
        'title': 'Home',
        'content': 'Главная страница магазина - Home'
    }
    template = 'main/index.html'
    return render(request, template, context)


def about(request):
    return HttpResponse('about page')
