from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from core.forms import FormCliente, FormVeiculo, FormMarca, FormTabela, FormMensalista, FormRotativo
from core.models import Cliente, Marca, Veiculo, Tabela, Mensalista, Rotativo
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


class Registrar(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('url_principal')
    template_name = 'registration/registrar.html'


# Create your views here.


def home(request):
    return render(request, 'core/index.html')

@login_required()
def altera_cliente(request, id):
    if request.user.is_staff:
        obj = Cliente.objects.get(id=id)
        form = FormCliente(request.POST or None, request.FILES or None, instance=obj)
        if request.POST:
            if form.is_valid():
                form.save()
                messages.success(request, 'Dados do cliente alterados com sucesso!')
                return redirect('url_lista_clientes')
        contexto = {'form': form, 'titulo_pagina':'EditCliente', 'txt_nome_pagina':'Altera Cliente'}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'core/aviso.html')

@login_required()
def altera_tabela(request, id):
    if request.user.is_staff:
        obj = Tabela.objects.get(id=id)
        form = FormTabela(request.POST or None, request.FILES or None, instance=obj)

        if request.POST:
            if form.is_valid():
                form.save()
            return redirect('url_tabela')

    contexto = {'form': form, 'titulo_pagina': 'Alterar_Tabelar', 'txt_nome_pagina': 'Editar Tabela'}
    return render(request, 'core/cadastro.html', contexto)

@login_required
def altera_marca(request, id):
    if request.user.is_staff:
        obj = Marca.objects.get(id=id)
        form = FormMarca(request.POST or None, request.FILES or None, instance=obj)
        if request.POST:
            if form.is_valid():
                form.save()
            return redirect('url_listaMarca')

    contexto = {'form': form, 'titulo_pagina': 'alter_Marca', 'txt_nome_pagina': 'Atualização de Marca'}
    return render(request, 'core/cadastro.html', contexto)

@login_required
def altera_veiculo(request, id):
    if request.user.is_staff:
        obj = Veiculo.objects.get(id=id)
        form = FormVeiculo(request.POST or None, request.FILES or None, instance=obj)

        if request.POST:
            if form.is_valid():
                form.save()
            return redirect('url_lista_veiculos')

    contexto = {'form': form, 'titulo_pagina': 'Alter_veiculo', 'txt_nome_pagina': 'Atualização Veiculo'}
    return render(request, 'core/cadastro.html', contexto)

@login_required
def alterar_rotativo(request, id):
    if request.user.is_staff:
        obj = Rotativo.objects.get(id=id)
        form = FormRotativo(request.POST or None, request.FILES or None, instance=obj)

        if request.POST:
            if form.is_valid():
                obj.calcula_total()
                form.save()
            return redirect('url_lista_rotativos')

    contexto = {'form': form, 'titulo_pagina': 'Alter_rotativo', 'txt_nome_pagina': 'Atualização Rotativo'}
    return render(request, 'core/cadastro_rotativo_dividido.html', contexto)

@login_required
def alterar_mensalista(request, id):
    if request.user.is_staff:
        obj = Mensalista.objects.get(id=id)
        form = FormMensalista(request.POST or None, request.FILES or None, instance=obj)

        if request.POST:
            if form.is_valid():
                form.save()
            return redirect('url_lista_mensalistas')

    contexto = {'form': form, 'titulo_pagina': 'Alter_mensalista', 'txt_nome_pagina': 'Atualização Mensalista'}
    return render(request, 'core/cadastro.html', contexto)

