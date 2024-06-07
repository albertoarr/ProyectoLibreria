# ProyectoLibreria

Programas necesarios:

Python 

Comandos de instalación en consola de Ubuntu:

0. Antes de empezar usamos:

python --version 

- SI APARECE LA VERSIÓN INSTALADA NO NECESITAMOS SEGUIR

1. Actualizamos herramienta de paquetes de Ubuntu:

sudo apt update

2. Descargamos software-properties-common

sudo apt install software-properties-common

3. Instalamos deadsnakes 

sudo add-apt-repository ppa:deadsnakes/ppa

4. Volvemos a actualizar los paquetes -y 

sudo apt update && sudo apt upgrade

5. Instalamos Python:

sudo apt-get install python3-pip


Dependencias necesarias:

asgiref==3.8.1
Django==5.0.6
sqlparse==0.5.0
tzdata==2024.1


Para instalar las anteriores dependencias debemos tener instalado python y usar los siguientes comandos (tanto windows como Ubuntu):

pip install asgiref==3.8.1

pip install Django==5.0.6

pip install sqlparse==0.5.0

pip install tzdata==2024.1



Si queremos activar el entorno virtual y no se nos permite por falta de una firma digital, en la consola usaremos el comando

Set-ExecutionPolicy Unrestricted -Scope Process