import django_filters
from .models import Livros


class LivroFilter(django_filters.FilterSet):
    nome_livro = django_filters.CharFilter(lookup_expr='icontains')
    ISBN = django_filters.CharFilter(lookup_expr='icontains')
    ano_min = django_filters.NumberFilter(field_name='Ano_de_publicacao', lookup_expr='year__gte')
    ano_max = django_filters.NumberFilter(field_name='Ano_de_publicacao', lookup_expr='year__lte')
    ordenar = django_filters.OrderingFilter(
        fields=(
            ('nome_livro', 'nome'),
            ('Ano_de_publicacao', 'ano'),
        ),
    )

    class Meta:
        model = Livros
        fields = ['nome_livro', 'ISBN']
