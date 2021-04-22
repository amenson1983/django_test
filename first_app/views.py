from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.template.response import TemplateResponse
from first_app.forms import UserForm
import cgi
path = 'C:\\Users\\Anastasia Siedykh\\Documents\\Backup\\django\\django_test_1'
months_path = '\\months.xlsx'

def index(request):
     with open('C:\\Users\\Anastasia Siedykh\\Documents\\Backup\\python_projects\\grindeks_company_main\\users.txt',
              'r') as file:
        user1_login = file.readline().rstrip('\n')
        user1_password = file.readline().rstrip('\n')
        user2_login = file.readline().rstrip('\n')
        user2_password = file.readline()
        dictionary_users = {user1_login: user1_password, user2_login: user2_password}
        users_logins = [user1_login, user2_login]
        ind = 0
        if request.method == "POST":
            login = request.POST.get("login")
            password = request.POST.get("password")
        else:
            userform = UserForm()
            return render(request, "first_app/index.html", {"form": userform})
        if login in users_logins:
            ind = users_logins.index(login)
        if login == users_logins[ind]:
            if password == dictionary_users.get(login):
                return cabinet(request)
            else:
                userform = UserForm()
                return render(request, "first_app/index.html", {"form": userform})
        else:
            userform = UserForm()
            return render(request, "first_app/index.html", {"form": userform})


def cabinet(request):
    login = request.POST.get("login")
    users = {"a.soloshenko": "Лёша", "a.turchyn":"Дрюня"}
    data = {}
    for log in users:
        if log == login:
            data = {"login": users[login]}
    return render(request,  "first_app/cabinet.html",context=data)

def about(request):
    return render(request,  "first_app/about.html")


def contact(request):
    return HttpResponseRedirect("/about")


def details(request):
    return HttpResponsePermanentRedirect("/")