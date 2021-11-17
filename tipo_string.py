"""
Tipo string

Em Python um dado sempre é considerado string sempre que :

- Estiver entre aspas simples -> 'Uma string', '123', 'a', 'True', '42.3'
- Estiver entre aspas duplas -> "Uma string", "123", "a', "True", "42.3"
- Estiver entre aspas simples triplas -> '''Uma string''', '''123''', '''a''', '''True''', '''42.3'''

nome = '''Rafael'''
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Rafael \nRamos'
print(nome)
print(type(nome))

nome = "Rafael Ramos"
print(nome)
print(type(nome))

print(nome.lower())
print(nome.upper())
print(nome.split()) # Transforma em uma lista de strings

nome = 'Rafael Ramos'
print(nome[0:4])  # Slice de string

print(nome[7:12])  # Slice de string

# [ 0,          1   ]
# ['Rafael', 'Ramos']
print(nome.split()[1])
"""

# Estiver entre aspas duplas triplas -> """Uma string""", """123""", """a""", """True""", """42.3"""

# [ 0,  1,   2,   3,   4,   5 , 6,  7,   8,   9    10   11 ]
# ['R','a', 'f', 'a', 'e', 'l',' ','R', 'a', 'm', 'o', 's' ]

nome = 'Rafael Ramos'

"""
[:: -1] -> Comece do primeiro elemento, vá até o ultimo elemnto e inverta
"""
print(nome[:: -1])  # Inversão da string Pytônico

print(nome.replace('R','G'))
print(type(nome))

texto = 'socorram me subino onibus em marrocos'  # Palíndromo
print(texto)

print(texto[:: -1])


