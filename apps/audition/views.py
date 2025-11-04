from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .forms import AuditionForm
from apps.auditioner.forms import AuditionerForm
from .models import Audition


class AuditionListView(ListView):
    template_name = "apps/audition/audition_list.html"
    model = Audition

class AuditionCreateView(CreateView):
    template_name = "apps/audition/audition_form.html"
    form_class = AuditionForm
    success_url = reverse_lazy("audition:audition-list")


class AuditionDetailView(DetailView):
    model = Audition
    template_name = "apps/audition/audition_detail.html"

class AuditionUpdateView(UpdateView):
    model = Audition
    form_class = AuditionForm
    template_name = 'apps/audition/audition_form.html'
    
    def get_success_url(self):
        return reverse_lazy('audition:audition-detail', kwargs={"pk": self.get_object().id})


class AuditionDeleteView(DeleteView):
    model = Audition
    success_url = reverse_lazy("audition:audition-list")

    """Overide get method for Creating DeleteView without templates_name"""
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
