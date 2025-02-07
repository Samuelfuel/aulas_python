'''
CALCULADORA IMC
entrada de dados
peso (float)
altura (float)
peso dividido por (altura elevada ao quadrado)
imprimir

'''

print("Calculadora IMC") 

peso=float(input("Digite seu peso em kilos: \n")) #entrada do peso

altura=float(input("Digite sua altura em metros:\n")) #entrada da altura

imc=peso/(altura**2) #calculo do imc

print(f"IMC: {imc:.2f}")


print("IMC: "+ str(round(imc,2))) #impressao do imc (resultado)
