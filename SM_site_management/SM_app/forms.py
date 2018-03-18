from django import forms
from django.core.exceptions import ValidationError
from .models import *



class AddSitesForm(forms.ModelForm):
    class Meta:
        model = Sites
        fields = '__all__'


class AddContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        exclude = ['sites']

class AddSitesContactsForm(forms.ModelForm):
    class Meta:
        model = SitesContacts
        exclude = ['contacts']


class AddMaterialsForm(forms.ModelForm):
    class Meta:
        model = Materials
        fields = '__all__'



class AddMachinesForm(forms.ModelForm):
    class Meta:
        model = Machines
        fields = '__all__'


class AddContractorsForm(forms.ModelForm):
    class Meta:
        model = Contractors
        fields = '__all__'


class SearchMaterialsForm(forms.Form):
    name = forms.CharField(label='Nazwa materiału', max_length=100, required=False)


class SearchMachinesForm(forms.Form):
    name = forms.CharField(label='Maszyna', max_length=100, required=False)

