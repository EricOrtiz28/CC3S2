# Actividad: Gestión ágil de proyectos con GitHub Projects: Configuración de Kanban Board y Creación de Historias de Usuario

**Parte 1**
En este ejercicio, aprenderás cómo configurar un Kanban board usando GitHub Projects para el repositorio del curso.

>Creamos nuestro proyecto y le pusimos el nombre de Lab Agile Planning.

![alt text](imagenes/image.png)

>Modificamos los nombres de las columnas.

![alt text](imagenes/image-1.png)

>Agregamos algunas columnas y finalmente quedó de esta manera.

![alt text](imagenes/image-2.png)

**Parte 2**
En este ejercicio, crearás una issue template en GitHub que te ayudará a escribir historias de usuario bien formateadas en el Kanban board.

>Se creó una plantilla de issue en GitHub seleccionando las configuraciones del repositorio, configurando las plantillas, eligiendo una plantilla personalizada, y editándola con el contenido necesario en formato markdown.

![alt text](imagenes/image-4.png)

>El resultado final se termina viendo así, con una plantilla de issue personalizada en GitHub que incluye campos como "name", "about", "title", "labels", y "assignees", además de una estructura para detalles y criterios de aceptación en formato markdown.

![alt text](imagenes/image-3.png)

**Parte 3**

En este ejercicio crearás siete historias de usuario basadas en los requisitos dados. Las primeras cuatro se te proporcionarán. Solo tendrás que copiarlas y pegarlas para familiarizarte con la creación de historias de usuario en GitHub. Deberás crear las últimas tres historias de usuario por ti mismo.Luego priorizarás estas historias y las moverás a las columnas apropiadas en tu Kanban board.

**1: Crear nuevas historias de usuario usando GitHub issues**

1. Ve a la pestaña Issues del repositorio del curso o donde estés trabajando la actividad.

![alt text](imagenes/image-5.png)

2. Haz clic en el botón New issue.

![alt text](imagenes/image-6.png)

3. Verás tu template listada aquí. Haz clic en el botón Get Started.

![alt text](imagenes/image-7.png)

4. Introduce el título para la primera historia como Need a service that has a counter y actualiza la sección de historia de usuario (es decir, As a, I need, So that) por ahora. Una vez hecho, haz clic en el botón Submit new issue.

![alt text](imagenes/image-8.png)

5. Tu primera historia de usuario ahora está creada.

![alt text](imagenes/image-9.png)

6. Agregar la historia de usuario creada al Kanban board, haz clic en el botón de configuración al lado de la opción Projects, y luego elige el proyecto Lab Agile Planning del menú desplegable que creaste en el ejercicio anterior.

![alt text](imagenes/image-10.png)

7. A continuación, selecciona el menú desplegable Status y elige New Issues. Esta acción moverá la historia de usuario creada a la columna 'New Issues' en el Kanban board.

![alt text](imagenes/image-11.png)

8. Para ver la historia de usuario recién creada en el Kanban board, navega a la pestaña Projects y selecciona el proyecto titulado Lab Agile Planning.

![alt text](imagenes/image-12.png)

9. Notarás que la historia de usuario recién creada ahora está listada bajo la columna New Issues.

![alt text](imagenes/image-13.png)

10. Dado que debemos crear un total de siete historias de usuario, ajustemos el límite predeterminado a 7. Para lograr esto, haz clic en los tres puntos de la columna New Issues, luego selecciona la opción Set limit.

![alt text](imagenes/image-14.png)

11. Introduce el límite como 7 en el campo de texto Column limit y haz clic en Save. Ten en cuenta que, similar a esto, puedes optar por modificar los límites de otras columnas o mantener los límites predeterminados.

![alt text](imagenes/image-15.png)
![alt text](imagenes/image-16.png)

12. Para regresar a la pestaña Issues para crear nuevas historias de usuario, simplemente haz clic en el botón de retroceso del navegador.

![alt text](imagenes/image-17.png)

13. Continúa agregando historias hasta que las siete estén creadas y tu Kanban board se parezca a la captura de pantalla mostrada a continuación. Las primeras cuatro historias se proporcionan en la lección. Deberás crear tu propio rol, función y beneficio para las últimas tres historias.

>Las primeras cuatro historias:

![alt text](imagenes/image-18.png)
![alt text](imagenes/image-19.png)
![alt text](imagenes/image-20.png)
![alt text](imagenes/image-21.png)

>las últimas tres historias:

![alt text](imagenes/image-22.png)
![alt text](imagenes/image-23.png)
![alt text](imagenes/image-24.png)

>Finalmente estas con las siete historias:

![alt text](imagenes/image-25.png)

**Ejercicio: Priorizar el product backlog**

En este ejercicio, moverás issues entre columnas para recrear el Kanban board del video de la lección **Building the Product Backlog.** Esto simulará un punto de partida inicial para nuestro próximo laboratorio sobre la refinación del backlog. Ten en cuenta que puedes mover los issues entre columnas simplemente arrastrándolos y soltándolos de una columna a otra.

1. Mueve la historia **Need a service that has a counter** al inicio de la columna **Product Backlog**.
2. Mueve la historia **Must allow multiple counters** a la columna **Icebox.**
3. Mueve la historia **Must persist counter across restarts** al final de la columna **Product Backlog.**
4. Mueve la historia **Counters can be reset** al final de la columna **Product Backlog.**
5. Deja las historias restantes en la columna **New Issues** por ahora. Las moveremos en un laboratorio posterior.

![alt text](imagenes/image-26.png)

