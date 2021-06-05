from django import forms
from .models import *


class DjangoModelForm(forms.ModelForm):
    class Meta:
        model = Django
        fields = '__all__'

class JsonModelForm(forms.ModelForm):
    class Meta:
        model = Json
        fields = '__all__'

class RestModelForm(forms.ModelForm):
    class Meta:
        model = Rest
        fields = '__all__'

class HtmlModelForm(forms.ModelForm):
    class Meta:
        model = Html
        fields = '__all__'

class CssModelForm(forms.ModelForm):
    class Meta:
        model = Css
        fields = '__all__'

class BootstrapModelForm(forms.ModelForm):
    class Meta:
        model = Bootstrap
        fields = '__all__'

class PythonModelForm(forms.ModelForm):
    class Meta:
        model = Python
        fields = '__all__'

class JsModelForm(forms.ModelForm):
    class Meta:
        model = Js
        fields = '__all__'
