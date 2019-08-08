from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('backend.debtors.urls')),

    # http://localhost:8000/api/admin/
    path('api/admin/', admin.site.urls),

    # http://localhost:8000/api/
    path('api/auth/', include('backend.authentication.urls')),
]


