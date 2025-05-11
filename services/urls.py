from django.urls import path

from services.views import ShowServicesList, ShowService

app_name = 'services'

urlpatterns = [
    path('', ShowServicesList.as_view(), name='services_list'),
    path('<slug:slug>/', ShowService.as_view(), name='services'),

]