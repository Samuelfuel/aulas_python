'''

2- Exercício: Calculadora de Área e Perímetro de um Retângulo
Crie um programa em Python que:
Solicite ao usuário que insira a largura e a altura de um retângulo.
Converta as entradas para números de ponto flutuante.
Calcule a ádos:
rea e o perímetro do retângulo.
Exiba os resultados utilizando diferentes métodos de impressão (print).
Utilize expressões para verificar se o retângulo é, na verdade, um quadrado (ou seja, largura igual à altura) e exiba o resultado dessa verificação.
Detalhamento:
Entrada de Dados:
Utilize a função input() para receber a largura e a altura do retângulo como strings.
Conversão de Tipos (Casting):
Converta as entradas para o tipo float para permitir cálculos com números decimais.
Cálculos:
Área = largura × altura
Perímetro = 2 × (largura + altura)
Saída de DaUtilize diferentes métodos de impressão para exibir os resultados:
Concatenação de strings com o operador +.
Função print() com múltiplos argumentos separados por vírgulas.
Strings formatadas (f-strings).
Valores Booleanos e Expressões:
Crie uma expressão que verifica se a largura é igual à altura e armazene o resultado em uma variável booleana.
Exiba o resultado da verificação utilizando uma mensagem apropriada.

'''
#Documentação
#print(f"IMC: {imc:.2f}")
#Entrada de Dados
altura=float(input("Digite a altura: "))
largura=float(input("Digite a largura: "))

#Cálculos
area=largura*altura
perimetro=2*(largura+altura)

#Impressões
print("Area: "+str(round(area)))
print("Perimetro: "+str(round(perimetro)))
print(f"Area: {area:.2f}")
print(f"Perimetro: {perimetro:.2f}")

#Eh quadrado?
eh_quadrado=largura==altura
print("É quadrado: "+str(eh_quadrado))
print(f"É quadrado: {eh_quadrado}")