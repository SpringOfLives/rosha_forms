from django import forms

class AgeEligibilityForm(forms.Form):
    """Form for Age-based eligibility criteria"""
    
    age_limit_type = forms.ChoiceField(
        choices=[
            ('Min', 'อายุต่ำสุด'),
            ('Max', 'อายุสูงสุด'),
        ],
        widget=forms.RadioSelect,
        required=False,
        label="ประเภทของอายุ"
    )

    age_years = forms.IntegerField(
        required=False,
        label="จำนวนปี"
    )


class ComplexClassEligibilityForm(forms.Form):
    """Form for Complex Class-based eligibility criteria"""
    
    cls_category = forms.CharField(
        required=False,
        label="หมวดหมู่คลาส",
    )
    
    complx_cls_name = forms.CharField(
        required=False,
        label="ชื่อคลาส",
    )

    min_age_years = forms.IntegerField(
        required=False,
        label="อายุขั้นต่ำ"
    )

    max_age_years = forms.IntegerField(
        required=False,
        label="อายุสูงสุด"
    )
    
    is_group = forms.BooleanField(
        required=False,
        label="เป็นกลุ่มหรือไม่",
    )
