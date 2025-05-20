from django.shortcuts import render
from django.views.generic import TemplateView


class ShowMainPage(TemplateView):
    template_name = 'src/index.html'

class ShowCooperationPage(TemplateView):
    template_name = 'src/cooperation.html'

class ShowContactsPage(TemplateView):
    template_name = 'src/contacts.html'
