'''1 / 2 - A Jornada da Classificação Frutífera
Descrição:
Nesta missão, sua tarefa é mais desafiadora do que nunca! 
Em um pomar mágico, as frutas têm características únicas que as diferenciam. 
Seu objetivo é criar um modelo de machine learning capaz de classificar frutas 
com base em três características: peso, textura (suave ou áspera) 
e cor (vermelha, laranja ou amarela). 
Cada tipo de fruta tem limites específicos para essas características.

Maçã:
Peso mínimo: 130 gramas
Textura: Ápera (rough)
Cor: Vermelha (red)

Laranja:
Peso mínimo: 120 gramas
Textura: Suave (smooth)
Cor: Laranja (orange)

Morango:
Peso mínimo: 150 gramas
Textura: Suave (smooth)
Cor: Vermelha (red)

Banana:
Peso mínimo: 150 gramas
Textura: Áspera (rough)
Cor: Amarela (yellow)

Entrada:
Seu código deve receber as seguintes entradas do usuário:
1. Peso da fruta (em gramas): um número real que representa o peso da fruta.
2. Textura da fruta (suave ou áspera): uma string indicando se a fruta é suave ("smooth") ou áspera ("rough").
3. Cor da fruta (vermelha, laranja ou amarela): uma string indicando a cor da fruta.

Saída:
O código deve produzir uma saída indicando a classificação da fruta 
com base nas características fornecidas.

Exemplos:
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas 
esperadas. Certifique-se de testar seu programa com esses exemplos 
e com outros casos possíveis.

Entrada:
150
smooth
red	

Saída:
A fruta é um morango!

Código fornecido:
def prever_fruta(peso, textura, cor):
    # Lógica de decisão baseada nas características fornecidas
    if peso >= 150 and textura == "smooth" and cor == "red":
        return "A fruta é um morango!"
# TODO: Desenvolva a Função para prever a classe da fruta


# Entrada do usuário
peso_fruta = float(input())
textura_fruta = input()
cor_fruta = input()

# Chamada da função de previsão
resultado = prever_fruta(peso_fruta, textura_fruta, cor_fruta)

# Saída da previsão
print(resultado)

'''

# Solução:
def prever_fruta(peso, textura, cor):
    # Lógica de decisão baseada nas características fornecidas
    if peso >= 150 and textura == "smooth" and cor == "red":
        return "A fruta é um morango!"
    elif peso >= 150 and textura == "rough" and cor == "yellow":
        return "A fruta é uma banana!"     
    elif peso >= 120 and textura == "smooth" and cor == "orange":
        return "A fruta é uma laranja!"
    elif peso >= 130 and textura == "rough" and cor == "red":
        return "A fruta é uma maçã!"
    else:
        return 'Não foi possível classificar a fruta.'
        
# TODO: Desenvolva a Função para prever a classe da fruta

# Entrada do usuário
peso_fruta = float(input())
textura_fruta = input()
cor_fruta = input()


# Chamada da função de previsão
resultado = prever_fruta(peso_fruta, textura_fruta, cor_fruta)


# Saída da previsão
print(resultado)




# Outra opção de solução:
def prever_fruta(peso, textura, cor):
    # Lógica de decisão baseada nas características fornecidas
    data = {'morango':[150,"smooth","red"," "],
            'banana':[150,"rough","yellow","a "],
            'maçã':[130,"rough","red","a "],
            'laranja':[120,"smooth","orange","a "]
    }
    check = False
    for a, b in data.items(): # << modificar  
        if all([peso >= b[0], textura == b[1], cor == b[2]]):
            answer, check = f'A fruta é um{b[3]}{a}!', True
            break
    
    return answer if check else 'Não foi possível classificar a fruta.'
        
# TODO: Desenvolva a Função para prever a classe da fruta
# Entrada do usuário
peso_fruta = float(input())
textura_fruta = input()
cor_fruta = input()

# Chamada da função de previsão
resultado = prever_fruta(peso_fruta, textura_fruta, cor_fruta)

# Saída da previsão
print(resultado)