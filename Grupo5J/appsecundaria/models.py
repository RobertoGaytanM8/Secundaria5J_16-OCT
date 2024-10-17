from django.db import models

# Create your models here.
class AlumnoT(models.Model):
    apaterno=models.CharField(max_length=50,verbose_name="Apellido Paterno")
    amaterno=models.CharField(max_length=50,verbose_name="Apellido Materno")
    nombre=models.CharField(max_length=50,verbose_name="Nombre")
    fecha_nacimiento=models.DateField(verbose_name="Fecha de nacimiento", null=False, blank=False)
    fecha_ingreso=models.DateField(verbose_name="Fecha Ingreso", null=False, blank=False)

class Meta:
    db_table="Alumnos"
    verbose_name="Alumno"
    verbose_name_plural="Alumno"

class Frase (models.Model):
    comentario=models.TextField(verbose_name="Comentario", max_length=400)
    Alumno_fk=models.ForeignKey(AlumnoT,on_delete=models.CASCADE)

class Meta:
    db_table="Frase"
    verbose_name="Frase"
    verbose_name_plural="frases"