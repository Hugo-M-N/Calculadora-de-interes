aporteInicial = float(input("Aporte Inicial: "))
aporteMensual = int(input("Aporte Mensual: "))
duracion = int(input("Duración en meses: "))
interes = float(input("Interes anual: "))
interesCalculado = 1 + (((interes/100)/12)/30)
cantidad = 0
if aporteInicial > 0 :
    cantidad = aporteInicial
for i in range (duracion):
    cantidad += aporteMensual
    for j in range(30):
        cantidad *= interesCalculado
print("Cantidad aportada: ", (aporteInicial + (aporteMensual * duracion)))
print("Beneficio: ", cantidad - (aporteMensual * duracion) - aporteInicial)
print("Total: ", cantidad)