from django.urls import path
from users.views import LoginAPIView, RegistrationAPIView

urlpatterns = [
    path('registration/', RegistrationAPIView.as_view()),
    path('authorization/', LoginAPIView.as_view()),
]