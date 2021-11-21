# DJANGO_FRAMEWORK_BASICO
Projeto básico do curso de  Programação Web com Python e Django Framework: Essencial da Udemy.  link: https://www.udemy.com/course/programacao-web-com-django-framework-do-basico-ao-avancado/


Aula 1 - Criar o diretório e a venv fora do arquivo do diretório
        pip install django
        pip freeze > requirements.txt ( cria o arquivo de requirements )



Aula 2 - django-admin startproject django1 .  (não esquecer do espaço + ponto)  

Aula 3 - django-admin startapp core 
        modificar o arquivo settings.py e adicionar a aplicação criada.
        adicionar 'templates' em 'DIRS' no dicionário TEMPLATES dentro de settings.py

Aula 7 - Para DEVENVOLVIMENTO, quando você precisar alterar DEBUG = False, colocar '*' em ALLOWED.HOSTS em settings.py, para a aplicação funcionar.
        Alterar LANGUAGE_CODE= 'en-us', para 'pt-br'

Aula 8 - Criação da função index em view.py dentro da aplicação core. Também foi criada a função contato.

Aula 9 - Criação de rotas no arquivo url.py, criar um arquivo url na aplicação (no caso em core), depois chamar todas as urls dessa aplicação no arquivo urls.py do projeto (dentro de django1)