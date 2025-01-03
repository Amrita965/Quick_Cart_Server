
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('User_App.urls')),
    path('', include('Customer_App.urls')),
    path('', include('Category_App.urls')),
    path('', include('Dashboard.urls')),
    path('', include('Product_App.urls')),
    path('', include('Invoice_App.urls')),

]
