# **Repositorio de DjangoAuth**

Este repositorio es creado con la finalidad de utilizar las API´s de autenticación como **Facebook**, **GitHub**, **Google**, **LinkedIn** y **Yahoo!** utilizando como lenguaje de programación **Python** y como framework **Django**

## **Nota**

Para saber más sobre **Django** puedes visitar la documentación dando click [**Aquí**](https://docs.djangoproject.com/en/3.2/)

## **Instalación**

**Nota:** Para clonar el repositorio debes tener descargado [**Git**](https://git-scm.com/download/win) en tu ordenador.

### **Paso 1**

**Forma 1:** Dar clic en **Code**, luego **Download Zip** y descomprimir el archivo en tu ordenador.

**Forma 2:** Abrir una terminal en tu ordenador y ejecutar el siguiente comando:

    git clone https://github.com/HenryGP14/DjangoAuth.git

### **Paso 2**

Instalar Python en: https://www.python.org/downloads/

### **Paso 3**

Instalar Django ejecutando el siguente comando en la consola de tu ordenador

    pip install django==3.0.8

### **Paso 4**

Configurar el archivo **.env**, este archivo es aquel que contendrá todas las configuraciones necesarias para que el aplicativo funcione.

-   **Primero:** Cambiar el nombre del archivo "**.env.example**"a "**.env**"

-   **Segundo:** Generar una Secret Key.

**Forma 1:** Generar la Secret Key por python consola [**Click aquí para más información.**](https://pypi.org/project/secret-key-generator/)

**Forma 2:** Generar la Secret Key por Online visitar la página de [**Djecrety.**](https://djecrety.ir/)

-   **Tercero:** Configurar el acceso del motor de base de datos.

-   **Cuarto:** Colocar la Secret Key en <font color=red>**SECRET_KEY**</font> en el archivo **.env**
-   **Quinto:** Configurar las **User ID** y **Secret Key** de las API's a utilizar en este caso [**Facebook**](https://developers.facebook.com/?locale=es_ES), [**GitHub**](https://github.com/settings/developers), [**LinkedIn**](https://www.linkedin.com/developers/), [**Google**](https://developers.google.com/) y [**Yahoo!**](https://developer.yahoo.com/).
-   **Sexto:** Instalar los paquetes para leer el archivo de configuración **.env** con los siguientes comandos en consola:

        pip install django-environ

    **y**

        pip install python-dotenv

-   **Séptimo:** Instalar el paquete **social-auth-app-django** ejecutar el siguente comando en consola:

        pip install social-auth-app-django

    , este paquete permitirá comunicar la aplicación con las API's sociales, [para más información del paquete consulte la documentación oficial de **social-auth-app-django**](https://python-social-auth.readthedocs.io/en/latest/index.html#).

### **Paso 5**

Configurar la conexión con el motor de base de datos a utilizar

**Nota:** Esta aplicación se realizó con la conexión al motor de base de datos de [**PostgreSQL**](https://www.postgresql.org/), para cambiar a otro motor de base de datos leer la documentación de [**Django Setting**](https://docs.djangoproject.com/en/3.2/ref/databases/#mysql-notes)

-   **Primero:** Intalar el paquete que permite conectar la aplicación con la base de datos, ejecutar el siguiente comando en consola:

          pip install psycopg2==2.8.6

-   **Segundo:** Configurar la conexión de la base de datos en el archivo **.env**
-   **Tercero:** Ejecutar el siguiente comando en consola:

        python manage.py migrate

### **Paso 6**

Ejecutar la aplicación con el siguiete comando en consola:

    python manage.py runserver

## **Contribución**

1. Crea un Fork del repositorio
2. Clonar en tu ordenador mediante git clone https://github.com/HenryGP14/DjangoAuth.git
3. Crear una nueva rama
4. Realizar tus cambios
5. Manda tu pull request
