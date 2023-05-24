import random

def jugar():
    elecciones = ["piedra", "papel", "tijera"]
    print("Bienvenido a piedra,papel o tijera.")

    while True:
        jugador = input("Ingresa tu elección (piedra/papel/tijera) o 'q' para : ").lower()

        if jugador == "q":
            print("Gracias por jugar.")
            break

        if jugador not in elecciones:
            print("Ingresa un elección válida.")
            continue

        computadora = random.choice(elecciones)

        print(f"\nElegiste: {jugador}")
        print(f"La computadora elige: {computadora}\n")

        resultado = determinar_ganador(jugador, computadora)
        print(resultado)
        print()
def determinar_ganador(jugador, computadora):
    if jugador == computadora:
        return "Es un empate"
    elif (
        (jugador == "piedra" and computadora == "tijera")
        or (jugador == "papel" and computadora == "piedra")
        or (jugador == "tijera" and computadora == "papel")
    ):
        return "Ganaste!"
    else:
        return "Gana la computadora!"

jugar()



