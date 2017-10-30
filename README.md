# <b>miiloos</b>

## <b>Navegação</b>
[Requerimentos](#requerimentos)<br>
[Instalação (Windows)](#instalação-windows)<br>
[Instalação (Linux)](#instalação-linux)<br>
[Execução](#execução)<br>


## Requerimentos
* Python (certifique que está no seu PATH)


## Instalação (Windows)
```
git clone https://github.com/JVUnderground/miiloos.git
cd miiloos
pip install virtualenv
virtualenv env
.\env\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

## Instalação (Linux)
```
git clone https://github.com/JVUnderground/miiloos.git
cd miiloos
pip install virtualenv
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

## Execução
```
python manage.py runserver
```