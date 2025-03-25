from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404, redirect
from ..models import Usuario

@login_required
def usuario_list(request):
    usuarios = Usuario.objects.all()
    context = {
        'musicas': usuarios,
    }
    return render(request, 'usuario/list.html', context)

@login_required
def usuario_read(request, musica_id):
    usuario = Usuario.objects.get(id=musica_id)
    context = {
        'musica': usuario,
    }
    return render(request, 'usuario/read.html', context)


@login_required
@permission_required("app_backend.delete_usuario", raise_exception=True)
def usuario_delete(request, usuario_id):
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    try:
        if request.method == "POST":
            v_usuario_id = request.POST.get("usuario_id", None)
            if int(v_usuario_id) == usuario_id:
                usuario.delete()
                return redirect('app_backend:usuario_list')
        else:
            context = {
                'usuario': usuario,
            }
            return render(request, 'usuario/delete.html', context)
    except:
        context = {
            'message': "Erro ao deletar o objeto."
        }
        return render (request, 'usuario/list.html', context)