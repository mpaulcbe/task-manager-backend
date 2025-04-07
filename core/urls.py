from django.contrib import admin
from django.urls import path, include
from .views import homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),
    path('', homepage),  # 👈 This makes the homepage visible
]
