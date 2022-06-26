from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.utils import timezone

from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = "articles/article_list.html"
    context_name = 'article_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Article.objects.filter(pub_date__lte=timezone.now(), published=True).order_by('-pub_date')

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'
    context_name = 'article'

    def get(self, request, **kwargs):
        article = Article.objects.get(pk=self.kwargs['pk'])
        if article.published and article.pub_date < timezone.now():
            return super().get(request, **kwargs)
        else:
            raise Http404('Статья не найдена')