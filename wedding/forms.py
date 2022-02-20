from django import forms

from .models import *


class WeddingForm(forms.ModelForm):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['drink'].empty_lable = "ff"

    class Meta:
        model = WeddingData
        # attendance = forms.ModelChoiceField(queryset=Attendance.objects.all(),  to_field_name="to_be"),
        # drink = forms.ModelMultipleChoiceField(queryset=WeddingData.objects.drink_set.all())

        fields = ['attendance', 'name', 'surname', 'housing', 'drink']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'surname': forms.TextInput(attrs={'class': 'form-input'}),
            'attendance': forms.Select(attrs={'class': 'select-field'}),
            'drink': forms.CheckboxSelectMultiple(attrs={'class': 'select-multiple'}),
            'housing': forms.CheckboxInput(attrs={'class': 'checkbox-btn'})
        }
