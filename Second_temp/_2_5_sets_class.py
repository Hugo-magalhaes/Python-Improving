s1 = {1, 2, 3, 4, 5}
s1.add(6)
s1.discard(1)

# Update itera para cada elemento incluído
s1.update('Frase')

# Set tira duplicados
s1.update([1, 2, 4, 5, 6], {3, 4, 5, 6})
# Set vazio
s2 = set()

# for v in s1:
    # print(v)

s3 = {12, 23, 34, 4, 5, 46, 37}
s4 = {1, 2, 3, 4, 5, 6, 7}

# Inner join - Interssecção
s5 = s4 & s3
print(s5)
# Left join - apenas os elementos que existem na esquerda
s6 = s3 - s4
print(s6)
# Full join - sem o que está em ambos
s7 = s3 ^ s4
print(s7)

l1 = ['a', 'b', 'c']
l2 = ['a', 'b', 'c', 'c', 'b']

l1 = set(l1)
l2 = set(l2)
print(l1 == l2)
