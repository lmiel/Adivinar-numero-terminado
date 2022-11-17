def menu():
    print("ADIVINA EL NUMERO")
    print("-----------------")
    print("1: Nivel Simple (Entre 0 y 100)")
    print("2: Nivel Intermedio (Entre 0 y 1000)")
    print("3: Nivel Avanzado (Entre 0 y 1000000)")
    print("4: Nivel Experto (Entre 0 1000000000000)")
    print("5: Salir")

#recibe la eleccion del menu del usuario
def niveles():
    while True:
        limMaximo = -1
        intentos = -1
        nivel=input("Introduzca el nivel de dificultad: ")
        nivel=int(nivel)
        if nivel == 1:
            limMaximo =  99
            intentos = 10
            break
        elif nivel == 2:
            limMaximo = 999
            intentos = 15
            break
        elif nivel == 3:
            limMaximo = 9999
            intentos = 20
            break
        elif nivel == 4:
            limMaximo = 999999999999
            intentos = 30
            break
        elif nivel == 5:
            limMaximo = -1
            intentos = -1
            break
    return limMaximo, intentos

#funcion de muestra de ayuda
def ayuda(limitemin, limitemax):

    ayuda = input("¿Quieres una pista?(s/n): ")

    if ayuda == "s":
        print("El numero se encuentra entre: " + str(limitemin) + " y " + str(limitemax))
