from django.urls import path
from . import views

app_name = "auditioner"

urlpatterns = [
   path("", views.AuditionerListView.as_view(), name="auditioner-list"),
   path("auditioner_form/<int:pk>/", views.AuditionerCreateView.as_view(), name="auditioner-create"),
   path("auditioner_update/<int:pk>/", views.AuditionerUpdateView.as_view(), name="auditioner-update"),
   path("auditioner_delete/<int:pk>/", views.AuditionerDeleteView.as_view(), name="auditioner-delete")
]
