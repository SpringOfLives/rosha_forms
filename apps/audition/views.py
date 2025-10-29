from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView,
    DetailView,
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
    success_url = "/"


class AuditionDetailView(DetailView):
    model = Audition
    template_name = "apps/audition/audition_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = AuditionerForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  # ดึง Audition object ที่เรากำลังดูอยู่
        form = AuditionerForm(request.POST)
        if form.is_valid():
            auditioner = form.save(commit=False)
            auditioner.audition = self.object
            auditioner.save()
            return redirect(self.request.path)
        context = self.get_context_data()
        context["form"] = form
        return self.render_to_response(context)


class AuditionUpdateView: ...


class AuditionDeleteView: ...
