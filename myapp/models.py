from django.db import models

# Create your models here.

class Persona(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def full_name(self):
        return self.first_name + " " + self.last_name
        
    class Meta:
        abstract = True

class Profesor(Persona):

    salario = models.FloatField(default=0)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ['id', 'first_name', 'last_name'], name = 'primary_key_profesor'
            )
        ]

class Salon(models.Model):
    aula = models.CharField(max_length=2)
    hora_entrada = models.TimeField()
    profesor_id = models.ForeignKey(Profesor, on_delete = models.CASCADE, default = 0) 


class Alumno(Persona):
    idSalon = models.ForeignKey(Salon, on_delete = models.CASCADE) 
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ['id', 'first_name', 'last_name'], name = 'primary_key_alumno'
            )
        ]

class OrderedAlum(Alumno):
    class Meta:
        ordering = ["last_name"]
        proxy = True

class Evaluacion(models.Model):
    hora_fecha = models.DateTimeField()
    curso = models.CharField(max_length=30)
    evaluador = models.CharField(max_length=50)

    class Meta:
        abstract = True

class Examen_Final(Evaluacion):
    duracion = models.IntegerField()
    n_preguntas = models.IntegerField()
    puntaje_total = models.IntegerField()

    def puntaje_pregunta(self):
        return self.puntaje_total / n_preguntas


class Proyecto(Evaluacion):
    tema_proyecto = models.CharField(max_length=100)
    n_grupos = models.IntegerField()

class OrderedNameProject(Proyecto):
    class Meta:
        proxy = True
        ordering = ["tema_proyecto"]