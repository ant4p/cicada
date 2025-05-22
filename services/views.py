from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView

from services.models import Service, ServiceItem


class ServicesListView(ListView):
    template_name = 'services/services_main.html'
    context_object_name = 'services_list'

    def get_queryset(self):
        return Service.objects.all()


class ServiceItemView(ListView):
    template_name = 'services/service.html'
    context_object_name = 'item'

    def get_queryset(self):
        return (ServiceItem.objects.filter(service__slug=self.kwargs['slug']).
                select_related('service').
                prefetch_related('tags_s'))

    # @staticmethod
    # def get_services():
    #     return Service.objects.all()







