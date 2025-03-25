from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import UsuarioSerializer
from app_backend.models import Usuario


class UsuarioListService(APIView):
    """
    Service para listar os usuarios.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get(self, request, format=None):
        """
        Retorna a lista de usuarios.
        """
        usuarios = Usuario.objects.all()
        context = {
            'request': request,
            'format': format
        }
        serializer = UsuarioSerializer(usuarios, many=True, context=context)
        return Response(serializer.data)


"""
da para fazer assim também:

@api_view(['GET'])
def get_usuario(request):
	usuarios = Usuario.objects.all()
	serializedData = UsuarioSerializer(usuarios, many=True).data
	return Response(serializedData)

"""


class UsuarioCreateService(APIView):
    """
    Service para criar usuarios.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def post(self, request, format=None):
        """
        Cria um novo usuaário.
        """
        dados = request.data
        context = {
            'request': request,
            'format': format
        }
        serializer = UsuarioSerializer(data=dados, context=context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)