''' 1 / 3 - O Robô inteligente
Desafio
Você foi contratado pela empresa DIO Robots para programar um robô capaz de 
classificar números em uma das seguintes categorias: negativo, positivo ou zero. 
Para isso, você deve criar uma função de classificação que receba um número como 
parâmetro e retorne a mensagem "negativo!" ou " positivo!", de acordo com sua categoria.

O programa deve ser executado continuamente, permitindo que o usuário insira vários números.
 Quando ele quiser encerrar a execução, deverá digitar um número igual a zero. 
 A cada novo número inserido, o robô deve classificá-lo e exibir a mensagem correspondente. 
 Ao final da execução, o programa deverá exibir a quantidade de números positivos, 
 negativos e zeros que foram inseridos.

Entrada:
A entrada deve receber valores inteiros.
    numero: valor inteiro que pode ser positivo, negativo ou zero. 
    Lembrando que a entrada zero deve encerrar o programa.

Saída:
O código deverá retornar uma mensagem (string) informando se o número é positivo ou não. 
Ao receber o valor 0, ele deverá encerrar o e informar quantos números foram positivos 
e negativos.

Exemplos:
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas 
esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos 
possíveis.

Entrada:
1
-1
2
0

Saída:
positivo!
negativo!
positivo!
2 números positivos, 1 números negativos

Entrada:
1
-1
0

Saída:
positivo!
negativo!
1 números positivos, 1 números negativos

Código fornecido:
# TODO: Crie a Função para classificar um número como positivo, negativo ou zero
def classificar_numero(numero):
    
def main():
    positivos = 0
    negativos = 0
    
    while True:
        numero = int(input())
        
        if numero == 0:
            break  # Encerra o loop se o usuário digitar 0.
        
        # Chama a função classificar_numero para imprimir a classificação do número
        print(classificar_numero(numero))
        
        # TODO: Faça a verificação para saber quantos números positivos e negativos foram inseridos
     
    
    # Imprime a quantidade de números positivos e negativos inseridos
    print(f"{positivos} números positivos, {negativos} números negativos")

if __name__ == "__main__":
    main()
'''

# Solução:
# TODO: Crie a Função para classificar um número como positivo, negativo ou zero
def classificar_numero(numero):
    if numero > 0:
        return 'positivo'
    else:
        return 'negativo'
        
def main():
    positivos = 0
    negativos = 0
    
    while True:
        numero = int(input())
        
        if numero == 0:
            break  # Encerra o loop se o usuário digitar 0.
        
        # Chama a função classificar_numero para imprimir a classificação do número
        print(f'{classificar_numero(numero)}!')
        
        # TODO: Faça a verificação para saber quantos números positivos e negativos foram inseridos
        if classificar_numero(numero) == 'positivo':
            positivos += 1
        else:
            negativos += 1 
    
    # Imprime a quantidade de números positivos e negativos inseridos
    print(f"{positivos} números positivos, {negativos} números negativos")


if __name__ == "__main__":
    main()


# Outra opção de solução:
def main():
    positivos, negativos = 0, 0
    txt = ('negativo', 'positivo')
    
    while True:
        numero = int(input())
        if numero != 0:
            resposta = classificar_numero(numero)
            # Chama a função classificar_numero para imprimir a classificação do número
            print(f'{txt[resposta]}!')
            # TODO: Faça a verificação para saber quantos números positivos e negativos foram inseridos
            positivos, negativos = (positivos+1, negativos) if resposta else (positivos, negativos+1)
            
        else:
            break
        
    # Imprime a quantidade de números positivos e negativos inseridos
    print(f"{positivos} números {txt[1]}s, {negativos} números {txt[0]}s")


if __name__ == "__main__":
    main()