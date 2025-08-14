# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. 
# Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.

nombre = input("Ingrese su Nombre: ")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.

nombre         = input("Ingrese Su Nombre: ")
apellido       = input("Ingrese SU Apellido: ")
edad           = int(input("Ingrese Su Edad: "))
paisResidencia = input("Ingrese Su País de Residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {paisResidencia}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.

radio     = float(input("Ingrese el Radio de un Circulo: "))
area      = round(3.14 * radio**2, 2)
perimetro = round(2 * 3.14 * radio, 2)
print(f"Area {area} Perimetro {perimetro}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

segundos = int(input("Ingrese la cantidad de segundos: "))
print(f"{segundos} segundos equivale a {round(segundos/3600,2)} horas")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

numero = int(input("Ingrese un Número: "))
for i in range(1, 11):
    print(f"{numero} * {i} = {numero*i}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero1 = 0
numero2 = 0
while numero1 != 0:
    numero1 = int(input("Ingrese El Primer Numero: "))

while numero2 != 0:
    numero2 = int(input("Ingrese El Segundo Numero: "))

print(f"Suma = {numero1+numero2} | Resta {numero1-numero2} | Multiplicación {numero1*numero2} | Divisioón {numero1/numero2}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo: 𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔/(𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)^2

altura = float(input("Ingrese Su Altura: "))
peso   = float(input("Ingrese Su Peso: "))
print(f"Su IMC es {round(peso/(altura**2), 2)}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:

TCelcius = int(input("Ingrese la Temperatura en Grados Celsius: "))
print(f"Temperatura en Grados Fahrenheit: {((9/5)*TCelcius) + 32}")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.

numero1 = int(input("Ingrese Primer Nro: "))
numero2 = int(input("Ingrese Segundo Nro: "))
numero3 = int(input("Ingrese Tercer Nro: "))

print(f"El promedio es {(numero1+numero2+numero3)/3}")