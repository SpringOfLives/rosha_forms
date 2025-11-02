from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
)
from django.urls import reverse_lazy

from .forms import AuditionerForm
from .models import Auditioner

class AuditionerListView(ListView):
   
   template_name = "apps/auditioner/auditioner_list.html"
   model = Auditioner