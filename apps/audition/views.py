from django.views.generic import (
    ListView,
    CreateView,
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

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     attrs = [a for a in dir(self) if not a.startswith("__")]
    #     print("Custom attributes/methods of this view:")
    #     for attr in attrs:
    #         print("-", attr)
    #     return queryset
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)

    #     print("Coontext data keys:", context.keys())
    #     for key, val in context.items():
    #         print(f"- {key}: {val}")

    #     return context


class AuditionCreateView(CreateView):
    template_name = "apps/audition/audition_form.html"
    form_class = AuditionForm
    success_url = reverse_lazy("audition:audition-list")


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
