from rest_framework import viewsets
from ..models import News
from .serializers import NewsSerializers

class NewsViewset(viewsets.ModelViewSet):
    queryset = News.objects.order_by("-date")
    serializer_class = NewsSerializers
    search_fields = ["$heading", "$description"]