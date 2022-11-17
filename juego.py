import random

def menu():
    print("ADIVINA EL NUMERO")
    print("-----------------")
    print("1: Nivel Simple (Entre 0 y 100)")
    print("2: Nivel Intermedio (Entre 0 y 1000)")
    print("3: Nivel Avanzado (Entre 0 y 1000000)")
    print("4: Nivel Experto (Entre 0 1000000000000)")
    print("5: Salir")

def niveles():
    while True:
        nivel=input("Introduzca el nivel de dificultad: ")
        nivel=int(nivel)
        if nivel == 1:
            return 99
            break
        elif nivel == 2:
            return 999
            break
        elif nivel == 3:
            return 9999
            break
        elif nivel == 4:
            return 999999999999
            break
        elif nivel == 5:
            break

def limites(maximo):
    numero = random.randint(0, maximo)
    return numero
    print(numero)

def juego():
    while True:

        intento = input("Introduzca numero entre 0 y " + str(maximo) + " incluidos: ")
        intento = int(intento)

        if intento < numero:
            print("El numero es demasiado pequeño")
        elif intento > numero:
            print("El numero es demasiado grande")
        else:
            print("¡Has acertado!")
            break

def ayuda(intento):

    ayuda = input("¿Quieres una pista?(s/n): ")
    
    if ayuda == "s":
        if intento < numero:
            minimo = intento
        elif intento > numero:
            maximo = intento


menu()
maximo=niveles()        
numero=limites(maximo)
juego()
