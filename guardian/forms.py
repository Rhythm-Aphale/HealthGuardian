from django import forms

class MedicalQueryForm(forms.Form):
    user_input = forms.CharField(
        label='Describe your medical concern',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Example: I have been experiencing headaches and dizziness for the past three days...'
        })
    )