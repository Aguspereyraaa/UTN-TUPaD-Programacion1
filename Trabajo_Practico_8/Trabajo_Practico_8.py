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
#