from django.shortcuts import render
from .models import *


def home(request):
    services = Service.objects.all()[:6]
    articles = Article.objects.all().order_by('-created')[:4]
    contacts = Contact.objects.all()
    plus_all = Plus.objects.filter(active=True)
    return render(request, 'sto/home.html', {
        'contacts': contacts,
        'plus_all': plus_all,
        'articles': articles,
        'services': services,
    })


def article_detail(request, id):
    article = Article.objects.get(pk=id)
    return render(request, 'sto/article_detail.html', {'article': article})


def service_detail(request, id):
    service = Service.objects.get(pk=id)
    return render(request, 'sto/service_detail.html', {'service': service})

    
def paz(request):
    paz = Paz.objects.get(id=1)
    return render(request, 'sto/paz.html', {'paz': paz})