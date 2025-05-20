from django.urls import path

from articles.views import ArticlesListView, ArticleView

app_name = 'articles'

urlpatterns = [
    path ('', ArticlesListView.as_view(), name='articles_list'),
    path('<slug:slug>/', ArticleView.as_view(), name='article'),

]