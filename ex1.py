velocidade = int(input("Velocidade de trafego"))
if velocidade > 110:
	multa = (velocidade - 110) * 5;
	print("Voce foi multado em", multa)
print("Voce nao foi multado")
