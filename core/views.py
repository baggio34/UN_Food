
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import MercadosModelForm, UsuarioModelForm, CestasModelForm
from .models import Mercados, Usuario, Cestas
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404



#
#rendenizar as telas
#

def cadastroMercado(request):
    return render(request, 'cadastroMercado.html')

def teste(request):
    return render(request, 'teste.html')

def Email_redefiniçao(request):
    return render(request, 'Email_redefiniçao.html')

def Home(request):
    return render(request, 'Home.html')

def Trocar_senha(request):
    return render(request, 'Trocar_senha.html')


def Cad_cesta(request):
    return render(request, 'Cad_cesta.html')

def HomeMercado(request):
    return render(request, 'HomeMercado.html')


#
#usuário cliente
#

def Cad_log(request):
    if request.method == 'POST':
        form = UsuarioModelForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = Usuario(
                nome = form.cleaned_data['nome'],  
                email = form.cleaned_data['email'],       
            )
            usuario.set_password(form.cleaned_data['password'])  # Define a senha
            usuario.save()  # Agora salva o usuário
            messages.success(request, 'Usuário salvo com sucesso.')
        else:
            messages.error(request, 'Erro ao salvar o Usuário')
    else:
        form = UsuarioModelForm()
    
    context = {
        'form': form
    }
    return render(request, 'Cad_log.html', context)


def login_usuario(request):
    if request.method == 'POST':
        email = request.POST.get('emailLog')
        senha = request.POST.get('senhaLog')
        
        # Autenticar o usuário
        usuario = authenticate(request, email=email, password=senha)
        
        if usuario is not None:
            login(request, usuario)  # Faz o login do usuário
            messages.success(request, 'Login realizado com sucesso.')
            return redirect('Home')  # Redireciona para a página inicial
        else:
            messages.error(request, 'Email ou senha inválidos.')
    
    return render(request, 'Cad_log.html')  # Retorna ao formulário se não for um POST


#
#mercado
#


def Cad_mercado(request):
    if request.method == 'POST':
        form = MercadosModelForm(request.POST, request.FILES)
        if form.is_valid():
            mercado = Mercados(
                nome = form.cleaned_data['nome'],  
                email_Mercado = form.cleaned_data['email_Mercado'],       
                endereco = form.cleaned_data['endereco'],       
                telefone = form.cleaned_data['telefone'],       
                imagem = form.cleaned_data['imagem'],       
                link_whatsapp = form.cleaned_data['link_whatsapp'],    
            )
            mercado.set_password(form.cleaned_data['password'])  # Define a senha
            mercado.save()  # Agora salva o usuário
            messages.success(request, 'Mercado salvo com sucesso.')
        else:
            messages.error(request, 'Erro ao salvar o Mercado')
    else:
        form = MercadosModelForm()
    
    context = {
        'form': form
    }
    return render(request, 'Cad_mercado.html', context)



def login_Mercado(request):
    if request.method == 'POST':
        email = request.POST.get('emailLog')  # Captura o email do formulário
        senha = request.POST.get('passwordLog')  # Captura a senha do formulário
        
        # Autenticar o usuário
        mercado = authenticate(request, email_Mercado=email, password=senha)
        
        if mercado is not None:
            login(request, mercado)  # Faz o login do usuário
            request.session['email_Mercado'] = mercado.email_Mercado  # Armazena o email do mercado na sessão
            print(f'Email do mercado armazenado na sessão: {request.session["email_Mercado"]}')  # Para depuração
            messages.success(request, 'Login realizado com sucesso.')
            return redirect('HomeMercado')  # Redireciona para a página inicial
        else:
            messages.error(request, 'Email ou senha inválidos.')
    
    return render(request, 'Cad_mercado.html')  # Retorna ao formulário se não for um POST



