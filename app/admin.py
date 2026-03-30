from django.contrib import admin
from .models import *

class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1
class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1
class DisciplinaInline(admin.TabularInline):
    model = Disciplina
    extra = 1
class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1


class OcupacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [PessoaInline]

class InstituicaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [CursoInline]

class AreadoSaberAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [CursoInline]

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [DisciplinaInline]

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [AvaliacaoInline]

class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [PessoaInline]

admin.site.register(Ocupacao, OcupacaoAdmin)
admin.site.register(InstituicaoEnsino, InstituicaoAdmin)
admin.site.register(Cidade)
admin.site.register(AreaSaber, AreadoSaberAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Turma)
admin.site.register(Avaliacao)
admin.site.register(Turnos)
admin.site.register(Pessoa)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Frequencia)
admin.site.register(Ocorrencia)
admin.site.register(Matricula)
admin.site.register(CursoDisciplina)
admin.site.register(AvaliacaoTipo)