# UTN-TUPaDProgramacion1
# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa   “Marcos”, el programa debe imprimir
#  por pantalla “Hola Marcos!”. Conasejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
name= input("Ingrese su nombre: ")
print(f"Hola {name} !")

#  3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#  imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#  “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#  años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#  la impresión por pantalla.

name=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
edad=int(input("Ingrese su edad: "))
nacionalidad=input("Ingrese su nacionalidad: ")
print(f"Hola me llamo {name} {apellido}, tengo {edad} años y soy de {nacionalidad}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.

import math
radio=float(input("Ingrese el radio del circulo: "))
area=math.pi*radio**2
perimetro=2*math.pi*radio
print(f"El area del circulo es: {area}")
print(f"El perimetro del circulo es: {perimetro}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.

print("Buenos dias ")
segundos=int(input("Ingrese la cantidad de segundos que desea convertir en horas: "))
horas=segundos/3600
print(f"La cantidad de horas es:{horas} hs")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

num_mult=int(input("Ingrese el numero que desea multiplicar: "))
for i in range(1, 11):
    resultado= num_mult * i
    print(f"{num_mult} X {i} = {resultado}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.   

num_1=int(input("Ingrese el primer numero: "))
num_2=int(input("Ingrese el segundo numero: "))
if num_1 == 0 and num_2 == 0:
    print("Ambos numeros son ceros") 
else:
    suma = num_1 + num_2
    resta = num_1 - num_2
    multiplicacion = num_1 * num_2
    if num_2 != 0: 
        division = num_1 / num_2
    else:
        print("No se puede dividir por cero")
print(f"La suma es: {suma}")
print(f"La resta es: {resta}")
print(f"La multiplicacion es: {multiplicacion}")
print(f"La division es: {division}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo:

altura=float(input("Ingrese su altura: "))
peso=float(input("Ingrese su peso: "))
imc=peso/(altura**2)
print(f"Su indice de masa corporal es: {imc}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:

grados_celsius= float(input("Ingrese la temperatura en grados Celsius: "))
g_fahrenheit= (9/5 * grados_celsius) + 32
print(f"La temperatura en grados Fahrenheit es: {g_fahrenheit}")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.

num1= int(input("Ingrese el primer numero: "))
num2= int(input("Ingrese el segundo numero: "))
num3= int(input("Ingrese el tercer numero: "))
suma= num1 + num2 + num3
promedio= suma / 3
print(f"La suma de los nuemros es: {suma}")