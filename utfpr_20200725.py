# lista01 = [1,2,3,4]
# print(lista01)
# tupla01 = tuple(lista01)
# print(tupla01)
# print(tupla01[-1])
# print(tupla01[-2])
# print(tupla01[0:2])
# print(tupla01[1:3])
# print(tupla01[-3:-1])
# print(tupla01[-3:])
# print(tupla01[:2])
# print(tupla01[:])
# tupla03 = tuple(tupla01[1:3])
# print(tupla01)
# # print(tupla03)
# tupla04 = (1, "Yuri", True, None, -2.44)
# print(tupla04)

# tupla05 = (3, 42, "Texto")
# tupla06 = (1, ("Elemento de outra tupla", 12, True), False, tupla05)
# # print(tupla06[1])

# # for item in tupla06:
# #     print(item)

# def iterar(t, espaco=""):
#     for item in t:
#         if isinstance(item, tuple) or isinstance(item, list):
#             print(type(item), ":")
#             iterar(item, espaco + "    ")
#         elif isinstance(item, dict):
#             continue  # ignora dicionários
#         else:
#             print(espaco, item, sep="")
            
# iterar(tupla06)

# tupla07 = ("Oi", 12, 13, ("Oi", "Oi"), True, "Oi", 12)

# print("len:", len(tupla07))  # Retorna o tamanho (número de itens) em uma Tupla
# print("count:", tupla07.count("Oi"))  # Número de Vezes que o elemento aparece na Tupla
# print("index:", tupla07.index(12))  # Retorna a posição da primeira ocorrencia do elemento na tupla

# print("Oi" in tupla07)
# print("Bom dia" in tupla07)

# conjunto = {'maça', 'banana', 'laranja', 'laranja'}
# print(conjunto)

# lista01 = [1, 2, 4, 7, 7, 8, 9, 0, 0, 1]
# print(set(lista01))

# conjunto01 = {2, 3, 2, 1, 5, 9, 9 ,0}
# for item in conjunto01:
#     print(item, end = " ")

# conjunto02 = {12, 11, 7, 15}
# print(conjunto02)
# conjunto02.add(20)
# print(conjunto02)
# conjunto02.add(20)  # Não tem efeito, item já existente
# print(conjunto02)

# conjunto03 = {'maça', 'banana', 'cereja', 'abacate', 'maracujá'}
# conjunto03.remove('maça')
# print(conjunto03)
# conjunto03.discard('maça')  # Não gera erro, 'remove' geraria pois 'maça' não está mais no conjunto
# print(conjunto03)
# conjunto03.discard('cereja')
# print(conjunto03)
# conjunto03.pop()  # Não é possível prever o item a ser removido com facilidade
# # print(conjunto03)

# s = {1, 3, 5, 7, 9, 11}
# t = {0,1,2,3,4}

# print("s | t", s | t)# União (s | t ou s.union(t)): Retorna um novo conjunto com elementos que estejam tanto em s quando em t (inclusive em ambos);
# print("s & t", s & t)# Intersecção (s \& t ou s.intersection(t)): Retorna um novo conjunto somente com elementos comuns a s e t (elementos que estão em ambos);
# print("s - t", s - t)# Diferença (s - t ou s.difference(t)): Retorna um novo conjunto com os elementos que estão em s mas não em t; e
# print("s ^ t", s ^ t)# Diferença Simétrica (s \^ t ou s.symmetric_difference(t)): Retorna um novo conjunto com elementos em s ou t mas não em ambos.

# s1 = {1, 3, 5}
# t1 = {0, 1, 2}

# print("s1 <= s", s1 <= s)# s <= t ou s.issubset(t): Retorna True se todo elemento em s existe em t
# print("s <= s1", s <= s1)
# print("s1 >= s", s1 >= s)# s >= t ou s.issuperset(t): Retorna True se todo elemento em t existe em s
# print("s >= s1", s >= s1)
# print("t1 <= s", t1 <= s)
# print("t1 >= s", t1 >= s)

# def eh_par(valor):
#     return (valor % 2) == 0

# def eh_impar(valor):
#     return (valor % 2) == 1

# lista = [x for x in range(0, 11)]  # equivalente a: lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("Todos:", lista)
# print("Par:", list(filter(eh_par, lista)))
# print("Ímpar:", list(filter(eh_impar, lista)))

# print(list(filter(lambda x: x % 2 == 0, lista)))

# lista = [1,2,4,6,8]
# print(list(map(lambda x: x*2, lista)))

# lista2 = [5, 6, 7, 8]
# print(list(map(lambda x, y: x+y, lista, lista2)))

# from functools import reduce

# lista = [1, 3, 5, 7]
# print(reduce(lambda a, b: a+b, lista))
# 16
# O código acima retorna o somatório dos itens da lista. Três chamadas a função lambda foram realizadas:

# 1, 3 que retornou 4;
# 4, 5 que retornou 9; e
# 9, 7 que retornou 16.

##questão 1

# a = {1, 3, 5, 7, 9, 11}
# b = {0,1,2,3,4}

# x = {'a','b','c'}
# y = {'b','c'}

# def uniao(A, B):
#     return A.union(B)

# def interseccao(A, B):
#     return A.intersection(B)

# def unicos(A,B):
#     return A.difference(B)

# def teste(A, valor):
#     if type(valor) is set:
#         if valor <= A:
#             return True
#         else:
#             return False
#     elif type(valor) is not set:
#         if valor in A:
#             return True
#         else:
#             return False
#     else:
#         return False

##questão 2

# from functools import reduce
# somaPares = 0
# entrada = input().split()
# entrada = list(map(int, entrada))
# entrada = list(filter(lambda x: x % 2 == 0,entrada))
# if(len(entrada) > 0):
#     entrada.sort()
#     somaPares = reduce(lambda a,b: a+b, entrada)

# for i in entrada:
#     print(i,end=' ')
# print()
# print(somaPares)

##questão 3

# n = int(input())
# for i in range(0,n+1):
#     for j in range(i):
#         valor = i**2
#         if j == 0:
#             print(valor, end=' ')
#         else:
#             print(valor + 2*j, end=' ')
#     print()


# n = int(input())
# for i in range(0,n+1):
#     for j in range(0,i):
#         valor = i**2
#         print(valor + 2*j, end=' ')
#     if i > 0:
#         print()
def pertinencia(id):
    if id in dicionario:
        return dicionario[id]
    else:
        return 0

dicionario = dict()

while True:
    cmd = input().split()
    if cmd[0] == 'set':
        ID = cmd[1]
        valor = int(cmd[2])
        dicionario[ID] = valor

    elif cmd[0] == 'sum':
        ID1 = cmd[1]
        ID2 = cmd[2]
        ID3 = cmd[3]
        aux1 = pertinencia(ID1)
        aux2 = pertinencia(ID2)
        dicionario[ID3] = aux1+aux2

    elif cmd[0] == 'mul':
        ID1 = cmd[1]
        ID2 = cmd[2]
        ID3 = cmd[3]
        aux1 = pertinencia(ID1)
        aux2 = pertinencia(ID2)
        dicionario[ID3] = aux1*aux2
        
    elif cmd[0] == 'get':
        ID1 = cmd[1]
        aux1 = pertinencia(ID1)
        print(aux1)
    elif cmd[0] == 'fim':
        break