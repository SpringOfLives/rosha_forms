from django import forms
from .models import Auditioner
from config.mixins import FormMixins

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Field, Column, Row


class AuditionerForm(FormMixins, forms.ModelForm):
    class Meta:
        model = Auditioner
        fields = "__all__"

        placeholders = {
            "name": "Your full name",
            "phone": "Your phone number",
            "instrument": "Musical instrument for performance",
            "email": "Your email",
            "birthdate": "Birthdate",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = "w-full mt-24"
        self.helper.label_class = "mb-0.5"
        self.helper.layout = Layout(
            HTML("<h5 class='text-primary-700'>{{audition.name|capfirst}} Form</h5>"),
            Field(
                "name",
                "nationality",
                "phone",
                "email",
                css_class="w-full input-primary",
            ),
            Field("instrument", css_class="w-full input-primary"),
            Field(
                "birthdate",
                template="crispy_tailwind/date_input.html",
            ),
            Submit("submit", "Submit", css_class="button btn-primary mt-8 mx-auto"),
        )
