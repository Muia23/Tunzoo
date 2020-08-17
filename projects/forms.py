from django import forms
from .models import Kura

class PigaKura(forms.ModelForm):
    class Meta:
        model = Kura
        fields = [ 'design','usability','content']
            