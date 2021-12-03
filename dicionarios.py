# Resumo: Dicionários são hashmaps que armazenam pares de chaves associadas a valores, numa ordem obtida mediante um cálculo interno de hash (as chaves são imutáveis justamente porque objetos mutáveis não são hasheaveis, posto que cada alteração no estado do dicionário provoca novo hash e se perde assim o original armazenado). Um dicionário pode ser convertido em uma tupla de tuplas, e vice-versa.

# para declarar um dicionário declaramos chave {}

d = {'nome': 'Ronaldo', 'cidade': 'Niterói', 'lat': 22.9, 'long': 43.1}
print(d)

print(d['nome'])

# atualizar valor na chave
d['nome'] = 'Ronaldo Bergara'
print(d['nome'])

# para verificar se uma chave existe no dicionário utilizar o operador in

print('asdf' in d)

# verificar se um valor esta no dicionário
print('Niterói' in d.values())

# acessar uma chave sem erro caso ela não existir, o valor retornado é none
print(d.get('asdf'))

# no Get tbem é possível passar um valor padrão caso não exista a chave
print(d.get('aqsdf', 'valor padrão'))

# verificar quantos elementos existe no dicionário, vai retornar o total de chaves
print(len(d))

# no python 3, os dicionários tem uma função auxiliar chamada direct view, 
# keys() informa as chaves do dicionário
# values() informa os valores
# items() informa os pares chave e valor em tupla

print(d.keys())
print(d.values())
print(d.items())

