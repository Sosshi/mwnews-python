from django.urls import path
from .views import NewsListView, my_view

urlpatterns = [path("", NewsListView.as_view()), path("run/", my_view)]
