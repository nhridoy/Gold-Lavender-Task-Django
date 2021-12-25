from django import forms

from mobilephones import models


class BrandForm(forms.ModelForm):
    class Meta:
        model = models.Brand
        fields = '__all__'


class PhoneForm(forms.ModelForm):
    class Meta:
        model = models.Phone
        exclude = ['jan_code']
