from django.shortcuts import render
from django.views.generic import TemplateView


class ShowMainPage(TemplateView):
    template_name = 'src/index.html'

