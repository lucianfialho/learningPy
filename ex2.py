# VAR 
minGastos = int(input("Numero de minutos gastos"))
if minGastos <= 200:
	resultado = minGastos * 0.20 
elif minGastos > 200 and minGastos <= 400:
	resultado = minGastos * 0.18
elif minGastos > 400:
	resultado = minGastos * 0.15
elif minGastos > 800:
	resultado = minGastos * 0.8
print ("O total da sua conta foi", resultado)
