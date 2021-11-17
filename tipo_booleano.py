"""
Tipo Booleano

Álgebra Booleana, criada por George Boole

2 constantes, Verdadeiro ou Falso

True -> Verdadeiro
False -> Falso

OBS: Sempre com a inicial maiúscula

Errado:

true, false

Certo:

True, False
"""

ativo = False
print(ativo)

"""
Operações básicas:
"""

# Negação (not):
"""
Fazendo a negação, se o valor booleano for veradadeiro, o resultado será falso,
se for falso, o resultado será verdadeiro. Ou seja, sempre o contrário.
"""
print(not ativo)
logado = True

# Ou(or):
"""
É uma operção binária, ou seja, depende de dois valores. Ou um outro deve ser verdadeiro.
True or False -> True
False ou True -> True
True ou True -> True
False or False -> False
"""
print(ativo or logado)

# E (and):
"""
Também é uma operação binária, ou seja, depende de dois valores.Ambos os valores devem ser verdadeiros.

True and True -> True 
True and False -> False
False and False -> False
False and False -> True

"""