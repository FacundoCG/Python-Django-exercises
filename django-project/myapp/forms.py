import datetime
from django import forms

class FormularioCurso(forms.Form):
    nombre = forms.CharField(label="Nombre del curso",max_length=100)
    inscriptos = forms.IntegerField(label="Inscriptos")
    descripcion = forms.CharField(label="Descripción", max_length=100, required=False, initial="Curso de programación", help_text="Modifique la descripción")
    comentarios = forms.CharField(label="Comentario", widget=forms.Textarea, required=False)
    
    importe = forms.DecimalField(label="Importe")
    es_oo = forms.BooleanField(label="¿Es en español?", required=False)

    Turnos = ((1,"Mañana"),(2, "Tarde"),(3, "Noche"))
    turno = forms.ChoiceField(label="Turno", choices=Turnos)

    #fecha_inicio = forms.DateField(label="Fecha Inicio", input_formats=["%d/%m/%Y"])
    fecha_inicio = forms.DateField(label="Fecha Inicio", widget=forms.DateInput(attrs={"type":"date"}))

    FechasDelCurso = ['2020','2021','2022',]
    fecha_nacimiento = forms.DateField(label="Años en los que hubo curso:", widget=forms.SelectDateWidget(years=FechasDelCurso))
    fecha_vencimiento = forms.DateField(label="Fecha Vecimiento", widget=forms.DateInput(attrs={"type":"date"}), help_text="Ingrese una fecha entre hoy y 4 semanas")
    target_email = forms.EmailField()
    
    def clean_importe(self):
        data = self.cleaned_data["importe"]
        if float(data) > 100:
            raise forms.ValidationError(("El importe no debe ser mayor a 100"))
        return data
    
    def clean_target_email(self):
        data = self.cleaned_data["target_email"]
        dom_validos = ["@outlook.com", "@gmail.com", "@yahoo.com",]
        for valido in dom_validos:
            if valido in data:
                break
        else:
            raise forms.ValidationError(("Email no permitido"))
        return data
    
    def clean_fecha_vencimiento(self):
        data = self.cleaned_data["fecha_vencimiento"]
        if data < datetime.date.today():
            raise forms.ValidationError(("Fecha Invalida menor a la fecha actual"))
        if data > datetime.date.today()+datetime.timedelta(weeks=4):
            raise forms.ValidationError(("Fecha Invalida mayor a 4 semanas"))
        return data

class FormularioCursoORM(forms.Form):
    nombre = forms.CharField(label="Nombre del curso",max_length=100)
    inscriptos = forms.IntegerField(label="Inscriptos")