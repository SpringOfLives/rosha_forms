from django import forms
from django.db import models
from django.forms.widgets import SplitDateTimeWidget

from .models import Audition
from config.mixins import FormMixins

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Field, Column, Row


class AuditionForm(FormMixins, forms.ModelForm):
    class Meta:
        model = Audition

        fields = "__all__"

        field_classes = {
            "deadline": forms.SplitDateTimeField,
            "annc_dt": forms.SplitDateTimeField,
            "conc_dt": forms.SplitDateTimeField,
        }

        widgets = {
            "deadline": SplitDateTimeWidget(),
            "annc_dt": SplitDateTimeWidget(),
            "conc_dt": SplitDateTimeWidget(),
        }

        placeholders = {
            "deadline": ["Select ", "hh:mm eg. 16:30"],
            "annc_dt": ["Select date", "hh:mm eg. 16:30"],
            "conc_dt": ["Select date", "hh:mm eg. 16:30"],
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = "w-4/5"
        self.helper.label_class = "mb-0.5"
        self.helper.layout = Layout(
            HTML("<h1 class='text-primary-700 underline'>Audition Form</h1>"),
            Field("name", css_class="w-full input-primary"),
            Field(
                "deadline",
                "annc_dt",
                "conc_dt",
                template="crispy_tailwind/datetime_input.html",
            ),
            Field("poster", template="crispy_tailwind/file_input.html"),
            Submit("submit", "Submit", css_class="button btn-primary mt-8 mx-auto"),
        )
