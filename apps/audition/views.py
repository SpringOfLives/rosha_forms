from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView, DetailView
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

class AuditionDetailView(DetailView):
    model = Audition
    template_name = "apps/audition/audition_detail.html"

class AuditionUpdateView: ...


class AuditionDeleteView: ...
