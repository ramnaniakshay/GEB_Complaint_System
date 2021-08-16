from django import forms
from GC.models import UserD

class UserDForm(forms.ModelForm):
    class Meta:
        model = UserD
        fields = "__all__"