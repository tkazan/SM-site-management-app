"""SM_site_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from SM_app.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^sites/$', SitesView.as_view(), name="sites"),
    url(r'^materials/$', MaterialsView.as_view(), name="materials"),
    url(r'^machines/$', MachinesView.as_view(), name="machines"),
    url(r'^contractors/$', ContractorsView.as_view(), name="contractors"),
    url(r'^providers/$', ProvidersView.as_view(), name="providers"),
    url(r'^calendar/$', CalendarView.as_view(), name="calendar"),
    url(r'^contacts/$', ContactsView.as_view(), name="contacts"),
    url(r'^blog/$', BlogView.as_view(), name="blog"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^logout/$', my_logout, name="logout"),
    url(r'^site/(?P<id>(\d)+)/$', SiteView.as_view(), name="site"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
