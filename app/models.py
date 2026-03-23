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
    nome = models.CharField(max_length=100, verbose_name="Nome da Cidade")
    
    def __str__(self):
        return {self.nome}
    
    class Meta:
        verbose_name = "Ocupacao"
        verbose_name_plural = "Ocupacoes"


class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Ocupação")
    
    def __str__(self):
        return {self.nome}
    
    class Meta:
        verbose_name = "Ocupacao"
        verbose_name_plural = "Ocupacoes"


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