from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Pagina, Produto, Contato, Pedido
from .forms import CadastroForm, LoginForm, ContatoForm, PedidoForm 
def is_superuser(user):
    return user.is_superuser

def get_pagina():
    return Pagina.objects.first()

def index(request):
    pagina = get_pagina()
    produtos = Produto.objects.all()
    
    if request.method == 'POST':
        form_contato = ContatoForm(request.POST)
        if form_contato.is_valid():
            Contato.objects.create(**form_contato.cleaned_data)
            messages.success(request, 'Sua mensagem foi enviada com sucesso!')
            return redirect('index')
    else:
        form_contato = ContatoForm()

    context = {
        'pagina': pagina,
        'produtos': produtos,
        'form_contato': form_contato,
    }
    return render(request, 'index.html', context) 

def cadastro_usuario(request):
    pagina = get_pagina() 

    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso! Faça login.')
            return redirect('login')
    else:
        form = CadastroForm()
    
    context = {'form': form, 'pagina': pagina}
    return render(request, 'cadastro.html', context)

def login_usuario(request):
    pagina = get_pagina()
   
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'Bem-vindo, {user.username}!') 
                return redirect('index')
            else:
                messages.error(request, 'Credenciais inválidas.') 
    else:
        form = LoginForm()
    
    context = {'form': form, 'pagina': pagina}
    return render(request, 'login.html', context)

@login_required 
def logout_usuario(request):
    logout(request)
    messages.info(request, 'Você foi desconectado com sucesso.')
    return redirect('index')

@login_required
def compra(request, produto_id):
    pagina = get_pagina()
    produto = get_object_or_404(Produto, pk=produto_id)
    
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            quantidade = form.cleaned_data['quantidade']
            
            if quantidade > produto.estoque:
                messages.error(request, 'Estoque insuficiente para esta quantidade.')
            else:
                total_pedido = produto.preco * quantidade
                Pedido.objects.create(
                    usuario=request.user,
                    produto=produto,
                    quantidade=quantidade,
                    total=total_pedido
                )
                
                produto.estoque -= quantidade
                produto.save()
                
                messages.success(request, 'Pedido finalizado com sucesso!')
                return redirect('perfil')
    else:
        form = PedidoForm()

    context = {
        'produto': produto,
        'form': form,
        'pagina': pagina
    }
    return render(request, 'compra.html', context) 

@login_required
def perfil_usuario(request):
    pagina = get_pagina()
    pedidos = Pedido.objects.filter(usuario=request.user).order_by('-data')
    
    context = {
        'pedidos': pedidos,
        'nome_usuario': request.user.username,
        'pagina': pagina
    }
    return render(request, 'perfil.html', context)
@login_required
@user_passes_test(is_superuser) 
def lista_mensagens(request):
    pagina = get_pagina()
    mensagens_contato = Contato.objects.all().order_by('-criado_em')
    
    context = {
        'mensagens_contato': mensagens_contato,
        'pagina': pagina
    }
    return render(request, 'mensagens.html', context)