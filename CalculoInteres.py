
print("Calcular total a pagar en un credito")



CapitalInicial = int(input("Ingresar Capital inicial: "))
TasaInteresAnual = float(input("Ingresar Capital inicial: "))
TiempoCreditoAnual = int(input("Ingresar Capital inicial: "))


InteresGenerado = CapitalInicial*TasaInteresAnual*TiempoCreditoAnual
print ("El interes geneado es: ", InteresGenerado)
print("---------------------------------------------")
TotalPago = CapitalInicial + InteresGenerado

print("El valor total a pagar por un Capital de:", CapitalInicial, "por", TiempoCreditoAnual, "Años es:", TotalPago) 



