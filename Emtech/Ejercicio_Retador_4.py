tipo_producto = ["Maiz grano", "Pepino", "Tomate verde"]
costo_por_caja = [285.55,334.72,129.00]
Envio = 0

Cajas_ventas = int(input("Ingrese el numero de cajas a vender:"))
id = int(input("Ingrese el id del producto que desea:"))

if Cajas_ventas <= 100:
    Envio=1500
    

if id==1:
    print (tipo_producto[0], "precio por caja:", costo_por_caja[0], "Costo total a pagar", round((Cajas_ventas*costo_por_caja[0]+Envio),2))
elif id==2:
    print (tipo_producto[1], "precio por caja:", costo_por_caja[1], "Costo total a pagar", round((Cajas_ventas*costo_por_caja[1]+Envio),2))
elif id==3:
    print (tipo_producto[2], "precio por caja:", costo_por_caja[2], "Costo total a pagar", round((Cajas_ventas*costo_por_caja[2]+Envio),2))
else:
    print("ingresaste un ID no reconocido") 

