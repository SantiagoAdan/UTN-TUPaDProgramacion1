# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

if int(input("Ingrese Su Edad ")) >= 18:
    print("Es mayor de Edad")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

if int(input("Ingrese su Nota: ")) >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

if int(input("Ingrese un numero par: ")) % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su Edad: "))

if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a Joven")
else:
    print("Adulto/a")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

LenPassword = len(input("Ingrese una contraseña de 8 a 14 caracteres: "))
if LenPassword >= 4 and LenPassword <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6) escribir un programa que tome la lista numeros_aleatorios, calcule su moda,
# su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media < mediana and mediana > moda:
    print("Con Sesgo Positivo")
elif media < mediana and mediana < moda:
    print("Con Sesgo Negativo")
else:
    print("Sin Sesgo")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

Vocales = ["a", "e", "i", "o", "u"]
Frase = input("Ingrese una Frase o Palabra: ")

if Frase[-1].lower() in Vocales:
    Frase += "!"

print(Frase)


# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
#   1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#   2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#   3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas


nombre = input("Ingrese su Nombe: ")
opc = int(
    input(
        "Ingrese una de las 3 Opciones: \n 1: Nombre en Mayusculas \n 2: Nombre en Minusculas \n 3: Primera letra del Nombre con Mayusculas \n"
    )
)

if opc == 1:
    print(nombre.upper())
elif opc == 2:
    print(nombre.lower())
else:
    print(nombre.title())


# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

escala = float(input("Ingrese la magnitud del Terremoto: "))

if escala < 3.0:
    print("Muy leve (imperceptible).")
elif escala >= 3 and escala < 4:
    print("Leve (ligeramente perceptible).")
elif escala >= 4 and escala < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif escala >= 5 and escala < 6:
    print("Fuerte (puede causar daños en estructurasdébiles).")
elif escala >= 6 and escala < 7:
    print("Muy Fuerte (puede causar daños significativos).")
else:
    print("Extremo (puede causar graves daños a gran escala).")

# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("¿En qué hemisferio estás? (N/S): ").strip().upper()
if hemisferio == "S" or hemisferio == "N":
    mes = int(input("Ingresa el mes en número (1-12): "))
    dia = int(input("Ingresa el día (1-31): "))
    fecha = (mes, dia)

    if (fecha >= (12, 21) and fecha <= (12, 31)) or (
        fecha >= (1, 1) and fecha <= (3, 20)
    ):
        estacion_sur = "Verano"
        estacion_norte = "Invierno"
    elif fecha >= (3, 21) and fecha <= (6, 20):
        estacion_sur = "Otoño"
        estacion_norte = "Primavera"
    elif fecha >= (6, 21) and fecha <= (9, 20):
        estacion_sur = "Invierno"
        estacion_norte = "Verano"
    elif fecha >= (9, 21) and fecha <= (12, 20):
        estacion_sur = "Primavera"
        estacion_norte = "Otoño"

    if hemisferio == "S":
        print(f"La estacion para el Hemisferio sur es ", estacion_sur)
    else:
        print(f"La estacion para el Hemisferio norte es ", estacion_norte)
else:
    print("Hemisferio Invalido.")
