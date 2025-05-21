from django.urls import path

from tags.views import TagsListView, TagView

app_name = 'tags'

urlpatterns = [
    path('', TagsListView.as_view(), name='tags_list'),
    path('<slug:slug>/', TagView.as_view(), name='tag'),
]