@login_required
def cadastro_cliente(request):
    if request.user.is_staff:
        form = FormCliente(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect('url_principal')
        contexto = {'form': form, 'titulo_pagina': 'Cad_Cliente', 'txt_nome_pagina': 'Cadastro de Cliente'}

        return render(request, 'core/cadastro.html', contexto)

    return render(request, 'aviso.html')

@login_required
def cadastro_marca(request):
    if request.user.is_staff:
        form = FormMarca(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_principal')
        contexto = {'form': form, 'titulo_pagina': 'Cad_Marca', 'txt_nome_pagina': 'Cadastro de Marca'}

        return render(request, 'core/cadastro.html', contexto)

    return render(request, 'aviso.html')

@login_required
def cadastro_mensalista(request):
    if request.user.is_staff:
        form = FormMensalista(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_principal')
        contexto = {'form': form, 'titulo_pagina': 'Cad_Mensalista', 'txt_nome_pagina': 'Cadastro Mensalista'}

        return render(request, 'core/cadastro.html', contexto)

    return render(request, 'aviso.html')

@login_required
def cadastro_rotativo(request):
    if request.user.is_staff:
        form = FormRotativo(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_principal')
        contexto = {'form': form, 'titulo_pagina': 'Cad_Rotativo', 'txt_nome_pagina': 'Cadastro de Rotativo'}

        return render(request, 'core/cadastro_rotativo_dividido.html', contexto)

    return render(request, 'aviso.html')


@login_required  # Bloqueia acesso sem login
def lista_clientes(request):
    if request.user.is_staff:
        if request.POST and request.POST['input_pesquisa']:
            dados_cliente = Cliente.objects.filter(nome__contains = request.POST['input_pesquisa'])
        else:
            dados_cliente = Cliente.objects.all()
        contexto = {'dados_cliente': dados_cliente, 'text_input':'Digite o nome do cliente', 'listagem':'listagem'}
        return render(request, 'core/lista_clientes.html', contexto)

    return render(request, 'aviso.html')

@login_required  # Bloqueia acesso sem login
def lista_mensalistas(request):
    if request.user.is_staff:
        if request.POST and request.POST['input_pesquisa']:
            dados_mensalista = Mensalista.objects.filter(id_veiculo__placa__contains=request.POST['input_pesquisa'])
        else:
            dados_mensalista = Mensalista.objects.all()
        contexto = {'dados_mensalista': dados_mensalista, 'text_input':'Digite a placa do veículo', 'listagem':'listagem'}
        return render(request, 'core/lista_mensalistas.html', contexto)

    return render(request, 'aviso.html')

@login_required  # Bloqueia acesso sem login
def lista_rotativos(request):
    if request.user.is_staff:
        if request.POST and request.POST['input_pesquisa']:
            dados_rotativo = Rotativo.objects.filter(id_veiculo__placa__contains=request.POST['input_pesquisa'])
        else:
            dados_rotativo = Rotativo.objects.all()
        contexto = {'dados_rotativo': dados_rotativo, 'text_input':'Digite a placa do veículo', 'listagem':'listagem'}
        return render(request, 'core/lista_rotativos.html', contexto)

    return render(request, 'aviso.html')

@login_required
def lista_veiculos(request):
    if request.user.is_staff:
        if request.POST and request.POST['input_pesquisa']:
            dados_veiculos = Veiculo.objects.filter(placa__contains = request.POST['input_pesquisa'])
        else:
            dados_veiculos = Veiculo.objects.all()
        contexto = {'dados_veiculos': dados_veiculos, 'text_input':'Digite a placa do veículo', 'listagem':'listagem'}
        return render(request, 'core/lista_veiculos.html', contexto)
    return render(request, 'aviso.html')

@login_required  # Bloqueia acesso sem login
def lista_marcas(request):
    if request.user.is_staff:
        if request.POST and request.POST['input_pesquisa']:
            dados_marca = Marca.objects.filter(nome__contains = request.POST['input_pesquisa'])
        else:
            dados_marca = Marca.objects.all()
        contexto = {'dados_marca': dados_marca, 'text_input':'Digite o nome da marca', 'listagem':'listagem'}
        return render(request, 'core/lista_marca.html', contexto)
    return render(request, 'aviso.html')

@login_required
def cadastro_veiculo(request):
    if request.user.is_staff:
        form = FormVeiculo(request.POST or None and request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_principal')
        contexto = {'form': form, 'titulo_pagina': 'Cad_Veiculo', 'txt_nome_pagina': 'Cadastro de Veículo'}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'aviso.html')

@login_required()
def cadastro_tabela(request):
    if request.user.is_staff:
        form = FormTabela(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_principal')

    contexto = {'form': form, 'titulo_pagina':'Cad-Tabela', 'txt_nome_pagina':'Cadastro de Tabela'}
    return render(request, 'core/cadastro.html', contexto)

@login_required()
def tabela(request):
    if request.user.is_staff:
        dados = Tabela.objects.all()
        contexto = {'dados':dados, 'listagem':'listagem'}
        return render(request, 'core/lista_tabelas.html', contexto)
    return render(request, 'aviso.html')

@login_required
def exclui_cliente(request, id):
    if request.user.is_staff:
        obj = Cliente.objects.get(id = id)
        if request.POST:
            obj.delete()
            messages.success(request, 'Cliente excluído com sucesso!')
            contexto = {'txt_tipo': 'Cliente', 'txt_info': obj.nome, 'txt_url': '/listaClientes'}
            return render(request, 'core/aviso_exclusao.html', contexto)
        else:
            contexto = {'txt_info': obj.nome}
            return render(request, 'excluir/confirma_exclusao.html', contexto)

@login_required
def excluir_veiculo(request, id):
    if request.user.is_staff:
        obj = Veiculo.objects.get(id = id)
        if request.POST:
            obj.delete()
            contexto = {'txt_tipo': 'Veiculo', 'txt_info': obj.modelo, 'txt_url':'/listaVeiculos'}
            return render(request, 'core/aviso_exclusao.html', contexto)
        else:
            contexto = {'txt_info': obj.modelo}
            return render(request, 'excluir/confirma_exclusao.html', contexto)

@login_required
def excluir_tabela(request, id):
    if request.user.is_staff:
        obj = Tabela.objects.get(id = id)
        if request.POST:
            obj.delete()
            contexto = {'txt_tipo': 'Tabela', 'txt_info': obj.descricao, 'txt_url':'/tabela'}
            return render(request, 'core/aviso_exclusao.html', contexto)
        else:
            contexto = {'txt_info': obj.descricao}
            return render(request, 'excluir/confirma_exclusao.html', contexto)

@login_required
def excluir_marca(request, id):
    if request.user.is_staff:
        obj = Marca.objects.get(id = id)
        contexto = {'txt_tipo': 'Marca', 'txt_info': obj.nome, 'txt_url':'/listaMarcas'}
        if request.POST:
            obj.delete()
            return render(request, 'core/aviso_exclusao.html', contexto)
        else:
            contexto.update({'txt_info': obj.nome})
            return render(request, 'excluir/confirma_exclusao.html', contexto)

@login_required
def excluir_rotativo(request, id):
    if request.user.is_staff:
        obj = Rotativo.objects.get(id = id)
        contexto = {'txt_tipo': 'Rotativo', 'txt_info': obj.id_veiculo, 'txt_url':'/listaRotativos'}
        if request.POST:
            obj.delete()
            return render(request, 'core/aviso_exclusao.html', contexto)
        else:
            contexto.update({'txt_info': obj.id_veiculo})
            return render(request, 'excluir/confirma_exclusao.html', contexto)

@login_required
def excluir_mensalista(request, id):
    if request.user.is_staff:
        obj = Mensalista.objects.get(id = id)
        contexto = {'txt_tipo': 'Mensalista', 'txt_info': obj.id_veiculo, 'txt_url':'/listaMensalistas'}
        if request.POST:
            obj.delete()
            return render(request, 'core/aviso_exclusao.html', contexto)
        else:
            contexto.update({'txt_info': obj.id_veiculo})
            return render(request, 'excluir/confirma_exclusao.html', contexto)
