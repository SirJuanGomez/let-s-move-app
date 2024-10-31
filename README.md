# Les't Move App

## Descripción
Les't Move App es una aplicación con una interfaz de usuario intuitiva basada en Tkinter, que utiliza la API de Fitbit para obtener datos sobre pasos, distancia recorrida y calorías quemadas. Esta herramienta te permite visualizar y analizar tus métricas de actividad física de manera sencilla y atractiva.

## Funcionalidades
- **Interfaz de usuario amigable**: Navega fácilmente por la aplicación utilizando Tkinter.
- **Obtener datos de pasos**: Accede a la cantidad de pasos diarios.
- **Distancia recorrida**: Consulta la distancia total recorrida en kilómetros.
- **Calorías quemadas**: Visualiza las calorías quemadas en el día.

## Tecnologías
- **Lenguaje**: Python
- **Framework**: Tkinter (para la interfaz de usuario), Pillow (para el procesamiento de imagenes) y matplotlib (para la creacion de graficos)
- **API**: API de Fitbit

## Requisitos
- Tener una cuenta de Fitbit y configurar una aplicación en el [portal de desarrolladores de Fitbit](https://dev.fitbit.com/).
- Python instalado en tu máquina.

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/SirJuanGomez/les_t_move_app.git
   cd les_t_move_app


2. Instala las dependencias desde ```setup.py```:
    
    ```bash
   cd les_t_move_app
   python setup.py


3.Configura las credenciales de la API de Fitbit. Edita un archivo llamado ```api.py``` dentro de la carpeta ```configuracion``` y agrega tus credenciales:

    CLIENT_ID="tu_client_id"
    CLIENT_SECRET="tu_client_secret"
    ACCES_TOKEN="tu_acces_token" 
    REFRESH_TOKEN="tu_token_de_refresco"


## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)

## Referencias de la API

La Les't Move App utiliza la API de Fitbit para acceder a la información de actividad física del usuario. A continuación se presentan las principales API y sus endpoints utilizados:

### 1. **Obtener Datos de Pasos**
- **Endpoint**: `GET /1/user/[user-id]/activities/steps/date/[date]/[period].json`
- **Descripción**: Obtiene el número de pasos que el usuario ha dado en un día específico.
- **Documentación**: [Fitbit Steps API](https://dev.fitbit.com/build/reference/web-api/activity/steps/)

### 2. **Obtener Distancia Recorrida**
- **Endpoint**: `GET /1/user/[user-id]/activities/distance/date/[date]/[period].json`
- **Descripción**: Recupera la distancia recorrida por el usuario en un día determinado.
- **Documentación**: [Fitbit Distance API](https://dev.fitbit.com/build/reference/web-api/activity/distance/)

### 3. **Obtener Calorías Quemadas**
- **Endpoint**: `GET /1/user/[user-id]/activities/calories/date/[date]/[period].json`
- **Descripción**: Obtiene el total de calorías quemadas en un día específico.
- **Documentación**: [Fitbit Calories API](https://dev.fitbit.com/build/reference/web-api/activity/calories/)

### Autenticación
Para acceder a la API de Fitbit, es necesario autenticar a los usuarios utilizando OAuth 2.0. Asegúrate de seguir las instrucciones en la [documentación de autenticación de Fitbit](https://dev.fitbit.com/build/reference/web-api/oauth2/).

## Notas Adicionales
- Asegúrate de revisar los límites de tasa y las políticas de uso de la API de Fitbit.
- Puedes encontrar más información sobre la API en el [portal de desarrolladores de Fitbit](https://dev.fitbit.com/).
- En el archivo de ```mas_opciones.py``` exite una importacion comentada donde el usuario puede quitarlo para obtener el codigo desde ``apy.py`` o desde ``test_data.py``
## Apéndices

### A. Consideraciones de Seguridad
- **Autenticación**: Asegúrate de que las credenciales de la API de Fitbit no se expongan en el código fuente. Utiliza un archivo `.env` o una carpeta de configuración para mantenerlas seguras.
- **Manejo de Datos**: Ten en cuenta las políticas de privacidad y manejo de datos de los usuarios. Asegúrate de que los datos obtenidos a través de la API se manejen de manera responsable y ética.

### B. Estructura del Proyecto
- **carpeta `configuracion`**: Contiene archivos de configuración, incluyendo `configr.py` para las credenciales de la API.
- **archivo `app.py`**: Archivo principal de la aplicación que inicia la interfaz de usuario y maneja la lógica del programa.
- **archivo `setup.py`**: Define las dependencias y la configuración del paquete para instalar las librerías necesarias.

### C. Dependencias
Las dependencias del proyecto están definidas en el archivo `setup.py`. Asegúrate de que están actualizadas y de que tu entorno de Python tiene acceso a ellas.

### D. Problemas Comunes
1. **Error de Autenticación**: Si encuentras un error al autenticarte con la API de Fitbit, verifica que tus credenciales en `api.py` sean correctas.
2. **Problemas de Conexión**: Asegúrate de que tu conexión a Internet sea estable y de que los endpoints de la API de Fitbit estén disponibles.

### E. Recursos Adicionales
- **Documentación de Tkinter**: [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- **Documentación de la API de Fitbit**: [Fitbit API Documentation](https://dev.fitbit.com/build/reference/web-api/)
- **Foros y Comunidades**: Considera unirte a foros como Stack Overflow para obtener ayuda y compartir conocimientos.

## Autores

- **Sir Juan Gómez**: [SirJuanGomez](https://github.com/SirJuanGomez) - Desarrollador principal y creador de la Les't Move App.

## Badges

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![GitHub Issues](https://img.shields.io/github/issues/SirJuanGomez/les_t_move_app)
![Last Commit](https://img.shields.io/github/last-commit/SirJuanGomez/les_t_move_app)
## Color Reference

| Color            | Hex                                                                |
| ---------------- | ------------------------------------------------------------------ |
| Dark Navy        | ![#0a192f](https://via.placeholder.com/10/0a192f?text=+) #0a192f  |
| Light Gray       | ![#f8f8f8](https://via.placeholder.com/10/f8f8f8?text=+) #f8f8f8  |
| Teal             | ![#00b48a](https://via.placeholder.com/10/00b48a?text=+) #00b48a  |
| Bright Teal      | ![#00d1a0](https://via.placeholder.com/10/00d1a0?text=+) #00d1a0  |
| White            | ![#ffffff](https://via.placeholder.com/10/ffffff?text=+) #ffffff  |
| Black            | ![#000000](https://via.placeholder.com/10/000000?text=+) #000000  |
| Blue             | ![#0000ff](https://via.placeholder.com/10/0000ff?text=+) #0000ff  |
| Red              | ![#ff0000](https://via.placeholder.com/10/ff0000?text=+) #ff0000  |

## Contributing

¡Las contribuciones son bienvenidas! Si deseas contribuir a **Les't Move App**, aquí hay algunas formas en las que puedes hacerlo:

1. **Reportar un problema**: Si encuentras un error o tienes una sugerencia de mejora, abre un issue en el repositorio. Proporciona tantos detalles como sea posible para que podamos entender el problema.

2. **Solicitar una nueva función**: Si tienes una idea para una nueva función que crees que mejoraría la aplicación, siéntete libre de abrir un issue para discutirla.

3. **Enviar un pull request**: Si deseas hacer cambios en el código, sigue estos pasos:
   - Haz un fork del repositorio.
   - Crea una nueva rama para tu función o corrección de errores:
     ```bash
     git checkout -b nombre-de-tu-rama
     ```
   - Realiza tus cambios y asegúrate de que todo funcione correctamente.
   - Envía tu pull request explicando los cambios que has realizado.


### Agradecimientos

¡Gracias por tu interés en contribuir a Les't Move App! Cada contribución ayuda a mejorar la aplicación y hacerla más útil para todos.
## Deployment

A continuación, se describen los pasos necesarios para desplegar la **Les't Move App** en tu entorno local.

### Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- Python 3.8 o superior
- pip (el gestor de paquetes de Python)
- Una cuenta de Fitbit y las credenciales de la API configuradas.

### Pasos de Despliegue

1. **Clonar el repositorio:**

   Abre tu terminal y ejecuta:

   ```bash
   git clone https://github.com/SirJuanGomez/les_t_move_app.git
   cd les_t_move_app
## Documentation

La documentación completa de **Les't Move App** incluye detalles sobre la instalación, configuración, uso y características avanzadas de la aplicación.

### Instalación

1. **Requisitos**: Asegúrate de tener Python 3.8 o superior y las dependencias instaladas (ver sección [Deployment](#deployment)).
2. **Configuración de la API**: Detalles sobre cómo configurar las credenciales de la API de Fitbit se encuentran en la sección [Deployment](#deployment).

### Uso

- **Interfaz de Usuario**: La aplicación está diseñada para ser intuitiva y fácil de usar. Al abrir la aplicación, verás un menú principal donde puedes elegir entre diferentes opciones para visualizar tus datos de actividad.
  
- **Funciones Clave**:
  - **Visualizar Datos de Pasos**: Accede a la cantidad de pasos diarios y visualízalos en un gráfico.
  - **Distancia Recorrida**: Consulta la distancia total recorrida en kilómetros.
  - **Calorías Quemadas**: Revisa las calorías quemadas durante el día.

### Ejemplo de Uso

1. Abre la aplicación y autentícate con tu cuenta de Fitbit.
2. Selecciona la opción deseada en el menú para ver tus estadísticas.

### API Reference

Para más detalles sobre la API de Fitbit, consulta la [Documentación de la API de Fitbit](https://dev.fitbit.com/build/reference/web-api/).

### Más Información

Para más detalles sobre la implementación y otras características avanzadas, consulta los archivos en el repositorio o contacta al autor.

## FAQ

### 1. ¿Necesito una cuenta de Fitbit para usar la aplicación?
Sí, debes tener una cuenta de Fitbit y las credenciales de la API para acceder a tus datos.

### 2. ¿Qué versiones de Python son compatibles?
La aplicación está diseñada para funcionar con Python 3.8 o superior.

### 3. ¿Qué hago si encuentro un error?
Si encuentras un error, por favor abre un issue en el repositorio con una descripción detallada del problema. Intentaremos solucionarlo lo antes posible.

### 4. ¿Puedo usar esta aplicación sin conexión a Internet?
No, la aplicación necesita acceso a Internet para conectarse a la API de Fitbit y obtener tus datos.

### 5. ¿Cómo puedo contribuir al proyecto?
Consulta la sección [Contributing](#contributing) para más información sobre cómo puedes contribuir.

### 6. ¿Dónde puedo encontrar más información sobre la API de Fitbit?
Puedes consultar la [Documentación de la API de Fitbit](https://dev.fitbit.com/build/reference/web-api/) para obtener detalles completos sobre los endpoints y cómo usarlos.

### 7. ¿Hay alguna guía para la instalación y configuración?
Sí, revisa la sección [Deployment](#deployment) para obtener instrucciones detalladas sobre cómo instalar y configurar la aplicación.

## Feedback

¡Tu opinión es muy importante para nosotros! Si has probado **Les't Move App**, nos encantaría escuchar tus comentarios.

### ¿Cómo dejar tu feedback?

1. **Abrir un Issue**: Si tienes sugerencias, comentarios o encontraste un error, puedes abrir un issue en el repositorio de GitHub. Por favor, incluye una descripción detallada para que podamos entender mejor tu experiencia.

2. **Enviar un Correo Electrónico**: Si prefieres, puedes enviar tus comentarios directamente a [juangomez154879@gmail.com]. 

3. **Encuesta de Satisfacción**: Estamos trabajando en una encuesta de satisfacción. Por favor, mantente atento a la sección de noticias en el repositorio para participar.

### Agradecimientos

Agradecemos de antemano tu tiempo y tus sugerencias. Tu feedback nos ayuda a mejorar y a hacer de **Les't Move App** una herramienta más útil y efectiva para todos.
## Used By

**Les't Move App** es un proyecto desarrollado como parte de la asignatura **Fundamentos de la Informática Electrónica** en [Universidad Santiago de Cali]. El objetivo del proyecto es integrar datos de Fitbit para ayudar a los usuarios a monitorear su actividad física y fomentar un estilo de vida saludable.

### Proyecto Académico

Este proyecto demuestra el uso de APIs, el desarrollo de interfaces de usuario con Tkinter y la gestión de datos en aplicaciones de Python. Se espera que sirva como un recurso útil para estudiantes y profesionales interesados en el desarrollo de aplicaciones relacionadas con la salud y el bienestar.

### ¿Tienes un proyecto similar?

Si has utilizado **Les't Move App** en un contexto académico o de investigación, ¡nos encantaría saberlo! Abre un issue o envíanos un correo a [juan.gomez44@usc.edu.co] para compartir tu experiencia.
## Support

Si necesitas ayuda con **Les't Move App**, aquí tienes algunas formas de obtener soporte:

### Reportar Problemas

Si encuentras un error o tienes un problema con la aplicación, por favor abre un issue en el [repositorio de GitHub](https://github.com/SirJuanGomez/les_t_move_app/issues). Proporciona una descripción detallada del problema, incluyendo pasos para reproducirlo si es posible.

### Preguntas Comunes

Consulta la sección de [FAQ](#faq) para ver si tu pregunta ya ha sido respondida.

### Documentación

Asegúrate de revisar la [Documentación](#documentation) para obtener información sobre la instalación, configuración y uso de la aplicación.

### Contacto

Si necesitas ayuda adicional, puedes contactarme directamente en [juan.gomez44@usc.edu.co]. Intentaré responder lo más rápido posible.

### Comunidades

Puedes unirte a comunidades de desarrolladores, como Stack Overflow o foros de Python, donde puedes hacer preguntas y compartir experiencias con otros desarrolladores.

