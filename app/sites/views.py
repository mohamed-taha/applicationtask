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
            result_obj = Sites.objects.all()
        except Sites.DoesNotExist:
            result_obj = None
        return result_obj

    def getDetail(request, pk):
        detail = Sites.objects.get(id=pk)
        value = Value.objects.filter(site_id=pk)
        result = list(value)
        return render(request, 'detail.html', {'result': value, 'detail': detail})

    def getSum(request):
        value = Sites.objects.values('name').annotate(Sum('value_site__a_value'), Sum('value_site__b_value'))
        return render(request, 'sum.html', {'result': value})

    def getAverage(request):
        value = Sites.objects.values('name').annotate(Avg('value_site__a_value'), Avg('value_site__b_value'))
        return render(request, 'average.html', {'result': value})