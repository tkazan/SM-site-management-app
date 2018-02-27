from django.shortcuts import render
from django.views import View



class HomeView(View):
    def get(self, request):
        ctx = {

        }
        return render(request, "home.html", ctx)


class SitesView(View):
    def get(self, request):
        ctx = {

        }
        return render(request, "sites.html", ctx)


class MaterialsView(View):
    def get(self, request):
        ctx = {

        }
        return render(request, "materials.html", ctx)


class MachinesView(View):
    def get(self, request):
        ctx = {

        }
        return render(request, "machines.html", ctx)


class ContractorsView(View):
    def get(self, request):
        ctx = {

        }
        return render(request, "contractors.html", ctx)


class ProvidersView(View):
    def get(self, request):
        ctx = {

        }
        return render(request, "providers.html", ctx)


class CalendarView(View):
    def get(self, request):
        ctx = {

        }
        return render(request, "calendar.html", ctx)


class ContactsView(View):
    def get(self, request):
        ctx = {

        }
        return render(request, "contacts.html", ctx)


class BlogView(View):
    def get(self, request):
        ctx = {

        }
        return render(request, "blog.html", ctx)