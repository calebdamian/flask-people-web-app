
Guía para ejecutar el proyecto Flask
====================================

Este es un proyecto Flask que utiliza una base de datos MySQL para almacenar información sobre personas. Sigue estas instrucciones para configurar y ejecutar el proyecto en tu máquina local.

Requisitos previos
------------------

-   Python 3.x instalado en tu sistema. Puedes descargarlo desde python.org.
-   Un gestor de bases de datos MySQL instalado en tu máquina. Puedes descargar MySQL Community Server desde mysql.com.
-   Git instalado en tu sistema. Puedes descargarlo desde git-scm.com.

Configuración del entorno virtual
---------------------------------

1.  Clona este repositorio en tu máquina local:

    `git clone https://github.com/calebdamian/flask-people-web-app.git`

2.  Navega al directorio del proyecto:

 
    `cd flask-people-web-app`


Instalación de dependencias
---------------------------

1.  Instala las dependencias del proyecto:

    `pip install -r requirements.txt`

Configuración de la base de datos
---------------------------------

1. Crea la base de datos y la tabla Persona en MySQL corriendo el script SQL presente en la raíz del proyecto.  



2. Abre el archivo `.env` en la raíz del proyecto y configura la URI de la base de datos según tu entorno:

    `SQLALCHEMY_DATABASE_URI=mysql+mysqlconnector://<usuario>:<contraseña>@<host>/<nombre_de_la_base_de_datos>`

Ejecución del proyecto
----------------------

1.  Ejecuta el siguiente comando para iniciar el servidor Flask:


    `python run.py`

2.  Abre tu navegador web y visita `http://127.0.0.1:5000` para ver la aplicación en funcionamiento.
