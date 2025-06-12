# predictor/views.py

from django.shortcuts import render
from .forms import InputForm
import joblib
import numpy as np

model = joblib.load('../diabetes_model/random_forest_model.pkl')

def predictor_view(request):
    result = None
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            data = np.array([[form.cleaned_data['age'],
                              form.cleaned_data['hypertension'],
                              form.cleaned_data['heart_disease'],
                              form.cleaned_data['bmi'],
                              form.cleaned_data['HbA1c_level'],
                              form.cleaned_data['blood_glucose_level']]])
            prediction = model.predict(data)
            result = 'Positive' if prediction[0] == 1 else 'Negative'
    else:
        form = InputForm()

    return render(request, 'index.html', {'form': form, 'result': result})
