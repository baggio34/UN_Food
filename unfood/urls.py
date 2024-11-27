from django.contrib import admin
from django.urls import path
from core.views import Cad_log, Email_redefiniçao, Home, Trocar_senha, login_usuario, Cad_cesta, Cad_mercado, HomeMercado, login_Mercado, carrossel, teste, ver, contato, contato_mercado
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Cad_log, name='Cad_log'),
    path('Email_redefiniçao/', Email_redefiniçao, name='Email_redefiniçao'),
    path('Home/', Home, name='Home'),
    path('Trocar_senha/', Trocar_senha, name='Trocar_senha'),
    path('login/', login_usuario, name='login_usuario'),
    path('Cad_cesta/', Cad_cesta, name='Cad_cesta'),
    path('Cad_mercado/', Cad_mercado, name='Cad_mercado'),
    path('login_Mercado/', login_Mercado, name='login_Mercado'),
    path('HomeMercado/', HomeMercado, name='HomeMercado'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='Cad_cesta.html'), name='login'),
    path('carrossel/', carrossel, name='carrossel'),
    path('teste/', teste, name='teste'),
    path('cad_cesta/', Cad_cesta, name='Cad_cesta'),
    path('ver/', ver, name='ver'),
    path('contato/', contato, name='contato'),
    path('contato/<str:email_mercado>/', contato_mercado, name='contato_mercado')
]


# Adiciona a configuração para servir arquivos de mídia durante o desenvolvimento
if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)