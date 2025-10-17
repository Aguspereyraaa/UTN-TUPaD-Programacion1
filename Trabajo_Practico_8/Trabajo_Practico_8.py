#Ej 1
#Crear archivo inicial con productos: Crear un archivo de texto llamado productos.txt con tres productos. 
# Cada línea debe tener: nombre,precio,cantidad

archivos_producto = open("productos.txt","w")
archivos_producto.write("Lapicera,150,8\n")
archivos_producto.write("Lapiz,250,9\n")
archivos_producto.write("Goma,20,5\n")
archivos_producto.close()

#Ej 2
#Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
#línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
#formato:
#Producto: Lapicera | Precio: $120.5 | Cantidad: 30

with open("productos.txt","r") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        print(f"Producto: {datos[0]} | Precio: {datos[1]} | Cantidad: {datos[2]}")

#Ej 3
#Agregar productos desde teclado: Modificar el programa para que luego de mostrar
#los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
#cantidad) y lo agregue al archivo sin borrar el contenido existente.


producto = input("Ingrese el nombre del nuevo producto: ")
producto=producto.capitalize()
precio = input(f"Ingrese el precio del producto {producto}: ")
cantidad = input(f"Ingrese la cantidad de {producto}: ")

with open("productos.txt", "a") as archivo:
        archivo.write(f"{producto},{precio},{cantidad}\n")

with open("productos.txt","r") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        print(f"Producto: {datos[0]} | Precio: {datos[1]} | Cantidad: {datos[2]}")

#Ej 4 
#Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
#una lista llamada productos, donde cada elemento sea un diccionario con claves:
#nombre, precio, cantidad.

def cargar_productos():
    productos=[]
    with open("productos.txt","r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            datos=linea.strip().split(",")
            if len(datos)==3:
                productos_dict={
                    "nombre": datos[0],
                    "precio": datos[1],
                    "cantidad": datos[2]
                }
                productos.append(productos_dict)
    return productos
def mostrar_productos(productos):
    print("---INVENTARIO---")
    for i in range(len(productos)):  
        producto = productos[i]
        print(f"{i+1}. {producto['nombre']} - Precio: ${producto['precio']} - Cantidad: {producto['cantidad']}")

lista_productos = cargar_productos()
mostrar_productos(lista_productos)

#Ej 5 
#Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
#producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
#no existe, mostrar un mensaje de error.

def buscar_productos(lista_productos):
    buscar_producto :str=input("Ingrese el nombre del producto que busca: ")
    buscar_producto =buscar_producto.capitalize()
    encontrado:bool=False
    for producto in lista_productos:
        if producto["nombre"].capitalize() == buscar_producto:
            print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
            encontrado:bool=True
            break
    if not encontrado:
        print(f"Error: No se encuentra el producto '{buscar_producto}'")

buscar_productos(lista_productos)

#Ej 6
#Guardar los productos actualizados: Después de haber leído, buscado o agregado
#productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
#productos actualizados desde la lista.
def guardar_productos():
    productos = []
    band = True
    
    while band:
        print("----Productos Nuevos----")
        nombre = input("Nombre: ").strip().capitalize()
        
        if not nombre:
            break
            
        precio = input("Precio: ").strip()
        cantidad = input("Cantidad: ").strip()
        
        productos.append({
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        })
        
        if len(productos) == 3:  
            band = False
    
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    
    print(f"✅ {len(productos)} productos guardados")


guardar_productos()