#https://www.urionlinejudge.com.br/judge/pt/problems/view/1114

senhaPadrao = 2002

def ValidaSenha(senhaPadrao):
    senha = int(input())
    if senha != senhaPadrao:
        print('Senha Invalida')
        ValidaSenha(senhaPadrao)
    else:
        print('Acesso Permitido')

ValidaSenha(senhaPadrao)

