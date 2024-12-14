
from django.urls import path
from User_App.views import user_list, user_detail

urlpatterns = [
    path('users/', user_list),
    path('users/<str:pk>', user_detail)
]
