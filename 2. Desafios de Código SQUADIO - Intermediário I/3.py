''' 3 / 3 - Validando a Força de Senhas no IAM
Desafio:
Você está trabalhando para uma empresa que utiliza extensivamente os serviços da AWS, 
e após algumas análises a equipe de segurança identificou que algumas senhas dos usuários 
no IAM são fracas e podem representar um risco à segurança dos dados da empresa. 
Para resolver esse problema, foi solicitado que você desenvolva um programa capaz de 
analisar as senhas dos usuários e fornecer uma validação de força com base em critérios predefinidos.

Requisitos de segurança para a senha:

1. A senha deve ter no mínimo 8 caracteres.
2. A senha deve conter pelo menos uma letra maiúscula (A-Z).
3. A senha deve conter pelo menos uma letra minúscula (a-z).
3; A senha deve conter pelo menos um número (0-9).
4. A senha deve conter pelo menos um caractere especial, como !, @, #, $, %, etc.

Entrada:
A entrada será uma única string representando a senha que precisa ser validada.

Saída:
Seu programa deve retornar uma mensagem indicando se a senha fornecida pelo usuário atende aos requisitos
de segurança ou não, juntamente com um feedback explicativo sobre os critérios considerados.

Entrada:
0101	

Saída:
Sua senha e muito curta. Recomenda-se no minimo 8 caracteres.

Entrada:
030609saturno*	

Saída:
Sua senha atende aos requisitos de seguranca. Parabens!

Entrada:
010203Jupiter	

Saída:
Sua senha nao atende aos requisitos de seguranca.

Código fornecido:
def verificar_forca_senha(senha):


  comprimento_minimo = 8
  tem_letra_maiuscula = False
  tem_letra_minuscula = False
  tem_numero = False
  tem_caractere_especial = False

  # Verificando o comprimento da senha
  if len(senha) < comprimento_minimo:
    return f"Sua senha e muito curta. Recomenda-se no minimo {comprimento_minimo} caracteres."

  # TODO: Verifique se a senha contém letras maiúsculas e minúsculas
  

  # Verificando se a senha contém sequências comuns
  sequencias_comuns = ["123456", "abcdef"]
  for sequencia in sequencias_comuns:
    if sequencia in senha:
      return "Sua senha contem uma sequencia comum. Tente uma senha mais complexa."

  # Verificando se a senha contém palavras comuns
  palavras_comuns = ["password", "123456", "qwerty"]
  if senha in palavras_comuns:
    return "Sua senha e muito comum. Tente uma senha mais complexa."

  # TODO: Verificar o comprimento mínimo e critérios de validação



# Obtendo a senha do usuário
senha = input().strip()

# Verificando a força da senha
resultado = verificar_forca_senha(senha)

# Imprimindo o resultado
print(resultado)
'''

# Solução:
def verificar_forca_senha(senha):

    comprimento_minimo = 8
    tem_letra_maiuscula = False
    tem_letra_minuscula = False
    tem_numero = False
    tem_caractere_especial = False
    
    # Verificando o comprimento da senha
    if len(senha) < comprimento_minimo:
        return f"Sua senha e muito curta. Recomenda-se no minimo {comprimento_minimo} caracteres."
    
    # TODO: Verifique se a senha contém letras maiúsculas e minúsculas
    letra_maiuscula = ['A','B','C','D','E','F','G','H','I','J','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']    
    for letra in letra_maiuscula:
        if letra in senha:
            tem_letra_maiuscula = True
        if letra.lower() in senha:
            tem_letra_minuscula = True
            
    # Verificando se a senha contém sequências comuns
    sequencias_comuns = ["123456", "abcdef"]
    for sequencia in sequencias_comuns:
        if sequencia in senha:
            return "Sua senha contem uma sequencia comum. Tente uma senha mais complexa."
    
    # Verificando se a senha contém palavras comuns
    palavras_comuns = ["password", "123456", "qwerty"]
    if senha in palavras_comuns:
        return "Sua senha e muito comum. Tente uma senha mais complexa."
    
    # TODO: Verificar o comprimento mínimo e critérios de validação
    numeros = ['0','1','2','3','4','5','6','7','8','9']
    for numero in numeros:
        if numero in senha:
            tem_numero = True
    
    simbolos = ['~','!','@','#','$','%','^','&','*','(',')','-','+','/','?','>','<','/','|','=']
    for simbolo in simbolos:
        if simbolo in senha:
            tem_caractere_especial = True
    
    return 'Sua senha atende aos requisitos de seguranca. Parabens!' if len(senha) >= 8 and tem_letra_maiuscula and tem_letra_minuscula and tem_numero and tem_caractere_especial else 'Sua senha nao atende aos requisitos de seguranca.'

# Obtendo a senha do usuário
senha = input().strip()

# Verificando a força da senha
resultado = verificar_forca_senha(senha)

# Imprimindo o resultado
print(resultado)