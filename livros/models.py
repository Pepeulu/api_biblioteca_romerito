from django.db import models

# Create your models here.
class Livros(models.Model):
    id_livro = models.AutoField(primary_key=True)
    nome_livro = models.TextField(null=False)
    foto_livro = models.ImageField(null= True)
    Ano_de_publicacao = models.DateField(null=False) 
    ISBN = models.TextField(null=False)
    livro_arquivo = models.FileField(upload_to="pdfs/", null=True)


