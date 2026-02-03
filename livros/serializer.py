from rest_framework import serializers
from .models import Livros

class LivroSerializer(serializers.ModelSerializer):
    foto_livro = serializers.ImageField(required=False, allow_null=True)
    livro_arquivo = serializers.FileField(required=False, allow_null=True)
    
    class Meta:
        model = Livros
        fields = [
            'id_livro',
            'nome_livro',
            'Ano_de_publicacao',
            'ISBN',
            'foto_livro',
            'livro_arquivo'
        ]
    