from django import forms
from .models import Mercados, Usuario, Cestas
from django.contrib.auth.forms import UserCreationForm

class MercadosModelForm(forms.ModelForm):
    class Meta:
        model = Mercados
        fields = ['nome', 'endereco', 'telefone', 'email_Mercado', 'imagem', 'link_whatsapp', 'password']
 

class UsuarioModelForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'password']
     


class CestasModelForm(forms.ModelForm):
    class Meta:
        model = Cestas
        fields = ['nome', 'imagem', 'preco', 'tamanho', 'descricao']