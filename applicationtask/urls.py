"""applicationtask URL Configuration

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
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from app.sites.views import SiteList

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', SiteList.as_view(), name='Site_list'),
    url(r'^sites/(?P<pk>\d+)$', SiteList.getDetail, name='Site_detail'),
    url(r'^summary$', SiteList.getSum, name='Site_summary'),
    url(r'^summary/average$', SiteList.getAverage, name='Site_average'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
