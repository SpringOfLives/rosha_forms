from django import forms
from django.db import models
from django.forms.widgets import SplitDateTimeWidget

from ..models import Audition
from config.mixins import FormMixins
from ..utils import ELIGIBILITY_TYPE
from .extra_forms import AgeEligibilityForm, ComplexClassEligibilityForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Field, Div


class AuditionForm(FormMixins, forms.ModelForm):

    elig_type = forms.ChoiceField(
        choices=ELIGIBILITY_TYPE,
        widget=forms.RadioSelect,
    )
    
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
        
        # เพิ่ม fields จาก AgeEligibilityForm
        age_form = AgeEligibilityForm()
        for field_name, field in age_form.fields.items():
            self.fields[field_name] = field
        
        # เพิ่ม fields จาก ComplexClassEligibilityForm
        complx_cls_form = ComplexClassEligibilityForm()
        for field_name, field in complx_cls_form.fields.items():
            self.fields[field_name] = field

        self.helper = FormHelper()
        self.helper.form_class = "w-4/5"
        self.helper.label_class = "mb-0.5"
        submit_text = "Update" if self.instance.pk else "Submit"
        
        self.helper.layout = Layout(
            HTML("""<h4 class='text-primary-700 underline capitalize{% if not form.instance.pk %} mb-20{% else %} mb-6{% endif %}'>{% if not form.instance.pk %}Create Audition Form{% else %} Update Audition{% endif %}</h4>
                    {% if form.instance.pk %}<h6 class='text-primary-700 mb-20'>{{ audition.name }}</h6>{% endif %}"""),
            Field("name", css_class="w-full input-primary py-4"),
            Field("elig_type", template="audition/layout/radioselect.html"),
            Div(
                Field("age_limit_type", template="audition/layout/radioselect.html"),
                Field("age_years", css_class="input-primary w-full"),
                css_id="age_form"
            ),
            Div(
                Field("cls_category", "complx_cls_name", "min_age_years", "max_age_years", css_class="input-primary w-full"),
                Field("is_group"),
                css_id="complx_form"
            ),
            Field("instrument"),
            Field("elig_crit", css_class="hidden"),
            Field(
                "deadline",
                "annc_dt",
                "conc_dt",
                template="crispy_tailwind/datetime_input.html",
            ),
            Field("poster", template="crispy_tailwind/file_input.html", wrapper_class="cursor-pointer bg-secondary-200/50 hover:bg-secondary-200 text-primaty-600 font-semibold px-6 py-3 rounded-lg shadow-sm transition flex justify-center items-center gap-2 w-1/2 transition duration-500 ease-linear"),
            
            Submit("submit", submit_text, css_class="btn btn-primary btn-xl w-1/4 mx-auto mt-32"),
        )

    def clean(self):
        cleaned_data = super().clean()
        eligibility_type = cleaned_data.get("elig_type")

        if eligibility_type == "AGE_FORM":
            cleaned_data["elig_crit"] = {
                "age_limit_type": cleaned_data.get("age_limit_type"),
                "age_years": cleaned_data.get("age_years"),
            }

        elif eligibility_type == "CLASS_FORM":
            cleaned_data["elig_crit"] = {
                "complex_cls": [
                    {
                        "category": cleaned_data.get("cls_category"),
                        "name": cleaned_data.get("complx_cls_name"),
                        "min_age_years": cleaned_data.get("min_age_years"),
                        "max_age_years": cleaned_data.get("max_age_years"),
                        "is_group": cleaned_data.get("is_group"),
                    }
                ],
            }

        return cleaned_data

