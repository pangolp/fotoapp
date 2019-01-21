from django.db import models

# Create your models here.

class Materia(models.Model):
	nombre = models.CharField(max_length=500)

	class Meta:
		verbose_name = "Materia"
		verbose_name_plural = "Materias"


class Carrera(models.Model):
	nombre = models.CharField(max_length=50)

	class Meta:
		verbose_name = "Carrera"
		verbose_name_plural = "Carreras"


class Comision(models.Model):
	nombre = models.CharField(max_length=50)
	carrera = models.ForeignKey('Carrera', on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Comision"
		verbose_name_plural = "Comisiones"


class Docente(models.Model):
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	email = models.EmailField(null=True, blank=True)

	class Meta:
		verbose_name = "Docente"
		verbose_name_plural = "Docentes"


class Tipo(models.Model):
	nombre = models.CharField(max_length=50)

	class Meta:
		verbose_name = "Tipo"
		verbose_name_plural = "Tipos"


class Apunte(models.Model):

	#codigo = models.CharField(max_length=50)
	nombre = models.CharField(max_length=500)
	materia = models.ManyToManyField('Materia')
	docente = models.ManyToManyField('docente')
	comision = models.ManyToManyField('Comision')
	tipo = models.ForeignKey('Tipo', on_delete=models.CASCADE)
	hojas = models.PositiveIntegerField()
	anillado = models.BooleanField()
	precio = models.FloatField()


	class Meta:
		verbose_name = "Apunte"
		verbose_name_plural = "Apuntes"