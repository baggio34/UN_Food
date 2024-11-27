from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Mercados, Usuario


# Customização para o modelo Mercados
class MercadosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'telefone', 'email_Mercado', 'imagem', 'link_whatsapp', 'password')


# Customização para o modelo Usuario
class CustomUsuarioAdmin(UserAdmin):
    # Remove os campos desnecessários
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    # Formulário de criação
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff'),
        }),
    )

    # Campos visíveis na listagem
    list_display = ('nome', 'email', 'is_staff', 'is_active')
    ordering = ('email',)
    search_fields = ('email', 'nome')


# Registra os modelos no admin
admin.site.register(Mercados, MercadosAdmin)
admin.site.register(Usuario, CustomUsuarioAdmin)
