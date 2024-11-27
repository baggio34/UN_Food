from django.contrib.auth.backends import ModelBackend
from .models import Mercados  # Certifique-se de que o caminho está correto

class EmailBackend(ModelBackend):
    def authenticate(self, request, email_Mercado=None, password=None, **kwargs):
        try:
            mercado = Mercados.objects.get(email_Mercado=email_Mercado)
        except Mercados.DoesNotExist:
            return None  # Retorna None se o usuário não existe

        # Verifica se a senha está correta
        if mercado.check_password(password):
            return mercado  # Retorna o usuário se a senha estiver correta
        return None  # Retorna None se a senha estiver incorreta