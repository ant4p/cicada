from django.urls import path

from src.views import ShowMainPage

app_name = 'src'

urlpatterns = [
    path('', ShowMainPage.as_view(), name='main'),
]