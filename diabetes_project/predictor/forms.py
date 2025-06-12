# predictor/forms.py

from django import forms

class InputForm(forms.Form):
    age = forms.FloatField(label='Age')
    hypertension = forms.IntegerField(label='Hypertension (0 or 1)')
    heart_disease = forms.IntegerField(label='Heart Disease (0 or 1)')
    bmi = forms.FloatField(label='BMI')
    HbA1c_level = forms.FloatField(label='HbA1c Level')
    blood_glucose_level = forms.IntegerField(label='Blood Glucose Level')
