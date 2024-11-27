from django.db import models
from django import forms
from stdimage.models import StdImageField
from django.contrib.auth.models import AbstractUser 

class Mercados(AbstractUser ):

    email_Mercado = models.EmailField('email_Mercado', null=False, blank=True, primary_key=True, unique=True)
    nome = models.CharField('nome', max_length=100, null=False,  blank=True)
    endereco = models.CharField('endereco', max_length=255, null=False, blank=True)
    telefone = models.CharField('telefone', max_length=15, null=False,  blank=True)
    imagem = StdImageField('Imagem', upload_to='mercados', null=False, variations={'thumb': (125, 125)}, blank=True)
    link_whatsapp = models.CharField('link_whatsapp', max_length=600, null=False, blank=True)
    password = models.CharField('password', max_length=128, null=False, blank=True)  # Armazene a senha de forma segura
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='mercados',  # Specify a unique related name
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='mercados_permissions',  # Specify a unique related name
        blank=True,
    )

    username = None  # Remove o campo username
    first_name = None  # Remove o campo first_name
    last_name = None  # Remove o campo last_name
    USERNAME_FIELD = 'email_Mercado'
    REQUIRED_FIELDS = ['email_Mercado']  # Campos ob
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = 'Mercado'
        verbose_name_plural = 'Mercados'
    
class Cestas(models.Model):

    imagem = StdImageField('Imagem', upload_to='cestas', variations={'thumb': (125, 125)}, blank=True)
    nome = models.CharField('Nome', max_length=100, blank=True)
    preco = models.DecimalField('Preço', max_digits=6, decimal_places=2, blank=True)
    tamanho = models.DecimalField('Tamanho', max_digits=3, decimal_places=1, blank=True)
    descricao = models.CharField('Descrição', max_length=300, blank=True)
    mercado = models.ForeignKey(Mercados, on_delete=models.CASCADE, related_name='cestas', blank=True, null=True)
    def __str__(self):

        return self.nome  


class Usuario(AbstractUser ):
    email = models.EmailField('email', blank=False, unique=True, primary_key=True)
    nome = models.CharField('nome', max_length=100, blank=True, null=False, unique=True)
    password = models.CharField('password', max_length=128, blank=True)  # Armazene a senha de forma segura

    username = None  # Remove o campo username

    first_name = None  # Remove o campo first_name

    last_name = None  # Remove o campo last_name

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['nome']  # Campos ob
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'