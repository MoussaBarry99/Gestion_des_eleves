from django import forms
from .models import Eleve, Enregistrement

class StudentForm(forms.ModelForm):
    class Meta:
        model = Eleve
        fields = ['prenom', 'nom', 'email', 'date_de_naissance']

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enregistrement
        fields = ['eleve', 'cours']