from django.shortcuts import render
from django.views.generic import ListView

from portfolio.models import PortfolioItem


# Create your views here.
class PortfolioListView(ListView):
    template_name = 'portfolio/portfolio_main.html'
    context_object_name = 'items'

    def get_queryset(self):
        return PortfolioItem.objects.all()

