'''
Exercício: Análise de Strings
Crie um programa em Python que:
Solicite ao usuário que insira duas strings(palavras).
Exiba o conteúdo de ambas as strings e seus respectivos comprimentos.
Informe se as duas strings possuem o mesmo comprimento e se são 
iguais ou diferentes no conteúdo.
Detalhamento:
Entrada de Dados:
Utilize a função input() para receber as duas strings do usuário.
Operações:
Calcule o comprimento de cada string usando a função len() (numero de caracteres).
Verifique se os comprimentos são iguais.
Verifique se o conteúdo das strings é igual.
Saída de Dados:
Exiba o conteúdo de cada string e seus respectivos comprimentos.
Informe se as strings possuem o mesmo comprimento.
Informe se as strings possuem o mesmo conteúdo.


'''

#Dados

nome1=input("Digite seu nome: ")
nome2=input("Digite nome do seu Pai: ")
print(nome1==nome2)

print(nome1.replace(" ", ""))
print(nome2.replace(" ", ""))

print(len(nome1))
print(len(nome2))