from django.urls import path
from . import views as vw


urlpatterns = [
#/////////////////////////////////////////////////////////////////////////////////////////////////
#---- USANDO FUNÇÕES PARA CRIAR AS VIEWS -----------    
    path('cadastro_musica',vw.cadastro_musica,name='cadastro_musica'),
    path('valida_cadastro_musica',vw.valida_cadastro_musica,name='valida_cadastro_musica'),
    path('lista_musicas',vw.lista_musicas,name='lista_musicas'),
    path('editar_musica/<int:id>',vw.editar_musica,name='editar_musica'),     # id vem do botão editar no html (ver html)
    path('valida_editar_musica/<int:id>',vw.valida_editar_musica,name='valida_editar_musica'),# id vem do botão action no html     
    path('excluir_musica/<int:id>',vw.excluir_musica,name='excluir_musica'), # id vem do botão excluir no html (ver html)

#/////////////////////////////////////////////////////////////////////////////////////////////////
#---- USANDO CLASSES PARA CRIAR AS VIEWS -----------
    path('cadastro_musica2',vw.MusicaCreateView.as_view(),name='cadastro_musica2'),
    path('listar_musica2',vw.MusicaListView.as_view(),name='listar_musica2'),    
    path('editar_musica2/<int:pk>',vw.MusicaUpdateView.as_view(),name='editar_musica2'),   # pk vem do botão editar no html (ver html)
    path('deletar_musica2/<int:pk>',vw.MusicaDeleteView.as_view(),name='deletar_musica2'), # pk vem do botão editar no html (ver html)
#/////////////////////////////////////////////////////////////////////////////////////////////////
] 