#
# Cestas
#
"""
def Cad_cesta(request):
    #print(f'Usuário:{request.user}')
    if request.method == 'POST':
        form = CestasModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cesta Salva com sucesso.')
            #return HttpResponse('Dados enviados com sucesso')
            form = CestasModelForm()
        else:
            messages.error(request, 'Erro ao salvar a cesta')
            #return HttpResponse('Os Dados não foram enviados')
    else:
        form = CestasModelForm()
    context = {
        'form': form
    }
    return render(request, 'Cad_cesta.html', context)
"""





def Cad_cesta(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        nome_cesta = request.POST.get('nome')  # Obtém o nome da cesta do formulário

        # Pega o email do mercado da sessão
        email_mercado = request.session.get('email_Mercado')

        if email_mercado:
            try:
                # Busca a instância do mercado correspondente ao email
                mercado = Mercados.objects.get(email_Mercado=email_mercado)
            except Mercados.DoesNotExist:
                messages.error(request, 'Erro: Mercado não encontrado.')
                return redirect('Cad_cesta')  # Redireciona se o mercado não for encontrado
        else:
            messages.error(request, 'Erro: Mercado não encontrado na sessão.')
            return redirect('Cad_cesta')  # Redireciona se o mercado não for encontrado

        if action == 'cadastrar':
            form = CestasModelForm(request.POST, request.FILES)
            if form.is_valid():
                cesta = form.save(commit=False)
                cesta.mercado = mercado  # Atribui o mercado à cesta
                cesta.save()
                messages.success(request, 'Cesta salva com sucesso.')
            else:
                messages.error(request, 'Erro ao salvar a cesta.')
        
        elif action == 'editar':
            try:
                cesta = Cestas.objects.get(nome=nome_cesta, mercado=mercado)
                form = CestasModelForm(request.POST, request.FILES, instance=cesta)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Cesta editada com sucesso.')
                else:
                    messages.error(request, 'Erro ao editar a cesta.')
            except Cestas.DoesNotExist:
                messages.error(request, 'Cesta não encontrada.')

        elif action == 'deletar':
            try:
                cesta = Cestas.objects.get(nome=nome_cesta, mercado=mercado)
                cesta.delete()
                messages.success(request, 'Cesta deletada com sucesso.')
            except Cestas.DoesNotExist:
                messages.error(request, 'Cesta não encontrada.')

    form = CestasModelForm()  # Inicializa o formulário para requisições GET
    context = {
        'form': form
    }
    return render(request, 'Cad_cesta.html', context)

   

def carrossel(request):
    mercados = Mercados.objects.all()  # Obtém todos os mercados cadastrados
    return render(request, 'carrossel.html', {'mercados': mercados})




def ver(request):
    # Pega o email do mercado da sessão
    email_mercado = request.session.get('email_Mercado')

    if email_mercado:
        try:
            # Busca a instância do mercado correspondente ao email
            mercado_logado = Mercados.objects.get(email_Mercado=email_mercado)
        except Mercados.DoesNotExist:
            messages.error(request, 'Erro: Mercado não encontrado.')
            return redirect('HomeMercado')  # Redireciona se o mercado não for encontrado
    else:
        messages.error(request, 'Erro: Mercado não encontrado na sessão.')
        return redirect('HomeMercado')  # Redireciona se o mercado não for encontrado

    # Filtra as cestas que pertencem ao mercado logado
    cestas_do_mercado = Cestas.objects.filter(mercado=mercado_logado)

    context = {
        'cestas': cestas_do_mercado
    }

    return render(request, 'ver.html', context)




def contato(request):
    return render(request, 'contato.html')

def contato_mercado(request, email_mercado):
    try:
        mercado = Mercados.objects.get(email_Mercado=email_mercado)
        # Filtra as cestas que pertencem ao mercado e limita a 3
        cestas_do_mercado = Cestas.objects.filter(mercado=mercado).order_by('-id')[:3]
    except Mercados.DoesNotExist:
        messages.error(request, 'Mercado não encontrado.')
        return redirect('Home')  # Redireciona para a página inicial se o mercado não for encontrado

    context = {
        'mercado': mercado,
        'cestas': cestas_do_mercado,
    }
    
    return render(request, 'contato.html', context)