from django import forms
from .models import Kura,Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name','url','description','screenshot','techs']
        widgets = {
            'techs': forms.CheckboxSelectMultiple(),
        }

class PigaKura(forms.ModelForm):
    class Meta:
        model = Kura
        fields = [ 'design','usability','content']
            