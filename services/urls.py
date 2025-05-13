from django.urls import path

from services.views import ServicesListView, ServiceItemView

app_name = 'services'

urlpatterns = [
    path('', ServicesListView.as_view(), name='services_list'),
    path('<slug:slug>/', ServiceItemView.as_view(), name='services_item'),

]