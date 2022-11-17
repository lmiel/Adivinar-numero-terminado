import entrada as en
import juego as jg


#funcion main, inicializacion de variables, llamada a play y guardado de record
def main():
    records = []

    while True:
        en.menu()
        limMaximo = -1 #dummy value
        intentosMax = -1

        #get the random number
        limMaximo, intentosMax = en.niveles()
        if limMaximo == -1 and intentosMax == -1:
            break        
        randomNum = jg.getRandomNum(limMaximo)

        jg.play(randomNum, limMaximo, intentosMax, records)
        print(records)


#El programa empieza aqui, llamamos a la funcion main
if __name__=="__main__":
    main()
