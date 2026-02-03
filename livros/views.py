from django.shortcuts import render
from django import views
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Livros
from .serializer import LivroSerializer
from .filters import LivroFilter
from pdf2image import convert_from_bytes
from django.core.files.base import ContentFile
from io import BytesIO
from rest_framework.response import Response


# Create your views here.

class LivroView(viewsets.ModelViewSet):
    queryset = Livros.objects.all()
    serializer_class = LivroSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = LivroFilter
    search_fields = ['nome_livro', 'ISBN']
    ordering_fields = ['nome_livro', 'Ano_de_publicacao', 'id_livro']
    ordering = ['id_livro']

    def get_permissions(self):
        return[AllowAny()]
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        
        if 'foto_livro' not in request.data or request.data.get('foto_livro') in [None, '', 'null', 'undefined']:
            request.data._mutable = True
            if 'foto_livro' in request.data:
                del request.data['foto_livro']
            request.data._mutable = False
        
        if 'livro_arquivo' not in request.data or request.data.get('livro_arquivo') in [None, '', 'null', 'undefined']:
            request.data._mutable = True
            if 'livro_arquivo' in request.data:
                del request.data['livro_arquivo']
            request.data._mutable = False
        
        return super().update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        
        if 'foto_livro' not in request.data or request.data.get('foto_livro') in [None, '', 'null', 'undefined']:
            request.data._mutable = True
            if 'foto_livro' in request.data:
                del request.data['foto_livro']
            request.data._mutable = False
        
        if 'livro_arquivo' not in request.data or request.data.get('livro_arquivo') in [None, '', 'null', 'undefined']:
            request.data._mutable = True
            if 'livro_arquivo' in request.data:
                del request.data['livro_arquivo']
            request.data._mutable = False
        
        return super().partial_update(request, *args, **kwargs)
    
    