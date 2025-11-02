from django.urls import path
from . import views

app_name = "auditioner"

urlpatterns = [
   path("", views.AuditionerListView.as_view(), name="auditioner-list"),
]
