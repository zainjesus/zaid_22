from django.urls import path
from users.views import authorization, registration

urlpatterns = [
    path('registration/', registration),
    path('authorization/', authorization),
]