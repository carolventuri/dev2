from django.urls import path
from .views.estaticas import api_root, saudacao
from .views.usuario import UsuarioListService

app_name = 'services'


urlpatterns = [

    path('', api_root, name="api-root"),
    path('saudacao/', saudacao, name="saudacao"),
    path('usuarios/', UsuarioListService.as_view(), name='usuario-list'),
]


