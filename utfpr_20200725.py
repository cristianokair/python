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

from functools import reduce

lista = [1, 3, 5, 7]
print(reduce(lambda a, b: a+b, lista))
# 16
# O código acima retorna o somatório dos itens da lista. Três chamadas a função lambda foram realizadas:

# 1, 3 que retornou 4;
# 4, 5 que retornou 9; e
# 9, 7 que retornou 16.