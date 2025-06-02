
from django.views.generic import ListView

from services.models import Service, ServiceItem


class ServicesListView(ListView):
    template_name = 'services/services_main.html'
    context_object_name = 'services_list'

    def get_queryset(self):
        return Service.objects.all()


class ServiceItemView(ListView):
    template_name = 'services/service.html'
    context_object_name = 'item'
    paginate_by = 5

    def get_queryset(self):
        return (ServiceItem.objects.filter(service__slug=self.kwargs['slug']).
                select_related('service').
                prefetch_related('tags_s'))







