tipo_producto = ["Maiz grano", "Pepino", "Tomate verde"]
costo_por_caja = [285.55,334.72,129.00]
Envio = 0
venta_productos = [[2, 122],[1, 89],[1, 22],[3, 48],[1, 75],[3, 322],[2, 95],[1, 148],[1, 83],[3, 100]]
Suma_productos_vendidos = int(venta_productos[0][1]) + int(venta_productos[1][1]) + int(venta_productos[2][1]) + int(venta_productos[3][1])\
                         + int(venta_productos[4][1])+ int(venta_productos[5][1]) + int(venta_productos[6][1]) + int(venta_productos[7][1])\
                         + int(venta_productos[8][1]) + int(venta_productos[9][1])
descuento = 0
Costo_total = 0

Cajas_ventas = int(input("Ingrese el numero de cajas a vender:"))
id = int(input("Ingrese el id del producto que desea:"))

Total_envios = Suma_productos_vendidos + Cajas_ventas
Aplica_descuento = Total_envios>1500

if Cajas_ventas <= 100:
    Envio=1500



if id==1:
    print ("El Producto es: ", tipo_producto[0], "precio por caja:", costo_por_caja[0])
    Costo_total=Cajas_ventas*costo_por_caja[0]+Envio
elif id==2:
    print ("El Producto es: ", tipo_producto[1], "precio por caja:", costo_por_caja[1])
    Costo_total=Cajas_ventas*costo_por_caja[1]+Envio
elif id==3:
    print ("El Producto es: ", tipo_producto[2], "precio por caja:", costo_por_caja[2])
    Costo_total=Cajas_ventas*costo_por_caja[2]+Envio
else:
    print("ingresaste un ID no reconocido") 



if Aplica_descuento :
    descuento = Costo_total*.20

Costo_total = round(Costo_total-descuento,2)

print ("aplica descuento 20% :", Aplica_descuento) 

print ("Costo total a pagar: ", Costo_total)

