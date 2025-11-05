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
        self.helper.form_class = "py-12 px-24"
        self.helper.label_class = "mb-0.5"
        submit_text = "Update" if self.instance.pk else "Submit"
        self.helper.layout = Layout(
            HTML("""<h4 class='text-primary-700 underline capitalize mb-6'>
                    {% if not form.instance.pk %}Register Form{% else %}Update Form{% endif %}</h4>
                    {% if not form.instance.pk %}<h6 class='text-primary-700 mb-20 capitalize'>{{ audition_name }}</h6>{% endif %}"""),
            Field(
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
            Submit("submit", submit_text, css_class="btn bg-primary-700 cursor-pointer hover:bg-primary-800 btn-xl w-1/4 mx-auto mt-32"),
        )
