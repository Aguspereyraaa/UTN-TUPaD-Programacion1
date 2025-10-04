#

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
print(f"El peso es: {peso} y la altura: {altura}, el indice de masa corporal es: {masa_corporal : .2f}")