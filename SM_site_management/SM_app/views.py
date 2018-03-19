from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from operator import itemgetter, attrgetter

from .models import *
from .forms import *


class HomeView(LoginRequiredMixin, View):
    login_url = '/login'
    def get(self, request):
        ctx = {

        }
        return render(request, "home.html", ctx)


class SitesView(LoginRequiredMixin, View):
    login_url = '/login'
    def get(self, request):

        sites = Sites.objects.all().order_by("id")
        ctx = {
            "sites":sites,
        }
        return render(request, "sites.html", ctx)


def siteslist(sites, sitesmaterials):
    result = [None] * len(sites)
    for index, site in enumerate(sites):
        if site.name in [d.sites.name for d in sitesmaterials]:
            result[index] = sitesmaterials.filter(sites__name=site.name)[0]
    return result

class MaterialsView(LoginRequiredMixin,View):
    login_url = '/login'

    def get(self, request):
        form = SearchMaterialsForm()
        sites = Sites.objects.all().order_by("name")
        materials = Materials.objects.all().order_by("name")
        result = {}
        for material in materials:
            sitesmaterials = material.sitesmaterials_set.all()
            result[material] = siteslist(sites, sitesmaterials)
        page = request.GET.get('page', 1)
        paginator = Paginator(tuple(result.items()), 15)
        try:
            results = paginator.page(page)
        except PageNotAnInteger:
            results = paginator.page(1)
        except EmptyPage:
            results = paginator.page(paginator.num_pages)

        ctx = {
            "sites": sites,
            "results": results,
            'form': form,
        }
        return render(request, "materials.html", ctx)

    def post(self, request):
        form = SearchMaterialsForm(request.POST)
        sites = Sites.objects.all().order_by("name")
        materials = Materials.objects.all().order_by("name")
        result = {}
        for material in materials:
            sitesmaterials = material.sitesmaterials_set.all()#.order_by("materials__name")
            result[material] = siteslist(sites, sitesmaterials)
            page = request.GET.get('page', 1)
            paginator = Paginator(tuple(result.items()), 15)
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                results = paginator.page(1)
            except EmptyPage:
                results = paginator.page(paginator.num_pages)

        if form.is_valid():
            name = form.cleaned_data['name']
            if len(name) == 0:
                searchmaterials = ''
            else:
                searchmaterials = Materials.objects.filter(name__icontains=name).order_by("name")
            search = {}
            for material in searchmaterials:
                sitesmaterials = material.sitesmaterials_set.all()
                search[material] = siteslist(sites, sitesmaterials)
        ctx = {
            'form': form,
            "search": search,
            "sites": sites,
            "results": results,
        }
        return render(request, "materials.html", ctx)


class MachinesView(LoginRequiredMixin, View):
    login_url = '/login'
    def get(self, request):
        form = SearchMachinesForm()
        machines = Machines.objects.all().order_by("name")
        ctx = {
            "machines": machines,
            "form": form,
        }
        return render(request, "machines.html", ctx)

    def post(self, request):
        form = SearchMachinesForm(request.POST)
        machines = Machines.objects.all().order_by("name")

        if form.is_valid():
            name = form.cleaned_data['name']
            if len(name) == 0:
                searchmachines = ""
            else:
                searchmachines = Machines.objects.filter(name__icontains=name).order_by("name")

        ctx = {
            "machines": machines,
            "form": form,
            "searchmachines": searchmachines,
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
        contacts = Contacts.objects.all().order_by("name")
        # sitescontacts = SitesContacts.objects.all().order_by("sites__name")
        ctx = {
            # "sitescontacts": sitescontacts,
            "contacts": contacts,
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


class SiteView(LoginRequiredMixin, View):
    login_url = '/login'
    def get(self, request, id):
        site = Sites.objects.get(id=id)
        contacts = site.sitescontacts_set.all().order_by("pk")
        contractors = site.contractors_set.all()
        materials = site.sitesmaterials_set.all().order_by("materials__name")
        machines = site.machines_set.all()
        sites = Sites.objects.all()

        ctx = {
            "site": site,
            "contacts": contacts,
            "contractors": contractors,
            "materials": materials,
            "machines": machines,
            "sites": sites,
        }

        return render(request, "site.html", ctx)


class AddContactsView(LoginRequiredMixin, View):
    login_url = '/login'
    def get(self, request):
        form = AddContactsForm()
        form2 = AddSitesContactsForm()
        return render(request, "add_contacts.html", {'form': form, 'form2': form2})

    def post(self, request):
        action = request.POST.get("submit")
        form = AddContactsForm(request.POST, request.FILES)
        form2 = AddSitesContactsForm(request.POST)
        if form.is_valid() and form2.is_valid():
            contact = form.save()
            sitescontacts = form2.save(commit=False)
            sitescontacts.contacts_id=contact.pk
            sitescontacts.save()

            if action == "Dodaj i kontynuuj dodawanie":
                return redirect(reverse("addcontacts"))
            return redirect(reverse("contacts"))
        return redirect(reverse("addcontacts"))

class AddSitesView(LoginRequiredMixin, View):
    login_url = '/login'
    def get(self, request):
        form = AddSitesForm()
        return render(request, "add_sites.html", {'form': form})

    def post(self, request):
        action = request.POST.get("submit")
        form = AddSitesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            if action == "Dodaj i kontynuuj dodawanie":
                return redirect(reverse("addsites"))
            return redirect(reverse("sites"))
        return redirect(reverse("addsites"))






