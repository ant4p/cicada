from django.shortcuts import render
from django.views.generic import TemplateView

from src.models import UserAgreement, TitleImageCooperation, CaseCooperation, IndexVideo


class ShowMainPage(TemplateView):
    template_name = "src/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["video_data"] = IndexVideo.objects.all()
        return context


class ShowCooperationPage(TemplateView):
    template_name = "src/cooperation.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_data"] = TitleImageCooperation.objects.all()
        context["case_data"] = CaseCooperation.objects.all()
        return context


class ShowContactsPage(TemplateView):
    template_name = "src/contacts.html"


class ShowUserAgreement(TemplateView):
    template_name = "src/user_agreement.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["agreement_data"] = UserAgreement.objects.all()
        return context


class ShowRobotsView(TemplateView):
    template_name = "robots.txt"
    content_type = "text/plain"


def handler_404(request, exception):
    return render(request, template_name="src/handlers/error_404.html")


def handler_500(request):
    return render(request, template_name="src/handlers/error_500.html")
