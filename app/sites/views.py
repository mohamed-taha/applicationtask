from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg, Sum
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from app.sites.models import Sites, Value
from applicationtask import settings


class SiteList(ListView):
    template_name = 'index.html'
    context_object_name = "result"

    def get_queryset(self):
        try:
            result_obj = Sites.objects.raw('SELECT * FROM sites_sites')
        except Sites.DoesNotExist:
            result_obj = None
        return result_obj

    def getDetail(request, pk):
        detail = Sites.objects.raw('SELECT * FROM sites_sites WHERE id=%s limit 1', [pk])
        value = Value.objects.raw('SELECT * FROM sites_value WHERE site_id=%s', [pk])
        result = list(value)
        return render(request, 'detail.html', {'result': list(value), 'detail': detail[0]})

    def getSum(request):
        value = Sites.objects.raw('SELECT * FROM sites_sites')
        return render(request, 'sum.html', {'result': list(value)})

    def getAverage(request):
        value = Sites.objects.raw('SELECT * FROM sites_sites')
        return render(request, 'average.html', {'result': list(value)})