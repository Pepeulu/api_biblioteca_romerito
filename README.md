
## Instalacao


Instale as dependencias:

```bash
pip install -r requirements.txt
```

Execute migração:

```bash
python manage.py makemigrations
python manage.py migrate
```

Inicie o servidor:

```bash
python manage.py runserver
```

Acesse em http://localhost:8000/api/livros/
