from django.views.generic import ListView

from portfolio.models import PortfolioItem

class PortfolioListView(ListView):
    template_name = 'portfolio/portfolio_main.html'
    context_object_name = 'items'
    paginate_by = 28

    def get_queryset(self):
        return PortfolioItem.objects.all()
