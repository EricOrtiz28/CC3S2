import random

# Función para seleccionar una palabra aleatoria desde un archivo
def seleccionar_palabra():
    
    with open("words.txt", "r") as file:
        palabras = file.read().splitlines()  
    return random.choice(palabras) 

# Función para manejar el intento de adivinar una letra
def adivinar_letra(palabra_secreta,progreso,letra,progreso_anterior):

    global intentos_restantes
    # Si la letra está en la palabra secreta, se actualiza el progreso
    if letra in palabra_secreta:
        print(f"\n    ¡Correcto! La letra '{letra}' está en la palabra.")

        for i in range(len(palabra_secreta)):
            if palabra_secreta[i] == letra:
                progreso[i] = letra
     # Si la letra no está en la palabra, se informa al jugador
    else:
        print(f"\n    La letra '{letra}' no está en la palabra\n") 

    # Reduce el número de intentos si el progreso no ha cambiado
    if progreso_anterior == progreso:
            intentos_restantes -= 1
            print(f"    Intentos restantes: {intentos_restantes}")

    return progreso

# Función para dar pistas al jugador
def dar_pista(palabra_secreta,progreso):

    global numero_pistas,intentos_restantes,Diferencia_intentos

    # Condiciones para dar una pista
    if numero_pistas > 0 and Diferencia_intentos - intentos_restantes == 2:

        respuesta = input("    ¿Necesitas una pista? (s/n): ")

        if respuesta == "s":
            # Selecciona una letra aleatoria que aún no ha sido adivinada y la revela en el progreso
            pista = random.choice(palabra_secreta)

            while pista in progreso:
                pista = random.choice(palabra_secreta)

            print(f"\n    Pista: La letra {pista} está en la palabra.\n")
            # Actualiza el progreso revelando la letra de la pista
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] == pista:
                    progreso[i] = pista

            print(f"    Palabra: {' '.join(progreso)} (progreso actual)\n")      
            # Actualiza el número de pistas restantes
            numero_pistas -= 1
            print(f"    Pistas restantes: {numero_pistas}\n")
            Diferencia_intentos = intentos_restantes # Restablece la diferencia de intentos

        else:
            print("")
            Diferencia_intentos = intentos_restantes 

    return progreso



# Código principal del juego
if __name__ == "__main__":

    # Inicialización de variables de juego
    palabra_secreta = seleccionar_palabra()
    progreso = ['_'] * len(palabra_secreta)
    intentos_restantes = 20
    numero_pistas = 5

    print("\n===================================================\n")
    print(f"    Palabra: {' '.join(progreso)} (progreso actual)\n") 

    Diferencia_intentos = intentos_restantes # Inicialización para seguimiento de intentos entre pistas

    # Bucle principal del juego
    while intentos_restantes > 0 and '_' in progreso:

        # Solicita al jugador que adivine una letra
        letra = input("    Adivinar una letra: ").lower()

        progreso_anterior = progreso[:] # Copia del progreso antes de adivinar
        progreso = adivinar_letra(palabra_secreta,progreso,letra,progreso_anterior)

        print("\n===================================================\n")
        print(f"    Palabra: {' '.join(progreso)}\n")
        # Llama a la función para dar pistas, si es necesario
        progreso = dar_pista(palabra_secreta,progreso)




        
                
                




        



 
    