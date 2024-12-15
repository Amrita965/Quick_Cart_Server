
from django.urls import path
from .views import dashborad_status

urlpatterns = [
    path("dashboard-status/<str:pk>", dashborad_status)
]
