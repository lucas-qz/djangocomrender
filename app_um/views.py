#/////////////////////////////////////////////////////////////////////////////////////////////////
#---- USANDO FUNÇÕES PARA CRIAR AS VIEWS -----------  
from django.shortcuts import render,redirect
from . import models
 
def cadastro_musica(request):
    return render(request, 'Fcadastro_musica.html')

def valida_cadastro_musica(request):
    if request.method == 'POST':
        musica = request.POST.get('musica')
        cantor = request.POST.get('cantor')
        genero = request.POST.get('genero')
        musica1 = models.Musica.objects.filter(musica=musica).first()
        if musica1:
            return redirect('cadastro_musica')
        models.Musica.objects.create(musica=musica, cantor=cantor, genero=genero)
        return redirect('lista_musicas')
    return redirect('cadastro_musica')

def lista_musicas(request):
    musica1 = models.Musica.objects.all()
    return render(request, 'Flista_musicas.html',{'musica1':musica1})

def excluir_musica(request, id): # id vem da rota (ver rota)
    musica1 = models.Musica.objects.get(id=id)
    musica1.delete()
    return redirect('lista_musicas')

def editar_musica(request, id): # id vem da rota (ver rota)
    musica1 = models.Musica.objects.get(id=id)
    return render(request, 'Feditar_musicas.html',{'musica1':musica1})

def valida_editar_musica(request, id): # id vem da rota (ver rota)
    if request.method == 'POST':
        musica = request.POST.get('musica')
        cantor = request.POST.get('cantor')
        genero = request.POST.get('genero')
        musica1 = models.Musica.objects.get(id=id)
        musica1.musica = musica
        musica1.cantor = cantor
        musica1.genero = genero
        musica1.save()
        return redirect('lista_musicas')
    return redirect('lista_musicas')


#/////////////////////////////////////////////////////////////////////////////////////////////////
#---- USANDO CLASSES PARA CRIAR AS VIEWS -----------
from . import models
from django.urls import reverse_lazy # redireciona o usuario para outra pagina após ele clicar no botão
from django.views.generic.edit import CreateView, UpdateView, DeleteView # serv p usar views padrão do django p insert, update e delete
from django.views.generic.list import ListView                           # serve pra usar as views padrão do django pra fazer select

class MusicaCreateView(CreateView):  
    model = models.Musica2                   # tabela que será feito insert (as tabelas estão em models.py)
    fields = ["musica", "cantor","genero"] # colunas da tabela que serão passadas pro formulario
    template_name = 'Ccadasta_edita.html'  # pagina html do formulario de insert *é a mesma do update
    success_url = reverse_lazy('listar_musica2') # se o cadastro nessa tela deu certo, ele será redirecionado para essa url
    #================== serve para passar textos, cores, etc, para o html 'template_name' usado acima
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Criar Musica"  
        context['botao'] = "Cadastrar"
        context['cor_botao'] = "button button5" # nome das classes do estilo.css, ou seja, é estilo do botão q quero aqui
        return context
    #==================

class MusicaUpdateView(UpdateView): 
    model = models.Musica2                   # tabela que será feito update (as tabelas estão em models.py)
    fields = ["musica", "cantor","genero"] # colunas da tabela que serão passadas pro formulario
    template_name = 'Ccadasta_edita.html'  # pagina html do formulario de update *é a mesma do insert
    success_url = reverse_lazy('listar_musica2') # se o update nessa tela deu certo, ele será redirecionado para essa url
    #================== serve para passar textos, cores, etc, para o html 'template_name' usado acima
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar Musica"
        context['botao'] = "Editar"
        context['cor_botao'] = "button button4" # nome das classes do estilo.css, ou seja, é estilo do botão q quero aqui
        return context
    #==================

class MusicaDeleteView(DeleteView): 
    model = models.Musica2                # tabela que será feito delete (as tabelas estão em models.py)
    template_name = 'Cconfirma_excluir.html' # pagina html de confirmação de exclusão
    success_url = reverse_lazy('listar_musica2') # se a exclusão nessa tela deu certo, ele será redirecionado para essa url
    #================== serve para passar textos, cores, etc, para o html 'template_name' usado acima
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Deletar Musica"
        context['botao'] = "Deletar"
        context['cor_botao'] = "button button6" # nome das classes do estilo.css, ou seja, é estilo do botão q quero aqui
        return context
    #==================

class MusicaListView(ListView): # **LoginRequiredMixin = somente usuario logado poderá acessar essa rota  
    model = models.Musica2                # tabela que será feito select (as tabelas estão em models.py)
    template_name = 'Clista_musicas.html' # pagina html para a qual mandará os dados do select
    #================== serve para passar textos, cores, etc, para o html 'template_name' usado acima
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Lista de Musica"
        context['botao'] = "Cadastrar Novo"
        context['cor_botao'] = "button button5" # nome das classes do estilo.css, ou seja, é estilo do botão q quero aqui
        return context
    #================== 
#///////////////////////////////////////////////////////////////////////////////////////////////// 