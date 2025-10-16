#Ej 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)

#Ej 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)

#Ej 3
lista_frutas = list(precios_frutas.keys())
print(lista_frutas)

#Ej 4
agenda = {}
for i in range(5):
    nombre: str = input(f"Ingrese el nombre del {i+1} contacto: ")
    band: bool = True
    while band:
        numero: str = input(f"Ingrese el numero de {nombre}: ")
        if numero.isdigit():  # Verificar si el string contiene solo dígitos
            numero = int(numero)
            band: bool = False
        else:
            print("Error, intente nuevamente ingresar el numero")
    agenda[nombre] = numero  # Guardar como entero

print("--Contactos de agenda--")
print(agenda)

nombre_buscado: str = input("Ingrese el nombre del contacto a buscar: ")
if nombre_buscado in agenda:
    numero = agenda[nombre_buscado]
    print(f"El numero de {nombre_buscado} es {numero}")
else:
    print(f"El contacto {nombre_buscado} no se encuentra en la agenda")

#Ej 5
def analizar_frase():
    frase = input("Ingresa una frase o texto: ")

    palabras = frase.lower()
    lista_palabras = palabras.split()

    if not lista_palabras:
        print("No se ingresó ninguna palabra.")
        return

    palabras_unicas = set(lista_palabras)

    print("\n Palabras Únicas (Set):")
    print(palabras_unicas)
    print(f"Total de palabras únicas: {len(palabras_unicas)}")

    conteo_palabras = {}
    for palabra in lista_palabras:
        if palabra in conteo_palabras:
            conteo_palabras[palabra] += 1
        else:
            conteo_palabras[palabra] = 1

    # También se puede hacer esto de forma más concisa con 'collections.Counter'
    # from collections import Counter
    # conteo_palabras = Counter(lista_palabras)

    # Imprimir el diccionario de conteo
    print("\n Conteo de Palabras (Diccionario):")
    # Imprimir el diccionario de forma más legible
    for palabra, conteo in conteo_palabras.items():
        print(f"'{palabra}': {conteo}")

analizar_frase()

#Ej 6
alumnos ={}
num_alumnos = 3
num_notas = 3
for i in range(num_alumnos):
    while True:
        nombre : str=input(f"Ingrese el nombre del alumno {i+1}: ")
        nombre = nombre.lower()
        if nombre.isalpha():
            break
        else:
            print("Error, intente nuevamente ingresar el nombre")
    list_notas=[]
    for e in range(num_notas):
        while True:
            nota_str: str = input(f"Ingrese la {e+1} nota de {nombre} (0-10): ")
            if nota_str.isdigit():
                nota_int = int(nota_str)
                if 0 <= nota_int <= 10:
                    list_notas.append(nota_int)
                    break # Nota válida, sale del bucle de nota
                else:
                    print("Error: La nota debe estar entre 0 y 10.")
            else:
                print("Error: La nota debe ser un número entero.")

alumnos[nombre] = tuple(list_notas)

print(alumnos)

#Ej 7
notas_parcial1 = {6, 8, 10, 7, 9}
notas_parcial2 = {10, 7, 5, 9, 8}

# 1. Notas en Ambos (Intersección)
ambas = notas_parcial1.intersection(notas_parcial2)
print("\n1. Notas que aparecen en AMBOS parciales:", ambas)

# 2. Notas en Solo Uno (Diferencia Simétrica)
solo_uno = notas_parcial1.symmetric_difference(notas_parcial2)
print("2. Notas que aparecen SOLO en UNO:", solo_uno)

# 3. Total de Notas Distintas (Unión)
todas = notas_parcial1.union(notas_parcial2)
print("3. TOTAL de notas distintas obtenidas:", todas)

