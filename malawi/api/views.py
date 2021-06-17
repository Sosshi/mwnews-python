from rest_framework import viewsets
from ..models import News
from .serializers import NewsSerializers
from url_filter.integrations.drf import DjangoFilterBackend

class NewsViewset(viewsets.ModelViewSet):
    queryset = News.objects.order_by("-date")
    serializer_class = NewsSerializers
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['heading', 'description']