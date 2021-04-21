from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.template.response import TemplateResponse

path = 'C:\\Users\\Anastasia Siedykh\\Documents\\Backup\\django\\django_test_1'
months_path = '\\months.xlsx'

def index(request):
    return render(request,  "first_app/index.html")
#return render(request, "first_app/index.html", context=data)


def about(request):
    return HttpResponse("About")


def contact(request):
    return HttpResponseRedirect("/about")


def details(request):
    return HttpResponsePermanentRedirect("/")