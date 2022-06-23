# Здесь мы можем отслеживать различные URL адреса.

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), # Панель администратора.
    path('', include('main.urls')),
    path('products/', include('products.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
