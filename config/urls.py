from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("audition/", include("apps.audition.urls")),

    # For testing
    path('', TemplateView.as_view(template_name="base.html"))
] + debug_toolbar_urls()
