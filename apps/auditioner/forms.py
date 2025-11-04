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
        self.helper.label_class = "mb-0.5"
        self.helper.layout = Layout(
            HTML("<h6 class='text-primary-700 capitalize'>{% if not form.instance.pk %}{{audition_name}} Form{% endif %}</h6>"),Field(
                "name",
                css_class="w-full input-primary",
            ),
            Field(
                "birthdate",
                template="crispy_tailwind/date_input.html",
            ),
            Field(
                "nationality",
                "phone",
                "email",
                css_class="w-full input-primary",
            ),
            Field("instrument", css_class="w-full input-primary"),
            Submit("submit", "Submit", css_class="button w-1/4 text-base btn-primary mt-40"),
        )
