from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from .forms import AuditionForm
from .models import Audition

class AuditionListView(ListView): 

    template_name = "apps/audition/audition_list.html"
    model = Audition

class AuditionCreateView(CreateView): 

    template_name = "apps/audition/audition_form.html"
    form_class = AuditionForm
    success_url = "/"
    
class AuditionUpdateView: ...

class AuditionDeleteView: ...