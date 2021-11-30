
# tuplas são sequências imutaveis
t = ('A', 'B', 'C')
print(t)

t = t + ('D', 'E')
print(t)

print(tuple('ronaldo'))

# tupla armazena qualquer tipo de objeto
m = ('A', 1, 5.5,['B', 'C', 'D'],(3, 'E'))
print(m)

# podemos acessar o indice e usar slice
print(m[2])
print(m[2:5])

# quem cria a tupla é  a virgula e não parenteses 
l = ('A')
o = ('A',)
print(type(l), type(o))