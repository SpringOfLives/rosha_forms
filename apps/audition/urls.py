from django.urls import path
from . import views

app_name = "audition"

urlpatterns = [
    path("", views.AuditionListView.as_view(), name="audition-list"),
    path("audition_form/", views.AuditionCreateView.as_view(), name="audition-form"),
    path("<int:pk>/", views.AuditionDetailView.as_view(), name="audition-detail"),
    path("audition_update/<int:pk>", views.AuditionUpdateView.as_view(), name="audition-update"),
    path("audition_delete/<int:pk>/", views.AuditionDeleteView.as_view(), name="audition-delete")
]
