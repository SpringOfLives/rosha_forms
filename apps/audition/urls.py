from django.urls import path
from . import views

app_name = "audition"

urlpatterns = [
    path("audition_form/", views.AuditionCreateView.as_view(), name="audition-form"),
]
