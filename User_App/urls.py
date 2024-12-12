
from django.urls import path
from User_App.views import user_view

urlpatterns = [
    path('users/', user_view)
]
