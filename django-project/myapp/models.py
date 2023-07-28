from django.db import models

# Create your models here.
class Curso (models.Model):
    nombre = models.CharField(max_length=100)
    inscriptos = models.IntegerField()
    creado = models.DateField(auto_now_add=True)
    actualizado = models.DateField(auto_now=True)

#Comandos para trabajar con models en: python .\manage.py shell
#from myapp.models import Curso
#curso_oracle = Curso(nombre="Oracle", inscriptos = 30)
#curso_oracle.save() Inserto el objeto en la tabla. Esta es una forma de crear registros en la BBDD
#Curso.objects.create(nombre="PHP", inscriptos = 50) Directamente creo el registro en la BBDD
#Curso.objects.bulk_create([Curso(nombre="HTML5",inscriptos=100), Curso(nombre="Cobol", inscriptos=45)]) Con este método puedo insertar varios registros a la vez en la BBDD

# curso_oracle.id   Esta línea me devuelve el id de la fila
# cursos = Curso.objects.all() Obtengo todos los objetos (registros) que tiene la tabla
# cursos[0].nombre  Esta línea me devuelve el nombre del primer registro
# for i in cursos:
    # print(i.id, i.nombre, i.inscriptos)   Así imprimo todos los registros de la tabla

# c_python = Curso.objects.get(id=1) Obtengo el registro con id igual a 1
# c_curso = Curso.objects.get(nombre="Java") Obtengo el registro con nombre igual a Java
# cursos2 = Cursos.objects.values() 
# list(cursos2) Me devuelve una lista compuesta de diccionarios que tienen los valores de los registros

# Curso.objects.filter(id=4).delete() Borro el objeto con id igual a 4
# Curso.objects.filter(nombre__startswith="P").values() Devuelve los registros que su nombre empieza con P
# Curso.objects.filter(nombre__startswith="P").count()

# f1 = Curso.objects.filter(nombre__startswith="P") | Curso.objects.filter(nombre__startswith="C")
# f1.values() Obtengo los valores de todos los objetos que cumplan con alguna de las dos condiciones anteriores

# f2 = Curso.objects.filter(nombre__contains="o")
# f2.values() Devuelve todos los registros en que su nombre tenga una o

# f3 = Curso.objects.all().order_by('nombre').values() Ordena todos los objetos alfabeticamente
# f4 = Curso.objects.all().order_by('-nombre', 'inscriptos').values() Ordena todos los objetos de modo inverso al alfabeticamente, y por la cantidad de inscriptos

# f5 = Curso.objects.filter(inscriptos__gte=65).values() Obtengo todos los registros con inscriptos mayor o igual a 65
# f6 = Curso.objects.filter(inscriptos__range=(20,65)).values() Obtengo todos los registros con inscriptos entre el rango de 20 y 65

# f7 = Curso.objects.all().filter(nombre__in=('Python','Java')).values() Obtengo todos los registros en que sus nombre figure la palabra Python o Java

# f8 = Curso.objects.all()
# str(f8.query) Esta línea me devuelve el SQL que se utilizó para cumplir con el pedido de objects.all