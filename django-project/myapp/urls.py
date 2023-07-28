from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("curso/<str:nombre_curso>", views.curso, name="curso"),
    path("cursoORM/<str:nombre_curso>", views.cursoORM, name="cursoORM"),
    path("cursos", views.cursos, name="listaCursos"),
    path("cursos-ORM", views.cursosORM, name="listaCursosORM"),
    path("curso_API", views.curso_API, name="curso_API"),
    path("nuevo_curso", views.nuevo_curso, name="nuevoCurso"),
    path("nuevo_curso-ORM", views.nuevoCursoORM, name="nuevoCursoORM"),
    path("curso_API_ORM", views.cursos_API_ORM, name="curso_API_ORM"),
]