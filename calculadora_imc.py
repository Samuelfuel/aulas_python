'''
CALCULADORA IMC
entrada de dados
peso (float)
altura (float)
peso dividido por (altura elevada ao quadrado)
imprimir

'''

print("Calculadora IMC")

peso=float(input("Digite seu peso em kilos: \n"))
altura=float(input("Digite sua altura em metros:\n"))
imc=peso/(altura**2)
print(f"IMC: {imc:.2f}")
print("IMC: "+ str(round(imc,2)))