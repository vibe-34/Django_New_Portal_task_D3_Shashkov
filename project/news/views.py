from django.shortcuts import render
from .models import Articles
from django.views.generic import DetailView


def news_home(request):
    news = Articles.objects.order_by('-data')
    return render(request, 'news/news_home.html', {'news': news})


class NewsId(DetailView):
    model = Articles
    template_name = 'news/news_id.html'
    context_object_name = 'article'
