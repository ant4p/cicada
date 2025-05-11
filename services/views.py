from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView

from services.models import Service


# class ShowServicesList(TemplateView):
#     template_name = 'services/services_list.html'

class ShowServicesList(ListView):
    template_name = 'services/services_list.html'
    context_object_name = 'services'

    def get_queryset(self):
        return Service.objects.all()

class ShowService(DetailView):
    model = Service
    template_name = 'services/service.html'
    context_object_name = 'services'

    def get_success_url(self):
        return reverse('services', kwargs={'slug': self.object.slug})


