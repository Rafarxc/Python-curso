"""
Listas

Listas em Python funciona como vetores/matrizes em outras linguagens, com a diferença se serem DINÂMICOS
e também de podermos colocar QUALQUER tipo de dado.

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array será SMEPRE do tipo
    inteiro e poderá ter SEMPRE no máximo 5 valores.

Já em Python:

- Dinâmico: Não possuem tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo; Ou seja, podemos colocar qualquer tipo de dado;

-------------------------------------------------------------------------------------------------------------------

As listas em Python são representadas por colchetes: []

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['R', 'a', 'f', 'a', 'e', 'l', '', 'R', 'a', 'm', 'o', 's']

lista3 = []

lista4 = list(range(11))

lista5 = list('Rafael Ramos')

-----------------------------------------------------------------------------

# Podemos facilmente checar se determinado valor está contido na lista
num = 7
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

------------------------------------------------------

# Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

--------------------------------------------------------------------------------

# Adicionar elementos em listas

# Para adicionar elementos em listas, utilizamos a função append

print(lista1)
lista1.append(42)
print(lista1)

# OBS: Com append nós só conseguimos adicionar um elemento por vez
# lista1.append(12, 34, 56)  # Erro

lista1.append([8, 3, 1])  # Coloca a lista como elemnto único (sublista)
print(lista1)

if [8, 3, 1] in lista1:
    print('Encontrei a lista...')
else:
    print('Não encontrei a lista')

lista1.extend([123, 44, 67])  # Coloca cada elemento da lista como valor adicional à lista
print(lista1)

------------------------------------------------------------------------------------------------

# Podemos inserir um novo elemnto na lista inforamndo a posição do índice
# OBS: Isso não substitui o valor inicial, o mesmo será deslocado para a direita da lista
lista1.insert(2, 'Novo valor')
print(lista1)

--------------------------------------------------------------------------------------------------

# Podemos facailmente juntar 2 listas
# lista6 = lista1 + lista2
lista1.extend(lista2)
print(lista1)

------------------------------------------------

# Podemos facilmente inverter uma lista

# Forma 1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

# Forma 2
print(lista1[:: -1])
print(lista2[:: -1])

---------------------------

# Copiar uma lista
lista6 = lista2.copy()
print(lista6)

------------------------

# Podemos contar quantos elemntos existem dentro da lista
print(len(lista5))

---------------------------------------------------------------
# Podemos remover facilmente o último elemento de uma lista
OBS: O pop não somente remove o último elemento mas também o retorna

print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo índice
# OBS: Os elementos a direita desse índice serão deslocados para esquerda
# OBS: se não houver elemnto no índice informado, teremos o IndexError

lista5.pop(2)
print(lista5)

----------------------------------------------------------

# Podemos remover todos os elementos(zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

----------------------------------------------------------

# Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

------------------------------------------------------------

# Podemos facilmente converter uma string para lista

# Exemplo1

curso = 'Programação em Python'
print(curso)
curso = curso.split()
print(curso)

# OBS: Por padrão, o split separa os elementos da lista pelo espaço entre elas.

# Exemplo 2
curso = 'Programação, em, Python'
print(curso)
curso = curso.split(',')
print(curso)

-----------------------------------------------------------------------------------------------------------

# Convertendo uma lista em uma string
lista6 = ['Programação', 'em', 'Python']
print(lista6)

# Abaixo estamos falando: Pega a lista 6, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

# Abaixo estamos falando: Pega a lista 6, coloca cifrão entre cada elemento e transforma em uma string
curso = '$'.join(lista6)
print(curso)

---------------------------------------------------------------------------------------------------------

# Podemos colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados

lista6 = [1, 2.34, True, 'Rafa', 'd', [1, 2, 3], 453543543]
print(lista6)
print(type(lista6))

--------------------------------------------------
# Iterando sobre listas

# Exemplo 1 - Utilizando for
soma = 0
for elemento in lista4:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 - Utilizando while
carrinho = []
produto = ''
while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
print('Seu carrinho é: ')
for produto in carrinho:
    print(produto)

------------------------------------------------------------------------------

# Utilizando variáveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

---------------------------------------------------
# Fazemos acesso aos elementos de forma indexada

cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])

# Fazer acesso aos elementos de forma indexada inversa
# Para entender melhor o índice negativo, pense na lista como um círculo, onde o final de um elemento está ligado
#ao início da lista

print(cores[-1])
print(cores[-2])
print(cores[-3])
print(cores[-4])

-------------------------------------------------------------
for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

--------------------------------

# Gerar índice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

-----------------------------
# Listas aceitam REPETIÇÃO
------------------------------
# Outros métodos não tão importantes mas também úteis

# Encontrar o índice de um elemento na lista

numeros = [5, 6, 7, 8, 9, 10]

# Em qual índice está o valor 6 ?

print(numeros.index(6))

# Em qual índice está o valor 9 ?

print(numeros.index(9))

# Buscando um número a partir de um índice proposto:
numeros = [5, 6, 7, 5, 8, 9, 10]

print(numeros.index(5, 1))
# OBS: Caso não tenha o número dentro do range, erro ValueError
-----------------------------------------
# Revisão de slicing
# lista[inicio:fim:passo]
# reange[inicio:fim:passo]

# Trabalhando com slice de lista com o parâmetro 'inicio'

lista = [1, 2, 3, 4]
print(lista[1:])  # Iniciando no índice 1 e pegando todos os elementos restantes

# Trabalhando com slice de lista com o parâmetro 'fim'
print(lista[:2])  # Começa em 0, pega até o índice 2 - 1
print(lista[:4])  # Começa em 0, pega até o índice 4 - 1
print(lista[1:3])   # Começa em 1, pega até o índice 3 - 1


# Trabalhando com slice de lista com o parâmetro 'passo'
lista = [1, 2, 3, 4]
print(lista[1::2])  # Começa em 1,pega até o final, pulando de 2 em 2

# OBS: Podendo usar valores negativos em todos esses métodos
-------------------------------------------------------------------------------------
# Invertendo valores em uma lista

nomes = ['Rafael', 'Ramos']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

nomes = ['Rafael', 'Ramos']
nomes.reverse()
print(nomes)

---------------------------------------------
# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
# * Se os valores forem todos inteiros ou reais

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))

------------------------------------------------

# Transformar listas em tuplas

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

---------------------------------------------
# Desempacotamento de listas

lista = [1, 2, 3]
num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

--------------------------------------------

# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Forma 1
lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)
nova.append(4)

print(lista)
print(nova)
# Veja que ao utilizarmos lista.copy()copiamos os dados da lista para uma nova lista, mas elas ficaram
# totalmente independentes, ou seja , modificando uma lista, não afeta a outra. Isso em Python é chamado de Deep Copy
----------------------------
# Forma 2 - Shallow Copy
lista = [1, 2, 3]
print(lista)

nova = lista

print(nova)
nova.append(4)

print(lista)
print(nova)

# Veja que utilizamos a copia vioa atribuição e copiamos os dados da lista para a nova lista mas após
# realizar modificação em uma das listas, essa mod se refletiu em ambas as listas.
# Isso em Pytohn é chamado de Shallow Copy
"""










