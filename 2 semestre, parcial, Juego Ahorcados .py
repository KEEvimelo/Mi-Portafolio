#Parcial 12/10/23

#JuegoAhorcado
import random

# Función para obtener una palabra aleatoria de una lista predefinida.
def obtener_palabra():
    Palabras = ["programacion", "perro", "game", "codigo", "lapiz"]
    palabra_aleatoria = random.choice(Palabras)
    return palabra_aleatoria

# Función para mostrar el tablero del juego.
def mostrar_Tablero(palabra_secreta, Letras_adivinadas):
    Tablero = ""
    for letra in palabra_secreta:
        if letra in Letras_adivinadas:
            Tablero += letra
        else:
            Tablero += "_"
    print(Tablero)

# Función principal para jugar el juego.
def Jugar():
    palabra_secreta = obtener_palabra()  # Obtiene una palabra aleatoria.
    Letras_adivinadas = []  # Inicializa la lista de letras adivinadas.
    Intentos_restantes = 8  # Número de intentos restantes antes de perder.

    while Intentos_restantes > 0:
        mostrar_Tablero(palabra_secreta, Letras_adivinadas)  # Muestra el tablero actual del juego.
        letra = input("Introduce una Letra: ").lower()  # Solicita al jugador una letra y la convierte a minúsculas.

        if letra in Letras_adivinadas:
            print("Ya has puesto una letra, Prueba con otra.")
            continue  # Si la letra ya se adivinó antes, se solicita otra letra.

        if letra in palabra_secreta:
            Letras_adivinadas.append(letra)  # Agrega la letra a la lista de letras adivinadas.
            if set(Letras_adivinadas) == set(palabra_secreta):
                print("Felicitaciones, has acertado la palabra.")
                break  # Si se han adivinado todas las letras de la palabra, se gana el juego.

        else:
            Intentos_restantes -= 1  # Reduce el número de intentos restantes.
            print(f"Letra incorrecta, Te quedan {Intentos_restantes} intentos.")

    if Intentos_restantes == 0:
        print(f"Has perdido. La palabra secreta era: {palabra_secreta}")

# Llama a la función principal para comenzar el juego.
Jugar()
