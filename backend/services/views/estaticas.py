from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.shortcuts import render

#REVISAR TUDO AQUI


@api_view(['GET'])
def saudacao(request):
    return Response({"saudacao": "Olá Mundo"})


@api_view(['GET'])
def api_root(request, format=None):
    """
     View que permitirá retornar um objeto JSON com todos os endpoints implementados..
    """

    return Response({
        'saudacao': reverse('services:saudacao', request=request, format=format),
        'usuarios': reverse('services:usuario-list', request=request, format=format),
    })