from django.contrib import admin
from .models import Curso, Aula, Reserva, Gafa

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'clase')

class AulaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'num_gafas', 'aforo')

class ReservaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'get_curso', 'num_personas', 'num_gafas', 'get_aula', 'fecha_hora', 'fecha_inicio', 'fecha_fin')
    def get_curso(self, obj):
        return obj.curso.nombre
    def get_aula(self, obj):
        return obj.aula.nombre

class GafaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'get_nombre')
    def get_nombre(self, obj):
        return obj.aula.nombre

# Register your models here.
admin.site.register(Curso, CursoAdmin)
admin.site.register(Aula, AulaAdmin)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(Gafa, GafaAdmin)