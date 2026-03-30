from django.db import models


class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")
    
    def __str__(self):
        return f"{self.nome}, {self.uf}"
    
    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"


class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Ocupação")
    
    def __str__(self):
        return {self.nome}
    
    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"


class Turma(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Turma")
    
    def __str__(self):
        return {self.nome}
    
    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"


class AreaSaber(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Area do Saber")
    
    def __str__(self):
        return {self.nome}
    
    class Meta:
        verbose_name = "Area do saber"
        verbose_name_plural = "Areas dos saberes"


class Turnos(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Turno")

    def __str__(self):
        return {self.nome}
    
    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"


class AvaliacaoTipo(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Tipo da Avaliação")

    def __str__(self):
        return {self.nome}
    
    class Meta:
        verbose_name = "Tipo da Avaliação"
        verbose_name_plural = "Tipos da Avaliação"


class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Pessoa")
    pai = models.CharField(max_length=100, verbose_name="Nome do Pai")
    mae = models.CharField(max_length=100,verbose_name="Nome da Mãe")

    data_nasc = models.DateField(verbose_name="Data de Nascimento")

    email = models.CharField(max_length=100, verbose_name="Email")

    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade da Pessoa")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE, verbose_name="Ocupação da Pessoa")

    def __str__(self):
        return {self.nome}
    
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"


class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Instituição")
    site = models.CharField(max_length=100, verbose_name="Site da Instituição")
    
    telefone = models.IntegerField(verbose_name="Telefone")
    
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade da Instituição")

    def __str__(self):
        return {self.nome}
    
    class Meta:
        verbose_name = "Instituição de Ensino"
        verbose_name_plural = "Instituições de Ensino"


class Curso(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Curso")
    
    carga_horaria_total = models.IntegerField(verbose_name="Carga Horária Total")
    duracao_meses = models.IntegerField(verbose_name="Duração Meses")

    areasaber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="Area Saber")
    instituicaoensino = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name="Instituição de Ensino")

    def __str__(self):
        return {self.nome}
    
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

class Disciplina(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Disciplina")
    areasaber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="Area do Saber")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, default="0" ,verbose_name="Curso")

    def __str__(self):
        return {self.nome}
    
    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"

class Matricula(models.Model):
    instituicaoensino = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name="Instituição de Ensino")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")

    data_inicio = models.DateField(verbose_name="Data de Início")
    data_previsao_termino = models.DateField(verbose_name="Data de Previsão de Término")

    def __str__(self):
        return f'{self.pessoa}, {self.curso}, {self.instituicaoensino}'
    
    class Meta:
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"

class Avaliacao(models.Model):
    descricao = models.TextField(max_length=300, verbose_name="Descrição")

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    avaliacaotipo = models.ForeignKey(AvaliacaoTipo, on_delete=models.CASCADE, verbose_name="Tipo da Avaliação")

    def __str__(self):
        return {self.descricao}
    
    class Meta: 
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"


class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")
    
    numero_faltas = models.IntegerField(verbose_name="Número de Faltas")

    def __str__(self):
        return {self.numero_faltas}
    
    class Meta:
        verbose_name = "Frequência"
        verbose_name_plural = "Frequências"


class CursoDisciplina(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    
    carga_horaria = models.IntegerField(verbose_name="Carga Horária")

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    
    periodo = models.CharField(max_length=100, verbose_name="Período")

    def __str__(self):
        return f'{self.curso}, {self.disciplina}'
    
    class Meta:
        verbose_name = "Curso Disciplina"
        verbose_name = "Cursos Disciplinas"


class Ocorrencia(models.Model):
    descricao = models.TextField(max_length=300, verbose_name="Descrição")
    
    data = models.DateField(verbose_name="Data")

    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")

    def __str__(self):
        return {self.descricao}
    
    class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"