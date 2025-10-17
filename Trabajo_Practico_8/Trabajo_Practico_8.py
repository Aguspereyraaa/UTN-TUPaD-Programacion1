#Ej 1
#Crear archivo inicial con productos: Crear un archivo de texto llamado productos.txt con tres productos. 
# Cada línea debe tener: nombre,precio,cantidad
archivos_producto = open("productos.txt","w")
archivos_producto.write("Lapicera,150,8\n")
archivos_producto.write("Lapiz,250,9\n")
archivos_producto.write("Goma,20,5\n")
archivos_producto.close()