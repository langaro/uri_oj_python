#https://www.urionlinejudge.com.br/judge/pt/problems/view/1114
#Resolvido através de uma simpels recursividade

senhaPadrao = 2002

def ValidaSenha(senhaPadrao):
    senha = int(input())
    if senha != senhaPadrao:
        print('Senha Invalida')
        ValidaSenha(senhaPadrao)
    else:
        print('Acesso Permitido')

ValidaSenha(senhaPadrao)

