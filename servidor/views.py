from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Servidor
from .serializers import ServidorSerializer
from django.db import models

class ServidorViewSet(viewsets.ModelViewSet):
    queryset = Servidor.objects.all()
    serializer_class = ServidorSerializer

    @action(detail=False, methods=['get'])
    def buscar_por_cpf_ou_matricula(self, request):
        identificador = request.query_params.get('identificador', '')

        servidor = Servidor.objects.filter(
            models.Q(cpf=identificador) |
            models.Q(matricula=identificador)
        ).first()

        if servidor:
            serializer = self.get_serializer(servidor)
            return Response(serializer.data)
        return Response({'detail': 'Servidor não encontrado'}, status=404)

def lista_servidores(request):
    servidores = Servidor.objects.all()
    return render(request, 'lista_servidores.html', {'servidores': servidores})

def perfil_servidor(request, identificador):
    servidor = get_object_or_404(
        Servidor,
        models.Q(cpf=identificador) | models.Q(matricula=identificador)
    )
    return render(request, 'perfil_servidor.html', {'servidor': servidor})