#print("Hello World")
#print("Segunda linha")

#print("Olá mundo", end=",   ")
#print("Na mesma linha!")

#x = True
#print("Primeiro objeto", 42, x)

#x = True
#print("Primeiro objeto", 42, x, sep="---")

#nome_usuario = input()
#print("Olá", nome_usuario)

# nome_usuario = input("Digite seu nome:")
# print("Olá", nome_usuario)

# str_entrada = input("Digite um número ")
# int_entrada = int(str_entrada)
# print(int_entrada + 5)

# str_entrada=input("Digite um número")# str_entrada é uma string
# num_entrada=float(str_entrada)
# print(num_entrada+5.2)

# var_1, var_2 = input("Digite dois valores inteiros:").split()
# soma = int(var_1) + int(var_2)
# print(soma)

# for k in type(42).__dict__:
    # print(k)

# str_1="Texto1, texto2, texto3"
# print(str_1.split(','))

# str_1="Um texto qualquer, não há nada de mais neste texto"
# print(str_1.count(' '))
# print(str_1.count('texto'))

# str_1="Autor:{1}, data:{data}, titulo:{0}"
# print(str_1.format("Python","Yuri", data="01/01/2020"))

# print("Valor:{:.2f}".format(3.222222))

# print("Valor 1:{1:.2f}, Valor 0:{0:.3f}".format(3.222222,5.444444))

# print("Usando :<8 resulta em'{:<8}'.".format(42))
# print("Usando :>8 resulta em'{:>8}'.".format(42))
# print("Usando :^8 resulta em'{:^8}'.".format(42))
# print("Usando :=8 resulta em'{:=8}'.".format(-42))
# print("Usando :+ resulta em'{:+8}'.".format(42))
# print("Usando :- resulta em'{:-8}'.".format(42))
# print("Usando :- resulta em'{:-8}'.".format(-42))
# print("Usando :, resulta em'{:,}'.".format(420000000))
# print("Usando :_ resulta em'{:_}'.".format(420000000))

# print()# Linha em branco!

# print("Usando :e resulta em'{:e}'.".format(420000000))
# print("Usando :E resulta em'{:E}'.".format(420000000))
# print("Usando :b resulta em'{:b}'.".format(420000000))
# print("Usando :o resulta em'{:o}'.".format(420000000))
# print("Usando :x resulta em'{:x}'.".format(420000000))
# print("Usando :X resulta em'{:X}'.".format(420000000))
# print()# Linha em branco!

# print("Usando :<+ resulta em'{:<+8}'.".format(42))
# print("Usando :<+10.2f resulta em'{:<+10.2f}'.".format(42.12345))
# print("Usando :^+12.3 resulta em'{:^+12.3f}'.".format(42.12345))



# # Criando uma lista de strings:
# lista_cidades = ["Dois Vizinhos", "Curitiba", "Londrina"]

# # Acessando um item
# print(lista_cidades[0])  # note que o índice é um inteiro e a primeira posição é 0

# # Alterando um item
# lista_cidades[0] = "DV"
# print(lista_cidades[0])

# # Descobrindo a quantidade de itens na lista
# quant = len(lista_cidades)
# print(quant)

# # Adicionando itens ao final
# lista_cidades.append("Francisco Beltrão")

# # Imprimindo toda a lista
# print(lista_cidades)

# # Inserindo item em uma posição
# lista_cidades.insert(1, "Pato Branco")
# print(lista_cidades)

# # Removendo item da lista
# lista_cidades.remove('DV')
# print(lista_cidades)

# lista_vazia = list()
# outra_lista_vazia = []

# # podemos converter outros iteráveis em listas, por exemplo a tupla abaixo
# tupla = ('a', 'e', 'i', 'o', 'u')  # definindo uma tupla
# lista_vogais = list(tupla)
# print(tupla)
# print(lista_vogais)

# Dicionários

# Criando um dicionário:

# capitais_do_sul = {
#     'Paraná': 'Curitiba',
#     'Santa Catarina': 'Florianópolis',
#     'Rio Grande do Sul': 'Porto Alegre'
# }

# print(capitais_do_sul)

# # Criando um dicionário vazio
# dicionario = dict()

# # Adcicionando um item
# dicionario['chave'] = "Valor"

# # Dicionários são heterogenios
# dicionario[1] = 'Olá'
# dicionario[2] = 0.44
# dicionario[3] = True
# dicionario[False] = "Valor bool na chave"

# print(dicionario)

# n = 10
# soma = 0
# for i in range(n+1):
#     soma += i
# print(soma)

# texto = input()

# texto = texto.lower()

# print(texto)

# valor = input()
# digito = 0

# for i in range(len(valor)):
#     digito += int(valor[i])

# print(digito)

meses = {
    'janeiro': 1,
    'fevereiro': 2,
    'março': 3,
    'abril': 4,
    'maio': 5,
    'junho': 6,
    'julho': 7,
    'agosto': 8,
    'setembro': 9,
    'outubro': 10,
    'novembro': 11,
    'dezembro': 12,
}
while(1):
    mes = input()
    if mes == 'fim':
        break
    for i in meses:
        if i == mes.lower():
            print(meses[i])