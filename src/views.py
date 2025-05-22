from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from src.models import UserAgreement


class ShowMainPage(TemplateView):
    template_name = 'src/index.html'

class ShowCooperationPage(TemplateView):
    template_name = 'src/cooperation.html'

class ShowContactsPage(TemplateView):
    template_name = 'src/contacts.html'

class ShowUserAgreement(DetailView):
    model = UserAgreement
    template_name = 'src/user_agreement.html'
    context_object_name = 'item'

    def get_object(self, queryset=None):
        return UserAgreement.objects.get()


class ShowRobotsView(TemplateView):
    template_name = 'robots.txt'
    content_type = 'text/plain'

def handler_404(request, exception):
    return render(request, template_name='src/handlers/error_404.html')

def handler_500(request):
    return render(request, template_name='src/handlers/error_500.html')
