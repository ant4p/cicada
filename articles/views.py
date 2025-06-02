from django.urls import reverse
from django.views.generic import ListView, DetailView

from articles.models import Article


class ArticlesListView(ListView):
    template_name = 'articles/articles_main.html'
    context_object_name = 'articles_list'
    paginate_by = 9


    def get_queryset(self):
        return Article.objects.all()


class ArticleView(DetailView):
    model = Article
    template_name = 'articles/article.html'
    context_object_name = 'item'

    def get_queryset(self):
        return Article.objects.filter().prefetch_related('tags_a')

    def get_success_url(self):
        return reverse('article', kwargs={'slug':self.object.slug})
