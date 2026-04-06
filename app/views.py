from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    
class PessoaView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        return render(request, 'pessoa.html', {'pessoas': pessoas})
    
class OcupacaoView(View):
    def get(self, request, *args, **kwargs):
        ocupacoes = Ocupacao.objects.all()
        return render(request, 'ocupacao.html', {'ocupacoes': ocupacoes})
    
class AvaliacaoView(View):
    def get(self, request, *args, **kwargs):
        avaliacoes = Avaliacao.objects.all()
        return render(request, 'avaliacao.html', {'avaliacoes': avaliacoes})
    
class AvaliacaoTipoView(View):
    def get(self, request, *args, **kwargs):
        avaliacoesTipo = AvaliacaoTipo.objects.all()
        return render(request, 'avaliacaotipo.html', {'avaliacoestipo': avaliacoesTipo})
    
class InstituicaoEnsinoView(View):
    def get(self, request, *args, **kwargs):
        instituicaoensino = InstituicaoEnsino.objects.all()
        return render(request, 'instituicaoensino.html', {'instituicaoensino': instituicaoensino})
    
class AreaSaberView(View):
    def get(self, request, *args, **kwargs):
        areasaber = AreaSaber.objects.all()
        return render(request, 'areasaber.html', {'areasaber': areasaber})
    
class CursoView(View):
    def get(self, request, *args, **kwargs):
        cursos = Curso.objects.all()
        return render(request, 'curso.html', {'cursos': cursos})

class TurmaView(View):
    def get(self, request, *args, **kwargs):
        turmas = Turma.objects.all()
        return render(request, 'turma.html', {'turmas': turmas})
    
class DisciplinaView(View):
    def get(self, request, *args, **kwargs):
        disciplinas = Disciplina.objects.all()
        return render(request, 'disciplina.html', {'disciplinas': disciplinas})
    
class MatriculaView(View):
    def get(self, request, *args, **kwargs):
        matriculas = Matricula.objects.all()
        return render(request, 'matricula.html', {'matriculas': matriculas})
    
class FrequenciaView(View):
    def get(self, request, *args, **kwargs):
        frequencias = Frequencia.objects.all()
        return render(request, 'frequencia.html', {'frequencias': frequencias})
    
class TurnosView(View):
    def get(self, request, *args, **kwargs):
        turnos = Turnos.objects.all()
        return render(request, 'turnos.html', {'turnos': turnos})
    
class UFview(View):
    def get(self, request, *args, **kwargs):
        ufs = UF.objects.all()
        return render(request, 'unidfederativa.html', {'ufs': ufs})
    
class CidadeView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})
    
class OcorrenciaView(View):
    def get(self, request, *args, **kwargs):
        ocorrencias = Ocorrencia.objects.all()
        return render(request, 'ocorrencia.html', {'ocorrencias': ocorrencias})
    
class CursoDisciplinaView(View):
    def get(self, request, *args, **kwargs):
        cursodisciplina = CursoDisciplina.objects.all()
        return render(request, 'cursodisciplina.html', {'cursodisciplina': cursodisciplina})