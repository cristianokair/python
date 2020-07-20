# a = '12' + '12'
# b = 12 + 12
# c = int(a) + b

# print(a, b, c)

# for i in range(1,5):
#     print(i, end=' ')

# for i in range(2,11,2):
#     print(i, end=' ')

# for i in range(10,1,-2):
#     print(i, end=' ')

# for i in range(1,5):
#     for j in range(2,6):
#         print(i*10 + j, end=' ')
#     print()

# parar_em = 5
# for i in range(1,10):
#     if i == parar_em:
#         break
#     print(i)

# for i in range(0,10):
#     if i % 2 == 0:
#         print()
#         continue
#     print(i, 'Número Ímpar')

# parar_em = 10
# for i in range(1,10):
#     if i == parar_em:
#         break
#     print(i, end=' ')
# else:
#     print("Não houve break!")

# lista_cidades = ['Dois Vizinhos','Curitiba','Londrina']

# print(lista_cidades[0])

# lista_cidades[0] = "DV"

# print(lista_cidades)

# quant = len(lista_cidades)
 
# print(quant)

# lista_cidades.append("Francisco Beltrao")

# print(lista_cidades)

# lista_cidades.insert(1, "pato branco")

# print(lista_cidades)

# lista_cidades.remove("DV")

# del(lista_cidades[0])

# print(lista_cidades)

# capitais_do_sul = {
#     'Parana': 'Curitiba',
#     'Santa Catarina': 'Florianópolis',
#     'Rio Grande do Sul': 'Porto Alegre',
# }

# dicionario = dict()

# dicionario['chave'] = "Valor"

# dicionario[1] = "Olá"
# dicionario[2] = 0.44
# dicionario[3] = True
# dicionario[False] = "Olá"
# print(dicionario)

# def minha_funcao():
#     print("Função 'minha_função' sendo executada.")

# def outra_funcao():
#     print("Argumento recebido:", argumento)

# def fn_1(nome, msg="Bem vindo"):
#     print(msg,nome)

# fn_1("Yuri")
# fn_1("Yuri", "Até Mais")

# def fn_2(nome, msg=None):
#     if msg is None:
#         print(nome)
#     else:
#         print(msg, nome)

# fn_2("Yuri")
# fn_2("Yuri", "Até Mais")
class Veiculo:
    def __init__(self, nome="", valor=0):
        self.nome = str(nome)
        self.valor = int(valor)
    
    def __str__(self):
        return self.nome
        
    def get_valor(self):
        return self.valor

class Carro(Veiculo):
    def __init__(self, portas, nome="", valor=0):
        super().__init__(nome, valor)
        self.portas = portas
    
    def get_portas(self):
        return self.portas

v1 = Veiculo("Corsa", 32000)
print(v1)
print(v1.get_valor())

v2 = Veiculo("Corsa 2")
print(v2)
print(v2.get_valor())

c1 = Carro(5, "Ka", 30000)
print(c1)
print(c1.get_valor())
print(c1.get_portas())

c2 = Carro(4, "Ka")
print(c2)
print(c2.get_valor())
print(c2.get_portas())