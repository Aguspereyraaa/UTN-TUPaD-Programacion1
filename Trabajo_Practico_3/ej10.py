#Ej10
hemisferio = str(input("Ingrese en que hemisferio se encuentra (Norte/Sur): ")).lower()
mes = str(input("Ingrese el mes se encuentra: ")).lower()
dia = int(input("Ingrese el dia en quie se encuentra:"))
if (hemisferio == "Norte"):
    if (mes == "diciembre" and dia >=21 ) or (mes == "enero" and dia <=20) or (mes == "febrero" and dia <=28) or (mes == "marzo" and dia <=20):
        print("Es invierno")
    elif (mes == "marzo" and dia >=21) or (mes == "abril" and dia <=30) or (mes == "mayo" and dia <=31) or (mes == "junio" and dia <=20):
        print("Es primavera")
    elif (mes == "junio" and dia >=21) or (mes == "julio" and dia <=31) or (mes == "agosto" and dia <=31) or (mes == "septiembre" and dia <=21):
        print("Es verano")
    elif (mes == "septiembre" and dia >=22) or (mes == "octubre" and dia <=31) or (mes =="noviembre" and dia <=30) and (mes == "diciembre" and dia <=20):
        print("Es otoño")
elif (hemisferio=="sur"):
    if (mes == "diciembre" and dia >=21 ) or (mes == "enero" and dia <=20) or (mes == "febrero" and dia <=28) or (mes == "marzo" and dia <=20):
        print("Es verano")
    elif (mes == "marzo" and dia >=21) or (mes == "abril" and dia <=30) or (mes == "mayo" and dia <=31) or (mes == "junio" and dia <=20):
        print("Es otoño")
    elif (mes == "junio" and dia >=21) or (mes == "julio" and dia <=31) or (mes == "agosto" and dia <=31) or (mes == "septiembre" and dia <=21):
        print("Es invierno")
    elif (mes == "septiembre" and dia >=22) or (mes == "octubre" and dia <=31) or (mes =="noviembre" and dia <=30) and (mes == "diciembre" and dia <=20):
        print("Es primavera")     