# Generated by Django 5.1.1 on 2024-11-27 11:00

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
import stdimage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True, verbose_name='email')),
                ('nome', models.CharField(blank=True, max_length=100, unique=True, verbose_name='nome')),
                ('password', models.CharField(blank=True, max_length=128, verbose_name='password')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Mercados',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email_Mercado', models.EmailField(blank=True, max_length=254, primary_key=True, serialize=False, unique=True, verbose_name='email_Mercado')),
                ('nome', models.CharField(blank=True, max_length=100, verbose_name='nome')),
                ('endereco', models.CharField(blank=True, max_length=255, verbose_name='endereco')),
                ('telefone', models.CharField(blank=True, max_length=15, verbose_name='telefone')),
                ('imagem', stdimage.models.StdImageField(blank=True, force_min_size=False, upload_to='mercados', variations={'thumb': (125, 125)}, verbose_name='Imagem')),
                ('link_whatsapp', models.CharField(blank=True, max_length=600, verbose_name='link_whatsapp')),
                ('password', models.CharField(blank=True, max_length=128, verbose_name='password')),
                ('groups', models.ManyToManyField(blank=True, related_name='mercados', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='mercados_permissions', to='auth.permission')),
            ],
            options={
                'verbose_name': 'Mercado',
                'verbose_name_plural': 'Mercados',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Cestas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', stdimage.models.StdImageField(blank=True, force_min_size=False, upload_to='cestas', variations={'thumb': (125, 125)}, verbose_name='Imagem')),
                ('nome', models.CharField(blank=True, max_length=100, verbose_name='Nome')),
                ('preco', models.DecimalField(blank=True, decimal_places=2, max_digits=6, verbose_name='Preço')),
                ('tamanho', models.DecimalField(blank=True, decimal_places=1, max_digits=3, verbose_name='Tamanho')),
                ('descricao', models.CharField(blank=True, max_length=300, verbose_name='Descrição')),
                ('mercado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cestas', to='core.mercados')),
            ],
        ),
    ]
