from django.shortcuts import render, redirect
from .models import Eleve, Cours, Enregistrement
from .forms import EleveForm, EnrollmentForm

def liste_eleve(request):
    Eleves = Eleve.objects.all()
    return render(request, 'enrollment/liste_eleve.html', {'Eleves': Eleves})

def Eleve_create(request):
    if request.method == 'POST':
        form = EleveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_eleve')
    else:
        form = EleveForm()
    return render(request, 'enrollment/Eleve_form.html', {'form': form})

def enrollment_create(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_eleve')
    else:
        form = EnrollmentForm()
    return render(request, 'enrollment/enrollment_form.html', {'form': form})