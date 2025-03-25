from django.shortcuts import render # shortcuts são atalhos que chamam métodos.
# o Render renderiza uma página com base em um template

def index (request): # sempre que eu for fazer um métod na view, preciso passar a requisicao que o usuário faz para o sistema (request)

   context = {  #é o contexto, é o que a página vai ter. Facilita na hora de retornar. Se eu pegar alguma variável no bd, vou colocar aqui

    "message": "Seja bem vindo(a) ao Sistema de Formulários do IFRS! :)"
   }
   return render(request, 'index.html', context)