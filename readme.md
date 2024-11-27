Sistema base para disponibilizar os dados para serem importados via api.
Nele contém apenas dados simples de servidores públicos ficticios que serão
consumidos pelo sistema 2. 

O intuito desse crud é o estudo de API com atutenticação.

O sistema que consome é o:

https://github.com/95Caique/Sistema2

1 - Para executar, clone o repostório

2 - Navegue até a pasta do projeto com o comando cd sistema_1

3 - Crie seu ambiente virtual (venv) para instalar os pacotes: Linux - python3 -m venv venv Ative com: source venv/bin/activate

Windows - python3 -m venv venv ative com: venv\Scripts\activate se estiver assim (venv) está ativada, pode instalar os 
requirements nesse ambiente criado

4 - Instale os requirements com a venv ativa (venv) com o comando pip install -r requirements.txt

5 - Execute o comando python manage.py makemigrations e python manage.py migrate para executar as migrações e popular 
o banco de dados, em seguida execute com python manage.py runserver na porta 8000.

