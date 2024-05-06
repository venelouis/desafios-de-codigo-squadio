'''2 / 3 - Estrutura de Dados: Organizando Os Seus Ativos
Descrição:
Após uma análise cuidadosa realizada pela equipe de desenvolvimento de uma empresa bancaria, 
foi identificado a necessidade de uma nova funcionalidade para otimizar os processos 
e melhorias da experiência dos usuários. 
Agora, sua tarefa é implementar uma solução que organize em ordem alfabética uma lista de ativos 
que será informada pelos usuários. Os ativos são representados por strings que representam seus tipos, 
como por exemplo: Reservas de liquidez, Ativos intangiveis e dentre outros.

Entrada:
A primeira entrada consiste em um número inteiro que representa a quantidade de ativos 
que o usuário possui. Em seguida, o usuário deverá  informar, em linhas separadas, 
os tipos (strings) dos respectivos ativos.

Saída:
Seu programa deve exibir a lista de Ativos organizada em ordem alfabética. 
Cada ativo deve ser apresentado em uma linha separada.

Exemplos:
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. 
Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada:
3
Financiamento de Imovel
Deposito
Reservas Bancarias

Saída:
Deposito
Financiamento de Imovel
Reservas Bancarias

Entrada:
3
Carteiras de credito
Investimentos em titulos
Derivativos financeiros	

Saída:
Carteiras de credito
Derivativos financeiros
Investimentos em titulos

Entrada:
3
Reservas de liquidez
Ativos intangiveis
Fundos de investimento	

Saída:
Ativos intangiveis
Fundos de investimento
Reservas de liquidez

Código fornecido:
ativos = []

// Entrada da quantidade de ativos
quantidadeAtivos = int(input())

// Entrada dos códigos dos ativos
for _ in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)

 //TODO: Ordenar os ativos em ordem alfabética.

    //TODO: Imprimir a lista de ativos ordenada, conforme a tabela de exemplos.
'''

# Solução:
ativos = []

# Entrada da quantidade de ativos
quantidadeAtivos = int(input())

# Entrada dos códigos dos ativos
for _ in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)

# TODO: Ordenar os ativos em ordem alfabética.
ativos.sort()

# TODO: Imprimir a lista de ativos ordenada, conforme a tabela de exemplos.
for item in ativos:
    print(item)