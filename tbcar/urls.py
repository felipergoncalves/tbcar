"""tbcar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from core.views import home, cadastro_cliente, lista_clientes, cadastro_veiculo, lista_veiculos, cadastro_tabela, tabela, Registrar, altera_cliente, exclui_cliente, excluir_veiculo,excluir_tabela, excluir_marca, altera_veiculo, altera_tabela, altera_marca, alterar_rotativo, alterar_mensalista, lista_mensalistas, lista_rotativos, cadastro_mensalista, cadastro_rotativo, excluir_rotativo, excluir_mensalista, lista_marcas, cadastro_marca

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registrar/', Registrar.as_view(), name='url_registrar'),
    path('', home, name="url_principal"),
    path('cadastroCliente/', cadastro_cliente, name="url_cadastro_cliente"),
    path('listaClientes/', lista_clientes, name="url_lista_clientes"),
    path('cadastroVeiculo/', cadastro_veiculo, name="url_cadastro_veiculo"),
    path('listaVeiculos/', lista_veiculos, name="url_lista_veiculos"),
    path('listaMensalistas/', lista_mensalistas, name="url_lista_mensalistas"),
    path('listaRotativos/', lista_rotativos, name="url_lista_rotativos"),
    path('listaMarcas/', lista_marcas, name="url_lista_marcas"),
    path('cadastroTabela/', cadastro_tabela, name="url_cadastro_tabela"),
    path('cadastroMensalista/', cadastro_mensalista, name="url_cadastro_mensalista"),
    path('cadastroRotativo/', cadastro_rotativo, name="url_cadastro_rotativo"),
    path('cadastroMarca/', cadastro_marca, name="url_cadastro_marca"),
    path('tabela/', tabela, name="url_tabela"),
    path('captcha/', include('captcha.urls')),
    path('altera_cliente/<int:id>/', altera_cliente, name="url_altera_cliente"),
    path('altera_veiculo/<int:id>/', altera_veiculo, name="url_altera_veiculo"),
    path('altera_tabela/<int:id>/', altera_tabela, name="url_altera_tabela"),
    path('altera_marca/<int:id>/', altera_marca, name="url_altera_marca"),
    path('altera_mensalista/<int:id>/', alterar_mensalista, name="url_altera_mensalista"),
    path('altera_rotativo/<int:id>/', alterar_rotativo, name="url_altera_rotativo"),
    path('excluir_cliente/<int:id>/', exclui_cliente, name='url_excluir_cliente'),
    path('excluir_veiculo/<int:id>/', excluir_veiculo, name='url_excluir_veiculo'),
    path('excluir_tabela/<int:id>/', excluir_tabela, name='url_excluir_tabela'),
    path('excluir_marca/<int:id>/', excluir_marca, name='url_excluir_marca'),
    path('excluir_rotativo/<int:id>/', excluir_rotativo, name='url_excluir_rotativo'),
    path('excluir_mensalista/<int:id>/', excluir_mensalista, name='url_excluir_mensalista')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
