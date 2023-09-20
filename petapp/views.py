from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Pet

def petsall(requests):
    pets=Pet.objects.all().values()
    template=loader.get_template('allpets.html')
    context={'pets':pets,}
    return HttpResponse(template.render(context,requests))


def petsdetails(request,id):
    pets=Pet.objects.get(id=id)
    template=loader.get_template('petsdetails.html')
    context={'pets':pets}
    return HttpResponse(template.render(context,request))


def main(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())