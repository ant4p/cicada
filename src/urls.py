from django.urls import path

from src.views import ShowMainPage, ShowCooperationPage, ShowContactsPage, ShowUserAgreement, handler_404, handler_500

app_name = 'src'

urlpatterns = [
    path('', ShowMainPage.as_view(), name='main'),
    path('cooperation/', ShowCooperationPage.as_view(), name='cooperation'),
    path('contacts/', ShowContactsPage.as_view(), name='contacts'),
    path('user_agreement/', ShowUserAgreement.as_view(), name='user_agreement')
]

handler404 = handler_404
handler500 = handler_500