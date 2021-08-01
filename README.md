# API de Atrações Turísticas

### Apps
* Atrações
* Comentários
* Avaliações
* Endereços
* Pontos Turísticos

#### Comandos úteis
* Criando ambiente virtual.

  `python -m venv venv`
* Ativando ambiente virtual
  * Windows

    `venv\Script\activate.bat`
  * Linux

    `source ./venv/bin/activate`
* Instalando pacotes: Ex: Django

  `pip install django`
* Iniciando servidor

  `python manage.py runserver`
* Registrando migrates

  `python manage.py makemigrations`
* Subindo migrates para o banco

  `python manage.py migrate`
* Criando usuário admin

  `python manage.py createsuperuser`
* Criando usuário admin(especificando o username e email)

  `python manage.py createsuperuser --username <username> --email <email>`
* Resetando a senha do admin

  `python manage.py changepassword <username>`

#### Dicas de URL no Settings (settings.py)
Nome da Pasta que salva imagem: `MEDIA_ROOT = 'imagens'` <br/>
Nome do Link de URL realacionado nos models: `MEDIA_URL = '/media/'`
