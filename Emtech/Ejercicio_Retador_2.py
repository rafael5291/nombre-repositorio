municipios = []
Habitantes = []
Suma_Habitantes = 0
Promedio_Habitantes = 0
municipios.append(input("ingrese el nombre del municipio 1: "))
Habitantes.append(input("ingrese el numero de habitantes de " + municipios[0] + ": "))
municipios.append(input("ingrese el nombre del municipio 2: "))
Habitantes.append(input("ingrese el numero de habitantes de " + municipios[1] + ": "))
municipios.append(input("ingrese el nombre del municipio 3: "))
Habitantes.append(input("ingrese el numero de habitantes de " + municipios[2] + ": "))
Suma_Habitantes = int(Habitantes[0]) + int(Habitantes[1]) + int(Habitantes[2])
Promedio_Habitantes = Suma_Habitantes/3
print ("El total de habitantes es:", Suma_Habitantes)
print ("El promedio de habitantes es:", round(Promedio_Habitantes,2))