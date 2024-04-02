from django import forms
from .models import Val


class TodoForm(forms.ModelForm):
	class Meta:
		model = Val
		fields = "__all__"
