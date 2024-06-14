from django.db import models

class Eleve(models.Model):
    prenom = models.CharField(max_length=30)
    nom= models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.prenom} {self.last_name}"

class Cour(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Enregistrement(models.Model):
    student = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    course = models.ForeignKey(Cour, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} enrolled in {self.course}"