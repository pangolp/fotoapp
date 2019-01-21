from django.contrib				import admin

# Register your models here.


from apps.apuntes.models		import (
										Materia,
										Carrera,
										Comision,
										Docente,
										Tipo,
										Apunte,
										)

admin.site.register(Materia)
admin.site.register(Carrera)
admin.site.register(Comision)
admin.site.register(Docente)
admin.site.register(Tipo)
admin.site.register(Apunte)