#08-Funções de Alta Ordem

# def soma(a, b):
#     return a + b

# minha_soma = soma
# print(minha_soma)
# print(soma)

def filtro2(fn, it):
    it2 = list()
    it3 = list()
    for valor in it:
        if fn(valor):
            it2.append(valor)
        else:
            it3.append(valor)
    return it2, it3

lista1 = [0, 1, 2, 3, 4, 5]
lista2, lista3 = filtro(lambda x: x % 2 == 1, lista1)  # mantemos os números pares
print(lista2)
print(lista3)

# def criar_verificador(tipo):  # função externa
#     tipo = tipo.lower()
#     if tipo == 'par':
#         return lambda x: x % 2 == 0  # função interna/retornada que é anônima
#     elif tipo == 'impar':
#         return lambda x: x % 2 == 1
#     elif tipo == 'positivo':
#         return lambda x: x > 0
#     elif tipo == 'negativo':
#         return lambda x: x < 0
#     else:
#         return lambda x: False
    
# ver = criar_verificador('par')
# print("par, 1:", ver(1))
# print("par, 2:", ver(2))
# ver = criar_verificador('negativo')
# print("negativo, -1:", ver(-1))
# print("negativo, 1:", ver(1))
# ver = criar_verificador('invalido')
# print("invalido, 1:", ver(1))

# def somador():  # função externa
#     def soma(a, b):  # função interna
#         return a + b
#     return soma  # a função externa retorna a interna

# fn = somador()
# print(fn(2, 3))

# def criar_multiplicador(x):  # função externa
#     def mult(y):  # função interna
#         return x * y
#     return mult
    
# dobro = criar_multiplicador(2)
# triplo = criar_multiplicador(3)

# print(dobro(4))
# print(triplo(4))

# def criar_fn(x):  # função externa
#     x_quad = x**2
#     def fn(a, b):  # função interna
#         return a*x_quad + b*x #2*4 + 3*2 = 8+6 = 14 // 2*9 + 3*3 = 18 + 9 = 27
#     return fn
    
# fn2 = criar_fn(2)
# fn3 = criar_fn(3)

# print(fn2(2, 3))
# print(fn3(2, 3))



#---------------------------------------------------------------------


# 09-Introdução ao Pandas


#---------------------------------------------------------------------
# import pandas as pd
# import numpy as np
# from pandas import Series, DataFrame

# sr1 = Series([1, 3, -5, 7])
# print(sr1)

# print(sr1.index)
# print(sr1.values)
# print(sr1.dtype)

# print(len(sr1))

# for i in range(len(sr1)):
#     print(sr1.values[i])

# sr2 = Series([1, 3, -5, 7], index=['a', 'b', 'c', 'd'])
# print(sr2)

# print(sr1[0])
# print(sr1[1])
# print(sr1[3])
# print("Na sr2:")
# print(sr2['a'])
# print(sr2['c'])

# print(sr2[sr2 > 0]) # Filtra mantendo apenas os positivos não negativos

# print(sr2 * 2) # Multiplicação por escalar

# print(np.exp(sr2)) # usando funções do NumPy