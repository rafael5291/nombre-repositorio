Cemento = 40
Yeso = 30
Peso_Maximo_camion = 3254
Pedido_Cemento = int(input ("Ingre la cantidad de sacos de cemento que solicita:"))
pedido_Yeso = int(input ("Ingrese la cantidad de yeso que solicita:"))
Peso_cemneto = Pedido_Cemento*Cemento
peso_yeso = pedido_Yeso*Yeso
Peso_Total = Peso_cemneto+peso_yeso
print (Peso_Total, "Kg")
Envio = Peso_Total>=(Peso_Maximo_camion/2) and Peso_Total<=Peso_Maximo_camion
print ("¿Se puede realizar el envio?", Envio)
