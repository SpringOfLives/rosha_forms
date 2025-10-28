from django.urls import path
from . import views

app_name = "audition"

urlpatterns = [
    path("", views.AuditionListView.as_view(), name="audition-list"),
    path("audition_form/", views.AuditionCreateView.as_view(), name="audition-form"),
    path("<pk>/", views.AuditionDetailView.as_view(), name="audition-detail")
]
