'''1 / 3 - O Grande Depósito - Solucionando Problemas Bancários
Desafio:
Você foi contratado por um banco para desenvolver um programa que auxilie seus clientes 
a realizar depósitos em suas contas. O programa deve solicitar ao cliente o valor do depósito 
e verificar se o valor é válido. 
Se o valor for maior do que zero, o programa deve adicionar o valor ao saldo da conta. 
Caso contrário, o programa deve exibir uma mensagem de erro. 
O programa deve solicitar apenas uma vez o valor de depósito.

Entrada:
O programa deve receber o valor de depósito digitado pelo cliente. 
Os valor pode ser decimal, representando valor em reais.

Saída:
O programa deve exibir uma mensagem de sucesso quando um valor de depósito válido for informado 
e o saldo da conta for atualizado. 
Se o valor for "0", deverá imprimir uma mensagem encerrando o programa. 
Caso um valor inválido seja digitado, o programa deve exibir uma mensagem de erro 
solicitando um novo valor.

Exemplos:
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. 
Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada:
1) 500.50	
2) -100
3) 0

Saída:
1)Deposito realizado com sucesso!
Saldo atual: R$ 500.50
2) Valor invalido! Digite um valor maior que zero.
3) Encerrando o programa...

Código fornecido:
valor = float(input())

if valor > 0:
    //TODO: Imprimir a mensagem de sucesso, formatando o saldo atual (vide Exemplos).
elif valor < 0:
   //TODO: Imprimir a mensagem de valor inválido.
else:
   //TODO: Imprimir a mensagem de encerrar o programa.
'''

# Solução:
valor = float(input())

if valor > 0:
  # TODO: Imprimir a mensagem de sucesso, formatando o saldo atual (vide Exemplos).
  print('Deposito realizado com sucesso!')
  print(f'Saldo atual: R$ {valor:.2f}')
elif valor < 0:
  # TODO: Imprimir a mensagem de valor inválido.
  print('Valor invalido! Digite um valor maior que zero.')
else:
  # TODO: Imprimir a mensagem de encerrar o programa.
  print('Encerrando o programa...')