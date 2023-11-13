# water_meter_app/forms.py

from django import forms
from .models import MeterReading

class MeterReadingForm(forms.ModelForm):
    class Meta:
        model = MeterReading
        fields = ['reading']