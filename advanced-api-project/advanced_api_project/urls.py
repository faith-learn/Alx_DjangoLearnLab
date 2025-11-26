from django.contrib import admin
from django.urls import path, include  # must import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # include your app-level URLs
]
