from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Article


def index(request):
    return render(request, 'article/index.html')


def about(request):
    return render(request, 'article/about.html')


class ArticleListView(ListView):
    model = Article


class ArticleDetailView(DetailView):
    model = Article
