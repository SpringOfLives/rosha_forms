from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("audition/", include("apps.audition.urls")),
    path("auditioner/", include("apps.auditioner.urls")),
    # For testing
    path("", TemplateView.as_view(template_name="base.html")),
    path("__reload__/", include("django_browser_reload.urls")),
] + debug_toolbar_urls()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
