# Ej 1
#1. Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.
def saludo():
    return "Hola Mundo!"

saludo=saludo()
print(saludo)

#Ej 2
#2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.
def saludo_nombre(nombre):
    return print(f"Hola {nombre}!!!")

nombre :str=input("Ingrese su nombre: ")
nombre = nombre.capitalize()
saludar = saludo_nombre(nombre)

#Ej 3
#3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.
def data(nombre,apellido,edad,residencia):
    return print(f"Soy {nombre} {apellido}, tengo {edad} y vivo en {residencia}")


nombre :str=input("Ingrese su nombre: ")
nombre = nombre.capitalize()
apellido :str=input("Ingrese su apellido: ")
apellido = apellido.capitalize()
edad :str=input("Ingrese su edad: ")
edad = int(edad)
residencia :str=input("Ingrese su residencia: ")
residencia = residencia.capitalize()
datos = data(nombre,apellido,edad,residencia)

#Ej 4
#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
#Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
from math import pi, pow

def calcular_area(radio):
    x = pi * pow(radio, 2)
    return x
def calcular_perimetro_circulo(radio):
    x = 2 * pi * radio
    return x

radio : str=input("Ingrese el radio del circulo: ")
radio = float(radio)
area = calcular_area(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"El Area del circulo es: {area} y el perimetro es: {perimetro} ")

#Ej 5 
#5. Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    horas= segundos/3600
    return horas

segundos :str=input("Ingrese los segundos que quiere combertir en horas: ")
segundos = int(segundos)
horas=segundos_a_horas(segundos)
print(f"Los segundos {segundos} son {horas} en horas")

#Ej 6
#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range(11):
        print(f"{numero} x {i} = {numero*i}")

numero = input("Ingrese un numero para conocer su tabla de multiplicar: " )
numero = int(numero)
tabla = tabla_multiplicar(numero)

#Ej 7
#7. Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    """
    Recibe dos números (a, b) y devuelve una tupla con los resultados
    de la suma, resta, multiplicación y división de ambos.
    """
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    
    if b != 0:
        division = a / b
    else:
        division = "Indefinida"
    
    # Devuelve una tupla con los cuatro resultados
    return (suma, resta, multiplicacion, division)

num1 = float(input("Ingrese el primer número (a): "))
num2 = float(input("Ingrese el segundo número (b): "))

resultados = operaciones_basicas(num1, num2)

suma, resta, multiplicacion, division = resultados

print(f"Suma ({num1} + {num2}) = \t\t{suma:.2f}")
print(f"Resta ({num1} - {num2}) = \t\t{resta:.2f}")
print(f"Multiplicación ({num1} * {num2}) = \t{multiplicacion:.2f}")
print(f"División ({num1} / {num2}) = \t\t{division}")

#Ej 8
#8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

from math import pow

def calcular_imc(peso, altura):
    imc = peso / pow(altura, 2)
    return imc

peso : str=input("Ingrese el peso en Kilogramos: ")
peso = int(peso)
altura : str=input("Ingrese la altura en metros: ")
altura = float(altura)
masa_corporal = calcular_imc(peso, altura)
print(f"El peso es: {peso} y la altura: {altura}, el indice de masa corporal es: {masa_corporal: .2f}")

#Ej 9 
#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.

def celsius_a_fahrenheit(celsius):
    farhenheit = (celsius * 1.8) + 32
    return farhenheit

celsius :str=input("Ingrese los grados celsius que desea convertir en farhenheit: ")
celsius = float(celsius)
grados_a_farenheit= celsius_a_fahrenheit(celsius)
print(f"Grados celsius {celsius: .2f} a Farenheit {grados_a_farenheit: .2f}")

#Ej 10
#10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta
#función.

def calcular_promedio (a,b,c):
    promedio= (a+b+c) / 3
    return promedio

promedio_1 : str=input("Ingrese un numero entero: ")
promedio_1=int(promedio_1)
promedio_2 : str=input("Ingrese otro numero entero: ")
promedio_2=int(promedio_2)
promedio_3 :str=input("Ingrese el ultimo numero entero: ")
promedio_3=int(promedio_3)
promedio_total = calcular_promedio(promedio_1,promedio_2,promedio_3)
print(f"El promedio de los numeros es: {promedio_total}")