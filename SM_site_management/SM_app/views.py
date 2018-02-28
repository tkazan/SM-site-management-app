from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .models import *



class HomeView(LoginRequiredMixin, View):
    login_url = '/login'
    def get(self, request):
        ctx = {

        }
        return render(request, "home.html", ctx)


class SitesView(LoginRequiredMixin, View):
    login_url = '/login'
    def get(self, request):

        sites = Sites.objects.all()
        ctx = {
            "sites":sites,
        }
        return render(request, "sites.html", ctx)


class MaterialsView(LoginRequiredMixin, View):
    login_url = '/login'
    def get(self, request):
        ctx = {

        }
        return render(request, "materials.html", ctx)


class MachinesView(LoginRequiredMixin, View):
    login_url = '/login'
    def get(self, request):
        ctx = {

        }
        return render(request, "machines.html", ctx)


class ContractorsView(LoginRequiredMixin, View):
    login_url = '/login'
    def get(self, request):
        ctx = {

        }
        return render(request, "contractors.html", ctx)


class ProvidersView(LoginRequiredMixin, View):
    login_url = '/login'
    def get(self, request):
        ctx = {

        }
        return render(request, "providers.html", ctx)


class CalendarView(LoginRequiredMixin, View):
    login_url = '/login'
    def get(self, request):
        ctx = {

        }
        return render(request, "calendar.html", ctx)


class ContactsView(LoginRequiredMixin, View):
    login_url = '/login'
    def get(self, request):
        ctx = {

        }
        return render(request, "contacts.html", ctx)


class BlogView(LoginRequiredMixin, View):
    login_url = '/login'
    def get(self, request):
        ctx = {

        }
        return render(request, "blog.html", ctx)

class LoginView(View):
    def get(self, request):

        return render(request, "login.html")

    def post(self, request):
        user_name = request.POST.get("login")
        password = request.POST.get("password")
        user = authenticate(username=user_name, password=password)
        if user is not None:
            login(request, user)
            url = request.GET.get("next")
            if url:
                return redirect(url)
            return render(request, "home.html")

        messages.warning(request, 'Błędny login i/lub hasło!')
        return render(request, "login.html")

def my_logout(request):
    previous_user = request.user.username
    logout(request)
    messages.info(request, 'Dobrego dnia {}! :-)'.format(previous_user))
    return redirect("/login/")


class SiteView(View):
    def get(self, request, id):
        site = Sites.objects.get(id=id)
        contacts = site.sitescontacts_set.all().order_by("pk")
        contractors = site.contractors_set.all()

        ctx = {
            "site": site,
            "contacts": contacts,
            "contractors": contractors,
        }

        return render(request, "site.html", ctx)


