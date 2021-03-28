from django.views.generic import ListView
from .models import News


class NewsListView(ListView):
    model = News
    context_object_name = "news"
    paginate_by = 20
    queryset = News.objects.order_by("-date")
