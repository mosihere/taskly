from django.contrib import admin
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('task.api.urls')),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
] + debug_toolbar_urls()
