# para criar listar basta declarar colchetes 

l = ['A', 'B', 'C']

print(l)

print(type(l))

l.append('D')
print(l)

l.sort(reverse=True)
print(l)

# ordena em ordem alfabética 
l.sort()
print(l)

# listas pode armazenar qualquer valor
li = ['A', 'B', 'C', 1, 2, 5.5, len, [1, 2, 'A']]
print(li)

# podemos utilizar slice
print(l[1:3])

# Objetos mutáveis ajuda a entender um pouco o comportamento do python com relação a referencia

# vamos copiar a variavel l para m
# agora temos 2 varaveis referenciando a mesma lista em memória
m = l

print(m, l)

# vamos ver se é o mesmo objeto utilizando a função id
print(id(l))
print(id(m))

#vamos acrescentar um a letra na variavel m
m.append('F')

#observe agora as 2 variaveis
# as 2 sofreram alteração, isso acontece pq as 2 variaveis esta referenciando a mesma lista em memória
print(l, m)

# para não sofrer esse efeito colateral podemos fazer o seguinte
# vamos criar uma função que vai copiar a lista e adicionar o valor

def g(x):
    x = x[:]
    x.append(51)
    return x
   
print(l, g(m))
