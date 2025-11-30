def _ready():
    odio = input("Del uno al diez, ¿qué tanto odio tienes hoy al ilegítimo estado genocida de Israel?")
    with open("Datos.txt", "a") as archivo:
        archivo.write(str(odio) + "\n")
_ready()

def _promedio():
    with open ("Datos.txt", "r") as archivo:
        líneas = archivo.readlines() #Convertir líneas de strings en listas
        números = [int(linea.strip()) for linea in líneas] #"strip" sirve para eliminar espacios en blanco y saltos de línea al principio y al final de la cadena. "for linea in líneas" dice que tiene que llaamr a eso "linea" y hacerlo en cada valor de "línea".
        promedio = sum(números) / len(números) #len(números) = cantidad de dígitos en "números"
    print("De media, tu odio hacia el ilegítimo estado genocida de Israel es", promedio)
    if promedio == 10:
        print("Muy bien")
_promedio()