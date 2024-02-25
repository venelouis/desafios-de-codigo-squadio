'''
Descrição:
Com as máquinas pesadas agrupadas estrategicamente, 
graças ao seu algoritmo de cálculo energético, 
agora a mineração está muito mais eficiente! 
Com isso, os CodeMiners logo terão que aumentar a capacidade de armazenamento de dados 
em seus discos de Mithril. Atualmente, cada máquina tem uma capacidade em teraflops 
e todas terão um upgrade! Escreva um programa que calcule 
a nova capacidade total de todas as máquinas após um aumento percentual específico.

Entrada:
Dois valores inteiros positivos, 
representando a capacidade atual total em teraflops e o aumento percentual, 
separados por espaço.

Saída:
A nova capacidade total em teraflops.

Exemplos:
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. 
Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada:
100
20

Saída:
120

'''
capacidade_atual, aumento_percentual = map(int, input().split()) 
# capacidade atual total em teraflops e o aumento percentual (separados por espaço)
# map é uma função que aplica uma função a todos os itens de uma entrada iterável.
# input().split() é uma função que divide a entrada em partes, separadas por espaço
# então map(int, input().split()) significa que a entrada é separada por espaço e convertida para inteiros
# capacidade_atual = primeiro valor da entrada
# aumento_percentual = segundo valor da entrada

# TODO: Calcule a nova capacidade do disco de Mithril
# TODO: Imprima a nova capacidade

# Cálculo do aumento em teraflops
aumento_teraflops = capacidade_atual * aumento_percentual / 100 # Cálculo do aumento em teraflops

# Cálculo da nova capacidade total
nova_capacidade = capacidade_atual + aumento_teraflops # Cálculo da nova capacidade total

# Impressão da nova capacidade
print(int(nova_capacidade)) # Impressão da nova capacidade total em teraflops (convertida para inteiro)