from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Servidor
from .serializers import ServidorSerializer


class ServidorViewSet(viewsets.ModelViewSet):
    queryset = Servidor.objects.all()
    serializer_class = ServidorSerializer

    @action(detail=False, methods=['get'])
    def buscar_por_cpf_ou_matricula(self, request):
        identificador = request.query_params.get('identificador', '')

        # Tenta buscar por CPF ou matrícula
        servidor = Servidor.objects.filter(
            models.Q(cpf=identificador) |
            models.Q(matricula=identificador)
        ).first()

        if servidor:
            serializer = self.get_serializer(servidor)
            return Response(serializer.data)
        return Response({'detail': 'Servidor não encontrado'}, status=404)