#Ej 8
def gestionar_inventario():
    inventario = {
        "manzanas": 50,
        "bananas": 30,
        "naranjas": 10
    }

    print("--- Sistema de Gestión de Inventario ---")

    while True:
        print("\nOpciones:")
        print("1. Consultar stock de producto")
        print("2. Agregar unidades / Nuevo producto")
        print("3. Mostrar todo el inventario y salir")

        opcion = input("Elige una opción (1, 2 o 3): ").strip()

        if opcion == '1':
            producto = input("Ingrese el nombre del producto a consultar: ").lower().strip()

            if producto in inventario:
                stock_actual = inventario[producto]
                print(f"Stock de '{producto}': {stock_actual} unidades.")
            else:
                print(f"El producto '{producto}' no existe en el inventario.")

        elif opcion == '2':
            producto = input("Ingrese el nombre del producto a modificar o agregar: ").lower().strip()

            while True:
                try:
                    cantidad = int(input("Ingrese la cantidad de unidades a agregar: "))
                    if cantidad <= 0:
                        print("La cantidad debe ser un número positivo.")
                        continue
                    break
                except ValueError:
                    print("Error: Ingrese un número entero válido para la cantidad.")

            if producto in inventario:
                inventario[producto] += cantidad
                print(f"Se agregaron {cantidad} unidades a '{producto}'. Stock total: {inventario[producto]}.")
            else:
                inventario[producto] = cantidad
                print(f"Producto '{producto}' agregado con un stock inicial de {cantidad} unidades.")

        elif opcion == '3':
            print("\n--- Inventario Final ---")
            if inventario:
                for prod, stock in inventario.items():
                    print(f"Producto: {prod.capitalize()} | Stock: {stock}")
            else:
                print("El inventario está vacío.")
                print("------------------------")
            break

        else:
            print("Opción no válida. Por favor, ingrese 1, 2 o 3.")

gestionar_inventario()

#Ej 9
def consultar_agenda():
    agenda = {
        ('lunes', 9): "Reunión de planificación",
        ('lunes', 14): "Clase de Python",
        ('martes', 11): "Entrenamiento de gimnasio",
        ('miércoles', 10): "Llamada con mi abuelo",
        ('viernes', 18): "Cena con amigos",
        ('sábado', 10): "Paseo por el parque"
    }

    print("--- Consulta de Agenda Personal ---")
    print("Días válidos: lunes, martes, miércoles, viernes, sábado")
    print("Horas válidas: 9, 10, 11, 14, 18 (o cualquier hora cargada)")

    dia_consulta = input("Ingrese el día: ").lower().strip()

    while True:
        hora_str = input("Ingrese la hora (formato 24h, solo número entero): ").strip()
        try:
            hora_consulta = int(hora_str)
            break
        except ValueError:
            print("Error: Por favor, ingrese la hora como un número entero.")

    clave_consulta = (dia_consulta, hora_consulta)

    print("\n--- Resultado de la Consulta ---")

    if clave_consulta in agenda:
        evento = agenda[clave_consulta]
        print(f"El evento para el {dia_consulta.capitalize()} a las {hora_consulta}:00 es: ")
        print(f"{evento}")
    else:
        print(f"No hay ninguna actividad programada para el {dia_consulta.capitalize()} a las {hora_consulta}:00.")

consultar_agenda()

#Ej 10
# Diccionario original: País (clave) -> Capital (valor)
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "España": "Madrid",
    "Francia": "París",
    "Alemania": "Berlín"
}

# Inicializar el nuevo diccionario vacío
capitales_paises = {}

# Iterar sobre el diccionario original y construir el nuevo
# El método .items() devuelve pares (clave, valor)
for pais, capital in paises_capitales.items():
    # Asignamos: la 'capital' se convierte en la nueva CLAVE
    # el 'pais' se convierte en el nuevo VALOR
    capitales_paises[capital] = pais

print("--- Diccionario Original (País -> Capital) ---")
print(paises_capitales)

print("\n--- Nuevo Diccionario Invertido (Capital -> País) ---")
print(capitales_paises)