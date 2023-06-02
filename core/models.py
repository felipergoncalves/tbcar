from django.db import models
import math

# Create your models here.
from django.db.models import DO_NOTHING
class Tabela(models.Model):
    descricao = models.CharField(max_length=50, verbose_name='Descrição')
    valor = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Valor")

    def __str__(self):
        return f'{self.descricao} - {self.valor}'

    class Meta:
        verbose_name_plural = 'Tabelas'

class Cliente(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    endereco = models.CharField(max_length=100, blank=True, null=True, verbose_name='Endereço')
    complemento = models.CharField(max_length=50, blank=True, null=True, verbose_name='Complemento')
    bairro = models.CharField(max_length=50, blank=True, null=True, verbose_name='Bairro')
    cidade = models.CharField(max_length=100, blank=True, null=True, verbose_name='Cidade')
    fone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Telefone')
    email = models.EmailField(max_length=100, verbose_name='E-mail')
    foto = models.ImageField(upload_to='cliente_foto', blank=True, null=True, verbose_name='Imagem')

    def __str__(self):
        return f'{self.nome}'


class Marca(models.Model):
    nome = models.CharField(max_length=30, verbose_name='Nome')
    url = models.URLField(blank=True, null=True, verbose_name='URL')
    logo = models.ImageField(upload_to='marca_foto', blank=True, null=True, verbose_name='Logo')

    def __str__(self):
        return f'{self.nome}'


class Veiculo(models.Model):
    placa = models.CharField(max_length=10, verbose_name='Placa')
    modelo = models.CharField(max_length=50, blank=True, null=True, verbose_name='Modelo')
    cor = models.CharField(max_length=50, blank=True, null=True, verbose_name='Cor')
    marca_id = models.ForeignKey(to=Marca, on_delete=models.CASCADE, verbose_name='Marca')
    ano = models.IntegerField(default=2023, blank=True, null=True, verbose_name='Ano')
    cliente_id = models.ForeignKey(to=Cliente, on_delete=models.CASCADE, verbose_name='Cliente')
    foto = models.ImageField(upload_to='veiculo_foto', blank=True, null=True, verbose_name='Foto')

    def __str__(self):
        return f'{self.modelo} - ({self.placa}) - {self.cor} - ({self.cliente_id})'

    class Meta:
        verbose_name_plural = 'Veículos'


class Mensalista(models.Model):
    id_veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, verbose_name='Veiculo')
    id_tabela = models.ForeignKey(Tabela, on_delete=models.CASCADE, verbose_name='Tabela')
    observacoes = models.TextField(blank=True, null=True, verbose_name="Obs.")

    class Meta:
        verbose_name_plural = "Mensalistas"

    def __str__(self):
        return f'{self.id_veiculo}'


class Rotativo(models.Model):
    id_veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, verbose_name='Veiculo')
    id_tabela = models.ForeignKey(Tabela, on_delete=models.CASCADE, verbose_name='Tabela')
    entrada = models.DateTimeField(auto_now=False, verbose_name='Hora de Entrada')
    saida = models.DateTimeField(auto_now=False, verbose_name='Hora de Saida', blank=True, null=True)
    total = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Valor Total', blank=True, null=True)
    pago = models.BooleanField(verbose_name="Pago", default=False)
    observacoes = models.TextField((""))

    class Meta:
        verbose_name_plural = "Rotativos"

    def __str__(self):
        return f'{self.id_veiculo} - {self.id_tabela}'

    def calcula_total(self):
        if self.saida:
            hora = (self.saida - self.entrada).total_seconds()/3600
            obj = Tabela.objects.get(id=self.id_tabela.pk)
            if hora <= 0.5:
                self.total = obj.valor/2
            else:
                self.total = math.ceil(hora) * obj.valor
            return self.total
        return 0.0