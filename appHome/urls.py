from django.urls import include, path

from Projeto import settings
from . import views


urlpatterns =[
    path('', views.index, name="index"),

    path('login/', views.login_usuario, name='login'), 
    path('cadastro/', views.cadastro_usuario, name='cadastro'),
    path('logout/', views.logout_usuario, name='logout'), 
    path('compra/<int:produto_id>/', views.compra, name='compra'), 
    path('perfil/', views.perfil_usuario, name='perfil'),
    path('mensagens/', views.lista_mensagens, name='lista_mensagens'),
    
]

