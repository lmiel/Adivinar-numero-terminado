import random
import entrada as en
import juego as jg

def scoreBoard(puntuacion, records):
    userName = input("Introduzca Usuario: ")
    records.append(str(userName) + " " + str(puntuacion))

def play(randomNum, maximo, intentosMax, records):
    
    limitemin = 0
    limitemax = maximo

    intentos = 0

    while True:
        en.ayuda(limitemin, limitemax)
        numberGuessed = int(input("Introduzca numero entre 0 y " + str(maximo) + " incluidos: "))

        intentos = intentos + 1

        if numberGuessed < randomNum:
            print("El numero es demasiado pequeño")
        elif numberGuessed > randomNum:
            print("El numero es demasiado grande")
        else:
            print("¡Has acertado!")
            scoreBoard(intentos, records)
            break
        
        if intentos > intentosMax:
            print("Demasiados intentos")
            break

        limitemin, limitemax = nuevoslim(numberGuessed, randomNum, limitemin, limitemax)

def nuevoslim(numberGuessed, randomNum, limitemin, limitemax):
    if numberGuessed < randomNum:
        if numberGuessed > limitemin:
            return numberGuessed, limitemax
    else:
        if numberGuessed < limitemax:
            return limitemin, numberGuessed
    return limitemin,limitemax

def getRandomNum(maximo):
    numero = random.randint(0, maximo)
    return numero
