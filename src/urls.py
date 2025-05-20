from django.urls import path

from src.views import ShowMainPage, ShowCooperationPage, ShowContactsPage, ShowUserAgreement

app_name = 'src'

urlpatterns = [
    path('', ShowMainPage.as_view(), name='main'),
    path('cooperation/', ShowCooperationPage.as_view(), name='cooperation'),
    path('contacts/', ShowContactsPage.as_view(), name='contacts'),
    path('user_agreement/', ShowUserAgreement.as_view(), name='user_agreement')
]