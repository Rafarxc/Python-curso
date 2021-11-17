"""
Estruturas Lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
    - not
Operadores binários:
    - and, or, is

Regras de funcionamento:

Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor do boolenao e invertido. Ou seja, se for True vira False e se for False vira True
Para o 'is', o valor e comparado com o segundo.

"""
ativo = False
logado = False

if not ativo:
    print("Você precisa ativar sua conta.Por favor, checar seu email de verificação")
else:
    print('Bem-vindo usuário')

# ativo é False?
print(ativo is False)
