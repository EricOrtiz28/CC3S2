## git rebase para mantener un historial lineal
![alt text](imagenes/image-20.png)
**Escenario de ejemplo:**
- Crea un nuevo repositorio Git y dos ramas, main y new-feature:
~~~
mkdir try-git-rebase   # Crea un nuevo directorio llamado 'try-git-rebase'
cd try-git-rebase      # Cambia al directorio 'try-git-rebase'
git init               # Inicializa un nuevo repositorio Git en el directorio actual
echo "# Mi Proyecto de Rebase" > README.md   # Crea un archivo README.md con el texto "# Mi Proyecto de Rebase"
git add README.md      # Añade el archivo README.md al área de staging
git commit -m "Commit inicial en main"   # Realiza un commit con el mensaje "Commit inicial en main"
~~~
![alt text](imagenes/image.png)
- Crea y cambia a la rama new-feature:
~~~
git checkout -b new-feature   # Crea y cambia a una nueva rama llamada 'new-feature'
echo "Esta es una nueva característica." > NewFeature.md   # Crea un archivo NewFeature.md con el texto "Esta es una nueva característica."
git add NewFeature.md         # Añade el archivo NewFeature.md al área de staging
git commit -m "Agregar nueva característica"   # Realiza un commit con el mensaje "Agregar nueva característica"
~~~
![alt text](imagenes/image-1.png)
![alt text](imagenes/image-2.png)
![alt text](imagenes/image-3.png)

-Cambiar de nuevo a 'main' y agregar nuevos commits
~~~
git checkout main   # Cambia de vuelta a la rama 'main'
echo "Updates to the project." >> Updates.md   # Añade la línea "Updates to the project." al archivo Updates.md (o lo crea si no existe)
git add Updates.md   # Añade el archivo Updates.md al área de staging
git commit -m "Update main"   # Realiza un commit con el mensaje "Update main"
~~~
![alt text](imagenes/image-4.png)
![alt text](imagenes/image-5.png)
![alt text](imagenes/image-6.png)

> Tarea: Realiza el rebase de new-feature sobre main con los siguientes comandos:
~~~
git checkout new-feature   # Cambia a la rama 'new-feature'
git rebase main   # Realiza el rebase de la rama 'new-feature' sobre la rama 'main'
~~~
![alt text](imagenes/image-8.png)
**3. Revisión:**
Después de realizar el rebase, visualiza el historial de commits con:
~~~
git log --graph --oneline   # Muestra el historial de commits en forma gráfica y compacta, después del rebase
~~~
![alt text](imagenes/image-7.png)
**4. Momento de fusionar y completar el proceso de git rebase:**
Cambiar a 'main' y realizar una fusión fast-forward
~~~
git checkout main   # Cambia a la rama 'main'
git merge new-feature   # Realiza una fusión fast-forward de la rama 'new-feature' en 'main', completando el proceso de rebase
~~~
![alt text](imagenes/image-9.png)
## git cherry-pick para la integración selectiva de commit
![alt text](imagenes/image-21.png)
ejemplo:
**Inicializar un nuevo repositorio**
~~~
mkdir try-cherry-pick   # Crea un nuevo directorio llamado 'try-cherry-pick'
cd try-cherry-pick      # Cambia al directorio 'try-cherry-pick'
git init                # Inicializa un nuevo repositorio Git en el directorio actual
~~~
![alt text](imagenes/image-10.png)
**Agregar y commitear README.md inicial a main**
~~~
echo "# My Project" > README.md   # Crea un archivo README.md con el texto "# My Project"
git add README.md                 # Añade el archivo README.md al área de staging
git commit -m "Initial commit"    # Realiza un commit con el mensaje "Initial commit"
~~~
![alt text](imagenes/image-11.png)
**Crear y cambiar a una nueva rama 'add-base-documents'**
~~~
git checkout -b add-base-documents   # Crea y cambia a una nueva rama llamada 'add-base-documents'
~~~
![alt text](imagenes/image-12.png)
**Hacer cambios y commitearlos**
**Agregar CONTRIBUTING.md**
~~~
echo "# CONTRIBUTING" >> CONTRIBUTING.md   # Crea el archivo CONTRIBUTING.md con el texto "# CONTRIBUTING"
git add CONTRIBUTING.md                    # Añade CONTRIBUTING.md al área de staging
git commit -m "Add CONTRIBUTING.md"        # Realiza un commit con el mensaje "Add CONTRIBUTING.md"
~~~
![alt text](imagenes/image-13.png)
**Agregar LICENSE.txt**
~~~
echo "LICENSE" >> LICENSE.txt   # Crea el archivo LICENSE.txt con el texto "LICENSE"
git add LICENSE.txt             # Añade LICENSE.txt al área de staging
git commit -m "Add LICENSE.txt" # Realiza un commit con el mensaje "Add LICENSE.txt"
~~~
![alt text](imagenes/image-14.png)
![alt text](imagenes/image-15.png)
**Echa un vistazo al log de la rama 'add-base-documents'**
~~~
git log add-base-documents --graph --oneline   # Muestra el historial de commits de la rama 'add-base-documents' en formato gráfico y compacto
~~~
![alt text](imagenes/image-16.png)
>Tarea: Haz cherry-pick de un commit de add-base-documents a main:
~~~
git checkout main                     # Cambia a la rama 'main'
git cherry-pick a80e8ad               # Aplica el commit específico con el hash 'a80e8ad' de la rama 'add-base-documents' en 'main'
~~~
![alt text](imagenes/image-17.png)

**Revisión: Revisa el historial nuevamente:**
~~~
git log --graph --oneline   # Muestra el historial de commits de manera gráfica y compacta para verificar que el cherry-pick fue exitoso
~~~
![alt text](imagenes/image-18.png)
![alt text](imagenes/image-19.png)
