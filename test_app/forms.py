from django import forms
from test_app.models import Test

class NewTestForm(forms.ModelForm):
  class Meta():
    model = Test
    fields = '__all__'
