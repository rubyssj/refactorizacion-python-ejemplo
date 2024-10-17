# aplicamos refactorizacion
#programa donde ingresas una escala de 1 a 5 si y solo si se cumple el rango de selecion de proceso (1 a 3)
# elegis la opcion de proceso y ingresa en puntacion y elegis del 1 al 5, si pones dentro del mismo rango
# podes introducir un comentario y si no te pide hasta salir del bucle, donde se guarda en un data.text. basicamente eso es el funcionamiento del 
#Programa

def ingresar_puntuacion():
    while True:
        point = input("Por favor, introduzca una puntuación en una escala de 1 a 5: ")
        if point.isdigit() and 1 <= int(point) <= 5:
            point = int(point)
            comentario = input('Por favor, introduzca un comentario: ')
            post = f'punto: {point} comentario: {comentario}'
            with open("data.txt", 'a') as archivo:
                archivo.write(f'{post}\n')
            break  # salir del bucle
        else:
            print('Por favor, introduzca un número entre 1 y 5.')

def resultados_actualizado():
    print("                      ")
    print('Resultados hasta la fecha:')
    print("                      ")
    try:
        with open("data.txt", "r") as archivo:
            resultados = archivo.read()
            if resultados:
                print(resultados)
            else:
                print("No hay resultados almacenados.")
    except FileNotFoundError:
        print("No se encontró el archivo de resultados.")

def seleccionar_proceso():
    while True:
        print("                                    ")
        print('Seleccione el proceso que desea aplicar:')
        print('1: Ingresar puntuación y comentario')
        print('2: Ver resultados obtenidos')
        print('3: Finalizar')
        print("                                     ")
        try:
            num = int(input("Ingrese el número del 1 al 3: "))
            if num == 1:
                ingresar_puntuacion()
            elif num == 2:
                resultados_actualizado()
            elif num == 3:
                print('Finalizando')
                break
            else:
                print("Por favor, ingrese un número válido entre 1 y 3.")
        except ValueError:
            print("ingrese un número, no cadena, válido entre 1 y 3")

if __name__ == "__main__":
    seleccionar_proceso()
