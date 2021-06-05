from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from malawi.api.views import NewsViewset

router = DefaultRouter()

router.register(r"news", NewsViewset, basename="news")



urlpatterns = [path("admin/", admin.site.urls), path("", include("malawi.urls"))]
