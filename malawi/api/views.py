from rest_framework import viewsets
from ..models import News
from .serializers import NewsSerializers

class NewsViewset(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializers