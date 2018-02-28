from django import forms
from .models import *


class AddSitesForm(forms.ModelForm):
    class Meta:
        model  = Sites
        fields = '__all__'


class AddContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'


class AddMaterialsForm(forms.ModelForm):
    class Meta:
        model = Materials
        fields = '__all__'


class AddMachinesForm(forms.ModelForm):
    class Meta:
        model = Machines
        fields = '__all__'


class