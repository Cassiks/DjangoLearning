from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Main


def index(request):
    myMain = Main.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'myMain': myMain,
    }
    return HttpResponse(template.render(context, request))


def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))


def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    member = Main(firstname=x, lastname=y)
    member.save()
    return HttpResponseRedirect(reverse('index'))


def delete(request, id):
    main = Main.objects.get(id=id)
    main.delete()
    return HttpResponseRedirect(reverse('index'))


def update(request, id):
    mymember = Main.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))


def updaterecord(request, id):
    first = request.POST['first']
    last = request.POST['last']
    member = Main.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.save()
    return HttpResponseRedirect(reverse('index'))