**Parte 4**

En este ejercicio, seguirás los pasos para llevar a cabo una reunión de refinamiento del backlog.Serás el product owner preparando el product backlog para tu próxima reunión de planificación del sprint. Esto implica preparar las historias que creamos en el último ejercicio para hacerlas listas para el sprint.

**1: Triage de nuevos issues**

En este ejercicio, tomarás todas las historias en la columna **New Issues** y las moverás a una columna apropiada o las rechazarás.

1. Ve a github.com e inicia sesión con tu cuenta de GitHub y abre tu Kanban board.
2. El primer nuevo issue es **Deploy service to the cloud.** Queremos hacer eso después de agregar persistencia, así que muévelo a la columna **Product Backlog** bajo **Must persist counter across restarts.**

![alt text](imagenes/image-27.png)

3. El siguiente nuevo issue es **Need the ability to remove a counter.** Solo tenemos un contador y no quisiéramos eliminarlo, así que muévelo al **Icebox** después de **Must allow multiple counters.**

![alt text](imagenes/image-28.png)

4. El último nuevo issue es **Need ability to update a counter to a new value.** Podríamos querer hacerlo como una mejora después de poder reiniciar el contador, así que muévelo al **Product Backlog** después de **Counters can be reset.**

![alt text](imagenes/image-29.png)

Ahora has completado el triage de nuevos issues y puedes comenzar a hacer que las historias en la columna **Product Backlog** estén listas para el sprint.

**2: Hacer que las historias estén listas para el sprint**

En este parte, agregarás más detalles a las historias en el **Product Backlog** que creas que podrían entrar en el próximo sprint. Se te proporcionarán los detalles para dos de las historias. Debes proporcionar los detalles para las otras tres.

1. Selecciona la primera historia en la parte superior de la columna **Product Backlog** para abrirla. Haz clic en los tres puntos y luego selecciona el botón **Edit** para editar el issue.

2. Edita los **Details y Assumptions** para que los desarrolladores sepan lo que sabemos, y edita los **Acceptance Criteria** para asegurar que todos entiendan cuál es la definición de "hecho". Haz que tu historia se vea como esta:

![alt text](imagenes/image-30.png)

3. Cuando termines de editar, presiona el botón Save para guardar las ediciones.
4. Cierra la ventana presionando el icono de X.

![alt text](imagenes/image-31.png)

5. Edita la historia **Must persist counter across restarts** de la misma manera.

![alt text](imagenes/image-32.png)
![alt text](imagenes/image-33.png)

6. Edita las siguientes historias con tus propios detalles, suposiciones y criterios de aceptación:
• Deploy service to the cloud
• Counters can be reset
• Need ability to update a counter to a new value 

Al completar este ejercicio, tu Kanban board debería tener suficientes detalles en todas las historias del **Product Backlog** para hacerlas listas para el sprint.

![alt text](imagenes/image-34.png)
![alt text](imagenes/image-35.png)

![alt text](imagenes/image-36.png)
![alt text](imagenes/image-37.png)

![alt text](imagenes/image-38.png)
![alt text](imagenes/image-39.png)

**3: Crear nuevas labels en GitHub**

En este ejercicio, crearás una nueva **label** en GitHub llamada **technical debt** para marcar aquellas historias que no aportan valor visible al cliente pero deben completarse para continuar con el desarrollo.

1. Desde la página de tu repositorio, selecciona la pestaña **Issues.**

![alt text](imagenes/image-40.png)

2. Desde la página de issues, selecciona el botón **Labels.**

![alt text](imagenes/image-41.png)

3. Desde la página de labels, selecciona el botón **New label.**

![alt text](imagenes/image-42.png)

4. En la sección de nueva **label**: (1) establece el nombre de la **label** como **technical debt**, (2)
establece el Color como amarillo (#FBCA04), y luego (3) presiona el botón **Create label.**

![alt text](imagenes/image-43.png)

5. Ahora deberías ver una label amarilla technical debt que podemos usar para anotar
nuestras historias.

![alt text](imagenes/image-43.png)

**4: Añadir labels a las historias**

En este ejercicio, añadirás **labels** a las historias en el **Product Backlog** para hacerlas aún más listas para el sprint. También usarás nuestra nueva **label** llamada **technical debt** para marcar aquellas historias que no aportan valor visible al cliente pero deben completarse para continuar con el desarrollo.

1. Selecciona la primera historia en la parte superior de la columna **Product Backlog** para abrirla. Luego, presiona el icono de engranaje al lado de **Labels** para asignar una **label.**

![alt text](imagenes/image-45.png)

2. Nuestra primera historia es una mejora a nuestro producto. Desde el menú de *labels**, selecciona *enhancement** para reflejar eso.

![alt text](imagenes/image-44.png)

3. Haz clic en cualquier parte fuera del menú de **labels** para cerrarlo. Ahora deberías ver que la **label enhancement** ha sido asignada a esta historia.

![alt text](imagenes/image-46.png)

4. Selecciona cada una de las siguientes historias en la columna Product Backlog y asígnales las labels correspondientes:

* Story Title: **Must persist counter across restarts** Label: enhancement

![alt text](imagenes/image-47.png)

* Story Title: **Deploy service to the cloud** Label: technical debt

![alt text](imagenes/image-48.png)

* Story Title: **Counters can be reset** Label: enhancement

![alt text](imagenes/image-49.png)

* Story Title: **Need ability to update a counter to new value** Label: enhancement

![alt text](imagenes/image-50.png)

![alt text](imagenes/image-51.png)

