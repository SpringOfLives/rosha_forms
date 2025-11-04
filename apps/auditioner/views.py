from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404

from .forms import AuditionerForm
from .models import Auditioner
from apps.audition.models import Audition


class AuditionerListView(ListView):
   template_name = "apps/auditioner/auditioner_list.html"
   model = Auditioner


class AuditionerCreateView(CreateView):
    model = Auditioner
    form_class = AuditionerForm
    template_name = 'apps/auditioner/auditioner_form.html'
    success_url = reverse_lazy("audition:audition-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get("pk")
        context["audition_name"] = Audition.objects.get(id=pk).name
        return context

    def form_valid(self, form):
        audition_id = self.kwargs.get('pk')
        audition = get_object_or_404(Audition, id=audition_id)
        form.instance.audition = audition

        return super().form_valid(form)


class AuditionerUpdateView(UpdateView):
    model = Auditioner
    form_class = AuditionerForm
    template_name = 'apps/auditioner/auditioner_form.html'
    success_url = reverse_lazy("auditioner:auditioner-list")


class AuditionerDeleteView(DeleteView):
    model = Auditioner
    success_url = reverse_lazy("auditioner:auditioner-list")

    """Overide get method for Creating DeleteView without templates_name"""
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)