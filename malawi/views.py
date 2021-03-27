from django.shortcuts import render
from django.views.generic import ListView
from .models import News
from .news_sites import run_code

from django.http import HttpResponse


def my_view(request):
    run_code()
    return HttpResponse("done")


class NewsListView(ListView):
    model = News
    context_object_name = "news"
    queryset = News.objects.order_by("-date")
